import type {
    AssessmentQuestionBank,
    Question,
} from "../assessmentQuestions";

/* =========================================================
   CLASS 11 PCM — APTITUDE ASSESSMENT
   ========================================================= */

const class11PCMAptitudeQuestions: Question[] = [
    {
        id: 11001,
        question:
            "A student solves 24 numerical problems in 3 hours. At the same rate, how many problems can be solved in 5 hours?",
        options: ["32", "36", "40", "45"],
        answer: 2,
        skill: "Numerical Ability",
    },
    {
        id: 11002,
        question:
            "The ratio of Mathematics books to Physics books is 5:3. If there are 64 books in total, how many are Mathematics books?",
        options: ["32", "36", "40", "48"],
        answer: 2,
        skill: "Arithmetic",
    },
    {
        id: 11003,
        question:
            "Find the next number in the sequence: 2, 6, 12, 20, 30, ?",
        options: ["36", "40", "42", "44"],
        answer: 2,
        skill: "Logical Reasoning",
    },
    {
        id: 11004,
        question:
            "A machine produces 180 components in 6 hours. How many components will it produce in 8 hours at the same rate?",
        options: ["210", "220", "240", "260"],
        answer: 2,
        skill: "Problem Solving",
    },
    {
        id: 11005,
        question:
            "If all conductors allow electric current and copper is a conductor, which conclusion is valid?",
        options: [
            "Copper does not allow current",
            "Copper allows electric current",
            "All materials are conductors",
            "Only copper allows current",
        ],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 11006,
        question:
            "The average of five observations is 28. If four observations are 20, 24, 30 and 32, what is the fifth observation?",
        options: ["30", "32", "34", "36"],
        answer: 2,
        skill: "Numerical Ability",
    },
    {
        id: 11007,
        question:
            "A quantity increases from 250 to 300. What is the percentage increase?",
        options: ["10%", "15%", "20%", "25%"],
        answer: 2,
        skill: "Arithmetic",
    },
    {
        id: 11008,
        question:
            "Which number does not follow the pattern: 4, 9, 16, 25, 35, 49?",
        options: ["16", "25", "35", "49"],
        answer: 2,
        skill: "Logical Reasoning",
    },
    {
        id: 11009,
        question:
            "A laboratory has a budget of ₹12,000 for 8 identical instruments. What is the maximum cost of each instrument?",
        options: ["₹1,200", "₹1,400", "₹1,500", "₹1,600"],
        answer: 2,
        skill: "Problem Solving",
    },
    {
        id: 11010,
        question:
            "P is north of Q. R is east of P. In which direction is R from Q?",
        options: [
            "North-West",
            "North-East",
            "South-East",
            "South-West",
        ],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 11011,
        question:
            "A number is reduced by 20% and becomes 480. What was the original number?",
        options: ["560", "580", "600", "620"],
        answer: 2,
        skill: "Numerical Ability",
    },
    {
        id: 11012,
        question:
            "If 12 machines complete a task in 10 hours, how many hours would 15 equally efficient machines require?",
        options: ["6", "8", "10", "12"],
        answer: 1,
        skill: "Arithmetic",
    },
    {
        id: 11013,
        question:
            "Equation is to Mathematics as Experiment is to:",
        options: [
            "History",
            "Physics",
            "Language",
            "Geography",
        ],
        answer: 1,
        skill: "Logical Reasoning",
    },
    {
        id: 11014,
        question:
            "A student must choose exactly two projects from Robotics, Coding and Art. If Robotics is selected, Art cannot be selected. Which pair is possible?",
        options: [
            "Robotics and Art",
            "Robotics and Coding",
            "All three projects",
            "Robotics only",
        ],
        answer: 1,
        skill: "Problem Solving",
    },
    {
        id: 11015,
        question:
            "A hypothesis is supported by three experiments but contradicted by a fourth experiment. What is the most scientific next step?",
        options: [
            "Ignore the fourth experiment",
            "Accept the hypothesis permanently",
            "Investigate the conflicting result",
            "Delete all experimental data",
        ],
        answer: 2,
        skill: "Critical Thinking",
    },
];

/* =========================================================
   CLASS 11 PCM — MATHEMATICS ASSESSMENT
   ========================================================= */

