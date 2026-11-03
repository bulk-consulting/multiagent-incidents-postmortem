# ADR-0003 — Static site generator

**Status:** Superseded in implementation — built with a dependency-light Python generator, not Astro.

## Original decision
The site would be built with Astro, binding incidents to a content collection whose schema mirrors `incident.schema.json`. Rationale: content-collection schema validation gives a second validation gate for free; islands keep the filter UI cheap.

## What shipped (and why the change)
M5 was built as `scripts/build_site.py` — a self-contained generator (stdlib + PyYAML) emitting static HTML/CSS with a little vanilla JS for filtering. Deployed to GitHub Pages by `.github/workflows/pages.yml`.

Reasons for the deviation:
- **The second-gate rationale is already covered.** `scripts/validate.py` (G-SCHEMA) validates every incident against `incident.schema.json` in CI, so Astro's content-collection validation would be redundant. `validate.yml` also runs `build_site.py` as a G-SITE smoke test.
- **Zero new toolchain.** No Node/npm/framework dependency; the repo is already Python-tooled (validate/exports/discovery), so contributors need nothing new, and the build is fast and reproducible.
- **Fully verifiable.** The generator builds and is inspected in-repo; no framework build step to debug.

Astro remains a reasonable future choice if the site grows (MDX content, richer interactivity); revisit then.

## Alternatives considered
- Astro — the original choice; its main benefit (schema validation) is already provided by `validate.py`.
- Hugo / Docusaurus — extra toolchains without a validation advantage here.
