from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


COLLEGE_CAREER_QUESTIONS: list[Question] = [

    # =====================================================
    # COLLEGE CAREER (COLLEGE-CAREER-001–010)
    # =====================================================


    Question(

        question_code="COLLEGE-CAREER-001",

        question=
        "Which platform is commonly used for professional networking?",

        options=[
            "LinkedIn",
            "Calculator",
            "Paint",
            "Notepad"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "LinkedIn is a professional networking platform.",
    ),



    Question(

        question_code="COLLEGE-CAREER-002",

        question=
        "A good resume should mainly contain:",

        options=[
            "Skills and achievements",
            "Only personal photos",
            "Random information",
            "Unrelated details"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Resume should highlight education, skills and achievements.",
    ),



    Question(

        question_code="COLLEGE-CAREER-003",

        question=
        "Which skill is important for software developers?",

        options=[
            "Problem Solving",
            "Ignoring errors",
            "Avoiding practice",
            "No communication"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Problem solving is a core skill for software development.",
    ),



    Question(

        question_code="COLLEGE-CAREER-004",

        question=
        "Mock interviews help students to:",

        options=[
            "Improve interview confidence",
            "Avoid preparation",
            "Remove skills",
            "Skip learning"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Mock interviews improve communication and confidence.",
    ),



    Question(

        question_code="COLLEGE-CAREER-005",

        question=
        "Which is important for career growth?",

        options=[
            "Learning new skills",
            "Stopping improvement",
            "Ignoring technology",
            "Avoiding projects"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Continuous skill development helps career growth.",
    ),



    Question(

        question_code="COLLEGE-CAREER-006",

        question=
        "A technical portfolio contains:",

        options=[
            "Projects and work samples",
            "Only marksheet",
            "Only certificates",
            "Only personal details"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Portfolio demonstrates practical skills through projects.",
    ),



    Question(

        question_code="COLLEGE-CAREER-007",

        question=
        "Internships provide:",

        options=[
            "Industry experience",
            "Only attendance",
            "No learning",
            "Only exams"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Internships expose students to real industry environments.",
    ),



    Question(

        question_code="COLLEGE-CAREER-008",

        question=
        "Which communication skill is important during interviews?",

        options=[
            "Clear explanation",
            "Avoiding answers",
            "Ignoring questions",
            "No interaction"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Clear communication helps express ideas effectively.",
    ),



    Question(

        question_code="COLLEGE-CAREER-009",

        question=
        "Which website is commonly used for code hosting?",

        options=[
            "GitHub",
            "YouTube",
            "Calculator",
            "WordPad"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "GitHub is used to store and manage code repositories.",
    ),



    Question(

        question_code="COLLEGE-CAREER-010",

        question=
        "Networking helps students to:",

        options=[
            "Find opportunities and connections",
            "Avoid learning",
            "Reduce skills",
            "Skip projects"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Professional networking helps discover career opportunities.",
    ),

]