const class11PCMMathematicsQuestions: Question[] = [
    {
        id: 11101,
        question:
            "If A = {1, 2, 3} and B = {3, 4, 5}, what is A ∩ B?",
        options: [
            "{1, 2}",
            "{3}",
            "{4, 5}",
            "{1, 2, 3, 4, 5}",
        ],
        answer: 1,
        skill: "Mathematics",
    },
    {
        id: 11102,
        question:
            "What is the domain of the function f(x) = 1/(x - 3)?",
        options: [
            "All real numbers",
            "All real numbers except 0",
            "All real numbers except 3",
            "Only positive real numbers",
        ],
        answer: 2,
        skill: "Mathematics",
    },
    {
        id: 11103,
        question:
            "If sin θ = 1/2 and θ is an acute angle, what is θ?",
        options: ["30°", "45°", "60°", "90°"],
        answer: 0,
        skill: "Mathematics",
    },
    {
        id: 11104,
        question:
            "What is the value of i², where i is the imaginary unit?",
        options: ["1", "-1", "i", "-i"],
        answer: 1,
        skill: "Mathematics",
    },
    {
        id: 11105,
        question:
            "The roots of x² - 5x + 6 = 0 are:",
        options: [
            "1 and 6",
            "2 and 3",
            "-2 and -3",
            "3 and 5",
        ],
        answer: 1,
        skill: "Problem Solving",
    },
    {
        id: 11106,
        question:
            "If the first term of an arithmetic progression is 4 and the common difference is 3, what is the fifth term?",
        options: ["13", "16", "19", "20"],
        answer: 1,
        skill: "Mathematics",
    },
    {
        id: 11107,
        question:
            "How many permutations of the letters A, B and C are possible?",
        options: ["3", "6", "8", "9"],
        answer: 1,
        skill: "Numerical Ability",
    },
    {
        id: 11108,
        question:
            "What is the value of 5!?",
        options: ["25", "60", "100", "120"],
        answer: 3,
        skill: "Arithmetic",
    },
    {
        id: 11109,
        question:
            "The coefficient of x² in the expansion of (1 + x)³ is:",
        options: ["1", "2", "3", "6"],
        answer: 2,
        skill: "Mathematics",
    },
    {
        id: 11110,
        question:
            "If a straight line has slope 2 and passes through the origin, its equation is:",
        options: [
            "y = x + 2",
            "y = 2x",
            "x = 2y",
            "y = 2",
        ],
        answer: 1,
        skill: "Mathematics",
    },
    {
        id: 11111,
        question:
            "The distance between the points (0, 0) and (3, 4) is:",
        options: ["4", "5", "6", "7"],
        answer: 1,
        skill: "Problem Solving",
    },
    {
        id: 11112,
        question:
            "If n(A) = 20, n(B) = 15 and n(A ∩ B) = 5, what is n(A ∪ B)?",
        options: ["25", "30", "35", "40"],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 11113,
        question:
            "What is the sum of the first 10 natural numbers?",
        options: ["45", "50", "55", "60"],
        answer: 2,
        skill: "Numerical Ability",
    },
    {
        id: 11114,
        question:
            "If tan θ = 1 for an acute angle θ, what is θ?",
        options: ["30°", "45°", "60°", "90°"],
        answer: 1,
        skill: "Mathematics",
    },
    {
        id: 11115,
        question:
            "A quadratic equation has discriminant equal to zero. What can be concluded about its roots?",
        options: [
            "The roots are imaginary",
            "The roots are real and equal",
            "The roots are real and unequal",
            "The equation has no roots",
        ],
        answer: 1,
        skill: "Analytical Thinking",
    },
];

/* =========================================================
   CLASS 11 PCM — ENGLISH ASSESSMENT
   ========================================================= */

