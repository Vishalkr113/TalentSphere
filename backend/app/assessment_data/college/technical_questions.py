from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


COLLEGE_TECHNICAL_QUESTIONS: list[Question] = [

    # =====================================================
    # COLLEGE TECHNICAL (COLLEGE-TECH-001–010)
    # =====================================================


    Question(

        question_code="COLLEGE-TECH-001",

        question=
        "Which data structure follows LIFO principle?",

        options=[
            "Queue",
            "Stack",
            "Tree",
            "Graph"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Stack follows Last In First Out principle.",
    ),



    Question(

        question_code="COLLEGE-TECH-002",

        question=
        "Which OOP concept allows code reusability?",

        options=[
            "Inheritance",
            "Encapsulation",
            "Abstraction",
            "Polymorphism"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.OOP,

        explanation=
        "Inheritance allows one class to reuse properties of another class.",
    ),



    Question(

        question_code="COLLEGE-TECH-003",

        question=
        "Which SQL command is used to retrieve data?",

        options=[
            "INSERT",
            "SELECT",
            "UPDATE",
            "DELETE"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DBMS,

        explanation=
        "SELECT command retrieves records from database tables.",
    ),



    Question(

        question_code="COLLEGE-TECH-004",

        question=
        "Which normal form removes partial dependency?",

        options=[
            "1NF",
            "2NF",
            "3NF",
            "BCNF"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DBMS,

        explanation=
        "Second Normal Form removes partial dependency.",
    ),



    Question(

        question_code="COLLEGE-TECH-005",

        question=
        "Which protocol is used for secure web communication?",

        options=[
            "HTTP",
            "HTTPS",
            "FTP",
            "SMTP"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.COMPUTER_NETWORK,

        explanation=
        "HTTPS provides secure communication using encryption.",
    ),



    Question(

        question_code="COLLEGE-TECH-006",

        question=
        "Which OS component manages process scheduling?",

        options=[
            "Compiler",
            "Scheduler",
            "Loader",
            "Editor"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.OPERATING_SYSTEM,

        explanation=
        "Scheduler decides which process gets CPU time.",
    ),



    Question(

        question_code="COLLEGE-TECH-007",

        question=
        "Which algorithm is used for shortest path finding?",

        options=[
            "Dijkstra",
            "Bubble Sort",
            "Binary Search",
            "DFS only"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "Dijkstra algorithm finds shortest path from source node.",
    ),



    Question(

        question_code="COLLEGE-TECH-008",

        question=
        "Which language is known as an object-oriented programming language?",

        options=[
            "HTML",
            "Java",
            "SQL",
            "CSS"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROGRAMMING,

        explanation=
        "Java supports object-oriented programming concepts.",
    ),



    Question(

        question_code="COLLEGE-TECH-009",

        question=
        "Which memory is fastest in computer hierarchy?",

        options=[
            "Hard Disk",
            "RAM",
            "Cache Memory",
            "DVD"
        ],

        answer="C",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.COMPUTER_ARCHITECTURE,

        explanation=
        "Cache memory is faster than RAM and storage devices.",
    ),



    Question(

        question_code="COLLEGE-TECH-010",

        question=
        "Which technology is used for version control?",

        options=[
            "Git",
            "Excel",
            "PowerPoint",
            "Photoshop"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Git is a distributed version control system.",
    ),



    Question(
        question_code="COLLEGE-TECH-011",
        question=
        "Which normal form removes partial dependency on a composite key?",
        options=[
            "1NF",
            "2NF",
            "3NF",
            "BCNF",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "Second normal form removes partial dependency on a composite key.",
    ),

    Question(
        question_code="COLLEGE-TECH-012",
        question=
        "Which index is often useful for equality and range lookups?",
        options=[
            "B-tree style index",
            "Plain text file only",
            "Audio index",
            "Screenshot",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "B-tree indexes efficiently support many equality and range queries.",
    ),

    Question(
        question_code="COLLEGE-TECH-013",
        question=
        "A foreign key primarily enforces:",
        options=[
            "Referential integrity",
            "CPU scheduling",
            "Encryption",
            "Compression",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "Foreign keys constrain references between related tables.",
    ),

    Question(
        question_code="COLLEGE-TECH-014",
        question=
        "Which SQL clause filters groups after aggregation?",
        options=[
            "WHERE",
            "HAVING",
            "ORDER BY",
            "FROM",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SQL,

        explanation=
        "HAVING filters grouped results after aggregation.",
    ),

    Question(
        question_code="COLLEGE-TECH-015",
        question=
        "Which SQL aggregate counts rows?",
        options=[
            "COUNT",
            "ROUND",
            "CONCAT",
            "CAST",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SQL,

        explanation=
        "COUNT returns the number of rows/values according to its form.",
    ),

    Question(
        question_code="COLLEGE-TECH-016",
        question=
        "A deadlock requires processes to be waiting in a:",
        options=[
            "Cycle",
            "Straight line only",
            "Tree with no cycles",
            "Single queue only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OPERATING_SYSTEM,

        explanation=
        "Deadlock involves a circular wait among processes/resources.",
    ),

    Question(
        question_code="COLLEGE-TECH-017",
        question=
        "Round-robin scheduling uses:",
        options=[
            "Time quantum",
            "Only priority values",
            "No preemption",
            "Disk blocks",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OPERATING_SYSTEM,

        explanation=
        "Round-robin gives each runnable process a time slice.",
    ),

    Question(
        question_code="COLLEGE-TECH-018",
        question=
        "Virtual memory allows a system to:",
        options=[
            "Use secondary storage to extend apparent memory",
            "Remove all RAM",
            "Disable processes",
            "Eliminate addresses",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OPERATING_SYSTEM,

        explanation=
        "Virtual memory provides an abstraction of larger memory using storage.",
    ),

    Question(
        question_code="COLLEGE-TECH-019",
        question=
        "A page fault occurs when:",
        options=[
            "A referenced page is not currently in physical memory",
            "CPU overheats",
            "A file is deleted",
            "A packet is lost",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OPERATING_SYSTEM,

        explanation=
        "A page fault occurs when a needed virtual page is absent from RAM.",
    ),

    Question(
        question_code="COLLEGE-TECH-020",
        question=
        "Context switching changes the CPU from:",
        options=[
            "One execution context to another",
            "One database to another",
            "One monitor to another",
            "One password to another",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OPERATING_SYSTEM,

        explanation=
        "The OS saves and restores execution state during a context switch.",
    ),

    Question(
        question_code="COLLEGE-TECH-021",
        question=
        "Which protocol translates private addresses for outbound network traffic?",
        options=[
            "NAT",
            "DNS",
            "FTP",
            "ARP only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER_NETWORK,

        explanation=
        "Network Address Translation maps private and public address spaces.",
    ),

    Question(
        question_code="COLLEGE-TECH-022",
        question=
        "Which device forwards packets between networks?",
        options=[
            "Router",
            "Switch only",
            "Keyboard",
            "Printer",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER_NETWORK,

        explanation=
        "Routers forward packets between IP networks.",
    ),

    Question(
        question_code="COLLEGE-TECH-023",
        question=
        "TLS is mainly used to provide:",
        options=[
            "Encrypted and authenticated communication",
            "Faster sorting",
            "Database joins",
            "CPU scheduling",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER_NETWORK,

        explanation=
        "TLS protects data in transit and authenticates endpoints.",
    ),

    Question(
        question_code="COLLEGE-TECH-024",
        question=
        "A subnet mask helps determine:",
        options=[
            "Network and host portions of an IP address",
            "CPU cache size",
            "SQL indexes",
            "File permissions",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER_NETWORK,

        explanation=
        "Subnet masks divide IP addresses into network and host portions.",
    ),

    Question(
        question_code="COLLEGE-TECH-025",
        question=
        "HTTP status 404 usually means:",
        options=[
            "Resource not found",
            "Success",
            "Server started",
            "Unauthorized only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "404 indicates the requested resource could not be found.",
    ),

    Question(
        question_code="COLLEGE-TECH-026",
        question=
        "Which HTTP status commonly indicates successful creation?",
        options=[
            "200",
            "201",
            "301",
            "500",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "201 Created indicates a resource was successfully created.",
    ),

    Question(
        question_code="COLLEGE-TECH-027",
        question=
        "Dependency injection helps by:",
        options=[
            "Providing dependencies from outside a component",
            "Encrypting source code",
            "Replacing testing",
            "Removing interfaces",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OOP,

        explanation=
        "Dependency injection separates construction from use and improves testability.",
    ),

    Question(
        question_code="COLLEGE-TECH-028",
        question=
        "An interface in OOP commonly defines:",
        options=[
            "A contract of operations",
            "Only database rows",
            "Only memory addresses",
            "A network route",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OOP,

        explanation=
        "Interfaces specify operations a class can provide.",
    ),

    Question(
        question_code="COLLEGE-TECH-029",
        question=
        "Method overriding occurs when a subclass:",
        options=[
            "Provides a new implementation of an inherited method",
            "Creates a database",
            "Deletes a parent",
            "Changes a variable type only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OOP,

        explanation=
        "Overriding replaces inherited behavior with a subclass implementation.",
    ),

    Question(
        question_code="COLLEGE-TECH-030",
        question=
        "Composition models a:",
        options=[
            "Has-a relationship",
            "Is-a relationship only",
            "Database lock",
            "Network hop",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OOP,

        explanation=
        "Composition represents objects containing/using other objects.",
    ),

    Question(
        question_code="COLLEGE-TECH-031",
        question=
        "A compiler typically converts:",
        options=[
            "Source code to a lower-level executable/bytecode form",
            "Database rows to images",
            "HTML to electricity",
            "RAM to disk",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROGRAMMING,

        explanation=
        "Compilers translate source programs into executable or intermediate representations.",
    ),

    Question(
        question_code="COLLEGE-TECH-032",
        question=
        "A stack overflow can result from:",
        options=[
            "Unbounded recursion",
            "A valid loop with no calls",
            "A database index",
            "A network packet",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROGRAMMING,

        explanation=
        "Deep or unbounded recursion can exhaust the call stack.",
    ),

    Question(
        question_code="COLLEGE-TECH-033",
        question=
        "Which testing type checks interactions between components?",
        options=[
            "Integration testing",
            "Unit testing only",
            "Load testing only",
            "Static typing",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_TESTING,

        explanation=
        "Integration tests verify component interactions.",
    ),

    Question(
        question_code="COLLEGE-TECH-034",
        question=
        "Regression testing checks that:",
        options=[
            "Existing behavior still works after changes",
            "Only new code compiles",
            "Users are online",
            "Hardware is new",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_TESTING,

        explanation=
        "Regression testing catches unintended breakage from changes.",
    ),

    Question(
        question_code="COLLEGE-TECH-035",
        question=
        "Cyclomatic complexity is related to:",
        options=[
            "Number of independent control-flow paths",
            "Database size",
            "Network speed",
            "RAM capacity",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_ENGINEERING,

        explanation=
        "Cyclomatic complexity measures control-flow complexity.",
    ),

    Question(
        question_code="COLLEGE-TECH-036",
        question=
        "A sequence diagram mainly shows:",
        options=[
            "Interactions between actors/objects over time",
            "Database normalization",
            "Disk partitions",
            "CPU voltage",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_ENGINEERING,

        explanation=
        "Sequence diagrams model message interactions in time order.",
    ),

    Question(
        question_code="COLLEGE-TECH-037",
        question=
        "Cache memory is used mainly to:",
        options=[
            "Reduce average data access latency",
            "Increase disk size",
            "Replace source code",
            "Store passwords only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER_ARCHITECTURE,

        explanation=
        "Caches keep frequently accessed data closer to the CPU.",
    ),

    Question(
        question_code="COLLEGE-TECH-038",
        question=
        "An instruction pipeline improves performance by:",
        options=[
            "Overlapping stages of instruction processing",
            "Removing the CPU",
            "Disabling memory",
            "Increasing file size",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER_ARCHITECTURE,

        explanation=
        "Pipelining overlaps instruction stages to increase throughput.",
    ),

    Question(
        question_code="COLLEGE-TECH-039",
        question=
        "RISC architectures generally favor:",
        options=[
            "A smaller set of simple instructions",
            "Only one instruction",
            "No registers",
            "Only interpreted code",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER_ARCHITECTURE,

        explanation=
        "RISC emphasizes a relatively small set of simple instructions.",
    ),

    Question(
        question_code="COLLEGE-TECH-040",
        question=
        "A database view is:",
        options=[
            "A virtual table defined by a query",
            "A physical CPU cache",
            "A password file",
            "A network cable",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "A view presents query results as a virtual table.",
    ),

    Question(
        question_code="COLLEGE-TECH-041",
        question=
        "A transaction isolation level controls:",
        options=[
            "Visibility of concurrent transaction effects",
            "File compression",
            "CPU clock",
            "Password length",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "Isolation controls how concurrent transactions interact.",
    ),

    Question(
        question_code="COLLEGE-TECH-042",
        question=
        "Which operation can prevent SQL injection when binding user input?",
        options=[
            "Parameterized queries",
            "String concatenation",
            "Ignoring validation",
            "Dynamic SQL with raw input",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Parameterized queries separate SQL code from user data.",
    ),

    Question(
        question_code="COLLEGE-TECH-043",
        question=
        "Hashing passwords should use:",
        options=[
            "A password-hashing algorithm with a unique salt",
            "Plain text",
            "Base64 only",
            "A reversible cipher only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Password hashing should be slow, salted and designed for passwords.",
    ),

    Question(
        question_code="COLLEGE-TECH-044",
        question=
        "Least privilege means:",
        options=[
            "Granting only the access required",
            "Giving everyone admin rights",
            "Removing authentication",
            "Sharing one account",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Least privilege limits permissions to what is necessary.",
    ),

    Question(
        question_code="COLLEGE-TECH-045",
        question=
        "A load balancer distributes:",
        options=[
            "Requests across service instances",
            "Database passwords",
            "CPU instructions only",
            "Source comments",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "Load balancers distribute traffic among healthy backends.",
    ),

    Question(
        question_code="COLLEGE-TECH-046",
        question=
        "Horizontal scaling means:",
        options=[
            "Adding more service instances",
            "Making one server larger only",
            "Reducing users",
            "Deleting replicas",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "Horizontal scaling adds instances to handle more load.",
    ),

    Question(
        question_code="COLLEGE-TECH-047",
        question=
        "A queue is useful for:",
        options=[
            "Asynchronous work processing",
            "Only sorting arrays",
            "Only encryption",
            "Only HTML rendering",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SYSTEM_DESIGN,

        explanation=
        "Queues decouple producers and consumers for asynchronous processing.",
    ),

    Question(
        question_code="COLLEGE-TECH-048",
        question=
        "Idempotent operations can be safely repeated with:",
        options=[
            "The same intended final effect",
            "Guaranteed duplication",
            "No validation",
            "Different semantics every time",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "An idempotent operation has the same intended effect when repeated.",
    ),

    Question(
        question_code="COLLEGE-TECH-049",
        question=
        "CAP theorem concerns trade-offs among:",
        options=[
            "Consistency, availability and partition tolerance",
            "CPU, API and power",
            "Caching, authentication and parsing",
            "Code, assets and pages",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SYSTEM_DESIGN,

        explanation=
        "CAP describes distributed-system trade-offs under network partition.",
    ),

    Question(
        question_code="COLLEGE-TECH-050",
        question=
        "A message broker is commonly used to:",
        options=[
            "Decouple producers and consumers",
            "Replace all databases",
            "Compile JavaScript",
            "Format CSS",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SYSTEM_DESIGN,

        explanation=
        "Message brokers buffer and route messages between producers and consumers.",
    ),
]