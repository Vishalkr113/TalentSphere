from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


PROFESSIONAL_TECHNICAL_QUESTIONS: list[Question] = [

    # =====================================================
    # PROFESSIONAL TECHNICAL (PROFESSIONAL-TECH-001–010)
    # =====================================================


    Question(

        question_code="PROFESSIONAL-TECH-001",

        question=
        "Which programming paradigm does Java mainly support?",

        options=[
            "Object-Oriented Programming",
            "Only Functional Programming",
            "Markup Programming",
            "Database Programming"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROGRAMMING,

        explanation=
        "Java is mainly based on Object-Oriented Programming concepts.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-002",

        question=
        "Which principle hides internal details of an object?",

        options=[
            "Encapsulation",
            "Inheritance",
            "Polymorphism",
            "Compilation"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.OOP,

        explanation=
        "Encapsulation hides data and implementation details.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-003",

        question=
        "Which database language is used to manage relational databases?",

        options=[
            "SQL",
            "HTML",
            "CSS",
            "XML"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DBMS,

        explanation=
        "SQL is used for managing relational database systems.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-004",

        question=
        "Which HTTP method is commonly used to retrieve data?",

        options=[
            "POST",
            "GET",
            "DELETE",
            "PATCH"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "GET method is used to request and retrieve data.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-005",

        question=
        "Which technology is used for containerization?",

        options=[
            "Docker",
            "Excel",
            "Photoshop",
            "Notepad"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "Docker is a popular containerization platform.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-006",

        question=
        "Which version control system is widely used in software development?",

        options=[
            "Git",
            "Paint",
            "Word",
            "Calculator"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Git is used for tracking code changes.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-007",

        question=
        "Which data structure is used for implementing BFS?",

        options=[
            "Stack",
            "Queue",
            "Heap",
            "Array"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "BFS uses Queue for level-wise traversal.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-008",

        question=
        "Which cloud service model provides virtual machines?",

        options=[
            "IaaS",
            "SaaS",
            "PaaS",
            "DBaaS"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "Infrastructure as a Service provides virtualized computing resources.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-009",

        question=
        "Which testing checks individual software components?",

        options=[
            "Unit Testing",
            "System Testing",
            "Performance Testing",
            "Security Testing"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_TESTING,

        explanation=
        "Unit testing verifies individual modules or components.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-010",

        question=
        "API stands for:",

        options=[
            "Application Programming Interface",
            "Advanced Program Internet",
            "Application Process Integration",
            "Automatic Programming Input"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "API allows communication between different software systems.",
    ),

]