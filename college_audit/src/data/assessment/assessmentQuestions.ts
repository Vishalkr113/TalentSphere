
import { class11PCMQuestionBank } from "./questions/class11PCMQuestions";export type AssessmentSkill =
    | "Numerical Ability"
    | "Arithmetic"
    | "Logical Reasoning"
    | "Analytical Thinking"
    | "Problem Solving"
    | "Critical Thinking"
    | "Grammar"
    | "Vocabulary"
    | "Reading Comprehension"
    | "Communication"
    | "Interpretation"
    | "Physics"
    | "Chemistry"
    | "Biology"
    | "Mathematics"
    | "Accountancy"
    | "Economics"
    | "Business Studies"
    | "Social Analysis";

export interface Question {
    id: number;
    question: string;
    options: string[];
    answer: number;
    skill: AssessmentSkill;
}

/* =========================================================
   APTITUDE ASSESSMENT — 15 QUESTIONS
   ========================================================= */

export const aptitudeQuestions: Question[] = [
    {
        id: 1,
        question:
            "A shopkeeper marks an item at ₹1,200 and gives a 15% discount. What is the selling price?",
        options: [
            "₹980",
            "₹1,000",
            "₹1,020",
            "₹1,080",
        ],
        answer: 2,
        skill: "Numerical Ability",
    },
    {
        id: 2,
        question:
            "The ratio of boys to girls in a class is 3:2. If there are 40 students, how many are girls?",
        options: [
            "14",
            "16",
            "20",
            "24",
        ],
        answer: 1,
        skill: "Numerical Ability",
    },
    {
        id: 3,
        question:
            "Find the next number in the series: 3, 8, 15, 24, 35, ?",
        options: [
            "46",
            "47",
            "48",
            "49",
        ],
        answer: 2,
        skill: "Logical Reasoning",
    },
    {
        id: 4,
        question:
            "A student completes 3/5 of a project in 6 days at a constant rate. How many more days are needed to finish the project?",
        options: [
            "2",
            "3",
            "4",
            "5",
        ],
        answer: 2,
        skill: "Problem Solving",
    },
    {
        id: 5,
        question:
            "All scientists are curious. Some curious people are writers. Which statement is definitely true?",
        options: [
            "All writers are scientists",
            "Some scientists are writers",
            "Scientists are curious",
            "No curious person is a scientist",
        ],
        answer: 2,
        skill: "Analytical Thinking",
    },
    {
        id: 6,
        question:
            "The average of five numbers is 24. Four numbers are 18, 21, 25 and 26. What is the fifth number?",
        options: [
            "28",
            "30",
            "32",
            "34",
        ],
        answer: 1,
        skill: "Numerical Ability",
    },
    {
        id: 7,
        question:
            "A train covers 180 km in 3 hours. At the same speed, how far will it travel in 4.5 hours?",
        options: [
            "240 km",
            "250 km",
            "270 km",
            "300 km",
        ],
        answer: 2,
        skill: "Arithmetic",
    },
    {
        id: 8,
        question:
            "Find the odd one out: 16, 25, 36, 45, 49.",
        options: [
            "16",
            "25",
            "45",
            "49",
        ],
        answer: 2,
        skill: "Logical Reasoning",
    },
    {
        id: 9,
        question:
            "A school has ₹18,000 for 12 identical science kits. What is the maximum cost per kit?",
        options: [
            "₹1,200",
            "₹1,400",
            "₹1,500",
            "₹1,800",
        ],
        answer: 2,
        skill: "Problem Solving",
    },
    {
        id: 10,
        question:
            "If P is north of Q and R is east of P, in which direction is R from Q?",
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
        id: 11,
        question:
            "A number is increased by 20% and becomes 360. What was the original number?",
        options: [
            "280",
            "300",
            "320",
            "340",
        ],
        answer: 1,
        skill: "Numerical Ability",
    },
    {
        id: 12,
        question:
            "If 8 workers complete a task in 15 days, how many days would 12 equally efficient workers take?",
        options: [
            "8",
            "10",
            "12",
            "18",
        ],
        answer: 1,
        skill: "Arithmetic",
    },
    {
        id: 13,
        question:
            "Book is to Reading as Fork is to:",
        options: [
            "Drawing",
            "Eating",
            "Writing",
            "Cutting",
        ],
        answer: 1,
        skill: "Logical Reasoning",
    },
    {
        id: 14,
        question:
            "A student must choose exactly two activities from Coding, Music and Sports. If Coding is chosen, Sports cannot be chosen. Which pair is possible?",
        options: [
            "Coding and Sports",
            "Coding and Music",
            "All three",
            "Coding only",
        ],
        answer: 1,
        skill: "Problem Solving",
    },
    {
        id: 15,
        question:
            "Meera scored more than Rohan but less than Aditi. Kabir scored less than Rohan. Who scored the highest?",
        options: [
            "Meera",
            "Rohan",
            "Aditi",
            "Kabir",
        ],
        answer: 2,
        skill: "Analytical Thinking",
    },
];

