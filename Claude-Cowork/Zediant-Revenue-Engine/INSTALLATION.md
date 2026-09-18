# Installation

Copy the following into the existing Zediant-Revenue-Engine project:

- `context/seo/` → existing `context/seo/`
- `skills/seo/` → existing `skills/seo/`
- `seo/` → new root-level `seo/`

Do NOT replace the existing `Claude.md`.

Review `CLAUDE_MD_SEO_ADDENDUM.md` and append it to the active Claude.md.

Then run:
`seo/prompts/initial_discovery.md`

The first run is intentionally read-only.

Important:
The current Claude.md references `operational/`. The screenshots supplied for this package show `context/`, `migration/`, `policies/`, `scheduler/`, and `skills/`, but do not show an `operational/` folder. Do not create or infer operational files as part of this SEO package. If the live project actually lacks `operational/`, treat that as a separate DATA GAP and resolve it before changing any existing revenue workflow.