const class11PCMEnglishQuestions: Question[] = [
    {
        id: 11201,
        question:
            "Choose the grammatically correct sentence.",
        options: [
            "The results of the experiment was surprising.",
            "The results of the experiment were surprising.",
            "The result of the experiments were surprising.",
            "The results was surprisingly.",
        ],
        answer: 1,
        skill: "Grammar",
    },
    {
        id: 11202,
        question:
            "Choose the word closest in meaning to 'precise'.",
        options: [
            "Approximate",
            "Accurate",
            "Confusing",
            "Ordinary",
        ],
        answer: 1,
        skill: "Vocabulary",
    },
    {
        id: 11203,
        question:
            "A report states: 'The temperature increased steadily for five minutes and then remained constant.' What happened after five minutes?",
        options: [
            "The temperature decreased",
            "The temperature continued increasing",
            "The temperature remained unchanged",
            "The experiment ended immediately",
        ],
        answer: 2,
        skill: "Reading Comprehension",
    },
    {
        id: 11204,
        question:
            "Choose the correct passive form of: 'The students conducted the experiment.'",
        options: [
            "The experiment conducted the students.",
            "The experiment was conducted by the students.",
            "The students were conducted by the experiment.",
            "The experiment is conducting students.",
        ],
        answer: 1,
        skill: "Grammar",
    },
    {
        id: 11205,
        question:
            "The word 'derive' most nearly means:",
        options: [
            "To obtain from a source",
            "To completely destroy",
            "To randomly guess",
            "To avoid studying",
        ],
        answer: 0,
        skill: "Vocabulary",
    },
    {
        id: 11206,
        question:
            "Which sentence communicates a scientific observation most clearly?",
        options: [
            "The object was kind of fast.",
            "The object travelled 20 metres in 4 seconds.",
            "The object looked really amazing.",
            "I think the object was probably moving.",
        ],
        answer: 1,
        skill: "Communication",
    },
    {
        id: 11207,
        question:
            "Choose the correct form: 'Neither the teacher nor the students ___ ready.'",
        options: ["was", "is", "were", "has"],
        answer: 2,
        skill: "Grammar",
    },
    {
        id: 11208,
        question:
            "Which word is the opposite of 'constant'?",
        options: [
            "Stable",
            "Fixed",
            "Variable",
            "Regular",
        ],
        answer: 2,
        skill: "Vocabulary",
    },
    {
        id: 11209,
        question:
            "A passage explains that repeated measurements reduce the effect of random errors. What is the main idea?",
        options: [
            "Measurements should never be repeated",
            "Repeated measurements can improve reliability",
            "Random errors always increase",
            "Only one observation is scientifically valid",
        ],
        answer: 1,
        skill: "Reading Comprehension",
    },
    {
        id: 11210,
        question:
            "Choose the correct sentence.",
        options: [
            "If I will study, I would understand.",
            "If I studied, I would understand.",
            "If I study yesterday, I understand.",
            "If I studying, I would understood.",
        ],
        answer: 1,
        skill: "Grammar",
    },
    {
        id: 11211,
        question:
            "What does 'infer' mean?",
        options: [
            "To reach a conclusion from evidence",
            "To copy a sentence",
            "To calculate only with a formula",
            "To remove all information",
        ],
        answer: 0,
        skill: "Vocabulary",
    },
    {
        id: 11212,
        question:
            "Which is the best opening sentence for a formal laboratory report?",
        options: [
            "This experiment was super cool.",
            "I really liked doing this practical.",
            "The experiment investigates the relationship between force and acceleration.",
            "You will not believe what happened.",
        ],
        answer: 2,
        skill: "Communication",
    },
    {
        id: 11213,
        question:
            "A scientific article says a result is 'significant'. In context, this usually suggests the result is:",
        options: [
            "Meaningful or important",
            "Always incorrect",
            "Completely unrelated",
            "Written informally",
        ],
        answer: 0,
        skill: "Interpretation",
    },
    {
        id: 11214,
        question:
            "Choose the correctly punctuated sentence.",
        options: [
            "Physics mathematics and chemistry are core subjects.",
            "Physics, mathematics, and chemistry are core subjects.",
            "Physics mathematics, and chemistry are core subjects",
            "Physics; mathematics and, chemistry are core subjects.",
        ],
        answer: 1,
        skill: "Grammar",
    },
    {
        id: 11215,
        question:
            "A graph description says: 'Velocity decreases uniformly with time.' Which statement best interprets this?",
        options: [
            "Velocity is increasing randomly",
            "Velocity remains constant",
            "Velocity decreases at a steady rate",
            "Time has stopped",
        ],
        answer: 2,
        skill: "Interpretation",
    },
];

/* =========================================================
   CLASS 11 PCM — SCIENCE ASSESSMENT
   ========================================================= */

