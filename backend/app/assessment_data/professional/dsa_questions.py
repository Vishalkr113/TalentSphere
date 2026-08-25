from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


PROFESSIONAL_DSA_QUESTIONS: list[Question] = [

    Question(
        question_code="PROFESSIONAL-DSA-001",
        question=
        "Problem: Given an array, return the length of the longest contiguous subarray with sum at most K when all values are non-negative. Best general approach?",
        options=[
            "Sliding window",
            "DFS",
            "Topological sort",
            "Union-find",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.ARRAY,

        explanation=
        "With non-negative values, expanding and shrinking a window maintains the sum constraint.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-002",
        question=
        "Problem: Return the first index where a target appears in a sorted array with duplicates. Which approach gives O(log n)?",
        options=[
            "Binary search biased left",
            "Linear scan",
            "Heap",
            "BFS",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.SEARCHING,

        explanation=
        "When target is found, continue searching the left half to find its first position.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-003",
        question=
        "Problem: Given intervals, merge all overlapping intervals. Which first step is most useful?",
        options=[
            "Sort by start time",
            "Sort by end only randomly",
            "Use DFS",
            "Build a linked list",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.SORTING,

        explanation=
        "Sorting intervals by start allows a single linear merge pass.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-004",
        question=
        "Problem: Given daily prices, find the maximum profit with unlimited transactions but no simultaneous holdings. Which strategy works?",
        options=[
            "Add every positive day-to-day increase",
            "Take only the global min and max",
            "Use BFS",
            "Sort prices",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.GREEDY,

        explanation=
        "Every positive consecutive increase can be captured by separate transactions.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-005",
        question=
        "Problem: Given an array, find the length of the shortest subarray whose sum is at least S with positive numbers. Which technique is appropriate?",
        options=[
            "Sliding window",
            "Floyd-Warshall",
            "Union-find",
            "Inorder traversal",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.ARRAY,

        explanation=
        "A moving window can shrink after reaching the required sum.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-006",
        question=
        "Problem: Given an array containing 1..n with one missing value, O(n) time and O(1) extra space can be achieved using:",
        options=[
            "XOR or arithmetic sum",
            "Sorting only",
            "Hash set",
            "BFS",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.DSA,
        topic=Topic.ARRAY,

        explanation=
        "XOR or the expected-minus-actual sum identifies the missing value.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-007",
        question=
        "Problem: Find the longest substring containing at most two distinct characters. Best pattern?",
        options=[
            "Sliding window with frequency map",
            "Binary tree",
            "Heap only",
            "Topological sort",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.STRING,

        explanation=
        "A frequency map tracks distinct characters inside a moving window.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-008",
        question=
        "Problem: Determine whether two strings are isomorphic. A correct approach maintains:",
        options=[
            "Two-way character mapping",
            "Only string lengths",
            "A stack only",
            "Graph BFS on indices",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.STRING,

        explanation=
        "A bijective mapping prevents two source characters mapping to one target character.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-009",
        question=
        "Problem: Given a string, find the minimum number of deletions to make it a palindrome. A useful DP relation compares the string with its:",
        options=[
            "Reverse",
            "Sorted version",
            "Hash only",
            "Prefix count only",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.DYNAMIC_PROGRAMMING,

        explanation=
        "Minimum deletions relate to the longest palindromic subsequence, which equals LCS with the reverse.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-010",
        question=
        "Problem: Given words, determine whether one word can be formed from the letters of another with limited counts. Best representation?",
        options=[
            "Frequency array/map",
            "Stack only",
            "Binary search tree",
            "Queue",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.DSA,
        topic=Topic.HASHING,

        explanation=
        "Character frequencies directly represent available counts.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-011",
        question=
        "Problem: Reverse nodes of a linked list in groups of k. Which extra structure is generally unnecessary for an iterative solution?",
        options=[
            "An array of all nodes",
            "Pointer references",
            "A current pointer",
            "A next pointer",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.LINKED_LIST,

        explanation=
        "The list can be rearranged in place with pointers; storing all nodes is unnecessary.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-012",
        question=
        "Problem: Determine whether a linked list is a palindrome in O(1) extra space. A common approach is:",
        options=[
            "Find middle, reverse second half, compare",
            "Sort the list",
            "Use a queue only",
            "Build a tree",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.LINKED_LIST,

        explanation=
        "Reversing the second half enables an in-place comparison.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-013",
        question=
        "Problem: Remove the nth node from the end of a singly linked list in one pass. Which technique works?",
        options=[
            "Two pointers with a fixed gap",
            "Binary search",
            "Heap",
            "DFS",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.LINKED_LIST,

        explanation=
        "Maintaining an n-node gap lets the first pointer reach the end while the second reaches the predecessor.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-014",
        question=
        "Problem: Add two non-negative integers represented by linked lists in reverse digit order. What must be tracked?",
        options=[
            "Carry",
            "Tree height",
            "Queue size only",
            "Graph degree",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.DSA,
        topic=Topic.LINKED_LIST,

        explanation=
        "Digit addition requires carrying values to the next position.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-015",
        question=
        "Problem: Clone a linked structure where each node has next and arbitrary pointer. A robust mapping is from:",
        options=[
            "Original node to cloned node",
            "Value to index only",
            "Edge to weight only",
            "Head to tail only",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.HASHING,

        explanation=
        "A node mapping preserves arbitrary-pointer relationships.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-016",
        question=
        "Problem: Evaluate an expression containing numbers and +,-,*,/ with standard precedence. A common stack-based approach uses:",
        options=[
            "Operator/value stacks or equivalent precedence handling",
            "BFS",
            "Union-find",
            "Heap sort",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.STACK,

        explanation=
        "Stacks can manage operators and intermediate values according to precedence.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-017",
        question=
        "Problem: Design a stack supporting getMin in O(1). Store each element with:",
        options=[
            "Current minimum information",
            "Only its index",
            "Its hash only",
            "Its next larger element",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.STACK,

        explanation=
        "A second stack or paired minimum maintains the current minimum.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-018",
        question=
        "Problem: Simplify a Unix-style path containing '.', '..' and repeated slashes. Natural structure:",
        options=[
            "Stack",
            "Heap",
            "Graph",
            "Binary search",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.DSA,
        topic=Topic.STACK,

        explanation=
        "A stack of path components handles directory navigation.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-019",
        question=
        "Problem: Implement a queue using two stacks. The expensive transfer should happen:",
        options=[
            "Only when the output stack is empty",
            "On every operation",
            "Never",
            "Only after errors",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.QUEUE,

        explanation=
        "Lazy transfer gives amortized O(1) operations.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-020",
        question=
        "Problem: Given a stream of numbers, maintain the median after each insertion. A standard approach uses:",
        options=[
            "Two heaps",
            "Two queues only",
            "DFS",
            "One sorted array with no insertion cost",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.HEAP,

        explanation=
        "A max-heap for the lower half and min-heap for the upper half maintain the median.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-021",
        question=
        "Problem: Find the kth largest element in an unsorted array without fully sorting it. Which approach can average O(n)?",
        options=[
            "Quickselect",
            "Merge sort always",
            "BFS",
            "Linked-list reversal",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.SEARCHING,

        explanation=
        "Quickselect partitions around pivots and has average linear time.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-022",
        question=
        "Problem: Given tasks with durations and deadlines, a greedy scheduling problem may prioritize by:",
        options=[
            "A criterion derived from the objective, such as earliest deadline",
            "Alphabetical name",
            "Random order",
            "Largest ID only",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.GREEDY,

        explanation=
        "Scheduling objectives determine the appropriate greedy ordering; earliest deadline is optimal for minimizing maximum lateness.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-023",
        question=
        "Problem: For a binary tree, return the visible nodes from the right side. A level-order approach records:",
        options=[
            "The last node at each level",
            "The first leaf only",
            "The root twice",
            "All left children",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.TREE,

        explanation=
        "The last visited node at each depth is visible from the right.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-024",
        question=
        "Problem: Check whether a binary tree is height-balanced. What condition is required at every node?",
        options=[
            "Left/right height difference is at most 1",
            "Both children must exist",
            "All values equal",
            "Depth must be even",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.TREE,

        explanation=
        "Balance requires subtree height difference no greater than one.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-025",
        question=
        "Problem: Find the lowest common ancestor in a binary search tree. Use:",
        options=[
            "BST ordering to move left/right",
            "BFS over all values always",
            "Sorting nodes",
            "A heap",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.TREE,

        explanation=
        "The BST property directs the search based on the target values.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-026",
        question=
        "Problem: Serialize a binary tree so it can be reconstructed. You must preserve:",
        options=[
            "Null child positions",
            "Only leaf values",
            "Only height",
            "Only sorted values",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.TREE,

        explanation=
        "Null markers or equivalent structure preserve tree shape.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-027",
        question=
        "Problem: Find the kth smallest value in a BST. An inorder traversal can stop after:",
        options=[
            "Visiting k nodes",
            "Visiting all nodes always",
            "Finding a leaf",
            "One level",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.TREE,

        explanation=
        "BST inorder traversal is sorted, so the kth visited node is the kth smallest.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-028",
        question=
        "Problem: Build a trie for lowercase words. Each node commonly stores:",
        options=[
            "Children by character and terminal marker",
            "Only a count of words globally",
            "A heap",
            "Graph weights",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.STRING,

        explanation=
        "Trie nodes represent prefixes and need child links plus word termination.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-029",
        question=
        "Problem: Detect whether an undirected graph has a cycle using DFS. A visited neighbor is a cycle edge when it is:",
        options=[
            "Not the current node's parent",
            "Always the root",
            "A leaf",
            "A higher-degree node",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.GRAPH,

        explanation=
        "In an undirected DFS, a visited neighbor other than the parent indicates a cycle.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-030",
        question=
        "Problem: Find connected components in an undirected graph. A standard approach is:",
        options=[
            "DFS/BFS from every unvisited vertex",
            "Binary search",
            "Merge sort",
            "Heap",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.DSA,
        topic=Topic.GRAPH,

        explanation=
        "Each traversal marks one connected component.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-031",
        question=
        "Problem: Given prerequisites between courses, determine whether all can be completed. This is equivalent to detecting a cycle in a:",
        options=[
            "Directed graph",
            "Heap",
            "Linked list",
            "Array",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.GRAPH,

        explanation=
        "A directed cycle makes prerequisites impossible to satisfy.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-032",
        question=
        "Problem: Find the shortest path in a grid where each move costs one. Best baseline algorithm:",
        options=[
            "BFS",
            "DFS without memoization",
            "Quick sort",
            "Union-find only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.DSA,
        topic=Topic.GRAPH,

        explanation=
        "BFS explores cells by increasing number of steps.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-033",
        question=
        "Problem: For weighted edges with some negative weights but no negative cycle, which shortest-path algorithm is appropriate?",
        options=[
            "Bellman-Ford",
            "Dijkstra",
            "BFS only",
            "Kruskal",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.GRAPH,

        explanation=
        "Bellman-Ford handles negative edge weights and detects negative cycles.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-034",
        question=
        "Problem: To compute all-pairs shortest paths in a dense graph, a classic DP algorithm is:",
        options=[
            "Floyd-Warshall",
            "BFS only",
            "Binary search",
            "Heapify",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.GRAPH,

        explanation=
        "Floyd-Warshall uses dynamic programming over intermediate vertices.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-035",
        question=
        "Problem: Find the minimum number of coins to make an amount with unlimited coin use. A standard solution is:",
        options=[
            "1D dynamic programming",
            "DFS without memoization",
            "Topological sort only",
            "Union-find",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.DYNAMIC_PROGRAMMING,

        explanation=
        "DP stores the best answer for each amount.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-036",
        question=
        "Problem: In 0/1 knapsack, each item can be used:",
        options=[
            "At most once",
            "Unlimited times",
            "Exactly twice",
            "Only if its value is zero",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.DSA,
        topic=Topic.DYNAMIC_PROGRAMMING,

        explanation=
        "The 0/1 constraint means each item is selected at most once.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-037",
        question=
        "Problem: The longest increasing subsequence can be solved in O(n log n) using:",
        options=[
            "Tails array with binary search",
            "BFS",
            "Union-find",
            "Heap sort",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.DYNAMIC_PROGRAMMING,

        explanation=
        "The patience-sorting-style tails method gives O(n log n).",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-038",
        question=
        "Problem: In edit distance, allowed operations are insert, delete and:",
        options=[
            "Replace",
            "Sort",
            "Rotate array",
            "Reverse only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.DSA,
        topic=Topic.DYNAMIC_PROGRAMMING,

        explanation=
        "Levenshtein distance uses insertion, deletion and substitution.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-039",
        question=
        "Problem: Generate all valid parentheses for n pairs. The backtracking state must track:",
        options=[
            "Counts of opens and closes used",
            "Only string length",
            "Graph degree",
            "Array sum",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.BACKTRACKING,

        explanation=
        "Validity depends on remaining open/close counts.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-040",
        question=
        "Problem: Solve a Sudoku-like constraint grid using backtracking. A candidate is valid when:",
        options=[
            "It violates none of the row/column/region constraints",
            "It is always the smallest digit",
            "It matches the previous row",
            "It is prime",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.BACKTRACKING,

        explanation=
        "Constraint checking determines whether a candidate can be placed.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-041",
        question=
        "Problem: Given a set of intervals, find the minimum number of rooms needed for meetings. A common efficient technique uses:",
        options=[
            "Sorted starts and ends with two pointers",
            "DFS",
            "Trie",
            "Stack only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.GREEDY,

        explanation=
        "Sorting start and end times lets us track concurrent meetings.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-042",
        question=
        "Problem: A monotonic deque can solve sliding-window maximum in O(n) because:",
        options=[
            "Each element enters and leaves the deque at most once",
            "It sorts the whole array each time",
            "It uses recursion",
            "It uses a graph",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.QUEUE,

        explanation=
        "The deque maintains decreasing candidates and each index is processed a constant number of times.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-043",
        question=
        "Problem: For range-sum queries with point updates, a Fenwick tree supports both in:",
        options=[
            "O(log n)",
            "O(n²)",
            "O(1) always",
            "O(2^n)",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.ADVANCED_DSA,

        explanation=
        "Fenwick trees provide logarithmic prefix sums and point updates.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-044",
        question=
        "Problem: For range queries and range updates, a segment tree is useful because it:",
        options=[
            "Stores aggregate information hierarchically",
            "Requires sorting after every update",
            "Only supports strings",
            "Cannot represent intervals",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.ADVANCED_DSA,

        explanation=
        "Segment trees decompose ranges into logarithmically many nodes.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-045",
        question=
        "Problem: A disjoint-set union structure is ideal for:",
        options=[
            "Maintaining connected components under unions",
            "Sorting strings",
            "Parsing HTML",
            "Finding medians",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.ADVANCED_DSA,

        explanation=
        "DSU supports near-constant amortized union/find operations.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-046",
        question=
        "Problem: To find whether a number is a happy number efficiently, cycle detection can use:",
        options=[
            "Floyd's tortoise-and-hare idea",
            "BFS on a tree",
            "Merge sort",
            "Topological sort",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.DSA,
        topic=Topic.HASHING,

        explanation=
        "Repeated state transitions can be checked for cycles with two-speed pointers.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-047",
        question=
        "Problem: A rolling hash is useful for:",
        options=[
            "Comparing substrings efficiently",
            "Balancing a binary tree",
            "Scheduling tasks",
            "Finding graph degrees",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.STRING,

        explanation=
        "Rolling hashes update substring hashes efficiently and support fast comparisons with collision considerations.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-048",
        question=
        "Problem: Find the first duplicate value in an array where values are in a constrained range. Which tool is often appropriate when extra space is allowed?",
        options=[
            "Hash set",
            "DFS",
            "Queue",
            "Binary tree",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.DSA,
        topic=Topic.HASHING,

        explanation=
        "A hash set can detect a repeated value in expected O(n).",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-049",
        question=
        "Problem: Given a sorted array, remove duplicates in-place and return the new length. Which pattern gives O(n) time O(1) extra space?",
        options=[
            "Two pointers",
            "Heap",
            "DFS",
            "Recursion with copying",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.DSA,
        topic=Topic.ARRAY,

        explanation=
        "A write pointer compacts unique values while a read pointer scans.",
    ),

    Question(
        question_code="PROFESSIONAL-DSA-050",
        question=
        "Problem: Given a graph with edge weights 0 or 1, a shortest-path algorithm can exploit weights using:",
        options=[
            "0-1 BFS with a deque",
            "Standard DFS",
            "Merge sort",
            "Binary search",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.DSA,
        topic=Topic.GRAPH,

        explanation=
        "0-1 BFS processes zero-weight edges from the front and one-weight edges from the back.",
    ),
]
