import type {
    AssessmentQuestionBank,
    Question,
} from "../assessmentQuestions";

/* CLASS 11 PCB ASSESSMENT QUESTION BANK */

/* APTITUDE QUESTIONS*/
const pcbAptitudeQuestions: Question[] = [
    {
        id: 11101,
        question:
            "A laboratory records 120 samples. If 25% of the samples are rejected, how many samples remain?",
        options: ["30", "60", "90", "100"],
        answer: 2,
        skill: "Numerical Ability",
    },
    {
        id: 11102,
        question:
            "A student completes 3 experiments in 45 minutes. At the same rate, how many experiments can be completed in 2 hours?",
        options: ["6", "8", "9", "12"],
        answer: 1,
        skill: "Problem Solving",
    },
    {
        id: 11103,
        question:
            "The ratio of red blood cell samples to white blood cell samples is 5:2. If there are 35 red blood cell samples, how many white blood cell samples are there?",
        options: ["10", "12", "14", "16"],
        answer: 2,
        skill: "Analytical Thinking",
    },
    {
        id: 11104,
        question:
            "A medicine dosage increases from 40 mg to 50 mg. What is the percentage increase?",
        options: ["10%", "20%", "25%", "40%"],
        answer: 2,
        skill: "Arithmetic",
    },
    {
        id: 11105,
        question:
            "If 5 microscopes cost ₹75,000 equally, what is the cost of one microscope?",
        options: [
            "₹10,000",
            "₹12,000",
            "₹15,000",
            "₹20,000",
        ],
        answer: 2,
        skill: "Logical Reasoning",
    },
    {
        id: 11106,
        question:
            "A culture doubles every hour. If it begins with 50 cells, how many cells will be present after 3 hours?",
        options: ["150", "200", "400", "800"],
        answer: 2,
        skill: "Numerical Ability",
    },
    {
        id: 11107,
        question:
            "The average of five test scores is 72. What is their total score?",
        options: ["300", "340", "360", "380"],
        answer: 2,
        skill: "Problem Solving",
    },
    {
        id: 11108,
        question:
            "A solution contains 20 mL of chemical in 100 mL total solution. What percentage of the solution is the chemical?",
        options: ["10%", "20%", "25%", "50%"],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 11109,
        question:
            "A researcher observes 240 organisms over 6 equal groups. How many organisms are in each group?",
        options: ["30", "40", "50", "60"],
        answer: 1,
        skill: "Arithmetic",
    },
    {
        id: 11110,
        question:
            "If the probability of an event is 0.25, what is the equivalent percentage?",
        options: ["2.5%", "20%", "25%", "40%"],
        answer: 2,
        skill: "Logical Reasoning",
    },
    {
        id: 11111,
        question:
            "A hospital has 80 beds and 60 are occupied. What fraction of the beds are occupied?",
        options: ["1/2", "2/3", "3/4", "4/5"],
        answer: 2,
        skill: "Numerical Ability",
    },
    {
        id: 11112,
        question:
            "A sequence follows 2, 6, 12, 20, 30. What is the next number?",
        options: ["36", "40", "42", "48"],
        answer: 2,
        skill: "Problem Solving",
    },
    {
        id: 11113,
        question:
            "If 8 students examine 64 specimens equally, how many specimens does each student examine?",
        options: ["6", "8", "10", "12"],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 11114,
        question:
            "A temperature changes from 20°C to 32°C. By how many degrees has it increased?",
        options: ["10°C", "12°C", "14°C", "16°C"],
        answer: 1,
        skill: "Arithmetic",
    },
    {
        id: 11115,
        question:
            "Three-fourths of 200 laboratory samples are valid. How many valid samples are there?",
        options: ["100", "125", "150", "175"],
        answer: 2,
        skill: "Logical Reasoning",
    },
];


/* =========================================================
   BIOLOGY QUESTIONS
   ========================================================= */

