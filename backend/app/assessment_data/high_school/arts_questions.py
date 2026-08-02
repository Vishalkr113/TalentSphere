from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


ARTS_QUESTIONS: list[Question] = [

    # =====================================================
    # ARTS / HUMANITIES QUESTIONS (HS-ARTS-001–010)
    # =====================================================


    Question(

        question_code="HS-ARTS-001",

        question=
        "History is the study of:",

        options=[
            "Future events",
            "Past events",
            "Scientific experiments",
            "Mathematical formulas"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.HISTORY,

        explanation=
        "History deals with the study of past events and civilizations.",
    ),



    Question(

        question_code="HS-ARTS-002",

        question=
        "Geography mainly studies:",

        options=[
            "Earth and its features",
            "Human emotions",
            "Computer systems",
            "Chemical reactions"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.GEOGRAPHY,

        explanation=
        "Geography studies Earth's physical features and human activities.",
    ),



    Question(

        question_code="HS-ARTS-003",

        question=
        "Political Science is related to the study of:",

        options=[
            "Government and politics",
            "Plants",
            "Numbers",
            "Machines"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.POLITICAL_SCIENCE,

        explanation=
        "Political Science studies government systems and political activities.",
    ),



    Question(

        question_code="HS-ARTS-004",

        question=
        "Sociology is the study of:",

        options=[
            "Society",
            "Space",
            "Animals",
            "Technology"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOCIOLOGY,

        explanation=
        "Sociology studies human society and social relationships.",
    ),



    Question(

        question_code="HS-ARTS-005",

        question=
        "The Constitution of India came into effect on:",

        options=[
            "15 August 1947",
            "26 January 1950",
            "2 October 1948",
            "26 November 1949"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.POLITICAL_SCIENCE,

        explanation=
        "Indian Constitution came into effect on 26 January 1950.",
    ),



    Question(

        question_code="HS-ARTS-006",

        question=
        "Economics mainly deals with:",

        options=[
            "Resources and production",
            "Human body",
            "Chemical elements",
            "Computer programs"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ECONOMICS,

        explanation=
        "Economics studies production, distribution and consumption of resources.",
    ),



    Question(

        question_code="HS-ARTS-007",

        question=
        "Who is known as the Father of Indian Constitution?",

        options=[
            "Mahatma Gandhi",
            "Dr. B. R. Ambedkar",
            "Jawaharlal Nehru",
            "Sardar Patel"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.HISTORY,

        explanation=
        "Dr. B. R. Ambedkar played a major role in drafting the Indian Constitution.",
    ),



    Question(

        question_code="HS-ARTS-008",

        question=
        "Which subject studies human behavior and mind?",

        options=[
            "Psychology",
            "Physics",
            "Chemistry",
            "Mathematics"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PSYCHOLOGY,

        explanation=
        "Psychology studies human behavior and mental processes.",
    ),



    Question(

        question_code="HS-ARTS-009",

        question=
        "Culture refers to:",

        options=[
            "Way of life of people",
            "Only language",
            "Only food",
            "Only clothing"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOCIOLOGY,

        explanation=
        "Culture includes traditions, beliefs, values and lifestyle.",
    ),



    Question(

        question_code="HS-ARTS-010",

        question=
        "Democracy means:",

        options=[
            "Rule by people",
            "Rule by king",
            "Military rule",
            "No government"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.POLITICAL_SCIENCE,

        explanation=
        "Democracy is a system where people choose their representatives.",
    ),

]