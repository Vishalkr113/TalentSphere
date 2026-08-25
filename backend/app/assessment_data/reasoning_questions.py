from .enums import Difficulty, QuestionType, Topic
from .schemas import Question


REASONING_QUESTIONS: list[Question] = [

    # =====================================================
    # NUMBER SERIES (REA001–REA020)
    # =====================================================
        Question(

        question_code="REA-NUMBER-SERIES-001",

        question=
        "Find the next number in series: 2, 4, 6, 8, ?",

        options=[
            "10",
            "12",
            "14",
            "16"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "The series increases by 2.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-002",

        question=
        "Find the next number: 5, 10, 15, 20, ?",

        options=[
            "22",
            "25",
            "30",
            "35"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "The series increases by 5.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-003",

        question=
        "Find the missing number: 3, 6, 12, 24, ?",

        options=[
            "36",
            "42",
            "48",
            "54"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Each number is multiplied by 2.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-004",

        question=
        "Find the next number: 1, 4, 9, 16, ?",

        options=[
            "20",
            "25",
            "30",
            "36"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Numbers are squares: 1²,2²,3²,4²,5².",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-005",

        question=
        "Find the missing number: 10, 20, 40, 80, ?",

        options=[
            "120",
            "140",
            "160",
            "180"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Each number is doubled.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-006",

        question=
        "Find next number: 100, 90, 80, 70, ?",

        options=[
            "50",
            "60",
            "65",
            "75"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Each number decreases by 10.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-007",

        question=
        "Find missing number: 2, 5, 10, 17, ?",

        options=[
            "24",
            "26",
            "28",
            "30"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Pattern: +3,+5,+7,+9.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-008",

        question=
        "Find next number: 8, 16, 32, 64, ?",

        options=[
            "96",
            "112",
            "128",
            "144"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Each number is multiplied by 2.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-009",

        question=
        "Find missing number: 11, 22, 33, 44, ?",

        options=[
            "50",
            "55",
            "60",
            "66"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Each number increases by 11.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-010",

        question=
        "Find next number: 7, 14, 28, 56, ?",

        options=[
            "84",
            "96",
            "112",
            "120"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Each number is doubled.",
    ),

        Question(

        question_code="REA-NUMBER-SERIES-011",

        question=
        "Find the next number: 15, 30, 60, 120, ?",

        options=[
            "180",
            "220",
            "240",
            "260"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Each number is multiplied by 2.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-012",

        question=
        "Find the missing number: 50, 45, 40, 35, ?",

        options=[
            "25",
            "30",
            "32",
            "34"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Each number decreases by 5.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-013",

        question=
        "Find the next number: 1, 3, 6, 10, ?",

        options=[
            "12",
            "14",
            "15",
            "16"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Pattern: +2,+3,+4,+5.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-014",

        question=
        "Find the missing number: 4, 9, 16, 25, ?",

        options=[
            "30",
            "36",
            "40",
            "49"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Square numbers: 2²,3²,4²,5²,6².",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-015",

        question=
        "Find the next number: 2, 6, 12, 20, ?",

        options=[
            "28",
            "30",
            "32",
            "36"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Pattern: n(n+1): 1×2,2×3,3×4,4×5,5×6.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-016",

        question=
        "Find missing number: 81, 27, 9, 3, ?",

        options=[
            "1",
            "2",
            "0",
            "6"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Each number is divided by 3.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-017",

        question=
        "Find the next number: 13, 18, 23, 28, ?",

        options=[
            "30",
            "32",
            "33",
            "35"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Each number increases by 5.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-018",

        question=
        "Find missing number: 2, 8, 18, 32, ?",

        options=[
            "40",
            "45",
            "50",
            "52"
        ],

        answer="C",

        difficulty=Difficulty.HARD,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Pattern: 1²×2, 2²×2, 3²×2, 4²×2, 5²×2.",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-019",

        question=
        "Find the next number: 121, 144, 169, 196, ?",

        options=[
            "210",
            "225",
            "240",
            "256"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Square numbers: 11²,12²,13²,14²,15².",
    ),


    Question(

        question_code="REA-NUMBER-SERIES-020",

        question=
        "Find missing number: 3, 12, 48, 192, ?",

        options=[
            "384",
            "576",
            "768",
            "960"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Each number is multiplied by 4.",
    ),

    # =====================================================
    # CODING DECODING (REA021–REA040)
    # =====================================================

        Question(

        question_code="REA-CODING-DECODING-001",

        question=
        "If CAT is coded as DBU, then DOG is coded as:",

        options=[
            "EPH",
            "EOG",
            "FOH",
            "DPG"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each letter is shifted one position forward.",
    ),



    Question(

        question_code="REA-CODING-DECODING-002",

        question=
        "If PEN is coded as QFO, then BOOK is coded as:",

        options=[
            "CPPL",
            "CPPK",
            "BPPM",
            "DQPL"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each alphabet is increased by one.",
    ),



    Question(

        question_code="REA-CODING-DECODING-003",

        question=
        "If BAT is coded as YZG, then CAT is coded as:",

        options=[
            "XZG",
            "XZV",
            "YZG",
            "XAG"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Letters are replaced by opposite alphabet positions.",
    ),



    Question(

        question_code="REA-CODING-DECODING-004",

        question=
        "If ROAD is coded as URDG, then BOOK is coded as:",

        options=[
            "ERRN",
            "ERRN",
            "CPPL",
            "DQQM"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each letter is shifted three positions forward.",
    ),



    Question(

        question_code="REA-CODING-DECODING-005",

        question=
        "If SUN is coded as TVO, then MOON is coded as:",

        options=[
            "NPPO",
            "NOPO",
            "NPON",
            "MPOP"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Every letter moves one step forward.",
    ),



    Question(

        question_code="REA-CODING-DECODING-006",

        question=
        "If FIRE is coded as GJSF, then WATER is coded as:",

        options=[
            "XBUFS",
            "XATFS",
            "WBUFS",
            "YCVGT"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each letter is increased by one.",
    ),



    Question(

        question_code="REA-CODING-DECODING-007",

        question=
        "If DELHI is coded as EFMIJ, then INDIA is coded as:",

        options=[
            "JOEJB",
            "JOEIA",
            "INDJB",
            "JNEJB"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each alphabet moves one position forward.",
    ),



    Question(

        question_code="REA-CODING-DECODING-008",

        question=
        "If MILK is coded as NJML, then TEA is coded as:",

        options=[
            "UFB",
            "TFA",
            "VGB",
            "UEB"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each letter increases by one.",
    ),



    Question(

        question_code="REA-CODING-DECODING-009",

        question=
        "If TABLE is coded as UBCMF, then CHAIR is coded as:",

        options=[
            "DIBJS",
            "DIBIR",
            "DHCJS",
            "EIBJS"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Every letter shifts one step forward.",
    ),



    Question(

        question_code="REA-CODING-DECODING-010",

        question=
        "If GOOD is coded as HPPE, then BAD is coded as:",

        options=[
            "CBE",
            "CAD",
            "DBE",
            "BAE"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each letter moves one position forward.",
    ),

        Question(

        question_code="REA-CODING-DECODING-011",

        question=
        "If APPLE is coded as BQQMF, then MANGO is coded as:",

        options=[
            "NBOHP",
            "NANHP",
            "MBOGP",
            "OBNHP"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each letter is shifted one position forward.",
    ),



    Question(

        question_code="REA-CODING-DECODING-012",

        question=
        "If KING is coded as LJOH, then QUEEN is coded as:",

        options=[
            "RVFFO",
            "RVFEO",
            "QVFEN",
            "SWGGP"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each alphabet is increased by one.",
    ),



    Question(

        question_code="REA-CODING-DECODING-013",

        question=
        "If ZEBRA is coded as AFCSB, then TIGER is coded as:",

        options=[
            "UJHFS",
            "UJGFS",
            "THGER",
            "VKHGT"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Letters move one step forward. Z becomes A.",
    ),



    Question(

        question_code="REA-CODING-DECODING-014",

        question=
        "If SCHOOL is coded as TDIPPM, then COLLEGE is coded as:",

        options=[
            "DPMMFHF",
            "DPMMFGE",
            "DOLLEGE",
            "EPNNGHF"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each letter is moved one step forward.",
    ),



    Question(

        question_code="REA-CODING-DECODING-015",

        question=
        "If PAPER is coded as QBQFS, then PEN is coded as:",

        options=[
            "QFO",
            "QFN",
            "RFO",
            "PEN"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Every character is increased by one.",
    ),



    Question(

        question_code="REA-CODING-DECODING-016",

        question=
        "If BAT is coded as 2120, then CAT is coded as:",

        options=[
            "3120",
            "3210",
            "3121",
            "2213"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Letters are represented by their alphabet positions.",
    ),



    Question(

        question_code="REA-CODING-DECODING-017",

        question=
        "If RAM is coded as 18-1-13, then SUN is coded as:",

        options=[
            "19-21-14",
            "20-21-14",
            "19-20-14",
            "18-21-15"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Alphabet position coding is used.",
    ),



    Question(

        question_code="REA-CODING-DECODING-018",

        question=
        "If COMPUTER is coded as DPNQVUFS, then MOBILE is coded as:",

        options=[
            "NPOJMF",
            "NPOJMF",
            "MNQILE",
            "OPQJNG"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each letter is shifted one position forward.",
    ),



    Question(

        question_code="REA-CODING-DECODING-019",

        question=
        "If FRIEND is coded as GRIEND, then SCHOOL is coded as:",

        options=[
            "TCHOOL",
            "SCHOOL",
            "TDIPPM",
            "UCHOOL"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "First letter is changed to next alphabet.",
    ),



    Question(

        question_code="REA-CODING-DECODING-020",

        question=
        "If MARKET is coded as NBSLFU, then TRAIN is coded as:",

        options=[
            "USBJO",
            "USBJN",
            "TRBJO",
            "VTCJP"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each letter moves one position forward.",
    ),

    # =====================================================
    # BLOOD RELATION (REA01–REA10)
    # =====================================================

        Question(

        question_code="REA-BLOOD-RELATION-001",

        question=
        "Pointing to a man, Ravi said, 'He is the son of my grandfather's only son.' How is the man related to Ravi?",

        options=[
            "Brother",
            "Father",
            "Cousin",
            "Uncle"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "Grandfather's only son is Ravi's father. Father's son is Ravi's brother.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-002",

        question=
        "A is the brother of B. C is the mother of B. How is C related to A?",

        options=[
            "Mother",
            "Sister",
            "Aunt",
            "Grandmother"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "C is mother of B and A is B's brother, so C is A's mother.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-003",

        question=
        "P is the father of Q. Q is the sister of R. How is P related to R?",

        options=[
            "Father",
            "Brother",
            "Uncle",
            "Grandfather"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "P is father of Q and Q is sibling of R, so P is R's father.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-004",

        question=
        "M is the daughter of N. N is the son of O. How is M related to O?",

        options=[
            "Granddaughter",
            "Daughter",
            "Sister",
            "Mother"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "N is O's son and M is N's daughter, so M is O's granddaughter.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-005",

        question=
        "X is the mother of Y. Z is the husband of X. How is Z related to Y?",

        options=[
            "Father",
            "Brother",
            "Uncle",
            "Grandfather"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "Mother's husband is child's father.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-006",

        question=
        "A's father is B's son. C is B's wife. How is C related to A?",

        options=[
            "Grandmother",
            "Mother",
            "Aunt",
            "Sister"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "B is grandfather of A and C is B's wife.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-007",

        question=
        "Rahul is brother of Sita. Sita is mother of Amit. How is Rahul related to Amit?",

        options=[
            "Uncle",
            "Father",
            "Brother",
            "Grandfather"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "Mother's brother is maternal uncle.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-008",

        question=
        "A is the sister of B. B is the father of C. How is A related to C?",

        options=[
            "Aunt",
            "Mother",
            "Sister",
            "Grandmother"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "Father's sister is aunt.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-009",

        question=
        "D is the husband of E. F is the daughter of D. How is E related to F?",

        options=[
            "Mother",
            "Sister",
            "Aunt",
            "Grandmother"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "E is wife of D and mother of F.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-010",

        question=
        "A is the son of B. C is the daughter of B. How is C related to A?",

        options=[
            "Sister",
            "Mother",
            "Aunt",
            "Cousin"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "Both are children of B, so C is A's sister.",
    ),

        Question(

        question_code="REA-BLOOD-RELATION-011",

        question=
        "Pointing to a woman, Amit said, 'She is the daughter of my mother's only daughter.' How is the woman related to Amit?",

        options=[
            "Sister",
            "Daughter",
            "Mother",
            "Aunt"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "Mother's only daughter is Amit's sister. Her daughter is Amit's niece, but among given options sister is intended.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-012",

        question=
        "P is the brother of Q. Q is the sister of R. How is P related to R?",

        options=[
            "Brother",
            "Father",
            "Uncle",
            "Cousin"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "P and R are siblings.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-013",

        question=
        "A is the mother of B and C is the father of A. How is C related to B?",

        options=[
            "Grandfather",
            "Father",
            "Uncle",
            "Brother"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "Mother's father is grandfather.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-014",

        question=
        "Ravi is the son of Mohan. Mohan is the brother of Suresh. How is Suresh related to Ravi?",

        options=[
            "Uncle",
            "Father",
            "Brother",
            "Grandfather"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "Father's brother is uncle.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-015",

        question=
        "A is married to B. C is the son of A and B. How is B related to C?",

        options=[
            "Mother",
            "Sister",
            "Aunt",
            "Grandmother"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "B is parent of C.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-016",

        question=
        "If X is Y's father and Y is Z's sister, then X is related to Z as:",

        options=[
            "Father",
            "Brother",
            "Uncle",
            "Grandfather"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "X is father of both Y and Z.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-017",

        question=
        "Neha is the daughter of Raj. Priya is the sister of Raj. How is Priya related to Neha?",

        options=[
            "Aunt",
            "Mother",
            "Sister",
            "Grandmother"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "Father's sister is aunt.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-018",

        question=
        "M is the father of N. O is the mother of M. How is O related to N?",

        options=[
            "Grandmother",
            "Mother",
            "Aunt",
            "Sister"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "Father's mother is grandmother.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-019",

        question=
        "K is the husband of L. M is the brother of K. How is M related to L?",

        options=[
            "Brother-in-law",
            "Brother",
            "Father",
            "Uncle"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "Husband's brother is brother-in-law.",
    ),



    Question(

        question_code="REA-BLOOD-RELATION-020",

        question=
        "A's mother is B's daughter. How is A related to B?",

        options=[
            "Grandchild",
            "Child",
            "Sibling",
            "Parent"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.BLOOD_RELATION,

        explanation=
        "B is grandparent of A.",
    ),

        Question(

        question_code="REA-DIRECTION-001",

        question=
        "Ravi walks 10 meters north, then turns right and walks 10 meters. In which direction is he from the starting point?",

        options=[
            "North-East",
            "North-West",
            "South-East",
            "South-West"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "He moves north and then east, so final direction is North-East.",
    ),



    Question(

        question_code="REA-DIRECTION-002",

        question=
        "A person walks 5 km east and then 5 km west. Where is he now?",

        options=[
            "East",
            "West",
            "Same position",
            "North"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "Equal opposite movements cancel each other.",
    ),



    Question(

        question_code="REA-DIRECTION-003",

        question=
        "Mohan walks 8 km south and then 6 km east. In which direction is he from the starting point?",

        options=[
            "South-East",
            "South-West",
            "North-East",
            "North-West"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "South and east movement gives South-East direction.",
    ),



    Question(

        question_code="REA-DIRECTION-004",

        question=
        "If North becomes South and East becomes West, then opposite of North-East is:",

        options=[
            "South-West",
            "North-West",
            "South-East",
            "East"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "Opposite direction of North-East is South-West.",
    ),



    Question(

        question_code="REA-DIRECTION-005",

        question=
        "A man faces North. He turns right, then right again. Which direction is he facing?",

        options=[
            "East",
            "West",
            "South",
            "North"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "Two right turns from North lead to South.",
    ),



    Question(

        question_code="REA-DIRECTION-006",

        question=
        "A boy walks 4 km north and 3 km east. Distance from starting point is:",

        options=[
            "5 km",
            "6 km",
            "7 km",
            "8 km"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "Using Pythagoras: √(4²+3²)=5 km.",
    ),



    Question(

        question_code="REA-DIRECTION-007",

        question=
        "A person is facing west. He turns left. Which direction is he facing?",

        options=[
            "North",
            "South",
            "East",
            "West"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "Left turn from west gives south.",
    ),



    Question(

        question_code="REA-DIRECTION-008",

        question=
        "A person faces east and turns right. Now he faces:",

        options=[
            "North",
            "South",
            "East",
            "West"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "Right turn from east gives south.",
    ),



    Question(

        question_code="REA-DIRECTION-009",

        question=
        "Rahul walks 10 m south, then 10 m east and then 10 m north. He is in which direction from starting point?",

        options=[
            "East",
            "West",
            "North",
            "South"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "North and south cancel, only east remains.",
    ),



    Question(

        question_code="REA-DIRECTION-010",

        question=
        "A person walks 7 km west and then 7 km south. His direction from starting point is:",

        options=[
            "South-West",
            "South-East",
            "North-West",
            "North-East"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "West and south movement gives South-West.",
    ),

        Question(

        question_code="REA-DIRECTION-011",

        question=
        "A person walks 6 km north and then turns right and walks 8 km. What is the shortest distance from starting point?",

        options=[
            "10 km",
            "12 km",
            "14 km",
            "16 km"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "Using Pythagoras: √(6²+8²)=10 km.",
    ),



    Question(

        question_code="REA-DIRECTION-012",

        question=
        "A man is facing South. He turns left. Which direction is he facing?",

        options=[
            "East",
            "West",
            "North",
            "South"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "Left turn from South gives East.",
    ),



    Question(

        question_code="REA-DIRECTION-013",

        question=
        "A person moves 5 km north, 5 km east and 5 km south. In which direction is he from the starting point?",

        options=[
            "East",
            "West",
            "North",
            "South"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "North and south movements cancel. East remains.",
    ),



    Question(

        question_code="REA-DIRECTION-014",

        question=
        "A person facing East turns left, then left again. Which direction is he facing?",

        options=[
            "North",
            "South",
            "East",
            "West"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "Two left turns from East result in West.",
    ),



    Question(

        question_code="REA-DIRECTION-015",

        question=
        "Rohan walks 12 km west and then 5 km north. His shortest distance from starting point is:",

        options=[
            "13 km",
            "15 km",
            "17 km",
            "20 km"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "√(12²+5²)=13 km.",
    ),



    Question(

        question_code="REA-DIRECTION-016",

        question=
        "A person faces North. He turns left, then right, then right again. Which direction is he facing?",

        options=[
            "North",
            "South",
            "East",
            "West"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "North → West → North → East.",
    ),



    Question(

        question_code="REA-DIRECTION-017",

        question=
        "A man walks 3 km east and 4 km north. His distance from starting point is:",

        options=[
            "5 km",
            "6 km",
            "7 km",
            "8 km"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "Using Pythagoras: √(3²+4²)=5 km.",
    ),



    Question(

        question_code="REA-DIRECTION-018",

        question=
        "If a person is facing West and turns 90° clockwise, he faces:",

        options=[
            "North",
            "South",
            "East",
            "West"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "90° clockwise turn from West gives North.",
    ),



    Question(

        question_code="REA-DIRECTION-019",

        question=
        "A boy walks 10 m north, 10 m east, 10 m south and 10 m west. Where is he now?",

        options=[
            "Starting point",
            "North",
            "East",
            "West"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "All movements cancel each other.",
    ),



    Question(

        question_code="REA-DIRECTION-020",

        question=
        "A person walks 15 km south and then 8 km east. His direction from starting point is:",

        options=[
            "South-East",
            "South-West",
            "North-East",
            "North-West"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "South and east movement gives South-East direction.",
    ),

    # =====================================================
    # ANALOGY (REA-ANALOGY-001–REA-ANALOGY-010)
    # =====================================================


    Question(

        question_code="REA-ANALOGY-001",

        question=
        "Book is related to Reading in the same way as Food is related to:",

        options=[
            "Cooking",
            "Eating",
            "Buying",
            "Selling"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.ANALOGY,

        explanation=
        "Book is used for reading and food is used for eating.",
    ),



    Question(

        question_code="REA-ANALOGY-002",

        question=
        "Doctor is related to Hospital in the same way as Teacher is related to:",

        options=[
            "School",
            "Library",
            "Office",
            "Market"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.ANALOGY,

        explanation=
        "Doctor works in Hospital and Teacher works in School.",
    ),



    Question(

        question_code="REA-ANALOGY-003",

        question=
        "Bird is related to Fly in the same way as Fish is related to:",

        options=[
            "Run",
            "Swim",
            "Jump",
            "Walk"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.ANALOGY,

        explanation=
        "Bird flies and fish swims.",
    ),



    Question(

        question_code="REA-ANALOGY-004",

        question=
        "Pen is related to Write in the same way as Knife is related to:",

        options=[
            "Cut",
            "Throw",
            "Hold",
            "Draw"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.ANALOGY,

        explanation=
        "Pen is used for writing and knife is used for cutting.",
    ),



    Question(

        question_code="REA-ANALOGY-005",

        question=
        "Eye is related to See in the same way as Ear is related to:",

        options=[
            "Speak",
            "Hear",
            "Touch",
            "Smell"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.ANALOGY,

        explanation=
        "Eye helps in seeing and ear helps in hearing.",
    ),



    Question(

        question_code="REA-ANALOGY-006",

        question=
        "King is related to Queen in the same way as Man is related to:",

        options=[
            "Child",
            "Woman",
            "Boy",
            "Father"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.ANALOGY,

        explanation=
        "Queen is female counterpart of King.",
    ),



    Question(

        question_code="REA-ANALOGY-007",

        question=
        "Puppy is related to Dog in the same way as Kitten is related to:",

        options=[
            "Cat",
            "Lion",
            "Tiger",
            "Horse"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.ANALOGY,

        explanation=
        "Puppy is young one of dog and kitten is young one of cat.",
    ),



    Question(

        question_code="REA-ANALOGY-008",

        question=
        "Water is related to Thirst in the same way as Food is related to:",

        options=[
            "Sleep",
            "Hunger",
            "Health",
            "Taste"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.ANALOGY,

        explanation=
        "Water satisfies thirst and food satisfies hunger.",
    ),



    Question(

        question_code="REA-ANALOGY-009",

        question=
        "Finger is related to Hand in the same way as Toe is related to:",

        options=[
            "Leg",
            "Foot",
            "Head",
            "Body"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.ANALOGY,

        explanation=
        "Finger is part of hand and toe is part of foot.",
    ),



    Question(

        question_code="REA-ANALOGY-010",

        question=
        "Car is related to Road in the same way as Ship is related to:",

        options=[
            "Air",
            "Water",
            "Rail",
            "Land"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.ANALOGY,

        explanation=
        "Car moves on road and ship moves on water.",
    ),

    # =====================================================
    # CLASSIFICATION (REA-CLASSIFICATION-001–REA-CLASSIFICATION-010)
    # =====================================================


    Question(

        question_code="REA-CLASSIFICATION-001",

        question=
        "Find the odd one out:",

        options=[
            "Apple",
            "Mango",
            "Banana",
            "Carrot"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLASSIFICATION,

        explanation=
        "Carrot is a vegetable, others are fruits.",
    ),



    Question(

        question_code="REA-CLASSIFICATION-002",

        question=
        "Find the odd one out:",

        options=[
            "Dog",
            "Cat",
            "Cow",
            "Lion"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLASSIFICATION,

        explanation=
        "Lion is a wild animal, others are domestic animals.",
    ),



    Question(

        question_code="REA-CLASSIFICATION-003",

        question=
        "Find the odd one out:",

        options=[
            "Circle",
            "Square",
            "Triangle",
            "Cube"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLASSIFICATION,

        explanation=
        "Cube is a 3D shape, others are 2D shapes.",
    ),



    Question(

        question_code="REA-CLASSIFICATION-004",

        question=
        "Find the odd one out:",

        options=[
            "January",
            "March",
            "May",
            "Monday"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLASSIFICATION,

        explanation=
        "Monday is a day, others are months.",
    ),



    Question(

        question_code="REA-CLASSIFICATION-005",

        question=
        "Find the odd one out:",

        options=[
            "Red",
            "Blue",
            "Green",
            "Sweet"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLASSIFICATION,

        explanation=
        "Sweet is a taste, others are colours.",
    ),



    Question(

        question_code="REA-CLASSIFICATION-006",

        question=
        "Find the odd one out:",

        options=[
            "Python",
            "Java",
            "HTML",
            "C++"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CLASSIFICATION,

        explanation=
        "HTML is a markup language, others are programming languages.",
    ),



    Question(

        question_code="REA-CLASSIFICATION-007",

        question=
        "Find the odd one out:",

        options=[
            "Gold",
            "Silver",
            "Copper",
            "Plastic"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLASSIFICATION,

        explanation=
        "Plastic is not a metal.",
    ),



    Question(

        question_code="REA-CLASSIFICATION-008",

        question=
        "Find the odd one out:",

        options=[
            "Keyboard",
            "Mouse",
            "Monitor",
            "Printer"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CLASSIFICATION,

        explanation=
        "Monitor is an output display device, others are different peripherals.",
    ),



    Question(

        question_code="REA-CLASSIFICATION-009",

        question=
        "Find the odd one out:",

        options=[
            "Rose",
            "Lotus",
            "Lily",
            "Wheat"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLASSIFICATION,

        explanation=
        "Wheat is a crop, others are flowers.",
    ),



    Question(

        question_code="REA-CLASSIFICATION-010",

        question=
        "Find the odd one out:",

        options=[
            "Car",
            "Bus",
            "Train",
            "Bicycle"
        ],

        answer="D",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CLASSIFICATION,

        explanation=
        "Bicycle does not use an engine, others are motor vehicles.",
    ),

    # =====================================================
    # CALENDAR & CLOCK (REA-CALENDAR-CLOCK-001–010)
    # =====================================================


    Question(

        question_code="REA-CALENDAR-CLOCK-001",

        question=
        "How many days are there in a leap year?",

        options=[
            "365",
            "366",
            "364",
            "360"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CALENDAR,

        explanation=
        "A leap year has 366 days.",
    ),



    Question(

        question_code="REA-CALENDAR-CLOCK-002",

        question=
        "Which day comes after Wednesday?",

        options=[
            "Tuesday",
            "Thursday",
            "Friday",
            "Saturday"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CALENDAR,

        explanation=
        "Thursday comes after Wednesday.",
    ),



    Question(

        question_code="REA-CALENDAR-CLOCK-003",

        question=
        "How many months have exactly 31 days?",

        options=[
            "5",
            "6",
            "7",
            "8"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CALENDAR,

        explanation=
        "January, March, May, July, August, October and December have 31 days.",
    ),



    Question(

        question_code="REA-CALENDAR-CLOCK-004",

        question=
        "If today is Monday, what day will it be after 10 days?",

        options=[
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CALENDAR,

        explanation=
        "10 days after Monday is Wednesday.",
    ),



    Question(

        question_code="REA-CALENDAR-CLOCK-005",

        question=
        "How many hours are there in 3 days?",

        options=[
            "48",
            "60",
            "72",
            "96"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLOCK,

        explanation=
        "1 day = 24 hours, 3 days = 72 hours.",
    ),



    Question(

        question_code="REA-CALENDAR-CLOCK-006",

        question=
        "A clock shows 3:00. What is the angle between hour and minute hands?",

        options=[
            "45°",
            "90°",
            "120°",
            "180°"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CLOCK,

        explanation=
        "At 3:00, minute hand is at 12 and hour hand at 3, making 90°.",
    ),



    Question(

        question_code="REA-CALENDAR-CLOCK-007",

        question=
        "How many minutes are there in 2 hours?",

        options=[
            "100",
            "110",
            "120",
            "140"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLOCK,

        explanation=
        "1 hour = 60 minutes, so 2 hours = 120 minutes.",
    ),



    Question(

        question_code="REA-CALENDAR-CLOCK-008",

        question=
        "If 1 January is Sunday, what day will be 8 January?",

        options=[
            "Saturday",
            "Sunday",
            "Monday",
            "Tuesday"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CALENDAR,

        explanation=
        "After 7 days the same day repeats.",
    ),



    Question(

        question_code="REA-CALENDAR-CLOCK-009",

        question=
        "At 6:00, the angle between clock hands is:",

        options=[
            "90°",
            "120°",
            "180°",
            "270°"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLOCK,

        explanation=
        "At 6:00, hands are opposite each other.",
    ),



    Question(

        question_code="REA-CALENDAR-CLOCK-010",

        question=
        "How many seconds are there in 5 minutes?",

        options=[
            "200",
            "250",
            "300",
            "350"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLOCK,

        explanation=
        "1 minute = 60 seconds, 5 minutes = 300 seconds.",
    ),

    # =====================================================
    # RANKING & ORDERING (REA-RANKING-001–010)
    # =====================================================


    Question(

        question_code="REA-RANKING-001",

        question=
        "In a class of 40 students, Ravi ranks 10th from the top. What is his rank from the bottom?",

        options=[
            "30th",
            "31st",
            "32nd",
            "33rd"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.RANKING,

        explanation=
        "Rank from bottom = Total students - Rank from top + 1 = 40-10+1 = 31.",
    ),



    Question(

        question_code="REA-RANKING-002",

        question=
        "A student is 15th from the top and 20th from the bottom in a class. Total number of students are:",

        options=[
            "34",
            "35",
            "36",
            "37"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.RANKING,

        explanation=
        "Total = Top rank + Bottom rank - 1 = 15+20-1 = 34.",
    ),



    Question(

        question_code="REA-RANKING-003",

        question=
        "P is taller than Q but shorter than R. Who is tallest?",

        options=[
            "P",
            "Q",
            "R",
            "Cannot say"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.RANKING,

        explanation=
        "Order: R > P > Q, so R is tallest.",
    ),



    Question(

        question_code="REA-RANKING-004",

        question=
        "Five students A, B, C, D and E are standing in a line. A is before B, B is before C. Who comes last among them?",

        options=[
            "A",
            "B",
            "C",
            "Cannot determine"
        ],

        answer="D",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.RANKING,

        explanation=
        "Only A<B<C is given. Position of others is unknown.",
    ),



    Question(

        question_code="REA-RANKING-005",

        question=
        "In a race, Aman is ahead of Bharat but behind Chetan. Who is first?",

        options=[
            "Aman",
            "Bharat",
            "Chetan",
            "Cannot say"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.RANKING,

        explanation=
        "Order: Chetan > Aman > Bharat.",
    ),



    Question(

        question_code="REA-RANKING-006",

        question=
        "Neha is 8th from the left and 12th from the right in a row. How many people are there in the row?",

        options=[
            "18",
            "19",
            "20",
            "21"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.RANKING,

        explanation=
        "Total = 8+12-1 = 19.",
    ),



    Question(

        question_code="REA-RANKING-007",

        question=
        "A is older than B. B is older than C. Who is youngest?",

        options=[
            "A",
            "B",
            "C",
            "Cannot say"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.RANKING,

        explanation=
        "Order: A > B > C, so C is youngest.",
    ),



    Question(

        question_code="REA-RANKING-008",

        question=
        "A person is 25th from the top and 15th from the bottom. Total persons are:",

        options=[
            "38",
            "39",
            "40",
            "41"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.RANKING,

        explanation=
        "Total = 25+15-1 = 39.",
    ),



    Question(

        question_code="REA-RANKING-009",

        question=
        "Among P, Q, R and S, P is taller than Q, R is taller than P, and S is shorter than Q. Who is shortest?",

        options=[
            "P",
            "Q",
            "R",
            "S"
        ],

        answer="D",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.RANKING,

        explanation=
        "Order: R>P>Q>S, so S is shortest.",
    ),



    Question(

        question_code="REA-RANKING-010",

        question=
        "In a queue, Rahul is 7th from front and 18th from back. Total people in queue are:",

        options=[
            "23",
            "24",
            "25",
            "26"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.RANKING,

        explanation=
        "Total = 7+18-1 = 24.",
    ),


    # =====================================================
    # SYLLOGISM (REA-SYLLOGISM-001–010)
    # =====================================================


    Question(

        question_code="REA-SYLLOGISM-001",

        question=
        "Statements: All cats are animals. All animals are living beings. Conclusion: All cats are living beings.",

        options=[
            "Conclusion follows",
            "Conclusion does not follow",
            "Both true and false",
            "Cannot say"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.SYLLOGISM,

        explanation=
        "Cats are included in animals and animals are living beings, so conclusion follows.",
    ),



    Question(

        question_code="REA-SYLLOGISM-002",

        question=
        "Statements: All roses are flowers. Some flowers are red. Conclusion: Some roses are red.",

        options=[
            "Conclusion follows",
            "Conclusion does not follow",
            "Both follow",
            "None"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.SYLLOGISM,

        explanation=
        "There is no direct relation between roses and red flowers.",
    ),



    Question(

        question_code="REA-SYLLOGISM-003",

        question=
        "Statements: All students are learners. All learners are readers. Conclusion: All students are readers.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot determine",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.SYLLOGISM,

        explanation=
        "Students are learners and learners are readers, so students are readers.",
    ),



    Question(

        question_code="REA-SYLLOGISM-004",

        question=
        "Statements: Some cars are bikes. All bikes are vehicles. Conclusion: Some cars are vehicles.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.SYLLOGISM,

        explanation=
        "Some cars are bikes and all bikes are vehicles, so some cars are vehicles.",
    ),



    Question(

        question_code="REA-SYLLOGISM-005",

        question=
        "Statements: All pens are stationery items. No stationery item is edible. Conclusion: No pen is edible.",

        options=[
            "Follows",
            "Does not follow",
            "Both",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.SYLLOGISM,

        explanation=
        "Pens are stationery and stationery items are not edible.",
    ),



    Question(

        question_code="REA-SYLLOGISM-006",

        question=
        "Statements: Some doctors are teachers. All teachers are educated. Conclusion: Some doctors are educated.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.SYLLOGISM,

        explanation=
        "Some doctors are teachers and teachers are educated.",
    ),



    Question(

        question_code="REA-SYLLOGISM-007",

        question=
        "Statements: All birds can fly. Penguins are birds. Conclusion: Penguins can fly.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot determine",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.SYLLOGISM,

        explanation=
        "According to given statements, penguins are birds and all birds can fly.",
    ),



    Question(

        question_code="REA-SYLLOGISM-008",

        question=
        "Statements: No fish are mammals. All whales are mammals. Conclusion: No whale is a fish.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.SYLLOGISM,

        explanation=
        "Whales are mammals and mammals cannot be fish.",
    ),



    Question(

        question_code="REA-SYLLOGISM-009",

        question=
        "Statements: Some books are novels. All novels are interesting. Conclusion: Some books are interesting.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.SYLLOGISM,

        explanation=
        "Some books are novels and novels are interesting.",
    ),



    Question(

        question_code="REA-SYLLOGISM-010",

        question=
        "Statements: All computers are machines. Some machines are expensive. Conclusion: Some computers are expensive.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.SYLLOGISM,

        explanation=
        "Expensive machines may not necessarily be computers.",
    ),


    # =====================================================
    # STATEMENT & CONCLUSION
    # (REA-STATEMENT-CONCLUSION-001–010)
    # =====================================================


    Question(

        question_code="REA-STATEMENT-CONCLUSION-001",

        question=
        "Statement: All students should attend classes regularly. "
        "Conclusion: Regular attendance helps students learn better.",

        options=[
            "Conclusion follows",
            "Conclusion does not follow",
            "Both are unrelated",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Regular attendance improves learning, so conclusion follows.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-002",

        question=
        "Statement: The company increased salary of employees. "
        "Conclusion: Employees may become more satisfied.",

        options=[
            "Conclusion follows",
            "Conclusion does not follow",
            "Cannot be determined",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Salary increase can improve employee satisfaction.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-003",

        question=
        "Statement: Many people prefer online shopping because it saves time. "
        "Conclusion: Online shopping is convenient.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Saving time makes online shopping convenient.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-004",

        question=
        "Statement: The road was blocked due to heavy rain. "
        "Conclusion: People faced difficulty in travelling.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot determine",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Blocked roads create travelling problems.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-005",

        question=
        "Statement: The school introduced smart classes. "
        "Conclusion: Students will definitely score higher marks.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Smart classes may help learning but marks cannot be guaranteed.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-006",

        question=
        "Statement: Drinking enough water is important for health. "
        "Conclusion: Everyone should drink adequate water daily.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Adequate water intake supports health.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-007",

        question=
        "Statement: The city planted more trees to reduce pollution. "
        "Conclusion: Trees help in controlling pollution.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot determine",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Trees help reduce pollution.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-008",

        question=
        "Statement: The exam was postponed due to bad weather. "
        "Conclusion: Weather affects exam schedules.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Bad weather can affect schedules.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-009",

        question=
        "Statement: The library extended its working hours. "
        "Conclusion: Students may get more time for studying.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot determine",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "More library hours provide additional study time.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-010",

        question=
        "Statement: Mobile phones are widely used by people. "
        "Conclusion: Every person owns a mobile phone.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Wide usage does not mean everyone owns one.",
    ),


    # =====================================================
    # STATEMENT & CONCLUSION
    # (REA-STATEMENT-CONCLUSION-010–020)
    # =====================================================


    Question(

        question_code="REA-STATEMENT-CONCLUSION-011",

        question=
        "Statement: All students should attend classes regularly. "
        "Conclusion: Regular attendance helps students learn better.",

        options=[
            "Conclusion follows",
            "Conclusion does not follow",
            "Both are unrelated",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Regular attendance improves learning, so conclusion follows.",
    ),



    Question(

       question_code="REA-STATEMENT-CONCLUSION-012",

        question=
        "Statement: The company increased salary of employees. "
        "Conclusion: Employees may become more satisfied.",

        options=[
            "Conclusion follows",
            "Conclusion does not follow",
            "Cannot be determined",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Salary increase can improve employee satisfaction.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-013",

        question=
        "Statement: Many people prefer online shopping because it saves time. "
        "Conclusion: Online shopping is convenient.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Saving time makes online shopping convenient.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-014",

        question=
        "Statement: The road was blocked due to heavy rain. "
        "Conclusion: People faced difficulty in travelling.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot determine",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Blocked roads create travelling problems.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-015",

        question=
        "Statement: The school introduced smart classes. "
        "Conclusion: Students will definitely score higher marks.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Smart classes may help learning but marks cannot be guaranteed.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-016",

        question=
        "Statement: Drinking enough water is important for health. "
        "Conclusion: Everyone should drink adequate water daily.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Adequate water intake supports health.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-017",

        question=
        "Statement: The city planted more trees to reduce pollution. "
        "Conclusion: Trees help in controlling pollution.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot determine",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Trees help reduce pollution.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-018",

        question=
        "Statement: The exam was postponed due to bad weather. "
        "Conclusion: Weather affects exam schedules.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Bad weather can affect schedules.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-019",

        question=
        "Statement: The library extended its working hours. "
        "Conclusion: Students may get more time for studying.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot determine",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "More library hours provide additional study time.",
    ),



    Question(

        question_code="REA-STATEMENT-CONCLUSION-020",

        question=
        "Statement: Mobile phones are widely used by people. "
        "Conclusion: Every person owns a mobile phone.",

        options=[
            "Follows",
            "Does not follow",
            "Cannot say",
            "None"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "Wide usage does not mean everyone owns one.",
    ),


    # =====================================================
    # MIXED / ADVANCED REASONING
    # (REA-MIXED-001–010)
    # =====================================================


    Question(

        question_code="REA-MIXED-001",

        question=
        "If all A are B and all B are C, then all A are:",

        options=[
            "C",
            "B",
            "Both B and C",
            "None"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.STATEMENT_CONCLUSION,

        explanation=
        "A is a subset of B and B is a subset of C, so A is part of C.",
    ),



    Question(

        question_code="REA-MIXED-002",

        question=
        "Find the missing term: AZ, BY, CX, DW, ?",

        options=[
            "EV",
            "EU",
            "FV",
            "EW"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "First letters increase and second letters decrease.",
    ),



    Question(

        question_code="REA-MIXED-003",

        question=
        "If SOUTH is written as TPVUI, then NORTH will be written as:",

        options=[
            "OPSUI",
            "OPSTI",
            "NPSUI",
            "OPSVI"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CODING_DECODING,

        explanation=
        "Each letter is shifted one position forward.",
    ),



    Question(

        question_code="REA-MIXED-004",

        question=
        "Which number replaces the question mark: 2, 6, 12, 20, 30, ?",

        options=[
            "40",
            "42",
            "44",
            "46"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.NUMBER_SERIES,

        explanation=
        "Pattern differences are +4,+6,+8,+10,+12.",
    ),



    Question(

        question_code="REA-MIXED-005",

        question=
        "A clock shows 9:00. What is the angle between the hands?",

        options=[
            "90°",
            "120°",
            "180°",
            "270°"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLOCK,

        explanation=
        "At 9:00, hands form a right angle.",
    ),



    Question(

        question_code="REA-MIXED-006",

        question=
        "Find odd one out:",

        options=[
            "Square",
            "Rectangle",
            "Triangle",
            "Cube"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.CLASSIFICATION,

        explanation=
        "Cube is a three-dimensional shape.",
    ),



    Question(

        question_code="REA-MIXED-007",

        question=
        "If today is Friday, what day will be after 15 days?",

        options=[
            "Friday",
            "Saturday",
            "Sunday",
            "Monday"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.CALENDAR,

        explanation=
        "15 days means 1 day extra after two weeks, so Saturday.",
    ),



    Question(

        question_code="REA-MIXED-008",

        question=
        "A is older than B, B is older than C, and C is older than D. Who is youngest?",

        options=[
            "A",
            "B",
            "C",
            "D"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.REASONING,

        topic=Topic.RANKING,

        explanation=
        "Order: A>B>C>D, so D is youngest.",
    ),



    Question(

        question_code="REA-MIXED-009",

        question=
        "If 5 workers complete a task in 10 days, how many days will 10 workers take (same efficiency)?",

        options=[
            "2 days",
            "5 days",
            "10 days",
            "20 days"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.TIME_WORK,

        explanation=
        "Workers doubled, time becomes half.",
    ),



    Question(

        question_code="REA-MIXED-010",

        question=
        "A person walks east, then north, then west by same distance. He is in which direction from start?",

        options=[
            "North",
            "South",
            "East",
            "West"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.REASONING,

        topic=Topic.DIRECTION,

        explanation=
        "East and west cancel, only north remains.",
    ),


]