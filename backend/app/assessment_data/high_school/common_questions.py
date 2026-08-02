from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


HIGH_SCHOOL_COMMON_QUESTIONS: list[Question] = [

    # =====================================================
    # HIGH SCHOOL COMMON (HS-COMMON-001–010)
    # =====================================================


    Question(

        question_code="HS-COMMON-001",

        question=
        "Which branch of science deals with living organisms?",

        options=[
            "Physics",
            "Chemistry",
            "Biology",
            "Mathematics"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BIOLOGY,

        explanation=
        "Biology is the study of living organisms.",
    ),



    Question(

        question_code="HS-COMMON-002",

        question=
        "What is the basic unit of life?",

        options=[
            "Atom",
            "Cell",
            "Tissue",
            "Organ"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BIOLOGY,

        explanation=
        "Cell is the basic structural and functional unit of life.",
    ),



    Question(

        question_code="HS-COMMON-003",

        question=
        "Which planet is known as the Red Planet?",

        options=[
            "Earth",
            "Mars",
            "Jupiter",
            "Venus"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.GENERAL_SCIENCE,

        explanation=
        "Mars appears red because of iron oxide on its surface.",
    ),



    Question(

        question_code="HS-COMMON-004",

        question=
        "What is the chemical formula of water?",

        options=[
            "CO2",
            "H2O",
            "O2",
            "NaCl"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CHEMISTRY,

        explanation=
        "Water contains two hydrogen atoms and one oxygen atom.",
    ),



    Question(

        question_code="HS-COMMON-005",

        question=
        "Which force attracts objects towards Earth?",

        options=[
            "Friction",
            "Gravity",
            "Magnetic Force",
            "Electric Force"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PHYSICS,

        explanation=
        "Gravity pulls objects towards Earth's center.",
    ),



    Question(

        question_code="HS-COMMON-006",

        question=
        "What is the SI unit of force?",

        options=[
            "Joule",
            "Newton",
            "Watt",
            "Pascal"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PHYSICS,

        explanation=
        "Newton is the SI unit of force.",
    ),



    Question(

        question_code="HS-COMMON-007",

        question=
        "Which organ pumps blood in the human body?",

        options=[
            "Brain",
            "Heart",
            "Lungs",
            "Kidney"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BIOLOGY,

        explanation=
        "Heart pumps blood throughout the body.",
    ),



    Question(

        question_code="HS-COMMON-008",

        question=
        "What is the value of π approximately?",

        options=[
            "2.14",
            "3.14",
            "4.14",
            "5.14"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.MATHEMATICS,

        explanation=
        "Pi value is approximately 3.14.",
    ),



    Question(

        question_code="HS-COMMON-009",

        question=
        "Which gas is essential for human respiration?",

        options=[
            "Nitrogen",
            "Oxygen",
            "Carbon Dioxide",
            "Hydrogen"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BIOLOGY,

        explanation=
        "Humans require oxygen for respiration.",
    ),



    Question(

        question_code="HS-COMMON-010",

        question=
        "Which mathematical operation is inverse of multiplication?",

        options=[
            "Addition",
            "Subtraction",
            "Division",
            "Power"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.MATHEMATICS,

        explanation=
        "Division is the inverse operation of multiplication.",
    ),





]