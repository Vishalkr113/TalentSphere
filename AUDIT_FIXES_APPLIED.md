# TalentSphere Audit Fixes

## Confirmed root cause fixed
- College assessment start crashed because `assessment_service.py` referenced `profile.degree`.
- The canonical backend `Profile` model stores the selected college degree in `profile.course`.
- Fixed the college assessment question lookup to use `profile.course` while continuing to filter by `profile.branch`.

## Assessment attempt state fix
- Removed frontend localStorage-based `submittedTypes` state from AssessmentHub.
- Retake is now determined from completed backend assessment history.
- A card remains `Start Assessment` until a submission is actually completed.
- This prevents stale localStorage from incorrectly showing `Retake Assessment`.

## Question-bank audit
- Current source loader contains 1,280 question objects.
- Question codes are unique across the loaded banks.
- High School: 250 questions across 5 dedicated banks (50 each).
- College: 200 dedicated questions across Common/Technical/Career/DSA, plus shared aptitude/coding/DSA/reasoning banks.
- Working Professional: 200 questions across Common/Technical/DSA/Situational (50 each).
- Language-specific DSA files are not loaded by the canonical loader.

## Validation
- Backend Python source compilation passed.
- TypeScript `tsc -b` passed.
- Full Vite build could not be executed in this Linux audit environment because the uploaded Windows `node_modules` lacks the Linux Rollup optional binary. This is an environment/package-install issue, not a TypeScript error.

## Privacy / cleanup
The final source ZIP intentionally excludes:
- backend `.env`
- frontend `.env`
- local SQLite database
- uploaded profile photos/resumes
- `venv`
- `node_modules`
- generated `dist`
- Python `__pycache__`

Keep your existing local `.env`, database and uploads on your machine. Run the project dependencies normally on Windows after extracting the source.
