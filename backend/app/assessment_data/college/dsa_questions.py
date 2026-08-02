from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


COLLEGE_DSA_QUESTIONS: list[Question] = [

    # =====================================================
    # COLLEGE DSA (COLLEGE-DSA-001–010)
    # =====================================================


    Question(

        question_code="COLLEGE-DSA-001",

        question=
        "Which data structure follows FIFO principle?",

        options=[
            "Stack",
            "Queue",
            "Tree",
            "Graph"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Queue follows First In First Out principle.",
    ),



    Question(

        question_code="COLLEGE-DSA-002",

        question=
        "What is the time complexity of binary search?",

        options=[
            "O(n)",
            "O(log n)",
            "O(n²)",
            "O(1)"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Binary search divides the search space into half each step.",
    ),



    Question(

        question_code="COLLEGE-DSA-003",

        question=
        "Which sorting algorithm uses Divide and Conquer approach?",

        options=[
            "Bubble Sort",
            "Merge Sort",
            "Selection Sort",
            "Insertion Sort"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Merge Sort divides the array into smaller parts and merges them.",
    ),



    Question(

        question_code="COLLEGE-DSA-004",

        question=
        "Which traversal visits Root, Left subtree and Right subtree?",

        options=[
            "Inorder",
            "Postorder",
            "Preorder",
            "Level Order"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Preorder traversal follows Root → Left → Right.",
    ),



    Question(

        question_code="COLLEGE-DSA-005",

        question=
        "Which algorithm is used to find shortest path in weighted graph?",

        options=[
            "Dijkstra",
            "Bubble Sort",
            "DFS only",
            "Binary Search"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Dijkstra algorithm finds shortest path from a source vertex.",
    ),



    Question(

        question_code="COLLEGE-DSA-006",

        question=
        "Which data structure is used for recursion?",

        options=[
            "Queue",
            "Stack",
            "Graph",
            "Array"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Recursive function calls are stored in stack memory.",
    ),



    Question(

        question_code="COLLEGE-DSA-007",

        question=
        "Average searching complexity in a Hash Table is:",

        options=[
            "O(1)",
            "O(n)",
            "O(log n)",
            "O(n²)"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Hash table provides constant average lookup time.",
    ),



    Question(

        question_code="COLLEGE-DSA-008",

        question=
        "Which algorithm is used for Minimum Spanning Tree?",

        options=[
            "Kruskal",
            "Linear Search",
            "Quick Sort",
            "BFS"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Kruskal algorithm is used to find Minimum Spanning Tree.",
    ),



    Question(

        question_code="COLLEGE-DSA-009",

        question=
        "Dynamic Programming uses:",

        options=[
            "Overlapping subproblems",
            "Only loops",
            "Random selection",
            "No memory"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "DP stores solutions of overlapping subproblems.",
    ),



    Question(

        question_code="COLLEGE-DSA-010",

        question=
        "Which data structure is used in BFS traversal?",

        options=[
            "Stack",
            "Queue",
            "Heap",
            "Tree"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "BFS uses queue for level-wise traversal.",
    ),

]