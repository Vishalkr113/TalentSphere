from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


COLLEGE_COMMON_QUESTIONS: list[Question] = [

    # =====================================================
    # COLLEGE COMMON QUESTIONS (COLLEGE-COMMON-001–010)
    # =====================================================


    Question(

        question_code="COLLEGE-COMMON-001",

        question=
        "Which skill is most important for career growth in technology?",

        options=[
            "Continuous Learning",
            "Ignoring new technology",
            "Only theoretical knowledge",
            "Avoiding practice"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Continuous learning helps professionals adapt to new technologies.",
    ),



    Question(

        question_code="COLLEGE-COMMON-002",

        question=
        "Which document is commonly used to apply for jobs?",

        options=[
            "Resume",
            "Invoice",
            "Receipt",
            "Certificate only"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Resume contains education, skills and experience details.",
    ),



    Question(

        question_code="COLLEGE-COMMON-003",

        question=
        "What does GPA represent?",

        options=[
            "Grade Point Average",
            "General Program Access",
            "Global Performance Area",
            "Grade Percentage Amount"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.EDUCATION,

        explanation=
        "GPA represents the average grade points obtained by a student.",
    ),



    Question(

        question_code="COLLEGE-COMMON-004",

        question=
        "Which activity improves programming skills?",

        options=[
            "Regular Coding Practice",
            "Avoiding projects",
            "Only reading theory",
            "Skipping problems"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROGRAMMING,

        explanation=
        "Regular coding practice improves problem-solving ability.",
    ),



    Question(

        question_code="COLLEGE-COMMON-005",

        question=
        "Which platform is commonly used for version control?",

        options=[
            "GitHub",
            "MS Paint",
            "Calculator",
            "Notepad"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "GitHub hosts Git repositories and manages code versions.",
    ),



    Question(

        question_code="COLLEGE-COMMON-006",

        question=
        "Soft skills include:",

        options=[
            "Communication and teamwork",
            "Only programming",
            "Only mathematics",
            "Only hardware knowledge"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Soft skills improve communication and professional interaction.",
    ),



    Question(

        question_code="COLLEGE-COMMON-007",

        question=
        "Internships help students by providing:",

        options=[
            "Practical experience",
            "Only marks",
            "No learning",
            "Only certificates"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Internships provide real-world industry experience.",
    ),



    Question(

        question_code="COLLEGE-COMMON-008",

        question=
        "Which is important before a technical interview?",

        options=[
            "Practice and preparation",
            "Ignoring concepts",
            "No revision",
            "Avoiding questions"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Preparation improves confidence and interview performance.",
    ),



    Question(

        question_code="COLLEGE-COMMON-009",

        question=
        "A project portfolio helps to:",

        options=[
            "Show practical skills",
            "Replace learning",
            "Avoid coding",
            "Remove experience"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Portfolio demonstrates projects and technical abilities.",
    ),



    Question(

        question_code="COLLEGE-COMMON-010",

        question=
        "Problem solving ability is improved by:",

        options=[
            "Practice and logical thinking",
            "Memorizing only",
            "Avoiding challenges",
            "Skipping algorithms"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Regular practice develops logical thinking and problem-solving skills.",
    ),

]