from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


COLLEGE_TECHNICAL_QUESTIONS: list[Question] = [

    # =====================================================
    # COLLEGE TECHNICAL (COLLEGE-TECH-001–010)
    # =====================================================


    Question(

        question_code="COLLEGE-TECH-001",

        question=
        "Which data structure follows LIFO principle?",

        options=[
            "Queue",
            "Stack",
            "Tree",
            "Graph"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Stack follows Last In First Out principle.",
    ),



    Question(

        question_code="COLLEGE-TECH-002",

        question=
        "Which OOP concept allows code reusability?",

        options=[
            "Inheritance",
            "Encapsulation",
            "Abstraction",
            "Polymorphism"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.OOP,

        explanation=
        "Inheritance allows one class to reuse properties of another class.",
    ),



    Question(

        question_code="COLLEGE-TECH-003",

        question=
        "Which SQL command is used to retrieve data?",

        options=[
            "INSERT",
            "SELECT",
            "UPDATE",
            "DELETE"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DBMS,

        explanation=
        "SELECT command retrieves records from database tables.",
    ),



    Question(

        question_code="COLLEGE-TECH-004",

        question=
        "Which normal form removes partial dependency?",

        options=[
            "1NF",
            "2NF",
            "3NF",
            "BCNF"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DBMS,

        explanation=
        "Second Normal Form removes partial dependency.",
    ),



    Question(

        question_code="COLLEGE-TECH-005",

        question=
        "Which protocol is used for secure web communication?",

        options=[
            "HTTP",
            "HTTPS",
            "FTP",
            "SMTP"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.COMPUTER_NETWORK,

        explanation=
        "HTTPS provides secure communication using encryption.",
    ),



    Question(

        question_code="COLLEGE-TECH-006",

        question=
        "Which OS component manages process scheduling?",

        options=[
            "Compiler",
            "Scheduler",
            "Loader",
            "Editor"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.OPERATING_SYSTEM,

        explanation=
        "Scheduler decides which process gets CPU time.",
    ),



    Question(

        question_code="COLLEGE-TECH-007",

        question=
        "Which algorithm is used for shortest path finding?",

        options=[
            "Dijkstra",
            "Bubble Sort",
            "Binary Search",
            "DFS only"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Dijkstra algorithm finds shortest path from source node.",
    ),



    Question(

        question_code="COLLEGE-TECH-008",

        question=
        "Which language is known as an object-oriented programming language?",

        options=[
            "HTML",
            "Java",
            "SQL",
            "CSS"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROGRAMMING,

        explanation=
        "Java supports object-oriented programming concepts.",
    ),



    Question(

        question_code="COLLEGE-TECH-009",

        question=
        "Which memory is fastest in computer hierarchy?",

        options=[
            "Hard Disk",
            "RAM",
            "Cache Memory",
            "DVD"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.COMPUTER_ARCHITECTURE,

        explanation=
        "Cache memory is faster than RAM and storage devices.",
    ),



    Question(

        question_code="COLLEGE-TECH-010",

        question=
        "Which technology is used for version control?",

        options=[
            "Git",
            "Excel",
            "PowerPoint",
            "Photoshop"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Git is a distributed version control system.",
    ),

]