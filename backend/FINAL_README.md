TalentSphere FINAL Backend

This package contains the source backend, Alembic migrations, assessment banks, and seed logic. Runtime/private files are intentionally excluded: .env, SQLite databases, venv, uploads, caches.

Assessment architecture:
- High School: Foundation, Science/PCM, Science/PCB, Commerce, Arts/Humanities, Aptitude, Logical Reasoning
- College: Common, Aptitude, Coding, DSA, Technical/Core CS, Career
- Working Professional: Common, Technical, DSA, Situational
- 10 questions per attempt; banks contain 50+ questions where applicable.
- Language-specific DSA banks are removed from the loader. DSA is language-neutral.
- Seed is idempotent. Run: python -m app.seed_assessments
- Current schema head remains a31f0e9b7c42; no new migration is required for these assessment-type strings.