const pcbBiologyQuestions: Question[] = [
    {
        id: 11201,
        question:
            "Which organelle is primarily responsible for ATP production in eukaryotic cells?",
        options: [
            "Ribosome",
            "Mitochondrion",
            "Golgi apparatus",
            "Lysosome",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 11202,
        question:
            "The basic structural and functional unit of life is the:",
        options: [
            "Tissue",
            "Organ",
            "Cell",
            "Organ system",
        ],
        answer: 2,
        skill: "Biology",
    },
    {
        id: 11203,
        question:
            "Which biomolecule is mainly responsible for storing hereditary information?",
        options: [
            "Carbohydrate",
            "Lipid",
            "DNA",
            "Vitamin",
        ],
        answer: 2,
        skill: "Biology",
    },
    {
        id: 11204,
        question:
            "The fluid mosaic model describes the structure of the:",
        options: [
            "Cell wall",
            "Plasma membrane",
            "Nucleus",
            "Chromosome",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 11205,
        question:
            "Which plant tissue transports water and minerals from roots?",
        options: [
            "Phloem",
            "Xylem",
            "Epidermis",
            "Cambium",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 11206,
        question:
            "Proteins are composed of smaller units called:",
        options: [
            "Fatty acids",
            "Nucleotides",
            "Amino acids",
            "Monosaccharides",
        ],
        answer: 2,
        skill: "Biology",
    },
    {
        id: 11207,
        question:
            "Which process produces two genetically identical daughter cells?",
        options: [
            "Meiosis",
            "Mitosis",
            "Fertilization",
            "Mutation",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 11208,
        question:
            "The functional unit of the human kidney is the:",
        options: [
            "Neuron",
            "Nephron",
            "Alveolus",
            "Villus",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 11209,
        question:
            "Which pigment absorbs light energy during photosynthesis?",
        options: [
            "Haemoglobin",
            "Melanin",
            "Chlorophyll",
            "Keratin",
        ],
        answer: 2,
        skill: "Biology",
    },
    {
        id: 11210,
        question:
            "Enzymes primarily function as:",
        options: [
            "Energy stores",
            "Biological catalysts",
            "Genetic material",
            "Structural minerals",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 11211,
        question:
            "Gas exchange in human lungs mainly occurs in the:",
        options: [
            "Trachea",
            "Bronchi",
            "Alveoli",
            "Diaphragm",
        ],
        answer: 2,
        skill: "Biology",
    },
    {
        id: 11212,
        question:
            "Which blood cells are mainly involved in defending the body against infection?",
        options: [
            "Red blood cells",
            "White blood cells",
            "Platelets",
            "Plasma cells only",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 11213,
        question:
            "The opening and closing of stomata is mainly controlled by:",
        options: [
            "Guard cells",
            "Xylem cells",
            "Root hairs",
            "Sieve tubes",
        ],
        answer: 0,
        skill: "Biology",
    },
    {
        id: 11214,
        question:
            "Which level of biological organization consists of similar cells performing a common function?",
        options: [
            "Organism",
            "Organ",
            "Tissue",
            "Organ system",
        ],
        answer: 2,
        skill: "Biology",
    },
    {
        id: 11215,
        question:
            "During aerobic respiration, most ATP is produced in the:",
        options: [
            "Nucleus",
            "Mitochondria",
            "Ribosomes",
            "Golgi bodies",
        ],
        answer: 1,
        skill: "Biology",
    },
];


/* =========================================================
   ENGLISH QUESTIONS
   ========================================================= */

const pcbEnglishQuestions: Question[] = [
    {
        id: 11301,
        question:
            "Choose the grammatically correct sentence.",
        options: [
            "The results was recorded carefully.",
            "The results were recorded carefully.",
            "The result were recorded carefully.",
            "The results is recorded carefully.",
        ],
        answer: 1,
        skill: "Grammar",
    },
    {
        id: 11302,
        question:
            "Choose the word closest in meaning to 'observe'.",
        options: [
            "Ignore",
            "Examine",
            "Destroy",
            "Forget",
        ],
        answer: 1,
        skill: "Vocabulary",
    },
    {
        id: 11303,
        question:
            "Complete the sentence: The researcher _____ the data before drawing a conclusion.",
        options: [
            "analyse",
            "analysed",
            "analysing",
            "have analyse",
        ],
        answer: 1,
        skill: "Reading Comprehension",
    },
    {
        id: 11304,
        question:
            "Which word is the opposite of 'increase'?",
        options: [
            "Expand",
            "Develop",
            "Decrease",
            "Improve",
        ],
        answer: 2,
        skill: "Communication",
    },
    {
        id: 11305,
        question:
            "Choose the correctly spelled word.",
        options: [
            "Enviroment",
            "Environment",
            "Envirnoment",
            "Enviornment",
        ],
        answer: 1,
        skill: "Interpretation",
    },
    {
        id: 11306,
        question:
            "Identify the adjective in the sentence: 'The careful student recorded the observation.'",
        options: [
            "Student",
            "Recorded",
            "Careful",
            "Observation",
        ],
        answer: 2,
        skill: "Grammar",
    },
    {
        id: 11307,
        question:
            "Choose the correct passive form of: 'The scientist conducted the experiment.'",
        options: [
            "The experiment conducted the scientist.",
            "The experiment was conducted by the scientist.",
            "The scientist was conducted by the experiment.",
            "The experiment is conducting the scientist.",
        ],
        answer: 1,
        skill: "Vocabulary",
    },
    {
        id: 11308,
        question:
            "The word 'accurate' most nearly means:",
        options: [
            "Incorrect",
            "Precise",
            "Uncertain",
            "Careless",
        ],
        answer: 1,
        skill: "Reading Comprehension",
    },
    {
        id: 11309,
        question:
            "Choose the correct article: She wants to become _____ doctor.",
        options: ["a", "an", "the", "no article"],
        answer: 0,
        skill: "Communication",
    },
    {
        id: 11310,
        question:
            "Which sentence expresses a logical conclusion?",
        options: [
            "The evidence supports the hypothesis.",
            "The evidence singing the hypothesis.",
            "Hypothesis evidence the support.",
            "Supports evidence hypothesis.",
        ],
        answer: 0,
        skill: "Interpretation",
    },
    {
        id: 11311,
        question:
            "Choose the correct plural form of 'analysis'.",
        options: [
            "Analysises",
            "Analysiss",
            "Analyses",
            "Analysis",
        ],
        answer: 2,
        skill: "Grammar",
    },
    {
        id: 11312,
        question:
            "Complete the sentence: If the temperature rises, the reaction rate _____ increase.",
        options: [
            "may",
            "were",
            "has been",
            "having",
        ],
        answer: 0,
        skill: "Vocabulary",
    },
    {
        id: 11313,
        question:
            "Which word best describes information supported by evidence?",
        options: [
            "Random",
            "Reliable",
            "Imaginary",
            "Careless",
        ],
        answer: 1,
        skill: "Reading Comprehension",
    },
    {
        id: 11314,
        question:
            "Choose the correct conjunction: The result was unexpected, _____ the experiment was repeated.",
        options: [
            "so",
            "but because",
            "unless",
            "although and",
        ],
        answer: 0,
        skill: "Communication",
    },
    {
        id: 11315,
        question:
            "Which sentence is most suitable for a scientific report?",
        options: [
            "The experiment was super cool.",
            "I kinda liked the result.",
            "The observations were recorded at regular intervals.",
            "The result was awesome!",
        ],
        answer: 2,
        skill: "Interpretation",
    },
];


/* =========================================================
   PCB SCIENCE QUESTIONS
   Physics + Chemistry + Biology
   ========================================================= */

const pcbScienceQuestions: Question[] = [
    {
        id: 11401,
        question:
            "The SI unit of force is:",
        options: [
            "Joule",
            "Newton",
            "Pascal",
            "Watt",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 11402,
        question:
            "Velocity differs from speed because velocity has:",
        options: [
            "Only magnitude",
            "Direction",
            "No unit",
            "Constant value",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 11403,
        question:
            "According to Newton's first law, an object continues in its state of rest or uniform motion unless:",
        options: [
            "Its mass changes",
            "An external force acts on it",
            "Its temperature falls",
            "Its volume increases",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 11404,
        question:
            "Which quantity is measured in joules?",
        options: [
            "Force",
            "Energy",
            "Pressure",
            "Current",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 11405,
        question:
            "The atomic number of an element represents the number of:",
        options: [
            "Neutrons only",
            "Protons",
            "Nucleons",
            "Electron shells",
        ],
        answer: 1,
        skill: "Chemistry",
    },
    {
        id: 11406,
        question:
            "A covalent bond is generally formed by:",
        options: [
            "Sharing electrons",
            "Sharing protons",
            "Losing neutrons",
            "Transferring nuclei",
        ],
        answer: 0,
        skill: "Chemistry",
    },
    {
        id: 11407,
        question:
            "One mole of a substance contains approximately:",
        options: [
            "6.022 × 10²³ particles",
            "3.0 × 10⁸ particles",
            "9.8 particles",
            "1.6 × 10⁻¹⁹ particles",
        ],
        answer: 0,
        skill: "Chemistry",
    },
    {
        id: 11408,
        question:
            "Which factor generally increases the rate of a chemical reaction?",
        options: [
            "Lowering temperature",
            "Reducing reactant contact",
            "Increasing temperature",
            "Removing all reactants",
        ],
        answer: 2,
        skill: "Chemistry",
    },
    {
        id: 11409,
        question:
            "Which cell organelle contains digestive enzymes?",
        options: [
            "Lysosome",
            "Ribosome",
            "Centriole",
            "Nucleolus",
        ],
        answer: 0,
        skill: "Biology",
    },
    {
        id: 11410,
        question:
            "Osmosis is the movement of water through a selectively permeable membrane from:",
        options: [
            "Lower water concentration to higher water concentration",
            "Higher water concentration to lower water concentration",
            "Solid to gas",
            "Gas to solid",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 11411,
        question:
            "Which organ is primarily responsible for pumping blood throughout the human body?",
        options: [
            "Lung",
            "Kidney",
            "Heart",
            "Liver",
        ],
        answer: 2,
        skill: "Biology",
    },
    {
        id: 11412,
        question:
            "Photosynthesis converts light energy mainly into:",
        options: [
            "Mechanical energy",
            "Chemical energy",
            "Sound energy",
            "Nuclear energy",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 11413,
        question:
            "If the net force acting on an object increases while mass remains constant, its acceleration:",
        options: [
            "Decreases",
            "Increases",
            "Becomes zero",
            "Always remains unchanged",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 11414,
        question:
            "The pH of a neutral aqueous solution at standard classroom conditions is approximately:",
        options: ["0", "5", "7", "14"],
        answer: 2,
        skill: "Chemistry",
    },
    {
        id: 11415,
        question:
            "Which process is directly involved in producing gametes?",
        options: [
            "Mitosis only",
            "Meiosis",
            "Binary fission",
            "Budding only",
        ],
        answer: 1,
        skill: "Biology",
    },
];


/* =========================================================
   SCIENTIFIC REASONING QUESTIONS
   ========================================================= */

const pcbReasoningQuestions: Question[] = [
    {
        id: 11501,
        question:
            "A plant kept in darkness for several days shows reduced starch formation. What is the most logical explanation?",
        options: [
            "Darkness increases respiration only",
            "Light is required for photosynthesis",
            "Roots stop absorbing water immediately",
            "The plant loses all chlorophyll instantly",
        ],
        answer: 1,
        skill: "Critical Thinking",
    },
    {
        id: 11502,
        question:
            "A researcher changes only the temperature while keeping all other experimental conditions constant. Temperature is the:",
        options: [
            "Dependent variable",
            "Independent variable",
            "Conclusion",
            "Control result",
        ],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 11503,
        question:
            "Two identical plants receive equal water and light. Plant A receives fertilizer and grows faster. What is the most reasonable initial inference?",
        options: [
            "Water stopped growth",
            "Fertilizer may have influenced growth",
            "Light destroys Plant B",
            "Plant A cannot photosynthesize",
        ],
        answer: 1,
        skill: "Interpretation",
    },
    {
        id: 11504,
        question:
            "A patient has a reduced number of red blood cells. Which function is most likely to be directly affected?",
        options: [
            "Oxygen transport",
            "Bone movement",
            "Nerve impulse generation only",
            "Food digestion in the stomach",
        ],
        answer: 0,
        skill: "Problem Solving",
    },
    {
        id: 11505,
        question:
            "An enzyme works best at 37°C but its activity falls sharply at 80°C. The most likely reason is:",
        options: [
            "The enzyme gains chromosomes",
            "The enzyme may become denatured",
            "The enzyme becomes a lipid",
            "The substrate becomes DNA",
        ],
        answer: 1,
        skill: "Critical Thinking",
    },
    {
        id: 11506,
        question:
            "A student repeats an experiment three times and obtains similar results. This mainly improves:",
        options: [
            "The colour of the experiment",
            "Reliability of the observations",
            "The size of the laboratory",
            "The number of variables",
        ],
        answer: 1,
        skill: "Critical Thinking",
    },
    {
        id: 11507,
        question:
            "If a drug is tested without a control group, which problem becomes more likely?",
        options: [
            "The drug automatically fails",
            "It becomes harder to compare treatment effects",
            "All patients recover",
            "The chemical formula changes",
        ],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 11508,
        question:
            "A cell is placed in a strongly hypertonic solution. What is the most likely movement of water?",
        options: [
            "Into the cell",
            "Out of the cell",
            "No water movement is possible",
            "Water becomes protein",
        ],
        answer: 1,
        skill: "Interpretation",
    },
    {
        id: 11509,
        question:
            "A population of bacteria increases rapidly under warm conditions but slowly under cold conditions. Which hypothesis should be tested first?",
        options: [
            "Temperature affects bacterial growth rate",
            "Bacteria are plants",
            "Cold creates sunlight",
            "Warmth removes all nutrients",
        ],
        answer: 0,
        skill: "Problem Solving",
    },
    {
        id: 11510,
        question:
            "A scientist obtains a result that contradicts the original hypothesis. What is the best scientific response?",
        options: [
            "Delete the result",
            "Change the observation secretly",
            "Review the evidence and reconsider the hypothesis",
            "Always keep the original hypothesis",
        ],
        answer: 2,
        skill: "Critical Thinking",
    },
    {
        id: 11511,
        question:
            "A person's breathing rate rises during exercise. Which explanation is most scientifically reasonable?",
        options: [
            "Muscles require increased oxygen and energy production",
            "The lungs stop functioning",
            "Blood circulation completely stops",
            "Cells no longer respire",
        ],
        answer: 0,
        skill: "Critical Thinking",
    },
    {
        id: 11512,
        question:
            "Leaves of the same plant are tested at different light intensities. Which variable should be measured to study photosynthetic response?",
        options: [
            "Rate of oxygen production",
            "Name of the plant",
            "Colour of the laboratory wall",
            "Student's height",
        ],
        answer: 0,
        skill: "Analytical Thinking",
    },
    {
        id: 11513,
        question:
            "A chemical reaction produces gas more rapidly after a catalyst is added. The evidence suggests that the catalyst:",
        options: [
            "Increased the reaction rate",
            "Stopped all molecular movement",
            "Changed into the final product completely",
            "Removed every reactant",
        ],
        answer: 0,
        skill: "Interpretation",
    },
    {
        id: 11514,
        question:
            "A genetic characteristic appears repeatedly across generations of a family. Which area should be investigated first?",
        options: [
            "Inheritance patterns",
            "Weather only",
            "Planetary motion",
            "Sound intensity",
        ],
        answer: 0,
        skill: "Problem Solving",
    },
    {
        id: 11515,
        question:
            "A biological conclusion is based on only one observation from one organism. What is the main limitation?",
        options: [
            "The sample size is too small",
            "The organism has cells",
            "Biology cannot use observations",
            "The result must always be correct",
        ],
        answer: 0,
        skill: "Critical Thinking",
    },
];


/* =========================================================
   CLASS 11 PCB QUESTION BANK
   ========================================================= */

export const class11PCBQuestionBank:
    AssessmentQuestionBank = {
    aptitude: pcbAptitudeQuestions,
    math: pcbBiologyQuestions,
    english: pcbEnglishQuestions,
    science: pcbScienceQuestions,
    reasoning: pcbReasoningQuestions,
};
