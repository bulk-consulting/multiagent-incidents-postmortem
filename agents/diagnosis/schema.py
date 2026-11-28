"""The shape of the Diagnosis agent's answer, checked with Pydantic.

Same idea as agents/triage/schema.py: if the model's answer does not fit the shape, Pydantic raises an
error and the agent asks the model to answer again.

The Diagnosis agent reads the findings of the Research agent and says:
  - the most likely causes of the current incident (up to 3 hypotheses), each based on past incidents;
  - whether the evidence is enough to write a diagnosis;
  - what is missing (gaps) and what should happen next.

There is no numeric confidence (0-1): a number written by the LLM is not calibrated, so we use three
levels with an explanation (matches / differs), as suggested in Dibia's book.
"""
from typing import Literal

from pydantic import BaseModel, Field, model_validator

MAX_HYPOTHESES = 3

# What the Diagnosis agent asks the graph to do next. The routing in code makes the final decision
# (for example, refine_search becomes an inconclusive report when the research rounds are over).
NextStep = Literal["report", "refine_search", "ask_analyst"]


class Hypothesis(BaseModel):
    """One possible cause of the current incident."""

    # The likely cause of the CURRENT incident, in 1 or 2 sentences.
    cause: str = Field(min_length=1)

    # post_mortem_ids of the findings that support this hypothesis (at least one), e.g. ["DAN-197"].
    based_on: list[str] = Field(min_length=1)

    # What matches between the current incident and the past ones, and what does not.
    matches: str
    differs: str

    # Three simple comparisons the model makes for this hypothesis. Code uses them to limit the confidence and to
    # decide whether the evidence is enough (decide() below): in the tests the model judged each point well, but
    # almost always said "the evidence is enough" when asked for an overall judgment.
    #   same_trigger: is the past trigger the same KIND as the current one? "unknown" when the current trigger is
    #                 not known.
    #   same_component: is the failing component the same KIND (for example a relational database, an edge
    #                   network, a coordination cluster)?
    same_trigger: Literal["yes", "no", "unknown"]
    same_component: Literal["yes", "no"]
    #   same_mechanism: would what broke in the past incident, and how it spread, explain the current symptoms in
    #                   the same way? (In the tests, the trigger and the component were marked "yes" when only the
    #                   general kind matched, e.g. a backend revision, while the failure itself was another one.)
    same_mechanism: Literal["yes", "no"]

    confidence: Literal["high", "medium", "low"]


class DiagnosisResult(BaseModel):
    """Everything the Diagnosis agent returns after reading the findings."""

    # Up to 3 hypotheses, from the most to the least likely. Can be empty when nothing fits.
    hypotheses: list[Hypothesis] = Field(default_factory=list, max_length=MAX_HYPOTHESES)

    # Is the evidence enough to write a diagnosis report?
    evidence_sufficient: bool

    # What is missing to be sure.
    gaps: list[str] = Field(default_factory=list)

    next_step: NextStep

    # Required when next_step is "refine_search": what the Research agent should look for now.
    search_request: str = ""

    # Required when next_step is "ask_analyst": questions about the current incident,
    # in the same language as the analyst's message.
    questions_for_analyst: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def check_consistency(self):
        """Rules that involve more than one field."""
        if self.evidence_sufficient:
            if self.next_step != "report":
                raise ValueError('evidence_sufficient is true, so next_step must be "report"')
            if not self.hypotheses:
                raise ValueError("evidence_sufficient is true, so there must be at least one hypothesis")
        if self.next_step == "refine_search" and not self.search_request.strip():
            raise ValueError('next_step is "refine_search", so search_request must say what to look for')
        if self.next_step == "ask_analyst" and not self.questions_for_analyst:
            raise ValueError('next_step is "ask_analyst", so questions_for_analyst must list the questions')
        return self


class DiagnosisDraft(BaseModel):
    """What the model writes. evidence_sufficient and next_step are decided by code (decide())."""

    hypotheses: list[Hypothesis] = Field(default_factory=list, max_length=MAX_HYPOTHESES)
    gaps: list[str] = Field(default_factory=list)
    # What to look for if a new search is needed (keywords in English). The model always writes it; code uses
    # it only when it decides on refine_search.
    search_request: str = ""
    # Questions that would decide between the hypotheses, in the analyst's language (can be empty).
    questions_for_analyst: list[str] = Field(default_factory=list, max_length=3)


CONFIDENCE_ORDER = ["low", "medium", "high"]


def _cap(confidence, top):
    return confidence if CONFIDENCE_ORDER.index(confidence) <= CONFIDENCE_ORDER.index(top) else top


def decide(draft, deepened_ids, research_round=1, max_rounds=3):
    """Turn the model's draft into the DiagnosisResult, applying the rules in code:

    1. Confidence limit: high only if same kind of trigger, component AND mechanism; medium at most otherwise;
       low if trigger and component both differ.
    2. Evidence is enough only if a high/medium hypothesis has the same kind of component and mechanism, is based
       on at least one deepened incident (with passages) and its trigger is the same, or unknown from the second
       research round on (with an unknown trigger, almost any incident with the same kind of component passed in
       the first round: one more search is tried first).
    3. Next step: enough → report. Not enough → refine_search while there are research rounds left (and a
       search_request); otherwise ask_analyst if there are questions; otherwise an inconclusive report.
    """
    deepened = set(deepened_ids)
    hypotheses = []
    for h in draft.hypotheses:
        if h.same_trigger == "yes" and h.same_component == "yes" and h.same_mechanism == "yes":
            top = "high"
        elif h.same_trigger == "no" and h.same_component == "no":
            top = "low"
        else:
            top = "medium"
        hypotheses.append(h.model_copy(update={"confidence": _cap(h.confidence, top)}))

    trigger_ok = ("yes", "unknown") if research_round > 1 or research_round >= max_rounds else ("yes",)
    sufficient = any(h.confidence in ("high", "medium") and h.same_component == "yes" and h.same_mechanism == "yes"
                     and h.same_trigger in trigger_ok and deepened.intersection(h.based_on) for h in hypotheses)
    if sufficient:
        next_step = "report"
    elif research_round < max_rounds and draft.search_request.strip():
        next_step = "refine_search"
    elif draft.questions_for_analyst:
        next_step = "ask_analyst"
    else:
        next_step = "report"
    return DiagnosisResult(
        hypotheses=hypotheses, evidence_sufficient=sufficient, gaps=draft.gaps, next_step=next_step,
        search_request=draft.search_request if next_step == "refine_search" else "",
        questions_for_analyst=draft.questions_for_analyst if next_step == "ask_analyst" else [])


def parse_diagnosis_answer(text):
    """Turn the model's text into a DiagnosisDraft.

    The model should answer with only a JSON object, but sometimes it adds words or a ```json fence
    around it. So we take everything between the first "{" and the last "}".
    Raises ValueError (Pydantic's errors are ValueErrors too) if the answer is not valid.
    """
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end < start:
        raise ValueError("the answer does not contain a JSON object")
    return DiagnosisDraft.model_validate_json(text[start : end + 1])


def check_based_on(result, finding_ids):
    """Every incident a hypothesis is based on must be in the Research agent's findings.
    This stops the model from inventing an incident. Raises ValueError if it is not."""
    known = set(finding_ids)
    for h in result.hypotheses:
        unknown = [i for i in h.based_on if i not in known]
        if unknown:
            raise ValueError(
                f"based_on must use only incidents from the findings: {sorted(known)}. "
                f"Not in the findings: {unknown}."
            )
