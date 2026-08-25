from .enums import Difficulty, QuestionType, Topic
from .schemas import Question


DSA_QUESTIONS: list[Question] = [

    # =====================================================
    # ARRAY & STRING (DSA-ARRAY-001–010)
    # =====================================================


    Question(

        question_code="DSA-ARRAY-001",

        question=
        "What is the time complexity of accessing an element in an array using index?",

        options=[
            "O(1)",
            "O(n)",
            "O(log n)",
            "O(n²)"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Array elements can be accessed directly using index, so complexity is O(1).",
    ),



    Question(

        question_code="DSA-ARRAY-002",

        question=
        "Which data structure stores elements in contiguous memory locations?",

        options=[
            "Linked List",
            "Array",
            "Tree",
            "Graph"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Arrays store elements continuously in memory.",
    ),



    Question(

        question_code="DSA-ARRAY-003",

        question=
        "Which algorithm is commonly used to find the maximum element in an array?",

        options=[
            "Linear Search",
            "Binary Search",
            "DFS",
            "BFS"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Linear traversal can compare each element and find maximum.",
    ),



    Question(

        question_code="DSA-ARRAY-004",

        question=
        "What is the worst-case time complexity of searching an element in an unsorted array?",

        options=[
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n²)"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "In worst case every element needs to be checked.",
    ),



    Question(

        question_code="DSA-ARRAY-005",

        question=
        "Which operation is costly in an array because elements need shifting?",

        options=[
            "Access",
            "Insertion",
            "Reading",
            "Indexing"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Insertion requires shifting elements to create space.",
    ),



    Question(

        question_code="DSA-ARRAY-006",

        question=
        "Which technique is used to find pairs with a given sum efficiently?",

        options=[
            "Two Pointer",
            "DFS",
            "Recursion",
            "Backtracking"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Two pointer technique efficiently solves sorted array pair problems.",
    ),



    Question(

        question_code="DSA-ARRAY-007",

        question=
        "Which method is used to reverse a string?",

        options=[
            "Swap characters",
            "Sort characters",
            "Delete characters",
            "Merge strings"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "String reversal can be done by swapping characters from both ends.",
    ),



    Question(

        question_code="DSA-ARRAY-008",

        question=
        "Which data structure is commonly used to implement dynamic arrays?",

        options=[
            "Stack",
            "Vector",
            "Queue",
            "Graph"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Vector provides dynamic array functionality.",
    ),



    Question(

        question_code="DSA-ARRAY-009",

        question=
        "What is the space complexity of storing n elements in an array?",

        options=[
            "O(1)",
            "O(n)",
            "O(log n)",
            "O(n²)"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Array stores n elements, requiring O(n) space.",
    ),



    Question(

        question_code="DSA-ARRAY-010",

        question=
        "Which string operation combines two strings together?",

        options=[
            "Concatenation",
            "Sorting",
            "Searching",
            "Traversal"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Joining two strings is called concatenation.",
    ),


    # =====================================================
    # LINKED LIST (DSA-LINKEDLIST-001–010)
    # =====================================================


    Question(

        question_code="DSA-LINKEDLIST-001",

        question=
        "Which data structure uses nodes connected through pointers?",

        options=[
            "Array",
            "Linked List",
            "Stack",
            "Queue"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Linked List stores data in nodes connected using pointers.",
    ),



    Question(

        question_code="DSA-LINKEDLIST-002",

        question=
        "What is the first node of a linked list called?",

        options=[
            "Tail",
            "Head",
            "Root",
            "Start Pointer"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "The first node of linked list is called head.",
    ),



    Question(

        question_code="DSA-LINKEDLIST-003",

        question=
        "What is the time complexity of inserting a node at the beginning of linked list?",

        options=[
            "O(1)",
            "O(n)",
            "O(log n)",
            "O(n²)"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Only head pointer needs to be changed, so insertion takes O(1).",
    ),



    Question(

        question_code="DSA-LINKEDLIST-004",

        question=
        "Which type of linked list contains a pointer to the previous and next node?",

        options=[
            "Singly Linked List",
            "Doubly Linked List",
            "Circular Linked List",
            "Linear List"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Doubly linked list stores both previous and next references.",
    ),



    Question(

        question_code="DSA-LINKEDLIST-005",

        question=
        "Which linked list has the last node connected to the first node?",

        options=[
            "Singly Linked List",
            "Doubly Linked List",
            "Circular Linked List",
            "Static List"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Circular linked list connects last node back to first node.",
    ),



    Question(

        question_code="DSA-LINKEDLIST-006",

        question=
        "What is the time complexity to search an element in a linked list?",

        options=[
            "O(1)",
            "O(n)",
            "O(log n)",
            "O(n log n)"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Linked list requires sequential traversal for searching.",
    ),



    Question(

        question_code="DSA-LINKEDLIST-007",

        question=
        "Which pointer is used to detect a cycle in linked list?",

        options=[
            "Two Pointer Technique",
            "Binary Search",
            "Hash Sorting",
            "Recursion Only"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Floyd's two pointer algorithm detects cycles.",
    ),



    Question(

        question_code="DSA-LINKEDLIST-008",

        question=
        "Which operation is easier in linked list compared to array?",

        options=[
            "Random Access",
            "Insertion and Deletion",
            "Index Searching",
            "Sorting"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Insertion and deletion are efficient because shifting is not required.",
    ),



    Question(

        question_code="DSA-LINKEDLIST-009",

        question=
        "A node in linked list contains data and:",

        options=[
            "Index",
            "Pointer",
            "Loop",
            "Function"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Each node contains data and pointer/reference to next node.",
    ),



    Question(

        question_code="DSA-LINKEDLIST-010",

        question=
        "Which data structure can be implemented using linked list?",

        options=[
            "Stack",
            "Queue",
            "Both Stack and Queue",
            "Only Array"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Both stack and queue can be implemented using linked lists.",
    ),


    # =====================================================
    # STACK & QUEUE (DSA-STACK-001–010)
    # =====================================================


    Question(

        question_code="DSA-STACK-001",

        question=
        "Which principle is followed by Stack?",

        options=[
            "FIFO",
            "LIFO",
            "Random Access",
            "Priority Based"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Stack follows Last In First Out (LIFO) principle.",
    ),



    Question(

        question_code="DSA-STACK-002",

        question=
        "Which operation inserts an element into a Stack?",

        options=[
            "Enqueue",
            "Push",
            "Insert",
            "Add"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Push operation adds an element to the top of stack.",
    ),



    Question(

        question_code="DSA-STACK-003",

        question=
        "Which operation removes an element from Stack?",

        options=[
            "Delete",
            "Remove",
            "Pop",
            "Dequeue"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Pop removes the top element from stack.",
    ),



    Question(

        question_code="DSA-STACK-004",

        question=
        "Which data structure is used for function call management?",

        options=[
            "Queue",
            "Stack",
            "Array",
            "Graph"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Function calls are stored in the call stack.",
    ),



    Question(

        question_code="DSA-STACK-005",

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

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Queue follows First In First Out principle.",
    ),



    Question(

        question_code="DSA-STACK-006",

        question=
        "Which operation adds an element to Queue?",

        options=[
            "Push",
            "Insert",
            "Enqueue",
            "Pop"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Enqueue operation inserts elements into queue.",
    ),



    Question(

        question_code="DSA-STACK-007",

        question=
        "Which operation removes an element from Queue?",

        options=[
            "Pop",
            "Delete",
            "Dequeue",
            "RemoveTop"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Dequeue removes the front element of queue.",
    ),



    Question(

        question_code="DSA-STACK-008",

        question=
        "Which data structure is used to check balanced parentheses?",

        options=[
            "Queue",
            "Stack",
            "Array",
            "Tree"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Stack stores opening brackets and matches closing brackets.",
    ),



    Question(

        question_code="DSA-STACK-009",

        question=
        "What is the time complexity of push operation in stack?",

        options=[
            "O(1)",
            "O(n)",
            "O(log n)",
            "O(n²)"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Push adds element at top, requiring constant time.",
    ),



    Question(

        question_code="DSA-STACK-010",

        question=
        "Which type of queue allows insertion and deletion from both ends?",

        options=[
            "Simple Queue",
            "Circular Queue",
            "Deque",
            "Priority Queue"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Deque (Double Ended Queue) allows operations at both ends.",
    ),

    # =====================================================
    # TREE & BINARY TREE (DSA-TREE-001–010)
    # =====================================================


    Question(

        question_code="DSA-TREE-001",

        question=
        "Which data structure represents hierarchical relationships?",

        options=[
            "Array",
            "Tree",
            "Stack",
            "Queue"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Tree is used to represent hierarchical data.",
    ),



    Question(

        question_code="DSA-TREE-002",

        question=
        "The topmost node of a tree is called:",

        options=[
            "Leaf",
            "Root",
            "Parent",
            "Child"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "The first node of a tree is called the root node.",
    ),



    Question(

        question_code="DSA-TREE-003",

        question=
        "A node with no children is called:",

        options=[
            "Root",
            "Leaf",
            "Parent",
            "Internal Node"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "A node without any child is called a leaf node.",
    ),



    Question(

        question_code="DSA-TREE-004",

        question=
        "Maximum number of children a binary tree node can have is:",

        options=[
            "1",
            "2",
            "3",
            "Unlimited"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "A binary tree node can have at most two children.",
    ),



    Question(

        question_code="DSA-TREE-005",

        question=
        "Which traversal visits Left subtree, Root, Right subtree?",

        options=[
            "Preorder",
            "Inorder",
            "Postorder",
            "Level Order"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Inorder traversal follows Left → Root → Right.",
    ),



    Question(

        question_code="DSA-TREE-006",

        question=
        "Which traversal follows Root → Left → Right order?",

        options=[
            "Preorder",
            "Inorder",
            "Postorder",
            "BFS"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Preorder traversal visits root before subtrees.",
    ),



    Question(

        question_code="DSA-TREE-007",

        question=
        "Which traversal is also known as Depth First Search in trees?",

        options=[
            "Level Order",
            "DFS Traversals",
            "Only BFS",
            "Sorting"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "DFS includes preorder, inorder and postorder traversals.",
    ),



    Question(

        question_code="DSA-TREE-008",

        question=
        "Binary Search Tree maintains which property?",

        options=[
            "Left child greater than root",
            "Left child smaller than root",
            "Random ordering",
            "No ordering"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "In BST, left subtree values are smaller than root.",
    ),



    Question(

        question_code="DSA-TREE-009",

        question=
        "What is the average search complexity in a balanced BST?",

        options=[
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n²)"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Balanced BST reduces search space by half.",
    ),



    Question(

        question_code="DSA-TREE-010",

        question=
        "Which data structure is used for level order traversal of a tree?",

        options=[
            "Stack",
            "Queue",
            "Array",
            "Linked List"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Level order traversal uses queue for BFS approach.",
    ),


    # =====================================================
    # GRAPH (DSA-GRAPH-001–010)
    # =====================================================


    Question(

        question_code="DSA-GRAPH-001",

        question=
        "Which data structure is used to represent connections between entities?",

        options=[
            "Array",
            "Graph",
            "Stack",
            "Queue"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Graph represents relationships using vertices and edges.",
    ),



    Question(

        question_code="DSA-GRAPH-002",

        question=
        "A node in a graph is called:",

        options=[
            "Edge",
            "Vertex",
            "Root",
            "Leaf"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Nodes of a graph are called vertices.",
    ),



    Question(

        question_code="DSA-GRAPH-003",

        question=
        "A connection between two vertices in a graph is called:",

        options=[
            "Node",
            "Edge",
            "Path",
            "Cycle"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "An edge connects two vertices of a graph.",
    ),



    Question(

        question_code="DSA-GRAPH-004",

        question=
        "Which algorithm is used to traverse a graph level by level?",

        options=[
            "DFS",
            "BFS",
            "Binary Search",
            "Merge Sort"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Breadth First Search visits nodes level by level.",
    ),



    Question(

        question_code="DSA-GRAPH-005",

        question=
        "Which data structure is used in BFS traversal?",

        options=[
            "Stack",
            "Queue",
            "Array",
            "Tree"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "BFS uses queue to maintain traversal order.",
    ),



    Question(

        question_code="DSA-GRAPH-006",

        question=
        "Which data structure is used in DFS traversal?",

        options=[
            "Queue",
            "Stack",
            "Heap",
            "Array"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "DFS uses stack or recursion internally.",
    ),



    Question(

        question_code="DSA-GRAPH-007",

        question=
        "Which algorithm finds the shortest path from a single source vertex?",

        options=[
            "Kruskal",
            "Dijkstra",
            "Prim",
            "DFS"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Dijkstra algorithm finds shortest path with non-negative weights.",
    ),



    Question(

        question_code="DSA-GRAPH-008",

        question=
        "Which algorithm is used to find Minimum Spanning Tree?",

        options=[
            "Dijkstra",
            "Kruskal",
            "Binary Search",
            "BFS"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Kruskal algorithm creates Minimum Spanning Tree.",
    ),



    Question(

        question_code="DSA-GRAPH-009",

        question=
        "A graph containing direction on edges is called:",

        options=[
            "Undirected Graph",
            "Directed Graph",
            "Simple Graph",
            "Complete Graph"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Directed graph has edges with a specific direction.",
    ),



    Question(

        question_code="DSA-GRAPH-010",

        question=
        "Which representation stores graph connections using a matrix?",

        options=[
            "Adjacency List",
            "Adjacency Matrix",
            "Linked List",
            "Tree"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Adjacency Matrix represents graph using a 2D matrix.",
    ),


    # =====================================================
    # SORTING & SEARCHING (DSA-SORT-001–010)
    # =====================================================


    Question(

        question_code="DSA-SORT-001",

        question=
        "Which sorting algorithm repeatedly swaps adjacent elements if they are in wrong order?",

        options=[
            "Merge Sort",
            "Bubble Sort",
            "Quick Sort",
            "Heap Sort"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Bubble Sort compares and swaps adjacent elements repeatedly.",
    ),



    Question(

        question_code="DSA-SORT-002",

        question=
        "What is the worst-case time complexity of Bubble Sort?",

        options=[
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n²)"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Bubble Sort has O(n²) worst-case complexity.",
    ),



    Question(

        question_code="DSA-SORT-003",

        question=
        "Which sorting algorithm uses Divide and Conquer technique?",

        options=[
            "Bubble Sort",
            "Merge Sort",
            "Selection Sort",
            "Insertion Sort"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Merge Sort divides the array into smaller parts and merges them.",
    ),



    Question(

        question_code="DSA-SORT-004",

        question=
        "What is the average time complexity of Quick Sort?",

        options=[
            "O(n)",
            "O(log n)",
            "O(n log n)",
            "O(n²)"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Quick Sort has average complexity O(n log n).",
    ),



    Question(

        question_code="DSA-SORT-005",

        question=
        "Which searching algorithm requires sorted data?",

        options=[
            "Linear Search",
            "Binary Search",
            "DFS",
            "BFS"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Binary Search works only on sorted data.",
    ),



    Question(

        question_code="DSA-SORT-006",

        question=
        "What is the time complexity of Binary Search?",

        options=[
            "O(n)",
            "O(log n)",
            "O(n²)",
            "O(1)"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Binary Search reduces search space by half each step.",
    ),



    Question(

        question_code="DSA-SORT-007",

        question=
        "Which sorting algorithm selects the minimum element repeatedly?",

        options=[
            "Selection Sort",
            "Bubble Sort",
            "Merge Sort",
            "Quick Sort"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Selection Sort selects minimum element and places it correctly.",
    ),



    Question(

        question_code="DSA-SORT-008",

        question=
        "Which sorting algorithm is stable and efficient for nearly sorted data?",

        options=[
            "Insertion Sort",
            "Heap Sort",
            "Quick Sort",
            "Selection Sort"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Insertion Sort performs well on nearly sorted arrays.",
    ),



    Question(

        question_code="DSA-SORT-009",

        question=
        "Searching every element one by one is called:",

        options=[
            "Binary Search",
            "Linear Search",
            "Hash Search",
            "Tree Search"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Linear Search checks elements sequentially.",
    ),



    Question(

        question_code="DSA-SORT-010",

        question=
        "Which sorting algorithm uses a pivot element?",

        options=[
            "Merge Sort",
            "Quick Sort",
            "Bubble Sort",
            "Insertion Sort"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Quick Sort partitions the array around a pivot.",
    ),


    # =====================================================
    # RECURSION & BACKTRACKING (DSA-RECURSION-001–010)
    # =====================================================


    Question(

        question_code="DSA-RECURSION-001",

        question=
        "A function calling itself is known as:",

        options=[
            "Iteration",
            "Recursion",
            "Compilation",
            "Inheritance"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "A function that calls itself is called recursion.",
    ),



    Question(

        question_code="DSA-RECURSION-002",

        question=
        "Which data structure is used internally during recursion?",

        options=[
            "Queue",
            "Stack",
            "Array",
            "Graph"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Recursive calls are stored in the call stack.",
    ),



    Question(

        question_code="DSA-RECURSION-003",

        question=
        "The condition that stops recursive calls is called:",

        options=[
            "Loop Condition",
            "Base Case",
            "Stop Function",
            "Exit Statement"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Base case prevents infinite recursive calls.",
    ),



    Question(

        question_code="DSA-RECURSION-004",

        question=
        "What is the time complexity of calculating factorial using simple recursion?",

        options=[
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n²)"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Factorial recursion makes n recursive calls.",
    ),



    Question(

        question_code="DSA-RECURSION-005",

        question=
        "Which problem is commonly solved using recursion?",

        options=[
            "Factorial",
            "Binary Tree Traversal",
            "Tower of Hanoi",
            "All of these"
        ],

        answer="D",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "All these problems naturally use recursion.",
    ),



    Question(

        question_code="DSA-RECURSION-006",

        question=
        "Backtracking is mainly based on which technique?",

        options=[
            "Greedy Approach",
            "Recursion",
            "Sorting",
            "Hashing"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Backtracking explores choices using recursion.",
    ),



    Question(

        question_code="DSA-RECURSION-007",

        question=
        "Which problem is solved using backtracking?",

        options=[
            "N-Queen Problem",
            "Binary Search",
            "Bubble Sort",
            "Linear Search"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "N-Queen is a classic backtracking problem.",
    ),



    Question(

        question_code="DSA-RECURSION-008",

        question=
        "What happens if a recursive function has no base case?",

        options=[
            "Fast execution",
            "Infinite recursion",
            "Compilation success",
            "Automatic stop"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Without base case recursion continues indefinitely.",
    ),



    Question(

        question_code="DSA-RECURSION-009",

        question=
        "Which algorithm technique tries different possible solutions and removes invalid choices?",

        options=[
            "Backtracking",
            "Binary Search",
            "Dynamic Programming",
            "Sorting"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Backtracking explores and rejects invalid paths.",
    ),



    Question(

        question_code="DSA-RECURSION-010",

        question=
        "Which approach can replace recursion in many cases?",

        options=[
            "Iteration",
            "Compilation",
            "Inheritance",
            "Encapsulation"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Loops can replace recursion in many problems.",
    ),



    # =====================================================
    # DYNAMIC PROGRAMMING (DSA-DP-001–010)
    # =====================================================


    Question(

        question_code="DSA-DP-001",

        question=
        "Dynamic Programming is mainly used to solve problems having:",

        options=[
            "Random data",
            "Overlapping subproblems",
            "Only loops",
            "No recursion"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "DP solves problems by storing results of overlapping subproblems.",
    ),



    Question(

        question_code="DSA-DP-002",

        question=
        "Which technique stores previously calculated results to avoid repeated work?",

        options=[
            "Greedy",
            "Memoization",
            "Sorting",
            "Searching"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Memoization stores results of solved subproblems.",
    ),



    Question(

        question_code="DSA-DP-003",

        question=
        "Which approach solves DP problems by building solutions from smaller problems?",

        options=[
            "Tabulation",
            "Backtracking",
            "DFS",
            "Binary Search"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Tabulation builds the solution using a bottom-up approach.",
    ),



    Question(

        question_code="DSA-DP-004",

        question=
        "Which problem is a classic example of Dynamic Programming?",

        options=[
            "Fibonacci Series",
            "Linear Search",
            "Bubble Sort",
            "Graph Coloring"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Fibonacci can be optimized using DP by storing previous results.",
    ),



    Question(

        question_code="DSA-DP-005",

        question=
        "The two main properties required for Dynamic Programming are:",

        options=[
            "Sorting and Searching",
            "Overlapping Subproblems and Optimal Substructure",
            "Loops and Conditions",
            "Arrays and Strings"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "DP works when problems have these two properties.",
    ),



    Question(

        question_code="DSA-DP-006",

        question=
        "Which algorithm is used to solve the shortest path problem with negative weights?",

        options=[
            "Dijkstra",
            "Bellman-Ford",
            "Binary Search",
            "Kruskal"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Bellman-Ford handles graphs with negative edge weights.",
    ),



    Question(

        question_code="DSA-DP-007",

        question=
        "Longest Common Subsequence (LCS) problem is solved using:",

        options=[
            "Dynamic Programming",
            "Greedy only",
            "Sorting",
            "Hashing"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "LCS is a standard Dynamic Programming problem.",
    ),



    Question(

        question_code="DSA-DP-008",

        question=
        "Which approach uses a table to store intermediate results?",

        options=[
            "Tabulation",
            "Recursion",
            "Divide and Conquer",
            "Linear Search"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Tabulation stores intermediate values in a table.",
    ),



    Question(

        question_code="DSA-DP-009",

        question=
        "What is the advantage of Dynamic Programming?",

        options=[
            "Increases repeated calculations",
            "Reduces time complexity",
            "Uses no memory",
            "Removes all loops"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "DP improves efficiency by avoiding repeated calculations.",
    ),



    Question(

        question_code="DSA-DP-010",

        question=
        "0/1 Knapsack problem is commonly solved using:",

        options=[
            "Dynamic Programming",
            "Binary Search",
            "DFS only",
            "Bubble Sort"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "0/1 Knapsack is a classic Dynamic Programming problem.",
    ),


    # =====================================================
    # HASHING (DSA-HASH-001–010)
    # =====================================================


    Question(

        question_code="DSA-HASH-001",

        question=
        "Hashing is mainly used for:",

        options=[
            "Fast searching",
            "Sorting only",
            "Graph traversal",
            "Memory deletion"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Hashing provides fast searching, insertion and deletion operations.",
    ),



    Question(

        question_code="DSA-HASH-002",

        question=
        "Which data structure stores data in key-value pairs?",

        options=[
            "Stack",
            "Hash Table",
            "Queue",
            "Tree"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Hash Table stores information using key-value mapping.",
    ),



    Question(

        question_code="DSA-HASH-003",

        question=
        "Average time complexity of searching in a hash table is:",

        options=[
            "O(1)",
            "O(n)",
            "O(log n)",
            "O(n²)"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Hash tables provide constant average lookup time.",
    ),



    Question(

        question_code="DSA-HASH-004",

        question=
        "A collision in hashing occurs when:",

        options=[
            "Two keys have same hash value",
            "Memory is full",
            "Data is deleted",
            "Table is empty"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Collision happens when multiple keys map to the same index.",
    ),



    Question(

        question_code="DSA-HASH-005",

        question=
        "Which technique resolves collisions by storing multiple values at same index?",

        options=[
            "Binary Search",
            "Chaining",
            "Sorting",
            "Recursion"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Chaining stores multiple elements using linked lists.",
    ),



    Question(

        question_code="DSA-HASH-006",

        question=
        "Which function converts a key into an index?",

        options=[
            "Search Function",
            "Hash Function",
            "Sort Function",
            "Delete Function"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Hash function converts keys into table indexes.",
    ),



    Question(

        question_code="DSA-HASH-007",

        question=
        "Which data structure is commonly used to implement a hash table?",

        options=[
            "Array",
            "Tree",
            "Graph",
            "Stack"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Hash tables commonly use arrays internally.",
    ),



    Question(

        question_code="DSA-HASH-008",

        question=
        "Which method handles collisions by finding another empty position?",

        options=[
            "Chaining",
            "Open Addressing",
            "DFS",
            "BFS"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Open addressing searches another location when collision occurs.",
    ),



    Question(

        question_code="DSA-HASH-009",

        question=
        "Which problem can be efficiently solved using hashing?",

        options=[
            "Two Sum Problem",
            "Bubble Sort",
            "Tree Traversal",
            "Merge Sort"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Hashing helps find pairs quickly in Two Sum problem.",
    ),



    Question(

        question_code="DSA-HASH-010",

        question=
        "What is the main advantage of a good hash function?",

        options=[
            "Uniform distribution of keys",
            "More memory usage",
            "Slower search",
            "Duplicate keys"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "A good hash function distributes keys evenly.",
    ),


    # =====================================================
    # HEAP & PRIORITY QUEUE (DSA-HEAP-001–010)
    # =====================================================


    Question(

        question_code="DSA-HEAP-001",

        question=
        "A Heap is a type of which data structure?",

        options=[
            "Linear Data Structure",
            "Tree Based Data Structure",
            "Graph",
            "Array Only"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Heap is a complete binary tree based data structure.",
    ),



    Question(

        question_code="DSA-HEAP-002",

        question=
        "Which property is satisfied by a Max Heap?",

        options=[
            "Parent node is smaller than children",
            "Parent node is greater than or equal to children",
            "All nodes are equal",
            "Random ordering"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "In Max Heap, parent node always has greater value than children.",
    ),



    Question(

        question_code="DSA-HEAP-003",

        question=
        "Which data structure is used to implement Priority Queue efficiently?",

        options=[
            "Linked List",
            "Heap",
            "Stack",
            "Array only"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Heap provides efficient insertion and deletion for priority queue.",
    ),



    Question(

        question_code="DSA-HEAP-004",

        question=
        "What is the time complexity of inserting an element into a binary heap?",

        options=[
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n²)"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Insertion requires moving element upward, taking O(log n) time.",
    ),



    Question(

        question_code="DSA-HEAP-005",

        question=
        "Which algorithm uses heap data structure for sorting?",

        options=[
            "Merge Sort",
            "Heap Sort",
            "Quick Sort",
            "Bubble Sort"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Heap Sort uses heap to repeatedly extract maximum/minimum element.",
    ),



    Question(

        question_code="DSA-HEAP-006",

        question=
        "A Binary Heap is always a:",

        options=[
            "Complete Binary Tree",
            "Full Binary Tree",
            "Balanced BST",
            "Graph"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Binary heap maintains complete binary tree structure.",
    ),



    Question(

        question_code="DSA-HEAP-007",

        question=
        "Which operation removes the root element from heap?",

        options=[
            "Insert",
            "Delete",
            "Search",
            "Traverse"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Deleting root removes maximum/minimum element depending on heap type.",
    ),



    Question(

        question_code="DSA-HEAP-008",

        question=
        "The smallest element is found at the root in:",

        options=[
            "Max Heap",
            "Min Heap",
            "Binary Tree",
            "BST"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Min Heap stores the smallest value at root.",
    ),



    Question(

        question_code="DSA-HEAP-009",

        question=
        "Heapify operation is used to:",

        options=[
            "Maintain heap property",
            "Search element",
            "Delete graph",
            "Sort strings"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Heapify restores heap property after insertion or deletion.",
    ),



    Question(

        question_code="DSA-HEAP-010",

        question=
        "What is the time complexity of building a heap from n elements?",

        options=[
            "O(n)",
            "O(log n)",
            "O(n log n)",
            "O(n²)"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Heap construction using bottom-up heapify takes O(n) time.",
    ),


    # =====================================================
    # GREEDY ALGORITHM (DSA-GREEDY-001–010)
    # =====================================================


    Question(

        question_code="DSA-GREEDY-001",

        question=
        "Greedy algorithm makes decisions based on:",

        options=[
            "Future possibilities",
            "Local best choice",
            "Random choice",
            "All possible solutions"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Greedy approach selects the best option available at current step.",
    ),



    Question(

        question_code="DSA-GREEDY-002",

        question=
        "Which problem is commonly solved using Greedy algorithm?",

        options=[
            "Activity Selection",
            "Binary Search",
            "Merge Sort",
            "Tower of Hanoi"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Activity Selection is a classic greedy algorithm problem.",
    ),



    Question(

        question_code="DSA-GREEDY-003",

        question=
        "Which algorithm is used for finding Minimum Spanning Tree using greedy approach?",

        options=[
            "Kruskal",
            "DFS",
            "Binary Search",
            "Floyd Warshall"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Kruskal algorithm uses greedy approach to build MST.",
    ),



    Question(

        question_code="DSA-GREEDY-004",

        question=
        "Which algorithm is also based on greedy strategy?",

        options=[
            "Dijkstra Algorithm",
            "Bubble Sort",
            "Binary Search",
            "DFS"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Dijkstra selects the minimum distance vertex greedily.",
    ),



    Question(

        question_code="DSA-GREEDY-005",

        question=
        "Greedy algorithms do not always provide:",

        options=[
            "Optimal solution",
            "Fast execution",
            "Local decisions",
            "Simple implementation"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Greedy works optimally only for certain problems.",
    ),



    Question(

        question_code="DSA-GREEDY-006",

        question=
        "Fractional Knapsack problem is solved using:",

        options=[
            "Greedy Algorithm",
            "Binary Search",
            "DFS",
            "Backtracking"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Fractional Knapsack uses greedy selection based on value/weight ratio.",
    ),



    Question(

        question_code="DSA-GREEDY-007",

        question=
        "Greedy algorithm generally follows which approach?",

        options=[
            "Top-down selection",
            "Bottom-up sorting",
            "Random search",
            "Complete exploration"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Greedy makes decisions step-by-step from current state.",
    ),



    Question(

        question_code="DSA-GREEDY-008",

        question=
        "Which property is required for greedy algorithms to work correctly?",

        options=[
            "Greedy Choice Property",
            "Binary Property",
            "Sorting Property",
            "Hash Property"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Greedy Choice Property allows locally optimal choices.",
    ),



    Question(

        question_code="DSA-GREEDY-009",

        question=
        "Huffman Coding is based on which algorithm technique?",

        options=[
            "Greedy",
            "Dynamic Programming",
            "Divide and Conquer",
            "Backtracking"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Huffman Coding repeatedly selects minimum frequency nodes greedily.",
    ),



    Question(

        question_code="DSA-GREEDY-010",

        question=
        "Main advantage of greedy algorithms is:",

        options=[
            "Simple and efficient solutions",
            "Always perfect solution",
            "No memory usage",
            "No computation"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Greedy algorithms are usually simple and efficient.",
    ),


    # =====================================================
    # BIT MANIPULATION (DSA-BIT-001–010)
    # =====================================================


    Question(

        question_code="DSA-BIT-001",

        question=
        "Which operator is used for bitwise AND operation?",

        options=[
            "&",
            "|",
            "^",
            "~"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "The & operator performs bitwise AND operation.",
    ),



    Question(

        question_code="DSA-BIT-002",

        question=
        "Which operator is used for bitwise OR operation?",

        options=[
            "&",
            "|",
            "^",
            "<<"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "The | operator performs bitwise OR operation.",
    ),



    Question(

        question_code="DSA-BIT-003",

        question=
        "Which operator performs XOR operation?",

        options=[
            "&",
            "|",
            "^",
            "%"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "^ operator performs bitwise XOR operation.",
    ),



    Question(

        question_code="DSA-BIT-004",

        question=
        "Left shift operator is represented by:",

        options=[
            ">>",
            "<<",
            "&",
            "^"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "<< shifts bits towards left side.",
    ),



    Question(

        question_code="DSA-BIT-005",

        question=
        "Right shift operator is represented by:",

        options=[
            "<<",
            ">>",
            "|",
            "~"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        ">> shifts bits towards right side.",
    ),



    Question(

        question_code="DSA-BIT-006",

        question=
        "Which operation is used to check whether a number is odd or even?",

        options=[
            "Addition",
            "Modulo",
            "Bitwise AND",
            "Multiplication"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Checking n & 1 determines odd or even number.",
    ),



    Question(

        question_code="DSA-BIT-007",

        question=
        "How many bits are changed when XOR is performed between same numbers?",

        options=[
            "All bits",
            "No bits",
            "Half bits",
            "One bit"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "XOR of same numbers always produces 0.",
    ),



    Question(

        question_code="DSA-BIT-008",

        question=
        "Which operation can be used to turn ON a specific bit?",

        options=[
            "OR operation",
            "AND operation",
            "Division",
            "Subtraction"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "OR with mask sets the required bit.",
    ),



    Question(

        question_code="DSA-BIT-009",

        question=
        "XOR of a number with itself gives:",

        options=[
            "Same number",
            "1",
            "0",
            "Negative number"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Any number XOR itself results in 0.",
    ),



    Question(

        question_code="DSA-BIT-010",

        question=
        "Bit manipulation is mainly used for:",

        options=[
            "Memory and performance optimization",
            "Sorting strings",
            "Database creation",
            "UI design"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Bit operations improve performance and reduce memory usage.",
    ),


    # =====================================================
    # ADVANCED DSA / COMPLEXITY (DSA-ADVANCED-001–010)
    # =====================================================


    Question(

        question_code="DSA-ADVANCED-001",

        question=
        "Big O notation is used to represent:",

        options=[
            "Memory address",
            "Algorithm time complexity",
            "Programming language",
            "Database structure"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Big O notation represents growth rate and time complexity of algorithms.",
    ),



    Question(

        question_code="DSA-ADVANCED-002",

        question=
        "Which complexity is considered the most efficient?",

        options=[
            "O(n²)",
            "O(n)",
            "O(log n)",
            "O(2ⁿ)"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "O(log n) grows slower compared to O(n) and O(n²).",
    ),



    Question(

        question_code="DSA-ADVANCED-003",

        question=
        "Space complexity measures:",

        options=[
            "Execution speed",
            "Memory usage",
            "Number of variables only",
            "Input size only"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Space complexity represents additional memory required by algorithm.",
    ),



    Question(

        question_code="DSA-ADVANCED-004",

        question=
        "Which technique divides a problem into smaller independent parts?",

        options=[
            "Divide and Conquer",
            "Greedy",
            "Hashing",
            "Backtracking"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Divide and Conquer breaks problem into smaller subproblems.",
    ),



    Question(

        question_code="DSA-ADVANCED-005",

        question=
        "Which algorithm follows Divide and Conquer approach?",

        options=[
            "Merge Sort",
            "Bubble Sort",
            "Selection Sort",
            "Linear Search"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Merge Sort divides array and combines sorted parts.",
    ),



    Question(

        question_code="DSA-ADVANCED-006",

        question=
        "Amortized analysis is used to calculate:",

        options=[
            "Average cost over multiple operations",
            "Only worst case",
            "Only best case",
            "Memory size"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Amortized analysis finds average performance over sequence of operations.",
    ),



    Question(

        question_code="DSA-ADVANCED-007",

        question=
        "Which data structure is used in implementing LRU Cache?",

        options=[
            "Array only",
            "HashMap and Doubly Linked List",
            "Stack only",
            "Queue only"
        ],

        answer="B",

        difficulty=Difficulty.HARD,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "LRU Cache uses HashMap with Doubly Linked List for O(1) operations.",
    ),



    Question(

        question_code="DSA-ADVANCED-008",

        question=
        "Which algorithm technique explores all possible solutions?",

        options=[
            "Brute Force",
            "Binary Search",
            "Greedy",
            "Hashing"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Brute Force checks all possible solutions.",
    ),



    Question(

        question_code="DSA-ADVANCED-009",

        question=
        "Which algorithm is used for detecting cycles in a linked list?",

        options=[
            "Floyd Cycle Detection",
            "Binary Search",
            "Merge Sort",
            "Dijkstra"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Floyd's algorithm uses slow and fast pointers to detect cycles.",
    ),



    Question(

        question_code="DSA-ADVANCED-010",

        question=
        "Which approach combines results of overlapping subproblems?",

        options=[
            "Dynamic Programming",
            "Sorting",
            "Searching",
            "Traversal"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Dynamic Programming stores and reuses subproblem results.",
    ),



]