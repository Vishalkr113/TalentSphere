from .enums import Difficulty, QuestionType, Topic
from .schemas import Question


# =====================================================
# C PROGRAMMING (COD-C-001–010)
# =====================================================

CODING_QUESTIONS: list[Question] = [

    Question(

        question_code="COD-C-001",

        question=
        "Which function is used to print output in C language?",

        options=[
            "scanf()",
            "printf()",
            "print()",
            "display()"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "printf() function is used to display output in C.",
    ),



    Question(

        question_code="COD-C-002",

        question=
        "Which header file is required for printf() function?",

        options=[
            "stdlib.h",
            "math.h",
            "stdio.h",
            "string.h"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "stdio.h contains input-output functions like printf and scanf.",
    ),



    Question(

        question_code="COD-C-003",

        question=
        "Which data type is used to store a single character in C?",

        options=[
            "int",
            "char",
            "float",
            "double"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "char data type stores a single character.",
    ),



    Question(

        question_code="COD-C-004",

        question=
        "Which operator is used to find remainder in C?",

        options=[
            "/",
            "%",
            "*",
            "//"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "Modulo operator % returns remainder.",
    ),



    Question(

        question_code="COD-C-005",

        question=
        "Which loop executes at least once even if condition is false?",

        options=[
            "for loop",
            "while loop",
            "do-while loop",
            "nested loop"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "do-while loop checks condition after execution.",
    ),



    Question(

        question_code="COD-C-006",

        question=
        "Which symbol is used to end a statement in C?",

        options=[
            ":",
            ";",
            ".",
            ","
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "Semicolon terminates statements in C.",
    ),



    Question(

        question_code="COD-C-007",

        question=
        "Which keyword is used to define a constant in C?",

        options=[
            "constant",
            "const",
            "define",
            "static"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "const keyword creates constant variables.",
    ),



    Question(

        question_code="COD-C-008",

        question=
        "Which memory is allocated dynamically in C?",

        options=[
            "Stack",
            "Heap",
            "Register",
            "Cache"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "Dynamic memory allocation happens in heap memory.",
    ),



    Question(

        question_code="COD-C-009",

        question=
        "Which function is used to read formatted input in C?",

        options=[
            "printf()",
            "scanf()",
            "gets()",
            "puts()"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "scanf() reads formatted input from user.",
    ),



    Question(

        question_code="COD-C-010",

        question=
        "Which of these is not a valid C variable name?",

        options=[
            "value1",
            "_number",
            "1value",
            "total"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "Variable names cannot start with a digit.",
    ),



    # =====================================================
    # C++ PROGRAMMING (COD-CPP-001–010)
    # =====================================================


    Question(

        question_code="COD-CPP-001",

        question=
        "Which feature of C++ allows the same function name with different parameters?",

        options=[
            "Inheritance",
            "Encapsulation",
            "Function Overloading",
            "Abstraction"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.CPP,

        explanation=
        "Function overloading allows multiple functions with same name but different parameters.",
    ),



    Question(

        question_code="COD-CPP-002",

        question=
        "Which symbol is used for scope resolution in C++?",

        options=[
            ".",
            "::",
            "->",
            ":"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.CPP,

        explanation=
        "Scope resolution operator (::) is used to access class members outside class.",
    ),



    Question(

        question_code="COD-CPP-003",

        question=
        "Which keyword is used to create an object dynamically in C++?",

        options=[
            "malloc",
            "new",
            "create",
            "alloc"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.CPP,

        explanation=
        "new keyword is used for dynamic memory allocation in C++.",
    ),



    Question(

        question_code="COD-CPP-004",

        question=
        "Which concept allows one class to acquire properties of another class?",

        options=[
            "Polymorphism",
            "Inheritance",
            "Encapsulation",
            "Compilation"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.CPP,

        explanation=
        "Inheritance allows a class to acquire properties of another class.",
    ),



    Question(

        question_code="COD-CPP-005",

        question=
        "Which header file is used for input and output in C++?",

        options=[
            "stdio.h",
            "iostream",
            "stdlib.h",
            "string.h"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.CPP,

        explanation=
        "iostream contains cin and cout for input-output operations.",
    ),



    Question(

        question_code="COD-CPP-006",

        question=
        "Which object is used for output in C++?",

        options=[
            "cin",
            "cout",
            "print",
            "scanf"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.CPP,

        explanation=
        "cout is used to display output in C++.",
    ),



    Question(

        question_code="COD-CPP-007",

        question=
        "Which OOP concept hides internal implementation details?",

        options=[
            "Inheritance",
            "Encapsulation",
            "Polymorphism",
            "Overloading"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.CPP,

        explanation=
        "Encapsulation hides data and implementation details.",
    ),



    Question(

        question_code="COD-CPP-008",

        question=
        "Which keyword is used to define a class in C++?",

        options=[
            "object",
            "class",
            "struct",
            "define"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.CPP,

        explanation=
        "class keyword is used to create classes.",
    ),



    Question(

        question_code="COD-CPP-009",

        question=
        "Which function is automatically called when an object is created?",

        options=[
            "Destructor",
            "Constructor",
            "Main function",
            "Virtual function"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.CPP,

        explanation=
        "Constructor initializes an object when it is created.",
    ),



    Question(

        question_code="COD-CPP-010",

        question=
        "Which feature allows same interface with different implementations?",

        options=[
            "Inheritance",
            "Polymorphism",
            "Encapsulation",
            "Abstraction"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.CPP,

        explanation=
        "Polymorphism allows one interface with multiple implementations.",
    ),



    # =====================================================
    # JAVA PROGRAMMING (COD-JAVA-001–010)
    # =====================================================


    Question(

        question_code="COD-JAVA-001",

        question=
        "Which keyword is used to create an object in Java?",

        options=[
            "create",
            "new",
            "object",
            "class"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.JAVA,

        explanation=
        "new keyword is used to create objects in Java.",
    ),



    Question(

        question_code="COD-JAVA-002",

        question=
        "Which method is the entry point of a Java program?",

        options=[
            "start()",
            "main()",
            "run()",
            "init()"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.JAVA,

        explanation=
        "main() method is the starting point of Java execution.",
    ),



    Question(

        question_code="COD-JAVA-003",

        question=
        "Which keyword is used to inherit a class in Java?",

        options=[
            "implements",
            "extends",
            "inherits",
            "super"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.JAVA,

        explanation=
        "extends keyword is used for class inheritance.",
    ),



    Question(

        question_code="COD-JAVA-004",

        question=
        "Which feature allows multiple methods with the same name in Java?",

        options=[
            "Inheritance",
            "Method Overloading",
            "Encapsulation",
            "Abstraction"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.JAVA,

        explanation=
        "Method overloading allows same method name with different parameters.",
    ),



    Question(

        question_code="COD-JAVA-005",

        question=
        "Which package contains Scanner class in Java?",

        options=[
            "java.lang",
            "java.util",
            "java.io",
            "java.net"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.JAVA,

        explanation=
        "Scanner class is available inside java.util package.",
    ),



    Question(

        question_code="COD-JAVA-006",

        question=
        "Which keyword is used to make a variable constant in Java?",

        options=[
            "static",
            "const",
            "final",
            "constant"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.JAVA,

        explanation=
        "final keyword creates constant variables.",
    ),



    Question(

        question_code="COD-JAVA-007",

        question=
        "Which concept hides data from outside access?",

        options=[
            "Polymorphism",
            "Encapsulation",
            "Inheritance",
            "Compilation"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.JAVA,

        explanation=
        "Encapsulation binds data and methods while hiding details.",
    ),



    Question(

        question_code="COD-JAVA-008",

        question=
        "Which memory area stores objects in Java?",

        options=[
            "Stack",
            "Heap",
            "Register",
            "Cache"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.JAVA,

        explanation=
        "Objects are created in heap memory.",
    ),



    Question(

        question_code="COD-JAVA-009",

        question=
        "Which keyword refers to the current object in Java?",

        options=[
            "self",
            "current",
            "this",
            "object"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.JAVA,

        explanation=
        "this keyword refers to the current object.",
    ),



    Question(

        question_code="COD-JAVA-010",

        question=
        "Which interface is implemented by a class to achieve abstraction in Java?",

        options=[
            "Interface",
            "Abstract",
            "Class",
            "Package"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.JAVA,

        explanation=
        "Interfaces are used to achieve abstraction in Java.",
    ),



    # =====================================================
    # PYTHON PROGRAMMING (COD-PYTHON-001–010)
    # =====================================================


    Question(

        question_code="COD-PYTHON-001",

        question=
        "Which keyword is used to define a function in Python?",

        options=[
            "func",
            "define",
            "def",
            "function"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "def keyword is used to create functions in Python.",
    ),



    Question(

        question_code="COD-PYTHON-002",

        question=
        "Which data type is mutable in Python?",

        options=[
            "Tuple",
            "String",
            "List",
            "Integer"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "Lists are mutable, meaning their elements can be changed.",
    ),



    Question(

        question_code="COD-PYTHON-003",

        question=
        "Which symbol is used for comments in Python?",

        options=[
            "//",
            "#",
            "/* */",
            "<!-- -->"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "# is used for single-line comments in Python.",
    ),



    Question(

        question_code="COD-PYTHON-004",

        question=
        "Which function is used to get input from the user in Python?",

        options=[
            "scan()",
            "input()",
            "read()",
            "get()"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "input() function takes input from the user.",
    ),



    Question(

        question_code="COD-PYTHON-005",

        question=
        "Which keyword is used to create a class in Python?",

        options=[
            "object",
            "class",
            "struct",
            "define"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "class keyword is used to create classes in Python.",
    ),



    Question(

        question_code="COD-PYTHON-006",

        question=
        "Which collection stores data in key-value pairs in Python?",

        options=[
            "List",
            "Tuple",
            "Dictionary",
            "Set"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "Dictionary stores data in key-value format.",
    ),



    Question(

        question_code="COD-PYTHON-007",

        question=
        "Which operator is used for exponentiation in Python?",

        options=[
            "^",
            "**",
            "//",
            "%"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "** operator is used for power calculation.",
    ),



    Question(

        question_code="COD-PYTHON-008",

        question=
        "Which keyword is used to handle exceptions in Python?",

        options=[
            "catch",
            "error",
            "try",
            "handle"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "try-except block is used for exception handling.",
    ),



    Question(

        question_code="COD-PYTHON-009",

        question=
        "Which method adds an element at the end of a Python list?",

        options=[
            "add()",
            "append()",
            "insertEnd()",
            "push()"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "append() adds an item to the end of a list.",
    ),



    Question(

        question_code="COD-PYTHON-010",

        question=
        "Which Python library is mainly used for numerical computations?",

        options=[
            "NumPy",
            "Django",
            "Flask",
            "Tkinter"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "NumPy is widely used for numerical and scientific computing.",
    ),



    # =====================================================
    # PYTHON PROGRAMMING (COD-PYTHON-011–020)
    # =====================================================


    Question(

        question_code="COD-PYTHON-011",

        question=
        "Which keyword is used to define a function in Python?",

        options=[
            "func",
            "define",
            "def",
            "function"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "def keyword is used to create functions in Python.",
    ),



    Question(

        question_code="COD-PYTHON-012",

        question=
        "Which data type is mutable in Python?",

        options=[
            "Tuple",
            "String",
            "List",
            "Integer"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "Lists are mutable, meaning their elements can be changed.",
    ),



    Question(

        question_code="COD-PYTHON-013",

        question=
        "Which symbol is used for comments in Python?",

        options=[
            "//",
            "#",
            "/* */",
            "<!-- -->"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "# is used for single-line comments in Python.",
    ),



    Question(

        question_code="COD-PYTHON-014",

        question=
        "Which function is used to get input from the user in Python?",

        options=[
            "scan()",
            "input()",
            "read()",
            "get()"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "input() function takes input from the user.",
    ),



    Question(

        question_code="COD-PYTHON-015",

        question=
        "Which keyword is used to create a class in Python?",

        options=[
            "object",
            "class",
            "struct",
            "define"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "class keyword is used to create classes in Python.",
    ),



    Question(

        question_code="COD-PYTHON-016",

        question=
        "Which collection stores data in key-value pairs in Python?",

        options=[
            "List",
            "Tuple",
            "Dictionary",
            "Set"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "Dictionary stores data in key-value format.",
    ),



    Question(

        question_code="COD-PYTHON-017",

        question=
        "Which operator is used for exponentiation in Python?",

        options=[
            "^",
            "**",
            "//",
            "%"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "** operator is used for power calculation.",
    ),



    Question(

        question_code="COD-PYTHON-018",

        question=
        "Which keyword is used to handle exceptions in Python?",

        options=[
            "catch",
            "error",
            "try",
            "handle"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "try-except block is used for exception handling.",
    ),



    Question(

        question_code="COD-PYTHON-019",

        question=
        "Which method adds an element at the end of a Python list?",

        options=[
            "add()",
            "append()",
            "insertEnd()",
            "push()"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "append() adds an item to the end of a list.",
    ),



    Question(

        question_code="COD-PYTHON-020",

        question=
        "Which Python library is mainly used for numerical computations?",

        options=[
            "NumPy",
            "Django",
            "Flask",
            "Tkinter"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "NumPy is widely used for numerical and scientific computing.",
    ),



    # =====================================================
    # SQL PROGRAMMING (COD-SQL-001–010)
    # =====================================================


    Question(

        question_code="COD-SQL-001",

        question=
        "Which SQL command is used to retrieve data from a database?",

        options=[
            "GET",
            "SELECT",
            "FETCH",
            "RETRIEVE"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.SQL,

        explanation=
        "SELECT statement is used to retrieve data from database tables.",
    ),



    Question(

        question_code="COD-SQL-002",

        question=
        "Which SQL command is used to insert new records into a table?",

        options=[
            "ADD",
            "INSERT",
            "CREATE",
            "UPDATE"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.SQL,

        explanation=
        "INSERT INTO command adds new records to a table.",
    ),



    Question(

        question_code="COD-SQL-003",

        question=
        "Which SQL clause is used to filter rows?",

        options=[
            "ORDER BY",
            "GROUP BY",
            "WHERE",
            "HAVING"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.SQL,

        explanation=
        "WHERE clause filters records based on conditions.",
    ),



    Question(

        question_code="COD-SQL-004",

        question=
        "Which command is used to remove a table permanently?",

        options=[
            "DELETE",
            "REMOVE",
            "DROP",
            "CLEAR"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.SQL,

        explanation=
        "DROP TABLE removes the complete table structure and data.",
    ),



    Question(

        question_code="COD-SQL-005",

        question=
        "Which key uniquely identifies each record in a table?",

        options=[
            "Foreign Key",
            "Primary Key",
            "Candidate Key",
            "Super Key"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.SQL,

        explanation=
        "Primary key uniquely identifies each row in a table.",
    ),



    Question(

        question_code="COD-SQL-006",

        question=
        "Which SQL command is used to modify existing records?",

        options=[
            "CHANGE",
            "MODIFY",
            "UPDATE",
            "ALTER"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.SQL,

        explanation=
        "UPDATE command modifies existing data.",
    ),



    Question(

        question_code="COD-SQL-007",

        question=
        "Which function returns the number of rows in SQL?",

        options=[
            "SUM()",
            "COUNT()",
            "TOTAL()",
            "NUMBER()"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.SQL,

        explanation=
        "COUNT() returns the number of records.",
    ),



    Question(

        question_code="COD-SQL-008",

        question=
        "Which SQL clause is used to sort query results?",

        options=[
            "SORT BY",
            "ORDER BY",
            "ARRANGE BY",
            "GROUP BY"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.SQL,

        explanation=
        "ORDER BY sorts results in ascending or descending order.",
    ),



    Question(

        question_code="COD-SQL-009",

        question=
        "Which JOIN returns matching records from both tables?",

        options=[
            "LEFT JOIN",
            "RIGHT JOIN",
            "INNER JOIN",
            "FULL JOIN"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.SQL,

        explanation=
        "INNER JOIN returns records where matching values exist in both tables.",
    ),



    Question(

        question_code="COD-SQL-010",

        question=
        "Which command is used to create a new table in SQL?",

        options=[
            "MAKE TABLE",
            "CREATE TABLE",
            "NEW TABLE",
            "ADD TABLE"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.SQL,

        explanation=
        "CREATE TABLE command creates a new database table.",
    ),



    # =====================================================
    # DATA STRUCTURES & ALGORITHMS (COD-DSA-001–010)
    # =====================================================


    Question(

        question_code="COD-DSA-001",

        question=
        "Which data structure follows FIFO (First In First Out) principle?",

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
        "Queue follows FIFO principle where first inserted element is removed first.",
    ),



    Question(

        question_code="COD-DSA-002",

        question=
        "Which data structure follows LIFO (Last In First Out) principle?",

        options=[
            "Queue",
            "Stack",
            "Array",
            "Linked List"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Stack follows LIFO principle.",
    ),



    Question(

        question_code="COD-DSA-003",

        question=
        "What is the time complexity of binary search?",

        options=[
            "O(n)",
            "O(log n)",
            "O(n²)",
            "O(1)"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Binary search divides the search space into half each time.",
    ),



    Question(

        question_code="COD-DSA-004",

        question=
        "Which data structure is used in recursion internally?",

        options=[
            "Queue",
            "Stack",
            "Array",
            "Tree"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Function calls are stored in call stack during recursion.",
    ),



    Question(

        question_code="COD-DSA-005",

        question=
        "Which sorting algorithm has average time complexity O(n log n)?",

        options=[
            "Bubble Sort",
            "Selection Sort",
            "Merge Sort",
            "Linear Search"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Merge Sort divides array and merges sorted parts with O(n log n).",
    ),



    Question(

        question_code="COD-DSA-006",

        question=
        "Which traversal is used to visit nodes of a tree level by level?",

        options=[
            "DFS",
            "BFS",
            "Inorder",
            "Postorder"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Breadth First Search visits nodes level by level.",
    ),



    Question(

        question_code="COD-DSA-007",

        question=
        "Which data structure stores elements in contiguous memory locations?",

        options=[
            "Linked List",
            "Tree",
            "Array",
            "Graph"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Array elements are stored in continuous memory locations.",
    ),



    Question(

        question_code="COD-DSA-008",

        question=
        "What is the worst-case time complexity of linear search?",

        options=[
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n log n)"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Linear search checks each element one by one.",
    ),



    Question(

        question_code="COD-DSA-009",

        question=
        "Which data structure is used to represent hierarchical relationships?",

        options=[
            "Array",
            "Tree",
            "Queue",
            "Stack"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Tree represents hierarchical data like file systems.",
    ),



    Question(

        question_code="COD-DSA-010",

        question=
        "Which algorithm technique divides a problem into smaller subproblems?",

        options=[
            "Greedy",
            "Divide and Conquer",
            "Backtracking",
            "Brute Force"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Divide and Conquer breaks problems into smaller subproblems.",
    ),



    # =====================================================
    # OOPS / DBMS / OS / COMPUTER NETWORKS
    # (COD-TECH-001–010)
    # =====================================================


    Question(

        question_code="COD-TECH-001",

        question=
        "Which OOP concept allows one object to take many forms?",

        options=[
            "Encapsulation",
            "Inheritance",
            "Polymorphism",
            "Abstraction"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.OOP,

        explanation=
        "Polymorphism allows the same interface to behave differently.",
    ),



    Question(

        question_code="COD-TECH-002",

        question=
        "Which OOP concept hides internal implementation details?",

        options=[
            "Inheritance",
            "Encapsulation",
            "Polymorphism",
            "Overloading"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.OOP,

        explanation=
        "Encapsulation binds data and methods together and hides details.",
    ),



    Question(

        question_code="COD-TECH-003",

        question=
        "Which normal form removes partial dependency in DBMS?",

        options=[
            "1NF",
            "2NF",
            "3NF",
            "BCNF"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DBMS,

        explanation=
        "Second Normal Form removes partial dependency.",
    ),



    Question(

        question_code="COD-TECH-004",

        question=
        "Which SQL operation combines rows from multiple tables?",

        options=[
            "JOIN",
            "INSERT",
            "DELETE",
            "UPDATE"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DBMS,

        explanation=
        "JOIN combines related data from multiple tables.",
    ),



    Question(

        question_code="COD-TECH-005",

        question=
        "Which scheduling algorithm uses time quantum?",

        options=[
            "FCFS",
            "Round Robin",
            "Priority Scheduling",
            "SJF"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.OPERATING_SYSTEM,

        explanation=
        "Round Robin scheduling assigns fixed time quantum to processes.",
    ),



    Question(

        question_code="COD-TECH-006",

        question=
        "Which OS component manages memory allocation?",

        options=[
            "Compiler",
            "Memory Manager",
            "Loader",
            "Scheduler"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.OPERATING_SYSTEM,

        explanation=
        "Memory Manager handles allocation and deallocation of memory.",
    ),



    Question(

        question_code="COD-TECH-007",

        question=
        "Which protocol is used for transferring web pages?",

        options=[
            "FTP",
            "HTTP",
            "SMTP",
            "TCP"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.COMPUTER_NETWORK,

        explanation=
        "HTTP is used for communication between browser and web server.",
    ),



    Question(

        question_code="COD-TECH-008",

        question=
        "Which layer is responsible for routing in OSI model?",

        options=[
            "Transport Layer",
            "Network Layer",
            "Session Layer",
            "Data Link Layer"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.COMPUTER_NETWORK,

        explanation=
        "Network layer performs routing using IP addresses.",
    ),



    Question(

        question_code="COD-TECH-009",

        question=
        "Which key uniquely identifies a record in a database table?",

        options=[
            "Foreign Key",
            "Primary Key",
            "Alternate Key",
            "Composite Key"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DBMS,

        explanation=
        "Primary key uniquely identifies each row.",
    ),



    Question(

        question_code="COD-TECH-010",

        question=
        "Which OSI layer provides end-to-end communication?",

        options=[
            "Network Layer",
            "Transport Layer",
            "Physical Layer",
            "Application Layer"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.COMPUTER_NETWORK,

        explanation=
        "Transport layer provides reliable end-to-end communication.",
    ),



    # =====================================================
    # DEBUGGING / OUTPUT BASED QUESTIONS
    # (COD-DEBUG-001–010)
    # =====================================================


    Question(

        question_code="COD-DEBUG-001",

        question=
        "What will be the output?\n\nint x = 5; printf(\"%d\", x++);",

        options=[
            "5",
            "6",
            "4",
            "Error"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "Post increment uses the current value first, then increases it.",
    ),



    Question(

        question_code="COD-DEBUG-002",

        question=
        "What will be the output?\n\nint a=10; int b=20; printf(\"%d\", a+b);",

        options=[
            "20",
            "30",
            "40",
            "Error"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.C,

        explanation=
        "Addition of 10 and 20 gives 30.",
    ),



    Question(

        question_code="COD-DEBUG-003",

        question=
        "What will be the output?\n\nPython: print(2+3*4)",

        options=[
            "20",
            "14",
            "24",
            "10"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "Multiplication has higher priority: 3*4=12, then 2+12=14.",
    ),



    Question(

        question_code="COD-DEBUG-004",

        question=
        "What will be the output?\n\nJavaScript: console.log(typeof 10);",

        options=[
            "integer",
            "number",
            "float",
            "object"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.JAVASCRIPT,

        explanation=
        "JavaScript uses number type for integers and decimals.",
    ),



    Question(

        question_code="COD-DEBUG-005",

        question=
        "What will be the output?\n\nJava: int x=5; System.out.println(x++);",

        options=[
            "4",
            "5",
            "6",
            "Error"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.JAVA,

        explanation=
        "Post increment prints value first then increases it.",
    ),



    Question(

        question_code="COD-DEBUG-006",

        question=
        "Which error occurs when accessing an array index outside its range?",

        options=[
            "Syntax Error",
            "Runtime Error",
            "Logical Error",
            "Compilation Error"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Invalid array index causes runtime error.",
    ),



    Question(

        question_code="COD-DEBUG-007",

        question=
        "What is the output of: Python print(len('Talent'))",

        options=[
            "5",
            "6",
            "7",
            "Error"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.PYTHON,

        explanation=
        "Talent contains 6 characters.",
    ),



    Question(

        question_code="COD-DEBUG-008",

        question=
        "Which bug occurs when program runs but gives incorrect output?",

        options=[
            "Syntax Bug",
            "Logical Bug",
            "Runtime Bug",
            "Compiler Bug"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.DSA,

        explanation=
        "Logical errors produce wrong results while program executes.",
    ),



    Question(

        question_code="COD-DEBUG-009",

        question=
        "What will be output?\n\nSQL: SELECT COUNT(*) FROM Student;",

        options=[
            "Returns number of rows",
            "Deletes rows",
            "Updates rows",
            "Creates table"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.SQL,

        explanation=
        "COUNT(*) returns total number of records.",
    ),



    Question(

        question_code="COD-DEBUG-010",

        question=
        "Which tool is commonly used to find bugs in code?",

        options=[
            "Debugger",
            "Compiler",
            "Browser",
            "Database"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.CODING,

        topic=Topic.CPP,

        explanation=
        "Debugger helps identify and fix errors during execution.",
    ),


]

