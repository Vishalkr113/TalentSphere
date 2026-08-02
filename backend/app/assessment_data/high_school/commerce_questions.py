from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


COMMERCE_QUESTIONS: list[Question] = [

    # =====================================================
    # COMMERCE QUESTIONS (HS-COMMERCE-001–010)
    # =====================================================


    Question(

        question_code="HS-COMMERCE-001",

        question=
        "Accounting is mainly concerned with:",

        options=[
            "Recording financial transactions",
            "Manufacturing products",
            "Selling goods",
            "Hiring employees"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.COMMERCE,

        explanation=
        "Accounting records, classifies and summarizes financial transactions.",
    ),



    Question(

        question_code="HS-COMMERCE-002",

        question=
        "The basic accounting equation is:",

        options=[
            "Assets = Liabilities + Capital",
            "Assets = Income + Expense",
            "Profit = Assets",
            "Capital = Expense"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ACCOUNTING,

        explanation=
        "The accounting equation is Assets = Liabilities + Owner's Equity.",
    ),



    Question(

        question_code="HS-COMMERCE-003",

        question=
        "Which book records daily transactions in accounting?",

        options=[
            "Ledger",
            "Journal",
            "Balance Sheet",
            "Cash Flow"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ACCOUNTING,

        explanation=
        "Journal is used for recording daily financial transactions.",
    ),



    Question(

        question_code="HS-COMMERCE-004",

        question=
        "A person who starts and manages a business is called:",

        options=[
            "Consumer",
            "Entrepreneur",
            "Employee",
            "Manager"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BUSINESS,

        explanation=
        "An entrepreneur starts and manages a business venture.",
    ),



    Question(

        question_code="HS-COMMERCE-005",

        question=
        "GDP stands for:",

        options=[
            "Gross Domestic Product",
            "General Development Plan",
            "Gross Demand Price",
            "Government Development Process"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ECONOMICS,

        explanation=
        "GDP represents total value of goods and services produced in a country.",
    ),



    Question(

        question_code="HS-COMMERCE-006",

        question=
        "Demand and supply are concepts of:",

        options=[
            "Physics",
            "Economics",
            "Biology",
            "Computer Science"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ECONOMICS,

        explanation=
        "Demand and supply are fundamental concepts in economics.",
    ),



    Question(

        question_code="HS-COMMERCE-007",

        question=
        "Which document shows financial position of a business?",

        options=[
            "Journal",
            "Balance Sheet",
            "Invoice",
            "Receipt"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ACCOUNTING,

        explanation=
        "Balance Sheet shows assets, liabilities and capital.",
    ),



    Question(

        question_code="HS-COMMERCE-008",

        question=
        "Marketing mainly focuses on:",

        options=[
            "Customer needs",
            "Only production",
            "Machine repair",
            "Accounting records"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BUSINESS,

        explanation=
        "Marketing identifies and satisfies customer needs.",
    ),



    Question(

        question_code="HS-COMMERCE-009",

        question=
        "Profit is calculated as:",

        options=[
            "Income - Expenses",
            "Assets - Liabilities",
            "Sales + Cost",
            "Capital - Assets"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ACCOUNTING,

        explanation=
        "Profit equals total income minus total expenses.",
    ),



    Question(

        question_code="HS-COMMERCE-010",

        question=
        "Banking is a part of which sector?",

        options=[
            "Primary Sector",
            "Secondary Sector",
            "Service Sector",
            "Agriculture Sector"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ECONOMICS,

        explanation=
        "Banking comes under the service sector.",
    ),

]