/* =========================================================
   MATHEMATICS ASSESSMENT — 15 QUESTIONS
   ========================================================= */

export const mathQuestions: Question[] = [
    {
        id: 101,
        question:
            "Solve: 3x - 7 = 2x + 5.",
        options: [
            "10",
            "12",
            "14",
            "16",
        ],
        answer: 1,
        skill: "Problem Solving",
    },
    {
        id: 102,
        question:
            "If x² - 9 = 0, what are the possible values of x?",
        options: [
            "3 only",
            "-3 only",
            "3 and -3",
            "9 and -9",
        ],
        answer: 2,
        skill: "Numerical Ability",
    },
    {
        id: 103,
        question:
            "A right triangle has perpendicular sides 6 cm and 8 cm. What is the hypotenuse?",
        options: [
            "9 cm",
            "10 cm",
            "12 cm",
            "14 cm",
        ],
        answer: 1,
        skill: "Problem Solving",
    },
    {
        id: 104,
        question:
            "What is the value of (2³ × 2⁴) ÷ 2⁵?",
        options: [
            "2",
            "4",
            "8",
            "16",
        ],
        answer: 1,
        skill: "Arithmetic",
    },
    {
        id: 105,
        question:
            "The mean of 6, 8, 10, 12 and x is 10. Find x.",
        options: [
            "12",
            "14",
            "16",
            "18",
        ],
        answer: 1,
        skill: "Numerical Ability",
    },
    {
        id: 106,
        question:
            "The circumference of a circle is 44 cm. Using π = 22/7, what is its radius?",
        options: [
            "5 cm",
            "7 cm",
            "10 cm",
            "14 cm",
        ],
        answer: 1,
        skill: "Problem Solving",
    },
    {
        id: 107,
        question:
            "Which of the following numbers is irrational?",
        options: [
            "0.25",
            "3/7",
            "√2",
            "0.125",
        ],
        answer: 2,
        skill: "Numerical Ability",
    },
    {
        id: 108,
        question:
            "Simplify: 5a - 2b + 3a + 4b.",
        options: [
            "8a + 2b",
            "8a - 6b",
            "2a + 2b",
            "8a + 6b",
        ],
        answer: 0,
        skill: "Arithmetic",
    },
    {
        id: 109,
        question:
            "A linear equation has graph y = 2x + 3. What is y when x = 4?",
        options: [
            "8",
            "9",
            "10",
            "11",
        ],
        answer: 3,
        skill: "Problem Solving",
    },
    {
        id: 110,
        question:
            "What is the probability of getting an even number when a fair die is rolled once?",
        options: [
            "1/6",
            "1/3",
            "1/2",
            "2/3",
        ],
        answer: 2,
        skill: "Numerical Ability",
    },
    {
        id: 111,
        question:
            "If sin θ = 3/5 for an acute angle θ, what is cos θ?",
        options: [
            "2/5",
            "3/4",
            "4/5",
            "5/3",
        ],
        answer: 2,
        skill: "Arithmetic",
    },
    {
        id: 112,
        question:
            "The area of a square is 196 cm². What is its perimeter?",
        options: [
            "28 cm",
            "42 cm",
            "56 cm",
            "64 cm",
        ],
        answer: 2,
        skill: "Problem Solving",
    },
    {
        id: 113,
        question:
            "The roots of x² - 5x + 6 = 0 are:",
        options: [
            "1 and 6",
            "2 and 3",
            "-2 and -3",
            "3 and 5",
        ],
        answer: 1,
        skill: "Numerical Ability",
    },
    {
        id: 114,
        question:
            "A quantity changes from 80 to 100. What is the percentage increase?",
        options: [
            "20%",
            "25%",
            "40%",
            "80%",
        ],
        answer: 1,
        skill: "Arithmetic",
    },
    {
        id: 115,
        question:
            "A cylindrical tank has radius 3 m and height 5 m. Which expression gives its volume?",
        options: [
            "15π m³",
            "30π m³",
            "45π m³",
            "90π m³",
        ],
        answer: 2,
        skill: "Problem Solving",
    },
];

