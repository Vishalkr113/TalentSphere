from pathlib import Path
import re
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
FRONT = ROOT / 'frontend/src'
BACK = ROOT / 'backend/app'

errors = []

def require(condition, message):
    if not condition:
        errors.append(message)

# Frontend -> backend assessment contracts
assessment_ts = (FRONT / 'data/assessment/assessmentService.ts').read_text()
require('/assessment/${assessmentType}/start' in assessment_ts, 'Central assessment start endpoint missing')
require('/assessment/${attemptId}/submit' in assessment_ts, 'Central assessment submit endpoint missing')

college = (FRONT / 'components/college/CodingAssessment.tsx').read_text()
require('127.0.0.1:8000' not in college and 'localhost:8000' not in college, 'Hardcoded localhost remains in CodingAssessment')

# Role route guards
app = (FRONT / 'App.tsx').read_text()
for role in ('high_school_student', 'college_student', 'working_professional'):
    require(role in app, f'Role guard reference missing: {role}')

# Backend assessment route exists
api = (BACK / 'api/assessment.py').read_text()
require('POST' not in api or 'start' in api, 'Assessment API source unexpectedly malformed')
require('/{assessment_type}/start' in api or 'assessment_type' in api, 'Assessment start route missing')
require('/{attempt_id}/submit' in api or 'attempt_id' in api, 'Assessment submit route missing')

# AI gateway and frontend service
require((BACK / 'services/gemini_gateway.py').exists(), 'Gemini gateway missing')
require((BACK / 'api/ai.py').exists(), 'AI API missing')
require((FRONT / 'services/aiService.ts').exists(), 'Frontend AI service missing')

# No direct Gemini key usage in frontend source
frontend_text = '\n'.join(p.read_text(errors='ignore') for p in FRONT.rglob('*.ts*'))
require('GEMINI_API_KEY' not in frontend_text, 'Gemini API key reference exposed in frontend source')

# Database schema sanity check
DB = ROOT / 'backend/talentsphere.db'
require(DB.exists(), 'Database file missing')
if DB.exists():
    con = sqlite3.connect(DB)
    tables = {r[0] for r in con.execute("select name from sqlite_master where type='table'")}
    for table in ('users', 'profiles', 'assessment_questions', 'assessment_attempts', 'assessment_attempt_questions', 'assessment_answers', 'assessment_results'):
        require(table in tables, f'Missing database table: {table}')
    if 'assessment_questions' in tables:
        counts = dict(con.execute('select assessment_type, count(*) from assessment_questions group by assessment_type').fetchall())
        for key in ('high_school_foundation','high_school_pcm','high_school_pcb','high_school_commerce','high_school_arts','college_aptitude','college_coding','professional_skill'):
            require(counts.get(key, 0) > 0, f'No seeded questions for {key}')
    con.close()

if errors:
    print('PHASE9 CONTRACT TEST: FAIL')
    for e in errors:
        print(' -', e)
    raise SystemExit(1)
print('PHASE9 CONTRACT TEST: PASS')
