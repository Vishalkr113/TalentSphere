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

        student_class="11-12",

        stream="ARTS",

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

        student_class="11-12",

        stream="ARTS",

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

        student_class="11-12",

        stream="ARTS",

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

        student_class="11-12",

        stream="ARTS",  

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

        student_class="11-12",

        stream="ARTS",

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

        student_class="11-12",

        stream="ARTS",

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

        student_class="11-12",

        stream="ARTS",

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

        student_class="11-12",

        stream="ARTS",

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

        student_class="11-12",

        stream="ARTS",

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

        student_class="11-12",

        stream="ARTS",

        explanation=
        "Democracy is a system where people choose their representatives.",
    ),


    # =====================================================
    # ADDITIONAL QUESTIONS (011–020)
    # =====================================================

    Question(
        question_code="HS-ARTS-011",
        question="The Revolt of 1857 began at:",
        options=[
            "Delhi",
            "Meerut",
            "Mumbai",
            "Kolkata"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.HISTORY,
        student_class="11-12",
        stream="ARTS",
        explanation="The Revolt of 1857 began at Meerut in May 1857.",
    ),
    Question(
        question_code="HS-ARTS-012",
        question="The Indian National Congress was founded in:",
        options=[
            "1885",
            "1905",
            "1919",
            "1947"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.HISTORY,
        student_class="11-12",
        stream="ARTS",
        explanation="The Indian National Congress was founded in 1885.",
    ),
    Question(
        question_code="HS-ARTS-013",
        question="The Tropic of Cancer passes through:",
        options=[
            "India",
            "Australia only",
            "United Kingdom",
            "Japan only"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GEOGRAPHY,
        student_class="11-12",
        stream="ARTS",
        explanation="The Tropic of Cancer passes through several Indian states.",
    ),
    Question(
        question_code="HS-ARTS-014",
        question="Which is a renewable natural resource?",
        options=[
            "Coal",
            "Petroleum",
            "Solar energy",
            "Natural gas"
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GEOGRAPHY,
        student_class="11-12",
        stream="ARTS",
        explanation="Solar energy is renewable because it is naturally replenished.",
    ),
    Question(
        question_code="HS-ARTS-015",
        question="The Constitution of India describes India as a:",
        options=[
            "Monarchy",
            "Sovereign socialist secular democratic republic",
            "Military state",
            "Colonial state"
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.POLITICAL_SCIENCE,
        student_class="11-12",
        stream="ARTS",
        explanation="The Preamble describes India as a sovereign socialist secular democratic republic.",
    ),
    Question(
        question_code="HS-ARTS-016",
        question="The Right to Equality is a:",
        options=[
            "Fundamental Right",
            "Directive Principle only",
            "Legal notice",
            "Tax rule"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.POLITICAL_SCIENCE,
        student_class="11-12",
        stream="ARTS",
        explanation="The Right to Equality is guaranteed as a Fundamental Right under Part III.",
    ),
    Question(
        question_code="HS-ARTS-017",
        question="Opportunity cost refers to:",
        options=[
            "The next best alternative forgone",
            "Total money saved",
            "Only production cost",
            "Government tax"
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,
        student_class="11-12",
        stream="ARTS",
        explanation="Opportunity cost is the value of the next best alternative given up.",
    ),
    Question(
        question_code="HS-ARTS-018",
        question="Socialization is the process through which individuals:",
        options=[
            "Learn social norms and values",
            "Study only geography",
            "Produce only goods",
            "Calculate taxes"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOCIOLOGY,
        student_class="11-12",
        stream="ARTS",
        explanation="Socialization helps individuals learn the norms, values and behaviors of society.",
    ),
    Question(
        question_code="HS-ARTS-019",
        question="Psychology is primarily concerned with the study of:",
        options=[
            "Behavior and mental processes",
            "Rocks and minerals",
            "Government budgets",
            "Chemical reactions"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PSYCHOLOGY,
        student_class="11-12",
        stream="ARTS",
        explanation="Psychology studies behavior and mental processes.",
    ),
    Question(
        question_code="HS-ARTS-020",
        question="A map scale shows the relationship between:",
        options=[
            "Map distance and ground distance",
            "Population and income",
            "Rainfall and temperature only",
            "Imports and exports"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GEOGRAPHY,
        student_class="11-12",
        stream="ARTS",
        explanation="Map scale relates a distance on the map to the corresponding ground distance.",
    ),


    Question(
        question_code="HS-ARTS-021",
        question=
        "The Indian Constitution came into force on:",
        options=[
            "15 August 1947",
            "26 January 1950",
            "26 November 1949",
            "2 October 1950",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.HISTORY,

        explanation=
        "The Constitution came into force on 26 January 1950.",
    ),

    Question(
        question_code="HS-ARTS-022",
        question=
        "The Industrial Revolution began first in:",
        options=[
            "Britain",
            "India",
            "Japan",
            "Brazil",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.HISTORY,

        explanation=
        "Britain was the first major center of the Industrial Revolution.",
    ),

    Question(
        question_code="HS-ARTS-023",
        question=
        "The United Nations was established in:",
        options=[
            "1919",
            "1945",
            "1955",
            "1965",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.HISTORY,

        explanation=
        "The UN was founded in 1945.",
    ),

    Question(
        question_code="HS-ARTS-024",
        question=
        "The term 'democracy' refers to government by:",
        options=[
            "A hereditary king only",
            "The people",
            "The military only",
            "Judges only",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.POLITICAL_SCIENCE,

        explanation=
        "Democracy is based on popular participation and consent.",
    ),

    Question(
        question_code="HS-ARTS-025",
        question=
        "Fundamental Rights in India are mainly contained in:",
        options=[
            "Part III",
            "Part I",
            "Part V",
            "Part IX",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.POLITICAL_SCIENCE,

        explanation=
        "Part III of the Constitution contains Fundamental Rights.",
    ),

    Question(
        question_code="HS-ARTS-026",
        question=
        "The Rajya Sabha is the:",
        options=[
            "Lower House",
            "Upper House",
            "State judiciary",
            "Election commission",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.POLITICAL_SCIENCE,

        explanation=
        "Rajya Sabha is the Council of States, the upper house of Parliament.",
    ),

    Question(
        question_code="HS-ARTS-027",
        question=
        "The Prime Minister of India is appointed by the:",
        options=[
            "President",
            "Chief Justice",
            "Speaker",
            "Election Commission",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.POLITICAL_SCIENCE,

        explanation=
        "The President appoints the Prime Minister.",
    ),

    Question(
        question_code="HS-ARTS-028",
        question=
        "Federalism involves division of powers between:",
        options=[
            "Different levels of government",
            "Only courts",
            "Only businesses",
            "Only villages",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.POLITICAL_SCIENCE,

        explanation=
        "Federal systems divide constitutional powers across levels of government.",
    ),

    Question(
        question_code="HS-ARTS-029",
        question=
        "A constitution primarily provides:",
        options=[
            "A framework of government and rights",
            "A company balance sheet",
            "A weather forecast",
            "A school timetable",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.POLITICAL_SCIENCE,

        explanation=
        "Constitutions establish institutions, powers, procedures and rights.",
    ),

    Question(
        question_code="HS-ARTS-030",
        question=
        "The Tropic of Cancer passes through:",
        options=[
            "India",
            "Australia only",
            "Canada only",
            "South Africa only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GEOGRAPHY,

        explanation=
        "The Tropic of Cancer crosses several Indian states.",
    ),

    Question(
        question_code="HS-ARTS-031",
        question=
        "The largest ocean is:",
        options=[
            "Atlantic",
            "Indian",
            "Pacific",
            "Arctic",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GEOGRAPHY,

        explanation=
        "The Pacific Ocean is the largest ocean.",
    ),

    Question(
        question_code="HS-ARTS-032",
        question=
        "Monsoon winds are important to India mainly because they:",
        options=[
            "Bring seasonal rainfall",
            "Create deserts everywhere",
            "Stop all rivers",
            "Cause earthquakes",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GEOGRAPHY,

        explanation=
        "Monsoon circulation supplies much of India's seasonal rainfall.",
    ),

    Question(
        question_code="HS-ARTS-033",
        question=
        "A delta is formed mainly by:",
        options=[
            "River deposition near its mouth",
            "Volcanic eruption only",
            "Glacial melting only",
            "Wind erosion only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GEOGRAPHY,

        explanation=
        "Sediment deposited near a river mouth can form a delta.",
    ),

    Question(
        question_code="HS-ARTS-034",
        question=
        "Latitude measures distance:",
        options=[
            "North or south of the Equator",
            "East or west of Greenwich",
            "Above sea level",
            "Between mountains",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GEOGRAPHY,

        explanation=
        "Latitude is angular distance north or south of the Equator.",
    ),

    Question(
        question_code="HS-ARTS-035",
        question=
        "A renewable resource is one that:",
        options=[
            "Can replenish naturally on a useful timescale",
            "Never changes",
            "Exists only underground",
            "Cannot be reused",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GEOGRAPHY,

        explanation=
        "Renewable resources can be naturally replenished.",
    ),

    Question(
        question_code="HS-ARTS-036",
        question=
        "Socialization is the process through which people:",
        options=[
            "Learn social norms and roles",
            "Stop communicating",
            "Avoid culture",
            "Become biologically identical",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOCIOLOGY,

        explanation=
        "Socialization transmits norms, values and roles.",
    ),

    Question(
        question_code="HS-ARTS-037",
        question=
        "Culture includes:",
        options=[
            "Shared values, beliefs and practices",
            "Only buildings",
            "Only income",
            "Only laws",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOCIOLOGY,

        explanation=
        "Culture encompasses learned shared meanings and practices.",
    ),

    Question(
        question_code="HS-ARTS-038",
        question=
        "A primary group is typically characterized by:",
        options=[
            "Close personal relationships",
            "Only formal contracts",
            "No interaction",
            "Temporary market exchange",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOCIOLOGY,

        explanation=
        "Primary groups such as families involve intimate, face-to-face relationships.",
    ),

    Question(
        question_code="HS-ARTS-039",
        question=
        "Social stratification refers to:",
        options=[
            "Structured inequality between social groups",
            "Random weather patterns",
            "Language translation",
            "Population counting only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOCIOLOGY,

        explanation=
        "Stratification organizes society into unequal social layers.",
    ),

    Question(
        question_code="HS-ARTS-040",
        question=
        "Psychology is the scientific study of:",
        options=[
            "Behavior and mental processes",
            "Only economics",
            "Only planets",
            "Only political parties",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PSYCHOLOGY,

        explanation=
        "Psychology studies behavior and mental processes.",
    ),

    Question(
        question_code="HS-ARTS-041",
        question=
        "Classical conditioning is associated with:",
        options=[
            "Learning through association",
            "Only memory loss",
            "Economic growth",
            "Political voting",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PSYCHOLOGY,

        explanation=
        "Classical conditioning links previously neutral stimuli with responses.",
    ),

    Question(
        question_code="HS-ARTS-042",
        question=
        "Short-term memory generally has:",
        options=[
            "Limited capacity and duration",
            "Unlimited storage",
            "No attention role",
            "Only visual content",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PSYCHOLOGY,

        explanation=
        "Working/short-term memory is limited in capacity and duration.",
    ),

    Question(
        question_code="HS-ARTS-043",
        question=
        "Motivation refers to processes that:",
        options=[
            "Energize and direct behavior",
            "Eliminate learning",
            "Stop decision-making",
            "Measure rainfall",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PSYCHOLOGY,

        explanation=
        "Motivation influences the direction, intensity and persistence of behavior.",
    ),

    Question(
        question_code="HS-ARTS-044",
        question=
        "A primary source in history is:",
        options=[
            "Evidence from the period studied",
            "A modern summary only",
            "A fictional novel about the past",
            "A random opinion",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.HISTORY,

        explanation=
        "Primary sources originate from the period or event being studied.",
    ),

    Question(
        question_code="HS-ARTS-045",
        question=
        "The Renaissance is associated with renewed interest in:",
        options=[
            "Classical learning and arts",
            "Only industrial machines",
            "Space travel",
            "Modern computing",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.HISTORY,

        explanation=
        "The Renaissance revived classical learning and artistic innovation.",
    ),

    Question(
        question_code="HS-ARTS-046",
        question=
        "The French Revolution began in:",
        options=[
            "1789",
            "1688",
            "1815",
            "1914",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.HISTORY,

        explanation=
        "The French Revolution began in 1789.",
    ),

    Question(
        question_code="HS-ARTS-047",
        question=
        "The Non-Cooperation Movement in India was led by:",
        options=[
            "Mahatma Gandhi",
            "Subhas Chandra Bose only",
            "Bhagat Singh only",
            "Dadabhai Naoroji only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.HISTORY,

        explanation=
        "Gandhi led the Non-Cooperation Movement beginning in 1920.",
    ),

    Question(
        question_code="HS-ARTS-048",
        question=
        "A parliamentary system typically has executive leadership drawn from:",
        options=[
            "The legislature",
            "The judiciary",
            "The army only",
            "The central bank",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.POLITICAL_SCIENCE,

        explanation=
        "In parliamentary systems, the executive is generally drawn from and accountable to the legislature.",
    ),

    Question(
        question_code="HS-ARTS-049",
        question=
        "Rule of law means:",
        options=[
            "Law applies equally and government acts under law",
            "Leaders are above law",
            "Only courts obey law",
            "Citizens have no rights",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.POLITICAL_SCIENCE,

        explanation=
        "Rule of law requires legal accountability and equality before law.",
    ),

    Question(
        question_code="HS-ARTS-050",
        question=
        "Urbanization means:",
        options=[
            "Growth of population in urban areas",
            "Decline of all cities",
            "Only rural farming",
            "Movement of rivers",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GEOGRAPHY,

        explanation=
        "Urbanization is the increasing share of people living in urban areas.",
    ),
]