/* =========================================================
   ENGLISH ASSESSMENT — 15 QUESTIONS
   ========================================================= */

export const englishQuestions: Question[] = [
    {
        id: 201,
        question:
            "Choose the grammatically correct sentence.",
        options: [
            "Neither of the students were absent.",
            "Neither of the students was absent.",
            "Neither of the student were absent.",
            "Neither students was absent.",
        ],
        answer: 1,
        skill: "Grammar",
    },
    {
        id: 202,
        question:
            "Choose the word closest in meaning to 'meticulous'.",
        options: [
            "Careless",
            "Precise",
            "Noisy",
            "Rapid",
        ],
        answer: 1,
        skill: "Vocabulary",
    },
    {
        id: 203,
        question:
            "Aarav noticed that rereading notes did not effectively test his learning. He started using practice questions and weekly self-checks. Why did Aarav change his study plan?",
        options: [
            "He wanted to study fewer subjects",
            "Rereading alone was not effectively testing his learning",
            "His school stopped giving notes",
            "He wanted to avoid revision",
        ],
        answer: 1,
        skill: "Reading Comprehension",
    },
    {
        id: 204,
        question:
            "Choose the correct reported speech: Riya said, 'I am preparing for the exam.'",
        options: [
            "Riya said that I am preparing for the exam.",
            "Riya said that she was preparing for the exam.",
            "Riya says she prepared for the exam.",
            "Riya said she is prepare for the exam.",
        ],
        answer: 1,
        skill: "Grammar",
    },
    {
        id: 205,
        question:
            "Choose the antonym of 'scarce'.",
        options: [
            "Rare",
            "Limited",
            "Abundant",
            "Small",
        ],
        answer: 2,
        skill: "Vocabulary",
    },
    {
        id: 206,
        question:
            "A school introduced a digital library, but students who followed a weekly reading schedule showed the greatest improvement. What is the main idea?",
        options: [
            "Digital libraries are unnecessary",
            "Printed books should be removed",
            "Regular reading habits matter more than access alone",
            "Students dislike digital resources",
        ],
        answer: 2,
        skill: "Reading Comprehension",
    },
    {
        id: 207,
        question:
            "Fill in the blank: By the time the teacher arrived, the students ___ the experiment.",
        options: [
            "complete",
            "completed",
            "had completed",
            "are completing",
        ],
        answer: 2,
        skill: "Grammar",
    },
    {
        id: 208,
        question:
            "Her explanation was so ___ that even a difficult concept became easy to understand.",
        options: [
            "vague",
            "clear",
            "random",
            "silent",
        ],
        answer: 1,
        skill: "Vocabulary",
    },
    {
        id: 209,
        question:
            "Kavya prefers projects where she can research a problem, compare evidence and explain her conclusion. Which activity best matches her preference?",
        options: [
            "Memorising a list without context",
            "Conducting an investigation and presenting findings",
            "Copying a paragraph repeatedly",
            "Avoiding open-ended questions",
        ],
        answer: 1,
        skill: "Reading Comprehension",
    },
    {
        id: 210,
        question:
            "Choose the correct passive form of: 'The team completed the project.'",
        options: [
            "The project completed the team.",
            "The project was completed by the team.",
            "The project is completing by the team.",
            "The team was completed by the project.",
        ],
        answer: 1,
        skill: "Grammar",
    },
    {
        id: 211,
        question:
            "What does 'evaluate' most nearly mean?",
        options: [
            "Ignore",
            "Assess",
            "Repeat",
            "Hide",
        ],
        answer: 1,
        skill: "Vocabulary",
    },
    {
        id: 212,
        question:
            "A city planted trees along busy roads. Some areas later recorded lower surface temperatures and improved shade. Which conclusion is best supported?",
        options: [
            "Trees always eliminate pollution",
            "Roads are unnecessary",
            "Urban trees can help reduce heat and improve pedestrian comfort",
            "All cities have the same climate",
        ],
        answer: 2,
        skill: "Reading Comprehension",
    },
    {
        id: 213,
        question:
            "Choose the sentence with correct subject-verb agreement.",
        options: [
            "The list of topics are on the desk.",
            "The list of topics is on the desk.",
            "The topics list are on the desk.",
            "The list of topic were on the desk.",
        ],
        answer: 1,
        skill: "Grammar",
    },
    {
        id: 214,
        question:
            "Choose the meaning of 'infer'.",
        options: [
            "Conclude from evidence",
            "Speak loudly",
            "Memorise exactly",
            "Disagree immediately",
        ],
        answer: 0,
        skill: "Vocabulary",
    },
    {
        id: 215,
        question:
            "Dev reviewed his mock-test errors and found that most came from time pressure and skipped calculation steps. What should Dev most logically improve?",
        options: [
            "Only handwriting",
            "Time management and careful calculation",
            "The number of school subjects",
            "His classroom seat",
        ],
        answer: 1,
        skill: "Reading Comprehension",
    },
];

