from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


PCM_QUESTIONS: list[Question] = [

    # =====================================================
    # PCM QUESTIONS (HS-PCM-001–010)
    # =====================================================


    Question(

        question_code="HS-PCM-001",

        question=
        "What is the SI unit of velocity?",

        options=[
            "m/s",
            "m²/s",
            "Newton",
            "Joule"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PHYSICS,

        explanation=
        "Velocity is measured in metre per second (m/s).",
    ),



    Question(

        question_code="HS-PCM-002",

        question=
        "Newton's first law of motion is also known as:",

        options=[
            "Law of Acceleration",
            "Law of Inertia",
            "Law of Gravitation",
            "Law of Energy"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PHYSICS,

        explanation=
        "Newton's first law explains the property of inertia.",
    ),



    Question(

        question_code="HS-PCM-003",

        question=
        "The rate of change of velocity is called:",

        options=[
            "Speed",
            "Acceleration",
            "Force",
            "Momentum"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PHYSICS,

        explanation=
        "Acceleration is the change in velocity per unit time.",
    ),



    Question(

        question_code="HS-PCM-004",

        question=
        "Which particle has a negative charge?",

        options=[
            "Proton",
            "Neutron",
            "Electron",
            "Nucleus"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CHEMISTRY,

        explanation=
        "Electron carries a negative electric charge.",
    ),



    Question(

        question_code="HS-PCM-005",

        question=
        "Atomic number represents the number of:",

        options=[
            "Neutrons",
            "Protons",
            "Electrons + Neutrons",
            "Atoms"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CHEMISTRY,

        explanation=
        "Atomic number is equal to the number of protons.",
    ),



    Question(

        question_code="HS-PCM-006",

        question=
        "pH value less than 7 represents:",

        options=[
            "Basic solution",
            "Neutral solution",
            "Acidic solution",
            "Salt solution"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CHEMISTRY,

        explanation=
        "Solutions with pH below 7 are acidic.",
    ),



    Question(

        question_code="HS-PCM-007",

        question=
        "Derivative of x² is:",

        options=[
            "x",
            "2x",
            "x²",
            "2"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.MATHEMATICS,

        explanation=
        "Using power rule, derivative of x² is 2x.",
    ),



    Question(

        question_code="HS-PCM-008",

        question=
        "Value of sin 90° is:",

        options=[
            "0",
            "1",
            "-1",
            "0.5"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.MATHEMATICS,

        explanation=
        "sin 90° has value 1.",
    ),



    Question(

        question_code="HS-PCM-009",

        question=
        "A matrix with equal number of rows and columns is called:",

        options=[
            "Rectangular Matrix",
            "Square Matrix",
            "Zero Matrix",
            "Row Matrix"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.MATHEMATICS,

        explanation=
        "A square matrix has equal rows and columns.",
    ),



    Question(

        question_code="HS-PCM-010",

        question=
        "Chemical bond formed by sharing electrons is called:",

        options=[
            "Ionic Bond",
            "Covalent Bond",
            "Metallic Bond",
            "Hydrogen Bond"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CHEMISTRY,

        explanation=
        "Covalent bonds are formed by sharing electrons.",
    ),

]