const class11PCMScienceQuestions: Question[] = [
    {
        id: 11301,
        question:
            "Which physical quantity has both magnitude and direction?",
        options: [
            "Distance",
            "Speed",
            "Mass",
            "Velocity",
        ],
        answer: 3,
        skill: "Physics",
    },
    {
        id: 11302,
        question:
            "The slope of a velocity-time graph represents:",
        options: [
            "Distance",
            "Acceleration",
            "Momentum",
            "Force",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 11303,
        question:
            "According to Newton's first law, an object remains at rest or in uniform motion unless:",
        options: [
            "Its mass becomes zero",
            "An external unbalanced force acts on it",
            "Its velocity is always positive",
            "Gravity disappears completely",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 11304,
        question:
            "What is the SI unit of work?",
        options: [
            "Newton",
            "Joule",
            "Watt",
            "Pascal",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 11305,
        question:
            "If the velocity of an object doubles, its kinetic energy becomes:",
        options: [
            "Half",
            "Double",
            "Four times",
            "Eight times",
        ],
        answer: 2,
        skill: "Physics",
    },
    {
        id: 11306,
        question:
            "One mole of any substance contains approximately:",
        options: [
            "6.022 × 10²³ particles",
            "3 × 10⁸ particles",
            "9.8 particles",
            "1.6 × 10⁻¹⁹ particles",
        ],
        answer: 0,
        skill: "Chemistry",
    },
    {
        id: 11307,
        question:
            "The atomic number of an element is equal to the number of:",
        options: [
            "Neutrons only",
            "Protons",
            "Protons and neutrons",
            "Electron shells",
        ],
        answer: 1,
        skill: "Chemistry",
    },
    {
        id: 11308,
        question:
            "Which quantum number primarily describes the main energy level of an electron?",
        options: [
            "Principal quantum number",
            "Magnetic quantum number",
            "Spin quantum number",
            "Azimuthal quantum number only",
        ],
        answer: 0,
        skill: "Chemistry",
    },
    {
        id: 11309,
        question:
            "An ionic bond is generally formed by:",
        options: [
            "Equal sharing of electrons",
            "Transfer of electrons",
            "Sharing of protons",
            "Transfer of neutrons",
        ],
        answer: 1,
        skill: "Chemistry",
    },
    {
        id: 11310,
        question:
            "Which law states that mass can neither be created nor destroyed in a chemical reaction?",
        options: [
            "Law of conservation of mass",
            "Boyle's law",
            "Charles's law",
            "Newton's law",
        ],
        answer: 0,
        skill: "Chemistry",
    },
    {
        id: 11311,
        question:
            "A body starts from rest and accelerates uniformly at 2 m/s² for 5 seconds. What is its final velocity?",
        options: [
            "5 m/s",
            "7 m/s",
            "10 m/s",
            "12 m/s",
        ],
        answer: 2,
        skill: "Problem Solving",
    },
    {
        id: 11312,
        question:
            "A 2 kg object experiences a net force of 10 N. What is its acceleration?",
        options: [
            "2 m/s²",
            "5 m/s²",
            "10 m/s²",
            "20 m/s²",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 11313,
        question:
            "Which pair represents isotopes of the same element?",
        options: [
            "Atoms with different proton numbers",
            "Atoms with the same proton number but different neutron numbers",
            "Atoms with different atomic numbers and mass numbers",
            "Two different compounds",
        ],
        answer: 1,
        skill: "Chemistry",
    },
    {
        id: 11314,
        question:
            "Why is dimensional analysis useful in physics?",
        options: [
            "It proves every equation is physically correct",
            "It can check dimensional consistency of equations",
            "It replaces all experiments",
            "It determines the exact numerical constant in every equation",
        ],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 11315,
        question:
            "An experimental value differs slightly from the accepted value. What should a student examine first?",
        options: [
            "Possible measurement and procedural errors",
            "How to change the accepted value",
            "How to remove the observation",
            "Whether formulas should be ignored",
        ],
        answer: 0,
        skill: "Critical Thinking",
    },
];

/* =========================================================
   CLASS 11 PCM — REASONING ASSESSMENT
   ========================================================= */

const class11PCMReasoningQuestions: Question[] = [
    {
        id: 11401,
        question:
            "Find the next number: 1, 4, 9, 16, 25, ?",
        options: ["30", "32", "36", "49"],
        answer: 2,
        skill: "Logical Reasoning",
    },
    {
        id: 11402,
        question:
            "If FORCE is coded as GPSDF by moving each letter one step forward, how is MASS coded?",
        options: [
            "NBTT",
            "NATT",
            "MBTT",
            "NBSS",
        ],
        answer: 0,
        skill: "Logical Reasoning",
    },
    {
        id: 11403,
        question:
            "All physicists study natural phenomena. Riya is a physicist. Which conclusion follows?",
        options: [
            "Riya studies natural phenomena",
            "Riya studies only chemistry",
            "Everyone is a physicist",
            "Natural phenomena do not involve physics",
        ],
        answer: 0,
        skill: "Analytical Thinking",
    },
    {
        id: 11404,
        question:
            "A is taller than B. B is taller than C. D is taller than A. Who is tallest?",
        options: ["A", "B", "C", "D"],
        answer: 3,
        skill: "Analytical Thinking",
    },
    {
        id: 11405,
        question:
            "Find the missing term: 3, 7, 15, 31, ?",
        options: ["47", "55", "63", "64"],
        answer: 2,
        skill: "Logical Reasoning",
    },
    {
        id: 11406,
        question:
            "A student observes that a pendulum takes longer to complete an oscillation when its length is increased. Which is the most reasonable inference?",
        options: [
            "Time period may depend on pendulum length",
            "Pendulum length never affects motion",
            "Mass must always become zero",
            "Gravity has disappeared",
        ],
        answer: 0,
        skill: "Critical Thinking",
    },
    {
        id: 11407,
        question:
            "Which number is the odd one out: 8, 27, 64, 100, 125?",
        options: ["27", "64", "100", "125"],
        answer: 2,
        skill: "Logical Reasoning",
    },
    {
        id: 11408,
        question:
            "If P > Q, Q = R and R > S, which statement is definitely true?",
        options: [
            "P < S",
            "P > S",
            "S > Q",
            "P = S",
        ],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 11409,
        question:
            "A formula works for five tested cases but fails in a sixth case. What should be concluded?",
        options: [
            "The sixth case must be deleted",
            "The formula should be examined for limitations",
            "The formula is automatically universal",
            "Testing is unnecessary",
        ],
        answer: 1,
        skill: "Critical Thinking",
    },
    {
        id: 11410,
        question:
            "A person walks 5 km north, 3 km east and then 5 km south. Where is the person relative to the starting point?",
        options: [
            "3 km east",
            "3 km west",
            "5 km north",
            "5 km south",
        ],
        answer: 0,
        skill: "Problem Solving",
    },
    {
        id: 11411,
        question:
            "Complete the analogy: Velocity : Motion :: Concentration : ?",
        options: [
            "Solution",
            "Distance",
            "Force",
            "Energy",
        ],
        answer: 0,
        skill: "Logical Reasoning",
    },
    {
        id: 11412,
        question:
            "Four students P, Q, R and S sit in a row. P is left of Q. R is right of Q. S is left of P. Who sits at the extreme left?",
        options: ["P", "Q", "R", "S"],
        answer: 3,
        skill: "Analytical Thinking",
    },
    {
        id: 11413,
        question:
            "A measurement is recorded as 10.2 cm, 10.3 cm, 10.2 cm and 15.8 cm. Which result should be investigated as a possible outlier?",
        options: [
            "10.2 cm",
            "10.3 cm",
            "15.8 cm",
            "All are equally similar",
        ],
        answer: 2,
        skill: "Critical Thinking",
    },
    {
        id: 11414,
        question:
            "If 2 → 6, 3 → 12 and 4 → 20 according to the same rule, then 5 → ?",
        options: ["25", "28", "30", "35"],
        answer: 2,
        skill: "Problem Solving",
    },
    {
        id: 11415,
        question:
            "Two explanations fit the same observation. What is the best scientific approach?",
        options: [
            "Choose the simpler explanation without testing",
            "Design further tests that distinguish between the explanations",
            "Accept both as permanently correct",
            "Ignore the observation",
        ],
        answer: 1,
        skill: "Critical Thinking",
    },
];

/* =========================================================
   CLASS 11 PCM QUESTION BANK
   ========================================================= */

export const class11PCMQuestionBank:
    AssessmentQuestionBank = {
    aptitude: class11PCMAptitudeQuestions,
    math: class11PCMMathematicsQuestions,
    english: class11PCMEnglishQuestions,
    science: class11PCMScienceQuestions,
    reasoning: class11PCMReasoningQuestions,
};