/* =========================================================
   SCIENCE ASSESSMENT — 15 QUESTIONS
   5 PHYSICS + 5 CHEMISTRY + 5 BIOLOGY
   ========================================================= */

export const scienceQuestions: Question[] = [
    {
        id: 301,
        question:
            "A car increases its speed from 10 m/s to 20 m/s in 5 seconds. What is its acceleration?",
        options: [
            "1 m/s²",
            "2 m/s²",
            "5 m/s²",
            "10 m/s²",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 302,
        question:
            "Two resistors of 2 Ω and 4 Ω are connected in series. What is their equivalent resistance?",
        options: [
            "1.3 Ω",
            "2 Ω",
            "6 Ω",
            "8 Ω",
        ],
        answer: 2,
        skill: "Physics",
    },
    {
        id: 303,
        question:
            "Why does a pencil appear bent when partly immersed in water?",
        options: [
            "Reflection",
            "Refraction",
            "Dispersion",
            "Diffusion",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 304,
        question:
            "An object is placed in front of a plane mirror. Which statement about its image is correct?",
        options: [
            "It is real and inverted",
            "It is virtual and of the same size",
            "It is smaller and real",
            "It is magnified and inverted",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 305,
        question:
            "Which energy conversion mainly occurs in an electric fan?",
        options: [
            "Mechanical to electrical",
            "Electrical to mechanical",
            "Chemical to light",
            "Heat to chemical",
        ],
        answer: 1,
        skill: "Physics",
    },
    {
        id: 306,
        question:
            "Which substance will most likely turn blue litmus paper red?",
        options: [
            "Soap solution",
            "Lime water",
            "Dilute hydrochloric acid",
            "Baking soda solution",
        ],
        answer: 2,
        skill: "Chemistry",
    },
    {
        id: 307,
        question:
            "In the reaction Zn + 2HCl → ZnCl₂ + H₂, which gas is released?",
        options: [
            "Oxygen",
            "Hydrogen",
            "Chlorine",
            "Nitrogen",
        ],
        answer: 1,
        skill: "Chemistry",
    },
    {
        id: 308,
        question:
            "Why is galvanisation used on iron objects?",
        options: [
            "To increase their mass",
            "To prevent corrosion",
            "To make iron magnetic",
            "To reduce conductivity",
        ],
        answer: 1,
        skill: "Chemistry",
    },
    {
        id: 309,
        question:
            "Which element has the electronic configuration 2, 8, 1?",
        options: [
            "Magnesium",
            "Sodium",
            "Chlorine",
            "Neon",
        ],
        answer: 1,
        skill: "Chemistry",
    },
    {
        id: 310,
        question:
            "A solution has pH 9. Which statement is most appropriate?",
        options: [
            "It is acidic",
            "It is basic",
            "It is neutral",
            "It must be pure water",
        ],
        answer: 1,
        skill: "Chemistry",
    },
    {
        id: 311,
        question:
            "Which cell organelle is primarily responsible for releasing energy through cellular respiration?",
        options: [
            "Nucleus",
            "Mitochondrion",
            "Ribosome",
            "Vacuole",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 312,
        question:
            "Which blood vessel carries oxygenated blood from the lungs to the heart?",
        options: [
            "Pulmonary artery",
            "Pulmonary vein",
            "Aorta",
            "Vena cava",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 313,
        question:
            "A plant shoot bends toward light mainly because of the action of:",
        options: [
            "Insulin",
            "Auxin",
            "Adrenaline",
            "Thyroxine",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 314,
        question:
            "Why is variation important in a population?",
        options: [
            "It guarantees every organism survives",
            "It can improve the chance that some individuals survive environmental changes",
            "It stops reproduction",
            "It makes all individuals identical",
        ],
        answer: 1,
        skill: "Biology",
    },
    {
        id: 315,
        question:
            "Which sequence correctly represents a simple food chain?",
        options: [
            "Tiger → Grass → Deer",
            "Grass → Deer → Tiger",
            "Deer → Tiger → Grass",
            "Grass → Tiger → Deer",
        ],
        answer: 1,
        skill: "Biology",
    },
];

/* =========================================================
   LOGICAL REASONING ASSESSMENT — 15 QUESTIONS
   ========================================================= */

export const reasoningQuestions: Question[] = [
    {
        id: 401,
        question:
            "Find the next number: 4, 9, 19, 39, 79, ?",
        options: [
            "119",
            "139",
            "159",
            "169",
        ],
        answer: 2,
        skill: "Logical Reasoning",
    },
    {
        id: 402,
        question:
            "If CAT is coded as DBU, how is DOG coded using the same rule?",
        options: [
            "EPH",
            "EOH",
            "FPH",
            "EOG",
        ],
        answer: 0,
        skill: "Analytical Thinking",
    },
    {
        id: 403,
        question:
            "Five students P, Q, R, S and T stand in a line. P is before Q, R is after Q and S is before P. Which order is possible?",
        options: [
            "P-S-Q-R-T",
            "S-P-Q-R-T",
            "Q-P-S-R-T",
            "R-Q-P-S-T",
        ],
        answer: 1,
        skill: "Problem Solving",
    },
    {
        id: 404,
        question:
            "Find the missing term: AZ, BY, CX, DW, ?",
        options: [
            "EV",
            "EU",
            "FV",
            "EW",
        ],
        answer: 0,
        skill: "Logical Reasoning",
    },
    {
        id: 405,
        question:
            "All laptops are devices. Some devices are portable. Which conclusion must be true?",
        options: [
            "All portable things are laptops",
            "Laptops are devices",
            "Some laptops are definitely portable",
            "No device is portable",
        ],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 406,
        question:
            "A clock gains 5 minutes every hour. If it is correct at 8:00 AM, what will it show at actual 12:00 noon?",
        options: [
            "12:05 PM",
            "12:15 PM",
            "12:20 PM",
            "12:25 PM",
        ],
        answer: 2,
        skill: "Problem Solving",
    },
    {
        id: 407,
        question:
            "Find the next number: 1, 2, 6, 24, 120, ?",
        options: [
            "240",
            "360",
            "600",
            "720",
        ],
        answer: 3,
        skill: "Logical Reasoning",
    },
    {
        id: 408,
        question:
            "A is the sister of B. B is the son of C. How is A related to C?",
        options: [
            "Daughter",
            "Mother",
            "Sister",
            "Aunt",
        ],
        answer: 0,
        skill: "Analytical Thinking",
    },
    {
        id: 409,
        question:
            "A student walks 4 km north, 3 km east and then 4 km south. How far and in which direction is the student from the starting point?",
        options: [
            "3 km east",
            "3 km west",
            "4 km north",
            "5 km east",
        ],
        answer: 0,
        skill: "Problem Solving",
    },
    {
        id: 410,
        question:
            "Find the next letter group: AB, DE, GH, JK, ?",
        options: [
            "LM",
            "MN",
            "NO",
            "OP",
        ],
        answer: 1,
        skill: "Logical Reasoning",
    },
    {
        id: 411,
        question:
            "If some artists are teachers and all teachers are readers, which conclusion follows?",
        options: [
            "All artists are readers",
            "Some artists are readers",
            "No reader is an artist",
            "All readers are teachers",
        ],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 412,
        question:
            "A test has 40 questions. A student gets 3 marks for each correct answer and loses 1 mark for each wrong answer. All questions are attempted and 30 are correct. What is the score?",
        options: [
            "70",
            "80",
            "90",
            "100",
        ],
        answer: 1,
        skill: "Problem Solving",
    },
    {
        id: 413,
        question:
            "Find the next number: 7, 10, 16, 25, 37, ?",
        options: [
            "49",
            "50",
            "52",
            "54",
        ],
        answer: 2,
        skill: "Logical Reasoning",
    },
    {
        id: 414,
        question:
            "No engineer is careless. Some students are engineers. Which conclusion is valid?",
        options: [
            "All students are careful",
            "Some students are not careless",
            "No student is careless",
            "All careful people are engineers",
        ],
        answer: 1,
        skill: "Analytical Thinking",
    },
    {
        id: 415,
        question:
            "Three boxes are labelled Apples, Oranges and Mixed, but every label is wrong. From which box should you pick one fruit first to identify all boxes?",
        options: [
            "Apples",
            "Oranges",
            "Mixed",
            "Any box gives the same information",
        ],
        answer: 2,
        skill: "Problem Solving",
    },
];

export type StudentClass = "10" | "11" | "12";

export type StudentStream =
    | "Science PCM"
    | "Science PCB"
    | "Science PCMB"
    | "Commerce with Mathematics"
    | "Commerce without Mathematics"
    | "Humanities"
    | string;

export type AssessmentCategory =
    | "aptitude"
    | "math"
    | "english"
    | "science"
    | "reasoning";

export interface AssessmentQuestionBank {
    aptitude: Question[];
    math: Question[];
    english: Question[];
    science: Question[];
    reasoning: Question[];
}

export interface AssessmentQuestionContext {
    studentClass: StudentClass;
    currentStream?: StudentStream | null;
}

/* CLASS 10 QUESTION BANK
   Purpose: Stream discovery and Class 11 stream recommendation. */

export const class10AssessmentQuestionBank:
    AssessmentQuestionBank = {
    aptitude: aptitudeQuestions,
    math: mathQuestions,
    english: englishQuestions,
    science: scienceQuestions,
    reasoning: reasoningQuestions,
};

/* CLASS 11 QUESTION BANKS */

export const class11PCBQuestionBank:
    AssessmentQuestionBank = {
    aptitude: aptitudeQuestions,
    math: mathQuestions,
    english: englishQuestions,
    science: scienceQuestions,
    reasoning: reasoningQuestions,
};

export const class11PCMBQuestionBank:
    AssessmentQuestionBank = {
    aptitude: aptitudeQuestions,
    math: mathQuestions,
    english: englishQuestions,
    science: scienceQuestions,
    reasoning: reasoningQuestions,
};

export const class11CommerceQuestionBank:
    AssessmentQuestionBank = {
    aptitude: aptitudeQuestions,
    math: mathQuestions,
    english: englishQuestions,
    science: scienceQuestions,
    reasoning: reasoningQuestions,
};

export const class11HumanitiesQuestionBank:
    AssessmentQuestionBank = {
    aptitude: aptitudeQuestions,
    math: mathQuestions,
    english: englishQuestions,
    science: scienceQuestions,
    reasoning: reasoningQuestions,
};

/* CLASS 12 QUESTION BANKS*/

export const class12PCMQuestionBank:
    AssessmentQuestionBank = {
    aptitude: aptitudeQuestions,
    math: mathQuestions,
    english: englishQuestions,
    science: scienceQuestions,
    reasoning: reasoningQuestions,
};

export const class12PCBQuestionBank:
    AssessmentQuestionBank = {
    aptitude: aptitudeQuestions,
    math: mathQuestions,
    english: englishQuestions,
    science: scienceQuestions,
    reasoning: reasoningQuestions,
};

export const class12PCMBQuestionBank:
    AssessmentQuestionBank = {
    aptitude: aptitudeQuestions,
    math: mathQuestions,
    english: englishQuestions,
    science: scienceQuestions,
    reasoning: reasoningQuestions,
};

export const class12CommerceQuestionBank:
    AssessmentQuestionBank = {
    aptitude: aptitudeQuestions,
    math: mathQuestions,
    english: englishQuestions,
    science: scienceQuestions,
    reasoning: reasoningQuestions,
};

export const class12HumanitiesQuestionBank:
    AssessmentQuestionBank = {
    aptitude: aptitudeQuestions,
    math: mathQuestions,
    english: englishQuestions,
    science: scienceQuestions,
    reasoning: reasoningQuestions,
};

/* STREAM NORMALIZATION */

function normalizeStream(
    stream?: StudentStream | null
):
    | "pcm"
    | "pcb"
    | "pcmb"
    | "commerce"
    | "humanities"
    | "unknown" {
    if (!stream) {
        return "unknown";
    }

    const normalized = stream
        .trim()
        .toLowerCase();

    if (
        normalized.includes("pcmb") ||
        (
            normalized.includes("physics") &&
            normalized.includes("chemistry") &&
            normalized.includes("mathematics") &&
            normalized.includes("biology")
        )
    ) {
        return "pcmb";
    }

    if (
        normalized.includes("pcm") ||
        (
            normalized.includes("physics") &&
            normalized.includes("chemistry") &&
            normalized.includes("mathematics")
        )
    ) {
        return "pcm";
    }

    if (
        normalized.includes("pcb") ||
        (
            normalized.includes("physics") &&
            normalized.includes("chemistry") &&
            normalized.includes("biology")
        )
    ) {
        return "pcb";
    }

    if (
        normalized.includes("commerce") ||
        normalized.includes("business")
    ) {
        return "commerce";
    }

    if (
        normalized.includes("humanities") ||
        normalized.includes("arts")
    ) {
        return "humanities";
    }

    return "unknown";
}

/* CLASS 11 QUESTION BANK RESOLVER */

function getClass11QuestionBank(
    currentStream?: StudentStream | null
): AssessmentQuestionBank {
    const stream =
        normalizeStream(currentStream);

    switch (stream) {
        case "pcm":
            return class11PCMQuestionBank;

        case "pcb":
            return class11PCBQuestionBank;

        case "pcmb":
            return class11PCMBQuestionBank;

        case "commerce":
            return class11CommerceQuestionBank;

        case "humanities":
            return class11HumanitiesQuestionBank;

        default:
            return class10AssessmentQuestionBank;
    }
}

/* CLASS 12 QUESTION BANK RESOLVER */

function getClass12QuestionBank(
    currentStream?: StudentStream | null
): AssessmentQuestionBank {
    const stream =
        normalizeStream(currentStream);

    switch (stream) {
        case "pcm":
            return class12PCMQuestionBank;

        case "pcb":
            return class12PCBQuestionBank;

        case "pcmb":
            return class12PCMBQuestionBank;

        case "commerce":
            return class12CommerceQuestionBank;

        case "humanities":
            return class12HumanitiesQuestionBank;

        default:
            return class10AssessmentQuestionBank;
    }
}

/*MAIN CLASS-AWARE QUESTION BANK RESOLVER */

export function getAssessmentQuestionBank({
    studentClass,
    currentStream,
}: AssessmentQuestionContext):
    AssessmentQuestionBank {
    switch (studentClass) {
        case "10":
            return class10AssessmentQuestionBank;

        case "11":
            return getClass11QuestionBank(
                currentStream
            );

        case "12":
            return getClass12QuestionBank(
                currentStream
            );

        default:
            return class10AssessmentQuestionBank;
    }
}

/*BACKWARD-COMPATIBLE QUESTION BANK
   Existing services can continue using:
   assessmentQuestionBank[category]*/

export const assessmentQuestionBank =
    class10AssessmentQuestionBank;

/* QUESTION RESOLVERS */

export function getAssessmentQuestions(
    category: AssessmentCategory
): Question[] {
    return assessmentQuestionBank[category];
}

export function getContextualAssessmentQuestions(
    context: AssessmentQuestionContext,
    category: AssessmentCategory
): Question[] {
    const questionBank =
        getAssessmentQuestionBank(context);

    return questionBank[category];
}