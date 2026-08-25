from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


PCB_QUESTIONS: list[Question] = [

    # =====================================================
    # HIGH SCHOOL PCB (CLASS 11-12)
    # =====================================================


    Question(
        question_code="HS-PCB-001",

        question="Which organelle is known as the powerhouse of the cell?",

        options=[
            "Nucleus",
            "Mitochondria",
            "Ribosome",
            "Golgi Body"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BIOLOGY,

        student_class="11-12",

        stream="PCB",

        explanation=
        "Mitochondria produces energy for the cell.",
    ),



    Question(
        question_code="HS-PCB-002",

        question="The basic unit of life is:",

        options=[
            "Tissue",
            "Cell",
            "Organ",
            "Atom"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BIOLOGY,

        student_class="11-12",

        stream="PCB",

        explanation=
        "Cell is the basic structural and functional unit of life.",
    ),



    Question(
        question_code="HS-PCB-003",

        question="Which pigment is responsible for photosynthesis?",

        options=[
            "Hemoglobin",
            "Chlorophyll",
            "Melanin",
            "Carotene"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BIOLOGY,

        student_class="11-12",

        stream="PCB",

        explanation=
        "Chlorophyll absorbs sunlight for photosynthesis.",
    ),



    Question(
        question_code="HS-PCB-004",

        question="What is the SI unit of velocity?",

        options=[
            "m/s",
            "Newton",
            "Joule",
            "Watt"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PHYSICS,

        student_class="11-12",

        stream="PCB",

        explanation=
        "Velocity is measured in metre per second.",
    ),



    Question(
        question_code="HS-PCB-005",

        question="Newton's first law of motion is also called:",

        options=[
            "Law of Acceleration",
            "Law of Inertia",
            "Law of Energy",
            "Law of Momentum"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PHYSICS,

        student_class="11-12",

        stream="PCB",

        explanation=
        "Newton's first law describes inertia.",
    ),



    Question(
        question_code="HS-PCB-006",

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

        stream="PCB",

        explanation=
        "Electron carries negative charge.",
    ),



    Question(
        question_code="HS-PCB-007",

        question="Atomic number represents the number of:",

        options=[
            "Neutrons",
            "Protons",
            "Molecules",
            "Atoms"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CHEMISTRY,

        student_class="11-12",

        stream="PCB",

        explanation=
        "Atomic number is equal to number of protons.",
    ),



    Question(
        question_code="HS-PCB-008",

        question="The chemical formula of water is:",

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

        student_class="11-12",

        stream="PCB",

        explanation=
        "Water contains two hydrogen and one oxygen atom.",
    ),



    Question(
        question_code="HS-PCB-009",

        question="Which blood cells help in fighting infections?",

        options=[
            "Red Blood Cells",
            "White Blood Cells",
            "Platelets",
            "Neurons"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BIOLOGY,

        student_class="11-12",

        stream="PCB",

        explanation=
        "White blood cells protect the body from infections.",
    ),



    Question(
        question_code="HS-PCB-010",

        question="DNA stands for:",

        options=[
            "Deoxyribonucleic Acid",
            "Dynamic Nuclear Acid",
            "Double Nitrogen Atom",
            "Digital Network Array"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BIOLOGY,

        student_class="11-12",

        stream="PCB",

        explanation=
        "DNA stands for Deoxyribonucleic Acid.",
    ),


    # =====================================================
    # ADDITIONAL QUESTIONS (011–020)
    # =====================================================

    Question(
        question_code="HS-PCB-011",
        question="Which molecule carries genetic information in most living organisms?",
        options=[
            "DNA",
            "ATP",
            "Glucose",
            "Water"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,
        student_class="11-12",
        stream="PCB",
        explanation="DNA stores hereditary genetic information in most organisms.",
    ),
    Question(
        question_code="HS-PCB-012",
        question="The functional unit of the kidney is:",
        options=[
            "Neuron",
            "Nephron",
            "Alveolus",
            "Villus"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,
        student_class="11-12",
        stream="PCB",
        explanation="The nephron is the structural and functional unit of the kidney.",
    ),
    Question(
        question_code="HS-PCB-013",
        question="Photosynthesis primarily takes place in the:",
        options=[
            "Mitochondria",
            "Chloroplast",
            "Nucleus",
            "Ribosome"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,
        student_class="11-12",
        stream="PCB",
        explanation="Chloroplasts contain chlorophyll and are the main site of photosynthesis.",
    ),
    Question(
        question_code="HS-PCB-014",
        question="Which blood group is commonly called the universal donor for red blood cells?",
        options=[
            "AB positive",
            "O negative",
            "A positive",
            "B negative"
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,
        student_class="11-12",
        stream="PCB",
        explanation="O negative red blood cells lack A, B and Rh(D) antigens.",
    ),
    Question(
        question_code="HS-PCB-015",
        question="The hormone that helps regulate blood glucose level is:",
        options=[
            "Insulin",
            "Adrenaline",
            "Thyroxine",
            "Melatonin"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,
        student_class="11-12",
        stream="PCB",
        explanation="Insulin helps cells take up glucose and lowers blood glucose levels.",
    ),
    Question(
        question_code="HS-PCB-016",
        question="The SI unit of electric current is:",
        options=[
            "Volt",
            "Ampere",
            "Ohm",
            "Coulomb"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,
        student_class="11-12",
        stream="PCB",
        explanation="Electric current is measured in amperes.",
    ),
    Question(
        question_code="HS-PCB-017",
        question="According to Newton's second law, force is related to:",
        options=[
            "Mass and acceleration",
            "Mass and velocity only",
            "Distance and time only",
            "Pressure and volume"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,
        student_class="11-12",
        stream="PCB",
        explanation="Newton's second law gives F = ma.",
    ),
    Question(
        question_code="HS-PCB-018",
        question="The pH of a neutral solution at room temperature is approximately:",
        options=[
            "0",
            "5",
            "7",
            "14"
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,
        student_class="11-12",
        stream="PCB",
        explanation="A neutral aqueous solution has a pH of about 7 at room temperature.",
    ),
    Question(
        question_code="HS-PCB-019",
        question="Which bond involves transfer of electrons from one atom to another?",
        options=[
            "Covalent bond",
            "Ionic bond",
            "Hydrogen bond",
            "Metallic bond"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,
        student_class="11-12",
        stream="PCB",
        explanation="Ionic bonding results from electron transfer and electrostatic attraction.",
    ),
    Question(
        question_code="HS-PCB-020",
        question="The molar mass of water (H₂O) is approximately:",
        options=[
            "10 g/mol",
            "18 g/mol",
            "28 g/mol",
            "32 g/mol"
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,
        student_class="11-12",
        stream="PCB",
        explanation="Water has two hydrogen atoms and one oxygen atom, giving a molar mass of about 18 g/mol.",
    ),


    Question(
        question_code="HS-PCB-021",
        question=
        "Which structure controls movement of substances into and out of a cell?",
        options=[
            "Cell wall",
            "Cell membrane",
            "Nucleolus",
            "Ribosome",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "The plasma membrane regulates transport across the cell boundary.",
    ),

    Question(
        question_code="HS-PCB-022",
        question=
        "DNA replication is described as:",
        options=[
            "Conservative",
            "Semi-conservative",
            "Dispersive only",
            "Random",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Each daughter DNA has one old and one newly synthesized strand.",
    ),

    Question(
        question_code="HS-PCB-023",
        question=
        "Which molecule carries amino acids to the ribosome?",
        options=[
            "mRNA",
            "tRNA",
            "rRNA",
            "DNA",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Transfer RNA brings amino acids during translation.",
    ),

    Question(
        question_code="HS-PCB-024",
        question=
        "The site of aerobic respiration is mainly:",
        options=[
            "Ribosome",
            "Mitochondrion",
            "Golgi body",
            "Lysosome",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Mitochondria are the main site of aerobic cellular respiration.",
    ),

    Question(
        question_code="HS-PCB-025",
        question=
        "Which blood cells are primarily responsible for oxygen transport?",
        options=[
            "Platelets",
            "Red blood cells",
            "White blood cells",
            "Plasma cells",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Hemoglobin in red blood cells transports oxygen.",
    ),

    Question(
        question_code="HS-PCB-026",
        question=
        "The functional unit of the kidney is:",
        options=[
            "Neuron",
            "Nephron",
            "Alveolus",
            "Villus",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "A nephron performs filtration and urine formation.",
    ),

    Question(
        question_code="HS-PCB-027",
        question=
        "Photosynthesis converts light energy mainly into:",
        options=[
            "Sound energy",
            "Chemical energy",
            "Nuclear energy",
            "Mechanical energy",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Light energy is stored in chemical bonds of carbohydrates.",
    ),

    Question(
        question_code="HS-PCB-028",
        question=
        "Which hormone lowers blood glucose?",
        options=[
            "Adrenaline",
            "Insulin",
            "Thyroxine",
            "Glucagon",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Insulin promotes glucose uptake and lowers blood glucose.",
    ),

    Question(
        question_code="HS-PCB-029",
        question=
        "Mitosis generally produces:",
        options=[
            "Four haploid cells",
            "Two genetically similar cells",
            "Two gametes",
            "One cell",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Mitosis produces two daughter cells with the same chromosome number.",
    ),

    Question(
        question_code="HS-PCB-030",
        question=
        "The exchange of gases in lungs occurs mainly in:",
        options=[
            "Trachea",
            "Alveoli",
            "Bronchi",
            "Diaphragm",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Thin-walled alveoli provide a large surface for gas exchange.",
    ),

    Question(
        question_code="HS-PCB-031",
        question=
        "Which enzyme begins protein digestion in the stomach?",
        options=[
            "Amylase",
            "Pepsin",
            "Lipase only",
            "Trypsin",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Pepsin is active in the acidic stomach environment.",
    ),

    Question(
        question_code="HS-PCB-032",
        question=
        "A gene is best described as:",
        options=[
            "A whole chromosome",
            "A DNA segment influencing a trait",
            "A protein",
            "A cell organelle",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "A gene is a functional segment of DNA.",
    ),

    Question(
        question_code="HS-PCB-033",
        question=
        "Which ecological level includes living organisms and their physical environment?",
        options=[
            "Population",
            "Community",
            "Ecosystem",
            "Species",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "An ecosystem includes biotic and abiotic components.",
    ),

    Question(
        question_code="HS-PCB-034",
        question=
        "The process by which plants lose water vapor is:",
        options=[
            "Respiration",
            "Transpiration",
            "Translocation",
            "Germination",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Transpiration is water loss mainly through stomata.",
    ),

    Question(
        question_code="HS-PCB-035",
        question=
        "Which organ filters blood to form urine?",
        options=[
            "Heart",
            "Kidney",
            "Liver",
            "Lung",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Kidneys filter blood and form urine.",
    ),

    Question(
        question_code="HS-PCB-036",
        question=
        "Which vitamin is synthesized in skin with sunlight exposure?",
        options=[
            "Vitamin A",
            "Vitamin C",
            "Vitamin D",
            "Vitamin K",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "UVB exposure helps skin synthesize vitamin D.",
    ),

    Question(
        question_code="HS-PCB-037",
        question=
        "Which class of biomolecules includes enzymes?",
        options=[
            "Carbohydrates",
            "Proteins",
            "Lipids",
            "Minerals",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Most biological enzymes are proteins.",
    ),

    Question(
        question_code="HS-PCB-038",
        question=
        "The basic unit of heredity is:",
        options=[
            "Gene",
            "Tissue",
            "Organ",
            "Cell wall",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Genes carry hereditary information.",
    ),

    Question(
        question_code="HS-PCB-039",
        question=
        "Which part of a neuron receives most incoming signals?",
        options=[
            "Axon",
            "Dendrites",
            "Myelin",
            "Synapse only",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Dendrites receive signals from other neurons.",
    ),

    Question(
        question_code="HS-PCB-040",
        question=
        "Natural selection acts directly on:",
        options=[
            "Phenotypes",
            "Only DNA molecules",
            "Species names",
            "Ecosystems only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Selection acts on observable traits that affect reproductive success.",
    ),

    Question(
        question_code="HS-PCB-041",
        question=
        "Which gas is required for aerobic respiration?",
        options=[
            "Nitrogen",
            "Oxygen",
            "Carbon dioxide",
            "Hydrogen",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "Aerobic respiration uses oxygen as the terminal electron acceptor.",
    ),

    Question(
        question_code="HS-PCB-042",
        question=
        "Which organelle modifies and packages proteins?",
        options=[
            "Golgi apparatus",
            "Centrosome",
            "Nucleus only",
            "Vacuole",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIOLOGY,

        explanation=
        "The Golgi apparatus processes and packages proteins.",
    ),

    Question(
        question_code="HS-PCB-043",
        question=
        "Which bond joins amino acids in a protein?",
        options=[
            "Peptide bond",
            "Glycosidic bond",
            "Phosphodiester bond",
            "Ionic bond only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Amino acids are linked by peptide bonds.",
    ),

    Question(
        question_code="HS-PCB-044",
        question=
        "The functional group of an alcohol is:",
        options=[
            "-COOH",
            "-OH",
            "-CHO",
            "-NH2",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Alcohols contain the hydroxyl group -OH.",
    ),

    Question(
        question_code="HS-PCB-045",
        question=
        "A buffer solution resists changes in:",
        options=[
            "Mass",
            "pH",
            "Temperature",
            "Volume",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Buffers resist significant pH changes when small amounts of acid/base are added.",
    ),

    Question(
        question_code="HS-PCB-046",
        question=
        "Which particle has a negative charge?",
        options=[
            "Proton",
            "Neutron",
            "Electron",
            "Positron",
        ],
        answer="C",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CHEMISTRY,

        explanation=
        "Electrons carry negative charge.",
    ),

    Question(
        question_code="HS-PCB-047",
        question=
        "The SI unit of electric current is:",
        options=[
            "Volt",
            "Ampere",
            "Ohm",
            "Coulomb",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "Electric current is measured in amperes.",
    ),

    Question(
        question_code="HS-PCB-048",
        question=
        "Acceleration due to gravity near Earth's surface is approximately:",
        options=[
            "9.8 m/s²",
            "98 m/s²",
            "0.98 m/s²",
            "980 m/s²",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "Near Earth, g is about 9.8 m/s².",
    ),

    Question(
        question_code="HS-PCB-049",
        question=
        "A convex lens can form a real image when the object is:",
        options=[
            "Between lens and focus",
            "Beyond focal length",
            "At optical center only",
            "Always at focus",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "For an object beyond the focal point, a convex lens can form a real image.",
    ),

    Question(
        question_code="HS-PCB-050",
        question=
        "The frequency of a wave determines its:",
        options=[
            "Pitch",
            "Loudness only",
            "Mass",
            "Charge",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PHYSICS,

        explanation=
        "For sound, higher frequency corresponds to higher pitch.",
    ),
]