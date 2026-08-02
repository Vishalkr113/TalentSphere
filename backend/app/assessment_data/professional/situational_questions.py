from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


PROFESSIONAL_SITUATIONAL_QUESTIONS: list[Question] = [

    # =====================================================
    # PROFESSIONAL SITUATIONAL (PROFESSIONAL-SITUATIONAL-001–010)
    # =====================================================


    Question(

        question_code="PROFESSIONAL-SITUATIONAL-001",

        question=
        "If a team member disagrees with your idea, you should:",

        options=[
            "Listen and discuss the concern",
            "Ignore the person",
            "Force your decision",
            "Leave the team"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Good professionals respect different opinions and discuss solutions.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-002",

        question=
        "If you miss a project deadline, the best action is:",

        options=[
            "Inform the team and explain the reason",
            "Hide the issue",
            "Blame others",
            "Stop working"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Transparency and communication help solve deadline issues.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-003",

        question=
        "When receiving negative feedback, you should:",

        options=[
            "Accept it and improve",
            "Argue immediately",
            "Ignore feedback",
            "Quit the task"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Constructive feedback helps improve performance.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-004",

        question=
        "A colleague needs help with a task. You should:",

        options=[
            "Support and guide them",
            "Ignore them",
            "Create problems",
            "Avoid communication"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.TEAMWORK,

        explanation=
        "Helping teammates improves collaboration.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-005",

        question=
        "If you find a bug in production, you should:",

        options=[
            "Report and fix it properly",
            "Ignore it",
            "Delete the project",
            "Hide the problem"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Production issues should be handled responsibly.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-006",

        question=
        "When working in a team, communication should be:",

        options=[
            "Clear and regular",
            "Avoided",
            "Only during problems",
            "Unnecessary"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.TEAMWORK,

        explanation=
        "Regular communication keeps teams aligned.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-007",

        question=
        "If you do not know a technology required for a task, you should:",

        options=[
            "Learn and ask for guidance",
            "Reject the task",
            "Pretend to know",
            "Ignore it"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Learning attitude helps professionals grow.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-008",

        question=
        "During a meeting, a professional should:",

        options=[
            "Listen actively and contribute",
            "Interrupt everyone",
            "Avoid participation",
            "Ignore discussion"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Active participation improves workplace communication.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-009",

        question=
        "When multiple tasks are assigned, you should:",

        options=[
            "Prioritize tasks based on importance",
            "Do random tasks",
            "Ignore deadlines",
            "Stop working"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "Prioritization helps complete important tasks efficiently.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-010",

        question=
        "A professional conflict should be resolved through:",

        options=[
            "Discussion and solution finding",
            "Arguments",
            "Avoidance forever",
            "Personal attacks"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Healthy discussion helps resolve workplace conflicts.",
    ),

]