CODING_QUESTIONS = [
    # =====================================================
    # PROGRAMMING FUNDAMENTALS
    # =====================================================

    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "programming_fundamentals",
        "skill": "programming_fundamentals",
        "question_text": (
            "What is the output of the following Python code? "
            "x = [1, 2, 3]; y = x; y.append(4); print(x)"
        ),
        "option_a": "[1, 2, 3]",
        "option_b": "[1, 2, 3, 4]",
        "option_c": "[4, 1, 2, 3]",
        "option_d": "Error",
        "correct_answer": "B",
        "explanation": (
            "Both x and y reference the same list object. "
            "Appending through y also changes the list referenced by x."
        ),
        "difficulty": "medium",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "programming_fundamentals",
        "skill": "programming_fundamentals",
        "question_text": (
            "Which programming construct is primarily used "
            "to repeat a block of code?"
        ),
        "option_a": "Loop",
        "option_b": "Class",
        "option_c": "Exception",
        "option_d": "Import",
        "correct_answer": "A",
        "explanation": (
            "Loops such as for and while are used to execute "
            "a block of code repeatedly."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "programming_fundamentals",
        "skill": "programming_fundamentals",
        "question_text": (
            "What is the main purpose of a function in programming?"
        ),
        "option_a": "To permanently store data",
        "option_b": "To organize reusable blocks of logic",
        "option_c": "To replace all variables",
        "option_d": "To create database tables",
        "correct_answer": "B",
        "explanation": (
            "Functions encapsulate reusable logic and help make "
            "programs modular and maintainable."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "programming_fundamentals",
        "skill": "programming_fundamentals",
        "question_text": (
            "What is the output of: print(10 // 3) in Python?"
        ),
        "option_a": "3",
        "option_b": "3.33",
        "option_c": "4",
        "option_d": "1",
        "correct_answer": "A",
        "explanation": (
            "The // operator performs floor division. "
            "10 // 3 evaluates to 3."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "programming_fundamentals",
        "skill": "programming_fundamentals",
        "question_text": (
            "Which statement best describes recursion?"
        ),
        "option_a": "A function calling itself to solve smaller instances",
        "option_b": "A loop that never terminates",
        "option_c": "A database query calling another table",
        "option_d": "A variable changing its data type",
        "correct_answer": "A",
        "explanation": (
            "Recursion solves a problem by having a function call "
            "itself on smaller subproblems until a base case is reached."
        ),
        "difficulty": "easy",
    },

    # =====================================================
    # DATA STRUCTURES
    # =====================================================

    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "data_structures",
        "skill": "data_structures",
        "question_text": (
            "Which data structure follows the Last In, First Out "
            "(LIFO) principle?"
        ),
        "option_a": "Queue",
        "option_b": "Stack",
        "option_c": "Graph",
        "option_d": "Heap",
        "correct_answer": "B",
        "explanation": (
            "A stack removes the most recently inserted element first."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "data_structures",
        "skill": "data_structures",
        "question_text": (
            "Which data structure is normally used by Breadth-First "
            "Search (BFS)?"
        ),
        "option_a": "Stack",
        "option_b": "Queue",
        "option_c": "Heap only",
        "option_d": "Hash table only",
        "correct_answer": "B",
        "explanation": (
            "BFS uses a queue to process vertices in level order."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "data_structures",
        "skill": "data_structures",
        "question_text": (
            "For a hash table with a good hash function, what is the "
            "average-case time complexity of a key lookup?"
        ),
        "option_a": "O(1)",
        "option_b": "O(log n)",
        "option_c": "O(n)",
        "option_d": "O(n²)",
        "correct_answer": "A",
        "explanation": (
            "Hash tables provide average O(1) lookup when hashing "
            "and collision handling behave well."
        ),
        "difficulty": "medium",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "data_structures",
        "skill": "data_structures",
        "question_text": (
            "Which property must hold for every node in a binary "
            "search tree?"
        ),
        "option_a": (
            "All values in the left subtree are smaller and all "
            "values in the right subtree are larger, under the "
            "tree's duplicate-key policy"
        ),
        "option_b": "Every node must have exactly two children",
        "option_c": "Every leaf must be at the same depth",
        "option_d": "The root must contain the smallest value",
        "correct_answer": "A",
        "explanation": (
            "A binary search tree maintains an ordering relationship "
            "between each node and the values in its subtrees."
        ),
        "difficulty": "medium",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "data_structures",
        "skill": "data_structures",
        "question_text": (
            "Which data structure is most suitable for implementing "
            "an Undo feature where the latest action is undone first?"
        ),
        "option_a": "Queue",
        "option_b": "Stack",
        "option_c": "Binary search tree",
        "option_d": "Adjacency matrix",
        "correct_answer": "B",
        "explanation": (
            "Undo operations naturally follow LIFO behavior, "
            "which is provided by a stack."
        ),
        "difficulty": "easy",
    },

    # =====================================================
    # ALGORITHMS AND COMPLEXITY
    # =====================================================

    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "algorithms_and_complexity",
        "skill": "algorithms_and_complexity",
        "question_text": (
            "What is the worst-case time complexity of binary search "
            "on a sorted array?"
        ),
        "option_a": "O(1)",
        "option_b": "O(log n)",
        "option_c": "O(n)",
        "option_d": "O(n log n)",
        "correct_answer": "B",
        "explanation": (
            "Binary search halves the remaining search space after "
            "each comparison, resulting in O(log n) time."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "algorithms_and_complexity",
        "skill": "algorithms_and_complexity",
        "question_text": (
            "What is the worst-case time complexity of merge sort?"
        ),
        "option_a": "O(log n)",
        "option_b": "O(n)",
        "option_c": "O(n log n)",
        "option_d": "O(n²)",
        "correct_answer": "C",
        "explanation": (
            "Merge sort performs logarithmic levels of splitting "
            "and O(n) merging work at each level."
        ),
        "difficulty": "medium",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "algorithms_and_complexity",
        "skill": "algorithms_and_complexity",
        "question_text": (
            "Two nested loops each execute n times. If the inner "
            "operation is constant time, what is the time complexity?"
        ),
        "option_a": "O(1)",
        "option_b": "O(n)",
        "option_c": "O(n log n)",
        "option_d": "O(n²)",
        "correct_answer": "D",
        "explanation": (
            "The inner operation executes n × n times, "
            "resulting in O(n²) work."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "algorithms_and_complexity",
        "skill": "algorithms_and_complexity",
        "question_text": (
            "Which sorting algorithm has O(n log n) worst-case time "
            "complexity among the following?"
        ),
        "option_a": "Bubble Sort",
        "option_b": "Insertion Sort",
        "option_c": "Merge Sort",
        "option_d": "Selection Sort",
        "correct_answer": "C",
        "explanation": (
            "Merge sort guarantees O(n log n) running time "
            "in the worst case."
        ),
        "difficulty": "medium",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "algorithms_and_complexity",
        "skill": "algorithms_and_complexity",
        "question_text": (
            "Dijkstra's shortest-path algorithm in its standard form "
            "requires which condition on edge weights?"
        ),
        "option_a": "Every edge must have weight 1",
        "option_b": "Edge weights must be non-negative",
        "option_c": "Every edge must have a negative weight",
        "option_d": "The graph cannot contain cycles",
        "correct_answer": "B",
        "explanation": (
            "Standard Dijkstra's algorithm assumes non-negative "
            "edge weights for its greedy choice to remain valid."
        ),
        "difficulty": "medium",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "algorithms_and_complexity",
        "skill": "algorithms_and_complexity",
        "question_text": (
            "Which technique stores previously computed results so "
            "that the same subproblem does not need to be solved again?"
        ),
        "option_a": "Memoization",
        "option_b": "Encapsulation",
        "option_c": "Normalization",
        "option_d": "Serialization",
        "correct_answer": "A",
        "explanation": (
            "Memoization caches results of previously solved "
            "subproblems and is commonly used in dynamic programming."
        ),
        "difficulty": "medium",
    },

    # =====================================================
    # OBJECT-ORIENTED PROGRAMMING
    # =====================================================

    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "object_oriented_programming",
        "skill": "object_oriented_programming",
        "question_text": (
            "Which OOP principle bundles data and the methods that "
            "operate on that data inside a class?"
        ),
        "option_a": "Encapsulation",
        "option_b": "Compilation",
        "option_c": "Iteration",
        "option_d": "Normalization",
        "correct_answer": "A",
        "explanation": (
            "Encapsulation groups state and behavior together "
            "and can control access to internal implementation details."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "object_oriented_programming",
        "skill": "object_oriented_programming",
        "question_text": (
            "What does inheritance primarily allow in "
            "object-oriented programming?"
        ),
        "option_a": "A class to derive behavior and attributes from another class",
        "option_b": "A database to automatically create indexes",
        "option_c": "A loop to execute recursively",
        "option_d": "Variables to exist without a data type",
        "correct_answer": "A",
        "explanation": (
            "Inheritance allows a derived class to reuse or extend "
            "features provided by a base class."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "object_oriented_programming",
        "skill": "object_oriented_programming",
        "question_text": (
            "What does polymorphism allow?"
        ),
        "option_a": "Only one class can exist in a program",
        "option_b": (
            "A common interface or operation to have different "
            "implementations for different types"
        ),
        "option_c": "Every variable must be private",
        "option_d": "A database table to have multiple primary keys",
        "correct_answer": "B",
        "explanation": (
            "Polymorphism allows the same interface or operation "
            "to exhibit type-specific behavior."
        ),
        "difficulty": "medium",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "object_oriented_programming",
        "skill": "object_oriented_programming",
        "question_text": (
            "Which concept focuses on exposing essential behavior "
            "while hiding unnecessary implementation details?"
        ),
        "option_a": "Abstraction",
        "option_b": "Iteration",
        "option_c": "Indexing",
        "option_d": "Recursion",
        "correct_answer": "A",
        "explanation": (
            "Abstraction presents relevant behavior while hiding "
            "implementation complexity from the user of an interface."
        ),
        "difficulty": "easy",
    },

    # =====================================================
    # SQL AND DATABASES
    # =====================================================

    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "sql_and_databases",
        "skill": "sql_and_databases",
        "question_text": (
            "Which SQL clause is used to filter rows before "
            "grouping or aggregation?"
        ),
        "option_a": "ORDER BY",
        "option_b": "WHERE",
        "option_c": "HAVING",
        "option_d": "GROUP BY",
        "correct_answer": "B",
        "explanation": (
            "WHERE filters individual rows before grouping. "
            "HAVING is commonly used to filter groups after aggregation."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "sql_and_databases",
        "skill": "sql_and_databases",
        "question_text": (
            "What is the primary purpose of a database primary key?"
        ),
        "option_a": "To uniquely identify each row",
        "option_b": "To encrypt every column",
        "option_c": "To automatically sort every query",
        "option_d": "To allow duplicate rows",
        "correct_answer": "A",
        "explanation": (
            "A primary key uniquely identifies each record "
            "within a table."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "sql_and_databases",
        "skill": "sql_and_databases",
        "question_text": (
            "Which SQL JOIN returns only rows that have matching "
            "values in both joined tables?"
        ),
        "option_a": "LEFT JOIN",
        "option_b": "RIGHT JOIN",
        "option_c": "INNER JOIN",
        "option_d": "CROSS JOIN",
        "correct_answer": "C",
        "explanation": (
            "INNER JOIN returns rows for which the join condition "
            "matches in both tables."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "sql_and_databases",
        "skill": "sql_and_databases",
        "question_text": (
            "Which normal form requires that attribute values be "
            "atomic, with no repeating groups in a relation?"
        ),
        "option_a": "First Normal Form (1NF)",
        "option_b": "Second Normal Form (2NF)",
        "option_c": "Third Normal Form (3NF)",
        "option_d": "BCNF only",
        "correct_answer": "A",
        "explanation": (
            "1NF requires atomic attribute values and eliminates "
            "repeating groups."
        ),
        "difficulty": "medium",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "sql_and_databases",
        "skill": "sql_and_databases",
        "question_text": (
            "What is a foreign key primarily used for?"
        ),
        "option_a": "To establish a relationship between tables",
        "option_b": "To compile application source code",
        "option_c": "To sort every table automatically",
        "option_d": "To replace all primary keys",
        "correct_answer": "A",
        "explanation": (
            "A foreign key references a candidate key, commonly "
            "a primary key, in another or the same table and helps "
            "enforce referential integrity."
        ),
        "difficulty": "easy",
    },

    # =====================================================
    # DEBUGGING AND PROBLEM SOLVING
    # =====================================================

    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "debugging_and_problem_solving",
        "skill": "debugging_and_problem_solving",
        "question_text": (
            "A loop uses the condition i <= len(arr) and accesses "
            "arr[i], with i starting at 0. What problem can occur "
            "when i becomes len(arr)?"
        ),
        "option_a": "Integer overflow",
        "option_b": "Out-of-bounds index access",
        "option_c": "Database deadlock",
        "option_d": "Infinite recursion",
        "correct_answer": "B",
        "explanation": (
            "For zero-based indexing, the last valid index is "
            "len(arr) - 1. Accessing arr[len(arr)] is out of bounds."
        ),
        "difficulty": "medium",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "debugging_and_problem_solving",
        "skill": "debugging_and_problem_solving",
        "question_text": (
            "A recursive function has no reachable base case. "
            "What is the most likely result?"
        ),
        "option_a": "The recursion continues until a recursion/stack limit is reached",
        "option_b": "The algorithm automatically becomes iterative",
        "option_c": "The database is normalized",
        "option_d": "The function always returns zero",
        "correct_answer": "A",
        "explanation": (
            "Without a reachable terminating condition, recursive "
            "calls continue until the runtime's recursion or stack "
            "limit is exhausted."
        ),
        "difficulty": "easy",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "debugging_and_problem_solving",
        "skill": "debugging_and_problem_solving",
        "question_text": (
            "You need to determine whether an array contains duplicate "
            "values efficiently. Which approach usually gives O(n) "
            "average time?"
        ),
        "option_a": "Compare every pair of elements",
        "option_b": "Insert elements into a hash set while checking membership",
        "option_c": "Use three nested loops",
        "option_d": "Generate every permutation",
        "correct_answer": "B",
        "explanation": (
            "Hash-set membership and insertion are O(1) on average, "
            "so scanning n elements takes O(n) average time."
        ),
        "difficulty": "medium",
    },
    {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "debugging_and_problem_solving",
        "skill": "debugging_and_problem_solving",
        "question_text": (
            "Given a sorted array of one million elements, which "
            "algorithm is generally preferable for searching for "
            "a specific value?"
        ),
        "option_a": "Linear search",
        "option_b": "Binary search",
        "option_c": "Bubble sort",
        "option_d": "Depth-first search",
        "correct_answer": "B",
        "explanation": (
            "Because the array is sorted, binary search can locate "
            "a value in O(log n) time."
        ),
        "difficulty": "easy",
    },
        {
        "assessment_type": "college_coding",
        "user_role": "college_student",
        "category": "debugging_and_problem_solving",
        "skill": "debugging_and_problem_solving",
        "question_text": (
            "Which algorithm can detect a cycle in a singly linked "
            "list using O(1) extra space?"
        ),
        "option_a": "Binary Search",
        "option_b": "Floyd's Cycle Detection Algorithm",
        "option_c": "Merge Sort",
        "option_d": "Breadth-First Search",
        "correct_answer": "B",
        "explanation": (
            "Floyd's Cycle Detection Algorithm uses a slow pointer "
            "and a fast pointer. If a cycle exists, the two pointers "
            "will eventually meet."
        ),
        "difficulty": "medium",
    },
]
