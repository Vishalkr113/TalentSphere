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

        student_class="9-10",

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

        student_class="9-10",

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

        student_class="9-10",

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

        student_class="9-10",

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

        student_class="9-10",

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

        student_class="9-10",

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

        student_class="9-10",

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

        student_class="9-10",

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

        student_class="9-10",

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

        student_class="9-10",

        explanation=
        "Division is the inverse operation of multiplication.",
    ),






    # =====================================================
    # ADDITIONAL QUESTIONS (011–020)
    # =====================================================

    Question(
        question_code="HS-COMMON-011",
        question="Which vitamin is mainly produced in the skin in response to sunlight?",
        options=[
            "Vitamin A",
            "Vitamin B12",
            "Vitamin C",
            "Vitamin D"
        ],
        answer="D",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,
        student_class="9-10",
        stream="None",
        explanation="Vitamin D can be synthesized in the skin when exposed to sunlight.",
    ),
    Question(
        question_code="HS-COMMON-012",
        question="Which gas is most abundant in Earth's atmosphere?",
        options=[
            "Oxygen",
            "Nitrogen",
            "Carbon dioxide",
            "Hydrogen"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GENERAL_SCIENCE,
        student_class="9-10",
        stream="None",
        explanation="Nitrogen makes up about 78 percent of Earth's atmosphere.",
    ),
    Question(
        question_code="HS-COMMON-013",
        question="The boiling point of water at sea level is:",
        options=[
            "0°C",
            "50°C",
            "100°C",
            "150°C"
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,
        student_class="9-10",
        stream="None",
        explanation="At standard atmospheric pressure, water boils at 100°C.",
    ),
    Question(
        question_code="HS-COMMON-014",
        question="Which of the following is a chemical change?",
        options=[
            "Melting ice",
            "Cutting paper",
            "Rusting iron",
            "Breaking glass"
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,
        student_class="9-10",
        stream="None",
        explanation="Rusting forms a new substance, so it is a chemical change.",
    ),
    Question(
        question_code="HS-COMMON-015",
        question="Which organ is mainly responsible for filtering waste from blood?",
        options=[
            "Heart",
            "Kidney",
            "Stomach",
            "Lung"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,
        student_class="9-10",
        stream="None",
        explanation="The kidneys filter blood and help remove metabolic wastes.",
    ),
    Question(
        question_code="HS-COMMON-016",
        question="If x + 5 = 12, the value of x is:",
        options=[
            "5",
            "7",
            "12",
            "17"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,
        student_class="9-10",
        stream="None",
        explanation="Subtracting 5 from both sides gives x = 7.",
    ),
    Question(
        question_code="HS-COMMON-017",
        question="The perimeter of a square with side 4 cm is:",
        options=[
            "8 cm",
            "12 cm",
            "16 cm",
            "20 cm"
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,
        student_class="9-10",
        stream="None",
        explanation="Perimeter of a square is 4 times its side, so 16 cm.",
    ),
    Question(
        question_code="HS-COMMON-018",
        question="Which instrument is used to measure temperature?",
        options=[
            "Barometer",
            "Thermometer",
            "Ammeter",
            "Hygrometer"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,
        student_class="9-10",
        stream="None",
        explanation="A thermometer is used to measure temperature.",
    ),
    Question(
        question_code="HS-COMMON-019",
        question="The process by which green plants make food is called:",
        options=[
            "Respiration",
            "Photosynthesis",
            "Digestion",
            "Transpiration"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,
        student_class="9-10",
        stream="None",
        explanation="Green plants use light energy to make food by photosynthesis.",
    ),
    Question(
        question_code="HS-COMMON-020",
        question="Which metal is liquid at room temperature?",
        options=[
            "Iron",
            "Copper",
            "Mercury",
            "Aluminium"
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GENERAL_SCIENCE,
        student_class="9-10",
        stream="None",
        explanation="Mercury is a metal that is liquid at ordinary room temperature.",
    ),


    Question(
        question_code="HS-COMMON-021",
        question=
        "Which organ pumps blood through the human body?",
        options=[
            "Lungs",
            "Heart",
            "Kidney",
            "Stomach",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GENERAL_SCIENCE,

        explanation=
        "The heart pumps blood through the circulatory system.",
    ),

    Question(
        question_code="HS-COMMON-022",
        question=
        "Water boils at sea level at approximately:",
        options=[
            "50°C",
            "75°C",
            "100°C",
            "150°C",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GENERAL_SCIENCE,

        explanation=
        "At standard atmospheric pressure, water boils at about 100°C.",
    ),

    Question(
        question_code="HS-COMMON-023",
        question=
        "The chemical symbol for sodium is:",
        options=[
            "So",
            "Na",
            "S",
            "Sn",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Sodium uses the symbol Na.",
    ),

    Question(
        question_code="HS-COMMON-024",
        question=
        "Which planet is known for its prominent rings?",
        options=[
            "Mars",
            "Saturn",
            "Mercury",
            "Venus",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GENERAL_SCIENCE,

        explanation=
        "Saturn is well known for its extensive ring system.",
    ),

    Question(
        question_code="HS-COMMON-025",
        question=
        "Which device converts electrical energy into mechanical motion?",
        options=[
            "Motor",
            "Battery only",
            "Resistor",
            "Fuse",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER,

        explanation=
        "An electric motor converts electrical energy into mechanical energy.",
    ),

    Question(
        question_code="HS-COMMON-026",
        question=
        "Binary numbers use which two digits?",
        options=[
            "0 and 1",
            "1 and 2",
            "0 and 2",
            "2 and 3",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER,

        explanation=
        "Binary is a base-2 number system using 0 and 1.",
    ),

    Question(
        question_code="HS-COMMON-027",
        question=
        "CPU stands for:",
        options=[
            "Central Processing Unit",
            "Computer Power Utility",
            "Core Program User",
            "Central Print Unit",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER,

        explanation=
        "CPU means Central Processing Unit.",
    ),

    Question(
        question_code="HS-COMMON-028",
        question=
        "Which storage is non-volatile?",
        options=[
            "RAM",
            "Cache",
            "SSD",
            "CPU register",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER,

        explanation=
        "SSD retains data without power.",
    ),

    Question(
        question_code="HS-COMMON-029",
        question=
        "A web browser is used mainly to:",
        options=[
            "Access web content",
            "Compile electricity",
            "Measure temperature",
            "Format hard drives",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER,

        explanation=
        "Browsers retrieve and render web content.",
    ),

    Question(
        question_code="HS-COMMON-030",
        question=
        "Which is a strong password practice?",
        options=[
            "Use a unique long password",
            "Reuse one password everywhere",
            "Share it publicly",
            "Use only your name",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER,

        explanation=
        "Long unique passwords reduce credential-reuse risk.",
    ),

    Question(
        question_code="HS-COMMON-031",
        question=
        "Which sentence is grammatically correct?",
        options=[
            "She go to school.",
            "She goes to school.",
            "She going school.",
            "She gone school.",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ENGLISH,

        explanation=
        "With singular subject 'she', the simple present verb is 'goes'.",
    ),

    Question(
        question_code="HS-COMMON-032",
        question=
        "A synonym of 'rapid' is:",
        options=[
            "Slow",
            "Quick",
            "Weak",
            "Late",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ENGLISH,

        explanation=
        "Rapid means quick or fast.",
    ),

    Question(
        question_code="HS-COMMON-033",
        question=
        "The mean of 4, 6 and 8 is:",
        options=[
            "5",
            "6",
            "7",
            "8",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "(4+6+8)/3 = 6.",
    ),

    Question(
        question_code="HS-COMMON-034",
        question=
        "If a triangle has angles 60°, 60° and 60°, it is:",
        options=[
            "Right",
            "Isosceles only",
            "Equilateral",
            "Scalene",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "All three equal angles imply an equilateral triangle.",
    ),

    Question(
        question_code="HS-COMMON-035",
        question=
        "What is 15% of 200?",
        options=[
            "20",
            "25",
            "30",
            "35",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "0.15 × 200 = 30.",
    ),

    Question(
        question_code="HS-COMMON-036",
        question=
        "Which force pulls objects toward Earth?",
        options=[
            "Friction",
            "Gravity",
            "Magnetism only",
            "Buoyancy",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "Gravity attracts masses toward Earth.",
    ),

    Question(
        question_code="HS-COMMON-037",
        question=
        "Which material is generally a good conductor of electricity?",
        options=[
            "Copper",
            "Rubber",
            "Glass",
            "Dry wood",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "Copper has high electrical conductivity.",
    ),

    Question(
        question_code="HS-COMMON-038",
        question=
        "Which gas makes up most of Earth's atmosphere?",
        options=[
            "Oxygen",
            "Nitrogen",
            "Carbon dioxide",
            "Hydrogen",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GENERAL_SCIENCE,

        explanation=
        "Nitrogen is the largest component of Earth's atmosphere.",
    ),

    Question(
        question_code="HS-COMMON-039",
        question=
        "The smallest unit of an element that retains its chemical identity is:",
        options=[
            "Molecule only",
            "Atom",
            "Tissue",
            "Cell",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "An atom is the basic unit of an element.",
    ),

    Question(
        question_code="HS-COMMON-040",
        question=
        "Which process changes liquid water into vapor?",
        options=[
            "Condensation",
            "Evaporation",
            "Freezing",
            "Melting",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GENERAL_SCIENCE,

        explanation=
        "Evaporation changes liquid to vapor.",
    ),

    Question(
        question_code="HS-COMMON-041",
        question=
        "A URL identifies:",
        options=[
            "A resource address on the web",
            "A computer battery",
            "A keyboard key",
            "A database table only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER,

        explanation=
        "URL means Uniform Resource Locator.",
    ),

    Question(
        question_code="HS-COMMON-042",
        question=
        "Which protocol is commonly used to securely access websites?",
        options=[
            "HTTP",
            "HTTPS",
            "FTP only",
            "SMTP",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER,

        explanation=
        "HTTPS adds encryption/authentication to HTTP connections.",
    ),

    Question(
        question_code="HS-COMMON-043",
        question=
        "Which part of a plant absorbs most water from soil?",
        options=[
            "Flower",
            "Roots",
            "Fruit",
            "Stem tip only",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GENERAL_SCIENCE,

        explanation=
        "Roots absorb water and minerals from soil.",
    ),

    Question(
        question_code="HS-COMMON-044",
        question=
        "The pH of pure water at room temperature is approximately:",
        options=[
            "3",
            "5",
            "7",
            "11",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Pure water is approximately neutral at pH 7.",
    ),

    Question(
        question_code="HS-COMMON-045",
        question=
        "Which number is prime?",
        options=[
            "21",
            "29",
            "35",
            "39",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "29 has no positive divisors other than 1 and itself.",
    ),

    Question(
        question_code="HS-COMMON-046",
        question=
        "The perimeter of a square with side 5 cm is:",
        options=[
            "10 cm",
            "15 cm",
            "20 cm",
            "25 cm",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "Perimeter = 4×5 = 20 cm.",
    ),

    Question(
        question_code="HS-COMMON-047",
        question=
        "Which renewable source uses moving air?",
        options=[
            "Solar",
            "Wind",
            "Coal",
            "Petroleum",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GENERAL_SCIENCE,

        explanation=
        "Wind energy uses moving air to generate power.",
    ),

    Question(
        question_code="HS-COMMON-048",
        question=
        "An algorithm is best described as:",
        options=[
            "A step-by-step procedure for solving a problem",
            "A physical cable",
            "A web browser",
            "A storage device",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER,

        explanation=
        "An algorithm is a finite sequence of steps for solving a problem.",
    ),

    Question(
        question_code="HS-COMMON-049",
        question=
        "Which chart is useful for comparing categories?",
        options=[
            "Bar chart",
            "Only a map",
            "Only a paragraph",
            "Audio file",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "Bar charts compare values across categories.",
    ),

    Question(
        question_code="HS-COMMON-050",
        question=
        "Which practice helps verify information found online?",
        options=[
            "Check reliable sources and corroborate claims",
            "Trust every headline",
            "Ignore dates",
            "Share immediately",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER,

        explanation=
        "Cross-checking reliable sources improves information quality.",
    ),
]