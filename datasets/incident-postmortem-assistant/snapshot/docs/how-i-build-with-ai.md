# How I build with AI coding tools

Written for TextCortex (Product Engineering Intern).

Nikhil Adhikari, Berlin. [github.com/kai2055](https://github.com/kai2055) · nikhiladhikari1@gmail.com

---

## What this repo is

An assistant that answers questions from 20 real incident post-mortems (Cloudflare, GitHub, GitLab, AWS and others).

It cites its sources, and it declines when the evidence is too weak.

A 39-query test suite runs on every push and blocks any change that makes it worse.

Current numbers: hit rate 1.00, MRR 0.92, zero invented citations.

It runs locally on a CPU. It is not deployed, and the README says why.

## Why I built it

I wanted to know one thing: when an AI system gives a confident answer, how do I know it is not making it up?

Post-mortems are a good test. They are long, technical and full of details that are easy to get almost right.

"Almost right" is the failure I care about.

I built it with Claude as my coding partner. Everything below is what I learned about doing that without fooling myself.

---

## The hacks

### 1. AI assembles. The source decides.

Claude built my corpus documents. It was fast, and one early draft was wrong.

A Sentry post-mortem came back with an invented timeline and duration. It read perfectly.

The fix was a rule, not a better prompt: every document must trace to a first-party source that was actually fetched and checked, detail by detail.

"Accurate-sounding" is not "sourced."

Evidence: [ADR-010](../decisions/adr-010-corpus-documents-assembled-by-claude-under-first-party-verification.md)

### 2. Put a gate where the AI cannot argue with it.

AI tools change a lot of code quickly. I cannot review every line as carefully as I would like.

So the test suite reviews it for me. Every push re-indexes, re-runs 39 queries and compares against a committed baseline.

Some metrics block the push on any drop. Some have a floor. Some only report.

If a suggestion makes retrieval worse, it does not get in, however good the explanation sounded.

### 3. Treat AI output like a developer's build. Test it and file the bug.

I worked as a manual tester before I built anything, and I kept the habit.

When a threshold change dropped filter precision from 1.00 to 0.33, I did not just patch it.

I wrote a bug report first: severity, reproduction steps, evidence, root cause, fix, verification.

Writing it down is what showed me the bug had been there all along. A config change only exposed it.

Evidence: [BUG-001](qa/bug-reports/BUG-001-distance-threshold.md)

### 4. One decision, one record.

AI will happily give you three options and a recommendation. A week later you will not remember why you agreed.

Every real decision in this repo has a short record: context, options considered, what I chose, what I rejected and why.

It also stops the AI from quietly reopening a settled question. I point it at the record.

Evidence: the [decisions](../decisions) folder.

### 5. Rebuild from blank.

After AI helps me write a module, I close the chat and write it again from an empty file.

Where I get stuck is exactly what I did not understand.

It is slow. It is also the only way I have found to own code that an AI helped write.

### 6. Make the AI question me, not the other way round.

I ask for a code review as questions: "what happens here if the path is a directory?"

I answer before I see the fix.

On my other projects this found real bugs that tests had missed: a missing `raise`, a typo in a dictionary key, a check that was always true.

### 7. Keep the failures in the repo.

The README has a "Known limitations" section, written by me, not softened.

The system matches vocabulary, not mechanism. It over-declines on some questions. Section accuracy is 0.50.

An AI will write you a README where everything works. Do not let it.

### 8. A slow test suite is a broken test suite.

Mine took 15 minutes 46 seconds. Every test passed, so nothing looked wrong.

But I had stopped running it, which meant it protected nothing.

I got it to 8.5 seconds. With AI tools this matters more, because you want to run the suite after every change.

Evidence: [case study](qa/case-studies/case-study-test-suite-speed.md)

---

## Your six questions

### Agency. What's the last thing nobody asked you to do but you did it?

Nobody asks for bug reports on a solo project.

I wrote them anyway, plus findings and case studies, because I wanted to practise the part of engineering that is not code.

They are all in [docs/qa](qa).

Second example: my credit-default model scored ROC-AUC 0.97. I flagged that number in public as a likely data leak instead of putting it on my CV as a win.

### See problems. How do you act?

I reproduce it, write it down, then fix it. In that order.

Once I spent a day chasing a retrieval bug that turned out not to exist in my code.

I wrote that up too, because the investigation found two real problems on the way.

Evidence: [Chasing a bug that didn't exist](qa/case-studies/case-study-retrieval-investigation.md)

### Obsession to learn. What has been the last thing you learned?

That a model which loses to "always guess zero" is telling you the question is wrong.

My Berlin train-delay project first tried to predict the exact delay. A baseline that always said "on time" beat it.

I changed the question to "more than three minutes late, yes or no?" and it worked (ROC-AUC 0.886).

The failed version is still in that repo: [berlin-transit](https://github.com/kai2055/berlin-transit), with a [live dashboard](https://transit-dashboard-184545841057.us-central1.run.app).

I am a slow learner on purpose. I would rather understand one thing from first principles than skim five.

### Understand yourself as first customer. How are you testing things?

I use what I build before I trust what the metrics say.

I ask it the questions I would really ask during an incident, including ones it should refuse.

Then I turn every surprise into a test case, so it stays caught.

That is how the suite grew from 23 queries to 39.

### Eye for good products. What product inspires you and why?

Ollama.

The whole product is one command: `ollama run qwen3:8b`, and a model is running on my laptop.

Underneath it is downloading weights, managing memory and serving an API, and I never have to see any of that.

That is what I look for in a product: few features, no clutter, and a simple layer that hides the hard part.

It did one job and got out of my way, which is why this whole project runs on it.

### This is new. No years required, but what makes you different?

I was a tester before I was a builder.

Most people use AI tools to go faster. I use them to go faster and then spend the saved time checking.

I also finish. Four projects, three of them live, each with its failures written down.

---

## What I am honest about

I have not worked on a product team before.

My German is A2.

I am an M.Sc. student. My coursework is done, and I can work full-time as my mandatory internship.