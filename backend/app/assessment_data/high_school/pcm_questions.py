from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


PCM_QUESTIONS: list[Question] = [

    # =====================================================
    # HIGH SCHOOL PCM (CLASS 11-12)
    # =====================================================


    Question(
        question_code="HS-PCM-001",

        question="What is the SI unit of velocity?",

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

        student_class="11-12",

        stream="PCM",

        explanation=
        "Velocity is measured in metre per second (m/s).",
    ),



    Question(
        question_code="HS-PCM-002",

        question="Newton's first law of motion is also known as:",

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

        student_class="11-12",

        stream="PCM",

        explanation=
        "Newton's first law explains the property of inertia.",
    ),



    Question(
        question_code="HS-PCM-003",

        question="The rate of change of velocity is called:",

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

        student_class="11-12",

        stream="PCM",

        explanation=
        "Acceleration is the change in velocity per unit time.",
    ),



    Question(
        question_code="HS-PCM-004",

        question="Which particle has a negative charge?",

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

        student_class="11-12",

        stream="PCM",

        explanation=
        "Electron carries a negative electric charge.",
    ),



    Question(
        question_code="HS-PCM-005",

        question="Atomic number represents the number of:",

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

        student_class="11-12",

        stream="PCM",

        explanation=
        "Atomic number is equal to the number of protons.",
    ),



    Question(
        question_code="HS-PCM-006",

        question="pH value less than 7 represents:",

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

        student_class="11-12",

        stream="PCM",

        explanation=
        "Solutions with pH below 7 are acidic.",
    ),



    Question(
        question_code="HS-PCM-007",

        question="Derivative of x² is:",

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

        student_class="11-12",

        stream="PCM",

        explanation=
        "Using power rule, derivative of x² is 2x.",
    ),



    Question(
        question_code="HS-PCM-008",

        question="Value of sin 90° is:",

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

        student_class="11-12",

        stream="PCM",

        explanation=
        "sin 90° has value 1.",
    ),



    Question(
        question_code="HS-PCM-009",

        question="A matrix with equal number of rows and columns is called:",

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

        student_class="11-12",

        stream="PCM",

        explanation=
        "A square matrix has equal rows and columns.",
    ),



    Question(
        question_code="HS-PCM-010",

        question="Chemical bond formed by sharing electrons is called:",

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

        student_class="11-12",

        stream="PCM",

        explanation=
        "Covalent bonds are formed by sharing electrons.",
    ),


    # =====================================================
    # ADDITIONAL QUESTIONS (011–020)
    # =====================================================

    Question(
        question_code="HS-PCM-011",
        question="If a body moves with constant velocity, its acceleration is:",
        options=[
            "Zero",
            "Constant but non-zero",
            "Increasing",
            "Decreasing"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,
        student_class="11-12",
        stream="PCM",
        explanation="Acceleration is zero when velocity remains constant.",
    ),
    Question(
        question_code="HS-PCM-012",
        question="The SI unit of work is:",
        options=[
            "Watt",
            "Joule",
            "Newton",
            "Pascal"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,
        student_class="11-12",
        stream="PCM",
        explanation="Work is measured in joules in the SI system.",
    ),
    Question(
        question_code="HS-PCM-013",
        question="Ohm's law is represented by:",
        options=[
            "V = IR",
            "P = VI",
            "F = ma",
            "Q = It"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,
        student_class="11-12",
        stream="PCM",
        explanation="Ohm's law states that voltage equals current multiplied by resistance.",
    ),
    Question(
        question_code="HS-PCM-014",
        question="Which quantity is a scalar?",
        options=[
            "Velocity",
            "Displacement",
            "Speed",
            "Acceleration"
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,
        student_class="11-12",
        stream="PCM",
        explanation="Speed has magnitude only and is therefore a scalar.",
    ),
    Question(
        question_code="HS-PCM-015",
        question="The number of protons plus neutrons in an atom is called:",
        options=[
            "Atomic number",
            "Mass number",
            "Valency",
            "Period number"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,
        student_class="11-12",
        stream="PCM",
        explanation="Mass number is the total number of protons and neutrons.",
    ),
    Question(
        question_code="HS-PCM-016",
        question="Which gas is evolved when an acid reacts with a metal?",
        options=[
            "Oxygen",
            "Hydrogen",
            "Nitrogen",
            "Chlorine"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,
        student_class="11-12",
        stream="PCM",
        explanation="Acids commonly release hydrogen gas when they react with active metals.",
    ),
    Question(
        question_code="HS-PCM-017",
        question="A substance that speeds up a chemical reaction without being consumed is a:",
        options=[
            "Reactant",
            "Catalyst",
            "Solvent",
            "Product"
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,
        student_class="11-12",
        stream="PCM",
        explanation="A catalyst changes reaction rate without being consumed in the overall reaction.",
    ),
    Question(
        question_code="HS-PCM-018",
        question="The integral of 1 with respect to x is:",
        options=[
            "1",
            "x",
            "x²",
            "0"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,
        student_class="11-12",
        stream="PCM",
        explanation="The antiderivative of 1 is x plus a constant.",
    ),
    Question(
        question_code="HS-PCM-019",
        question="The determinant of a 2 × 2 identity matrix is:",
        options=[
            "0",
            "1",
            "2",
            "-1"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,
        student_class="11-12",
        stream="PCM",
        explanation="The identity matrix has determinant 1.",
    ),
    Question(
        question_code="HS-PCM-020",
        question="The probability of getting a head when a fair coin is tossed once is:",
        options=[
            "0",
            "1/4",
            "1/2",
            "1"
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,
        student_class="11-12",
        stream="PCM",
        explanation="A fair coin has two equally likely outcomes, so the probability is 1/2.",
    ),


    Question(
        question_code="HS-PCM-021",
        question=
        "What is the acceleration when velocity changes from 10 m/s to 20 m/s in 5 s?",
        options=[
            "1 m/s²",
            "2 m/s²",
            "4 m/s²",
            "5 m/s²",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "Acceleration is change in velocity divided by time: 10/5 = 2 m/s².",
    ),

    Question(
        question_code="HS-PCM-022",
        question=
        "Which quantity is conserved in an isolated system during an elastic collision? ",
        options=[
            "Momentum only",
            "Kinetic energy only",
            "Both momentum and kinetic energy",
            "Neither",
        ],
        answer="C",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "An ideal elastic collision conserves both momentum and kinetic energy.",
    ),

    Question(
        question_code="HS-PCM-023",
        question=
        "The SI unit of electric charge is:",
        options=[
            "Volt",
            "Coulomb",
            "Ohm",
            "Watt",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "Electric charge is measured in coulombs.",
    ),

    Question(
        question_code="HS-PCM-024",
        question=
        "If resistance is doubled while voltage stays constant, current becomes:",
        options=[
            "Double",
            "Half",
            "Four times",
            "Unchanged",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "Ohm's law gives I = V/R, so doubling R halves I.",
    ),

    Question(
        question_code="HS-PCM-025",
        question=
        "The work done by a force perpendicular to displacement is:",
        options=[
            "Maximum",
            "Zero",
            "Negative always",
            "Equal to force",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "W = Fs cos 90°, so the work is zero.",
    ),

    Question(
        question_code="HS-PCM-026",
        question=
        "Which lens is used to correct myopia?",
        options=[
            "Convex",
            "Concave",
            "Cylindrical only",
            "Plane glass",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "A concave lens diverges rays and corrects short-sightedness.",
    ),

    Question(
        question_code="HS-PCM-027",
        question=
        "The slope of a velocity-time graph represents:",
        options=[
            "Distance",
            "Acceleration",
            "Momentum",
            "Force",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "The slope dv/dt is acceleration.",
    ),

    Question(
        question_code="HS-PCM-028",
        question=
        "For a projectile, ignoring air resistance, horizontal acceleration is:",
        options=[
            "g",
            "2g",
            "0",
            "g/2",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "Gravity acts vertically, so horizontal acceleration is zero.",
    ),

    Question(
        question_code="HS-PCM-029",
        question=
        "Which law relates pressure and volume at constant temperature?",
        options=[
            "Charles' law",
            "Boyle's law",
            "Avogadro's law",
            "Faraday's law",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Boyle's law states PV is constant at constant temperature.",
    ),

    Question(
        question_code="HS-PCM-030",
        question=
        "The oxidation state of oxygen in H2O is:",
        options=[
            "+2",
            "-2",
            "0",
            "+1",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Oxygen normally has oxidation state -2 in water.",
    ),

    Question(
        question_code="HS-PCM-031",
        question=
        "A catalyst primarily changes the:",
        options=[
            "Equilibrium constant",
            "Activation energy",
            "Products formed",
            "Atomic number",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Catalysts provide an alternative pathway with lower activation energy.",
    ),

    Question(
        question_code="HS-PCM-032",
        question=
        "Which bond is formed by sharing electron pairs?",
        options=[
            "Ionic",
            "Covalent",
            "Metallic",
            "Hydrogen only",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Covalent bonds involve shared electron pairs.",
    ),

    Question(
        question_code="HS-PCM-033",
        question=
        "pH of a neutral solution at 25°C is approximately:",
        options=[
            "0",
            "5",
            "7",
            "14",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Neutral water has pH about 7 at 25°C.",
    ),

    Question(
        question_code="HS-PCM-034",
        question=
        "The molar mass of CO2 is:",
        options=[
            "28 g/mol",
            "32 g/mol",
            "44 g/mol",
            "48 g/mol",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "12 + 2×16 = 44 g/mol.",
    ),

    Question(
        question_code="HS-PCM-035",
        question=
        "Which particle determines the atomic number?",
        options=[
            "Neutron",
            "Electron",
            "Proton",
            "Nucleon",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Atomic number equals the number of protons.",
    ),

    Question(
        question_code="HS-PCM-036",
        question=
        "A solution containing the maximum solute at a given temperature is:",
        options=[
            "Dilute",
            "Unsaturated",
            "Saturated",
            "Colloidal",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "A saturated solution contains the maximum dissolved solute at that condition.",
    ),

    Question(
        question_code="HS-PCM-037",
        question=
        "What is the derivative of x² with respect to x?",
        options=[
            "x",
            "2x",
            "x²",
            "2",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "The derivative of x² is 2x.",
    ),

    Question(
        question_code="HS-PCM-038",
        question=
        "The determinant of [[a,0],[0,b]] is:",
        options=[
            "a+b",
            "ab",
            "a-b",
            "0",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "For a diagonal 2×2 matrix the determinant is the product of diagonal entries.",
    ),

    Question(
        question_code="HS-PCM-039",
        question=
        "If log10(1000) equals:",
        options=[
            "2",
            "3",
            "10",
            "100",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "10³ = 1000, so the logarithm is 3.",
    ),

    Question(
        question_code="HS-PCM-040",
        question=
        "The probability of getting a head on a fair coin is:",
        options=[
            "0",
            "1/4",
            "1/2",
            "1",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "There is one favorable outcome among two equally likely outcomes.",
    ),

    Question(
        question_code="HS-PCM-041",
        question=
        "If sin θ = 1 for an acute angle θ, then θ is:",
        options=[
            "0°",
            "30°",
            "60°",
            "90°",
        ],
        answer="D",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "Sine reaches 1 at 90°.",
    ),

    Question(
        question_code="HS-PCM-042",
        question=
        "The sum of first n natural numbers is:",
        options=[
            "n²",
            "n(n+1)/2",
            "n(n-1)/2",
            "2n",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "The standard formula is n(n+1)/2.",
    ),

    Question(
        question_code="HS-PCM-043",
        question=
        "A matrix with equal rows is necessarily:",
        options=[
            "Identity",
            "Singular",
            "Orthogonal",
            "Diagonal",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "Equal rows make the determinant zero, so the matrix is singular.",
    ),

    Question(
        question_code="HS-PCM-044",
        question=
        "The roots of x²-5x+6=0 are:",
        options=[
            "1,6",
            "2,3",
            "-2,-3",
            "0,6",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "The quadratic factors as (x-2)(x-3).",
    ),

    Question(
        question_code="HS-PCM-045",
        question=
        "The vector magnitude of (3,4) is:",
        options=[
            "5",
            "7",
            "12",
            "1",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "Magnitude is sqrt(3²+4²)=5.",
    ),

    Question(
        question_code="HS-PCM-046",
        question=
        "Which quantity is dimensionless?",
        options=[
            "Velocity",
            "Force",
            "Refractive index",
            "Energy",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "Refractive index is a ratio and has no dimensions.",
    ),

    Question(
        question_code="HS-PCM-047",
        question=
        "The frequency of a wave is 5 Hz. Its period is:",
        options=[
            "5 s",
            "0.2 s",
            "25 s",
            "10 s",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "Period T = 1/f = 1/5 = 0.2 s.",
    ),

    Question(
        question_code="HS-PCM-048",
        question=
        "Which gas is released when an acid reacts with a carbonate?",
        options=[
            "Oxygen",
            "Hydrogen",
            "Carbon dioxide",
            "Nitrogen",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Acid-carbonate reactions release CO2.",
    ),

    Question(
        question_code="HS-PCM-049",
        question=
        "Which quantum number primarily determines the shell of an electron?",
        options=[
            "Principal n",
            "Azimuthal l",
            "Magnetic m",
            "Spin s",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "The principal quantum number n identifies the main shell.",
    ),

    Question(
        question_code="HS-PCM-050",
        question=
        "In an arithmetic progression, the difference between consecutive terms is:",
        options=[
            "Common ratio",
            "Common difference",
            "Mean",
            "Product",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.MATHEMATICS,

        explanation=
        "An AP has a constant common difference.",
    ),
]