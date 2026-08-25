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



    Question(
        question_code="COLLEGE-DSA-011",
        question=
        "Given nums=[2,7,11,15] and target=9, which pair of indices adds to target?",
        options=[
            "[0,1]",
            "[1,2]",
            "[0,3]",
            "[2,3]",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ARRAY,

        explanation=
        "The values 2 and 7 at indices 0 and 1 sum to 9.",
    ),

    Question(
        question_code="COLLEGE-DSA-012",
        question=
        "Given nums=[-1,0,1,2,-1,-4], which technique is suitable for finding unique triples summing to zero?",
        options=[
            "Sort plus two pointers",
            "Only binary search",
            "Stack only",
            "BFS",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ARRAY,

        explanation=
        "Sorting and two pointers is a standard O(n²) approach.",
    ),

    Question(
        question_code="COLLEGE-DSA-013",
        question=
        "For an array, the maximum subarray sum can be found in linear time using:",
        options=[
            "Kadane's algorithm",
            "Floyd-Warshall",
            "Dijkstra",
            "Heap sort only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ARRAY,

        explanation=
        "Kadane's algorithm maintains the best ending and global sums.",
    ),

    Question(
        question_code="COLLEGE-DSA-014",
        question=
        "Given heights=[1,8,6,2,5,4,8,3,7], the maximum container area is:",
        options=[
            "49",
            "42",
            "36",
            "56",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ARRAY,

        explanation=
        "The best pair is heights 8 and 7 separated by 7 positions, area 49.",
    ),

    Question(
        question_code="COLLEGE-DSA-015",
        question=
        "To remove duplicates from a sorted array in-place while preserving order, use:",
        options=[
            "Two pointers",
            "DFS",
            "Hash tree only",
            "Recursion only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ARRAY,

        explanation=
        "A slow/fast pointer approach compacts unique values.",
    ),

    Question(
        question_code="COLLEGE-DSA-016",
        question=
        "For nums=[3,2,3], the majority element is:",
        options=[
            "2",
            "3",
            "No majority",
            "0",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ARRAY,

        explanation=
        "3 occurs twice out of three elements.",
    ),

    Question(
        question_code="COLLEGE-DSA-017",
        question=
        "A rotated sorted array can be searched in O(log n) by:",
        options=[
            "Modified binary search",
            "Linear scan only",
            "BFS",
            "Merge sort first always",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SEARCHING,

        explanation=
        "Modified binary search determines which half is sorted.",
    ),

    Question(
        question_code="COLLEGE-DSA-018",
        question=
        "For an array where every value appears twice except one, the O(n) O(1)-space solution uses:",
        options=[
            "XOR",
            "Sorting only",
            "Hash map only",
            "Stack",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BIT_MANIPULATION,

        explanation=
        "XOR cancels equal pairs and leaves the unique value.",
    ),

    Question(
        question_code="COLLEGE-DSA-019",
        question=
        "Given prices=[7,1,5,3,6,4], maximum single-transaction profit is:",
        options=[
            "5",
            "6",
            "4",
            "7",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ARRAY,

        explanation=
        "Buy at 1 and sell at 6 for profit 5.",
    ),

    Question(
        question_code="COLLEGE-DSA-020",
        question=
        "To move all zeros to the end while preserving non-zero order, use:",
        options=[
            "Two-pointer compaction",
            "Heap",
            "DFS",
            "Binary tree",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ARRAY,

        explanation=
        "Compacting non-zero values then filling zeros preserves order.",
    ),

    Question(
        question_code="COLLEGE-DSA-021",
        question=
        "Given s='abcabcbb', the longest substring without repeating characters has length:",
        options=[
            "3",
            "4",
            "5",
            "2",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.STRING,

        explanation=
        "The longest unique substring is 'abc', length 3.",
    ),

    Question(
        question_code="COLLEGE-DSA-022",
        question=
        "For s='(()())', the parentheses are:",
        options=[
            "Valid",
            "Invalid",
            "Unbalanced only at end",
            "Not a string",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.STRING,

        explanation=
        "Every opening parenthesis is properly matched before the sequence ends.",
    ),

    Question(
        question_code="COLLEGE-DSA-023",
        question=
        "To test whether two strings are anagrams efficiently, compare:",
        options=[
            "Character frequency counts",
            "Only lengths",
            "First characters",
            "Sorted lengths",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.STRING,

        explanation=
        "Equal character frequency maps imply anagrams.",
    ),

    Question(
        question_code="COLLEGE-DSA-024",
        question=
        "The longest common prefix of ['flower','flow','flight'] is:",
        options=[
            "fl",
            "flow",
            "f",
            "flower",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.STRING,

        explanation=
        "All three strings share the prefix 'fl'.",
    ),

    Question(
        question_code="COLLEGE-DSA-025",
        question=
        "For s='racecar', the longest palindromic substring is:",
        options=[
            "racecar",
            "ace",
            "rac",
            "e",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.STRING,

        explanation=
        "The entire string reads the same forward and backward.",
    ),

    Question(
        question_code="COLLEGE-DSA-026",
        question=
        "A string can be checked for palindrome in O(n) space O(1) by:",
        options=[
            "Comparing characters from both ends",
            "Building a graph",
            "Using BFS",
            "Sorting it",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.STRING,

        explanation=
        "Two pointers compare mirrored characters.",
    ),

    Question(
        question_code="COLLEGE-DSA-027",
        question=
        "To group anagrams, a common key is:",
        options=[
            "Sorted characters or frequency signature",
            "First character only",
            "String length only",
            "Hash of memory address",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.HASHING,

        explanation=
        "Anagrams share the same character multiset.",
    ),

    Question(
        question_code="COLLEGE-DSA-028",
        question=
        "For a singly linked list, the middle node can be found in one pass using:",
        options=[
            "Slow and fast pointers",
            "Two stacks",
            "Binary search",
            "Heap",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LINKED_LIST,

        explanation=
        "Fast moves twice as quickly as slow, leaving slow at the middle.",
    ),

    Question(
        question_code="COLLEGE-DSA-029",
        question=
        "To detect a cycle in a linked list with O(1) extra space, use:",
        options=[
            "Floyd's tortoise and hare",
            "DFS stack",
            "Sorting",
            "Hash table only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LINKED_LIST,

        explanation=
        "Two pointers moving at different speeds detect a cycle.",
    ),

    Question(
        question_code="COLLEGE-DSA-030",
        question=
        "Reversing a singly linked list iteratively requires tracking:",
        options=[
            "Previous, current and next",
            "Only current",
            "Only head",
            "A queue only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LINKED_LIST,

        explanation=
        "Three references safely reverse each next pointer.",
    ),

    Question(
        question_code="COLLEGE-DSA-031",
        question=
        "Merging two sorted linked lists can be done in:",
        options=[
            "O(n+m)",
            "O(nm) always",
            "O(log n)",
            "O(1) time",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LINKED_LIST,

        explanation=
        "Each node is visited once.",
    ),

    Question(
        question_code="COLLEGE-DSA-032",
        question=
        "A stack is ideal for:",
        options=[
            "Valid parentheses matching",
            "Level-order traversal",
            "Shortest path in unweighted graph",
            "FIFO scheduling",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.STACK,

        explanation=
        "Stacks naturally match nested opening/closing symbols.",
    ),

    Question(
        question_code="COLLEGE-DSA-033",
        question=
        "The next greater element problem is efficiently solved using a:",
        options=[
            "Monotonic stack",
            "Queue only",
            "BFS",
            "Union-find",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.STACK,

        explanation=
        "A decreasing monotonic stack finds next greater values in linear time.",
    ),

    Question(
        question_code="COLLEGE-DSA-034",
        question=
        "For a queue implemented with two stacks, enqueue/dequeue can be amortized:",
        options=[
            "O(1)",
            "O(n²)",
            "O(log n) only",
            "O(n) every operation",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.QUEUE,

        explanation=
        "Each element moves between stacks a bounded number of times.",
    ),

    Question(
        question_code="COLLEGE-DSA-035",
        question=
        "BFS on an unweighted graph finds shortest paths in:",
        options=[
            "Number of edges",
            "Weighted cost",
            "Lexicographic order only",
            "Random order",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GRAPH,

        explanation=
        "BFS explores vertices by increasing edge distance.",
    ),

    Question(
        question_code="COLLEGE-DSA-036",
        question=
        "DFS is especially useful for:",
        options=[
            "Exploring connected components",
            "Always finding weighted shortest path",
            "Sorting numbers",
            "Hashing strings",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GRAPH,

        explanation=
        "DFS systematically explores reachable vertices.",
    ),

    Question(
        question_code="COLLEGE-DSA-037",
        question=
        "Topological sorting is defined for:",
        options=[
            "Directed acyclic graphs",
            "Any undirected graph",
            "Only complete graphs",
            "Only trees with cycles",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GRAPH,

        explanation=
        "A DAG admits a topological ordering.",
    ),

    Question(
        question_code="COLLEGE-DSA-038",
        question=
        "Dijkstra's algorithm assumes edge weights are:",
        options=[
            "Non-negative",
            "All negative",
            "All equal to zero",
            "Only strings",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GRAPH,

        explanation=
        "Dijkstra's correctness relies on non-negative edge weights.",
    ),

    Question(
        question_code="COLLEGE-DSA-039",
        question=
        "For a minimum spanning tree, Kruskal's algorithm commonly uses:",
        options=[
            "Disjoint set union",
            "Stack",
            "Trie",
            "Sliding window",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.GRAPH,

        explanation=
        "DSU efficiently checks whether an edge joins different components.",
    ),

    Question(
        question_code="COLLEGE-DSA-040",
        question=
        "Binary tree inorder traversal visits:",
        options=[
            "Left, root, right",
            "Root, left, right",
            "Left, right, root",
            "Right, root, left",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TREE,

        explanation=
        "Inorder traversal is left-root-right.",
    ),

    Question(
        question_code="COLLEGE-DSA-041",
        question=
        "In a binary search tree, inorder traversal produces:",
        options=[
            "Sorted order",
            "Reverse level order always",
            "Random order",
            "Only leaves",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TREE,

        explanation=
        "BST inorder traversal yields keys in nondecreasing order.",
    ),

    Question(
        question_code="COLLEGE-DSA-042",
        question=
        "A heap is useful for implementing a:",
        options=[
            "Priority queue",
            "Linked list",
            "Trie only",
            "Hash map",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.HEAP,

        explanation=
        "Heaps efficiently provide access to the minimum or maximum element.",
    ),

    Question(
        question_code="COLLEGE-DSA-043",
        question=
        "Heap sort has worst-case time complexity:",
        options=[
            "O(n log n)",
            "O(n²)",
            "O(log n)",
            "O(1)",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SORTING,

        explanation=
        "Heap construction and repeated extraction give O(n log n).",
    ),

    Question(
        question_code="COLLEGE-DSA-044",
        question=
        "Merge sort has auxiliary space complexity commonly:",
        options=[
            "O(n)",
            "O(1) always",
            "O(log n) only",
            "O(n²)",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SORTING,

        explanation=
        "Standard merge sort uses O(n) temporary storage.",
    ),

    Question(
        question_code="COLLEGE-DSA-045",
        question=
        "Quick sort's worst-case time complexity is:",
        options=[
            "O(n²)",
            "O(n)",
            "O(log n)",
            "O(1)",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SORTING,

        explanation=
        "Poor pivot choices can produce highly unbalanced partitions.",
    ),

    Question(
        question_code="COLLEGE-DSA-046",
        question=
        "Binary search reduces the search interval by approximately:",
        options=[
            "Half each step",
            "One element total",
            "Two elements only",
            "None",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SEARCHING,

        explanation=
        "Each comparison discards about half the sorted search space.",
    ),

    Question(
        question_code="COLLEGE-DSA-047",
        question=
        "Memoization is:",
        options=[
            "Caching results of overlapping subproblems",
            "Sorting an array",
            "Encrypting a graph",
            "Deleting recursion",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DYNAMIC_PROGRAMMING,

        explanation=
        "Memoization stores computed results to avoid repeated work.",
    ),

    Question(
        question_code="COLLEGE-DSA-048",
        question=
        "For Fibonacci with memoization, time complexity becomes:",
        options=[
            "O(n)",
            "O(2^n)",
            "O(n² log n)",
            "O(1)",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DYNAMIC_PROGRAMMING,

        explanation=
        "Each Fibonacci state is computed once.",
    ),

    Question(
        question_code="COLLEGE-DSA-049",
        question=
        "Backtracking is useful for:",
        options=[
            "Generating combinations or permutations under constraints",
            "Only binary search",
            "Only database joins",
            "Only hashing",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BACKTRACKING,

        explanation=
        "Backtracking explores choices and undoes them when needed.",
    ),

    Question(
        question_code="COLLEGE-DSA-050",
        question=
        "The classic 'climbing stairs' problem can be solved using:",
        options=[
            "Dynamic programming",
            "Dijkstra",
            "Union-find only",
            "BFS only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DYNAMIC_PROGRAMMING,

        explanation=
        "The number of ways follows a Fibonacci-like recurrence.",
    ),
]