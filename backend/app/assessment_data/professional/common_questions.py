from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


PROFESSIONAL_COMMON_QUESTIONS: list[Question] = [

    # =====================================================
    # PROFESSIONAL COMMON (PROFESSIONAL-COMMON-001–010)
    # =====================================================


    Question(

        question_code="PROFESSIONAL-COMMON-001",

        question=
        "Professional communication mainly focuses on:",

        options=[
            "Clear exchange of information",
            "Avoiding discussion",
            "Ignoring feedback",
            "Using difficult words only"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Professional communication requires clear and effective information sharing.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-002",

        question=
        "Teamwork means:",

        options=[
            "Working together to achieve a goal",
            "Working alone always",
            "Avoiding responsibilities",
            "Ignoring team members"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Teamwork involves collaboration among team members.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-003",

        question=
        "A good leader should have:",

        options=[
            "Decision making ability",
            "No responsibility",
            "Poor communication",
            "No planning"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.LEADERSHIP,

        explanation=
        "Leadership requires decision making and responsibility.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-004",

        question=
        "Time management helps to:",

        options=[
            "Complete tasks efficiently",
            "Delay work",
            "Avoid planning",
            "Reduce productivity"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Time management improves productivity and task completion.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-005",

        question=
        "Feedback is useful because it:",

        options=[
            "Improves performance",
            "Creates confusion only",
            "Stops learning",
            "Avoids improvement"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Constructive feedback helps improve skills and performance.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-006",

        question=
        "A professional should maintain:",

        options=[
            "Work ethics",
            "Negative attitude",
            "Poor communication",
            "Irresponsibility"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Work ethics are important for professional behavior.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-007",

        question=
        "Problem solving requires:",

        options=[
            "Logical thinking",
            "Ignoring problems",
            "Random decisions",
            "Avoiding analysis"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Logical thinking helps identify and solve problems.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-008",

        question=
        "Adaptability means:",

        options=[
            "Ability to adjust with changes",
            "Rejecting changes",
            "Avoiding learning",
            "Stopping improvement"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Adaptability helps professionals handle changing situations.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-009",

        question=
        "A professional resume should be:",

        options=[
            "Clear and relevant",
            "Very lengthy with unnecessary details",
            "Without skills",
            "Incomplete"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "A resume should clearly highlight relevant skills and experience.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-010",

        question=
        "Continuous learning helps professionals to:",

        options=[
            "Stay updated with skills",
            "Stop growth",
            "Avoid technology",
            "Reduce knowledge"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Continuous learning keeps professionals updated and competitive.",
    ),

]