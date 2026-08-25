from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


COLLEGE_COMMON_QUESTIONS: list[Question] = [

    # =====================================================
    # COLLEGE COMMON QUESTIONS (COLLEGE-COMMON-001–010)
    # =====================================================


    Question(

        question_code="COLLEGE-COMMON-001",

        question=
        "Which skill is most important for career growth in technology?",

        options=[
            "Continuous Learning",
            "Ignoring new technology",
            "Only theoretical knowledge",
            "Avoiding practice"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Continuous learning helps professionals adapt to new technologies.",
    ),



    Question(

        question_code="COLLEGE-COMMON-002",

        question=
        "Which document is commonly used to apply for jobs?",

        options=[
            "Resume",
            "Invoice",
            "Receipt",
            "Certificate only"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Resume contains education, skills and experience details.",
    ),



    Question(

        question_code="COLLEGE-COMMON-003",

        question=
        "What does GPA represent?",

        options=[
            "Grade Point Average",
            "General Program Access",
            "Global Performance Area",
            "Grade Percentage Amount"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.EDUCATION,

        explanation=
        "GPA represents the average grade points obtained by a student.",
    ),



    Question(

        question_code="COLLEGE-COMMON-004",

        question=
        "Which activity improves programming skills?",

        options=[
            "Regular Coding Practice",
            "Avoiding projects",
            "Only reading theory",
            "Skipping problems"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROGRAMMING,

        explanation=
        "Regular coding practice improves problem-solving ability.",
    ),



    Question(

        question_code="COLLEGE-COMMON-005",

        question=
        "Which platform is commonly used for version control?",

        options=[
            "GitHub",
            "MS Paint",
            "Calculator",
            "Notepad"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "GitHub hosts Git repositories and manages code versions.",
    ),



    Question(

        question_code="COLLEGE-COMMON-006",

        question=
        "Soft skills include:",

        options=[
            "Communication and teamwork",
            "Only programming",
            "Only mathematics",
            "Only hardware knowledge"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Soft skills improve communication and professional interaction.",
    ),



    Question(

        question_code="COLLEGE-COMMON-007",

        question=
        "Internships help students by providing:",

        options=[
            "Practical experience",
            "Only marks",
            "No learning",
            "Only certificates"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Internships provide real-world industry experience.",
    ),



    Question(

        question_code="COLLEGE-COMMON-008",

        question=
        "Which is important before a technical interview?",

        options=[
            "Practice and preparation",
            "Ignoring concepts",
            "No revision",
            "Avoiding questions"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Preparation improves confidence and interview performance.",
    ),



    Question(

        question_code="COLLEGE-COMMON-009",

        question=
        "A project portfolio helps to:",

        options=[
            "Show practical skills",
            "Replace learning",
            "Avoid coding",
            "Remove experience"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Portfolio demonstrates projects and technical abilities.",
    ),



    Question(

        question_code="COLLEGE-COMMON-010",

        question=
        "Problem solving ability is improved by:",

        options=[
            "Practice and logical thinking",
            "Memorizing only",
            "Avoiding challenges",
            "Skipping algorithms"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Regular practice develops logical thinking and problem-solving skills.",
    ),



    Question(
        question_code="COLLEGE-COMMON-011",
        question=
        "A Git commit is used to:",
        options=[
            "Record a set of repository changes",
            "Delete the repository",
            "Deploy hardware",
            "Create a database server",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "A commit records a snapshot of changes in version control.",
    ),

    Question(
        question_code="COLLEGE-COMMON-012",
        question=
        "Which HTTP method is commonly used to retrieve a resource?",
        options=[
            "GET",
            "POST",
            "PATCH",
            "DELETE",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "GET is intended for retrieving resources.",
    ),

    Question(
        question_code="COLLEGE-COMMON-013",
        question=
        "What does API stand for?",
        options=[
            "Application Programming Interface",
            "Applied Program Internet",
            "Application Process Input",
            "Automated Program Index",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "An API defines a programmatic interface for interacting with software.",
    ),

    Question(
        question_code="COLLEGE-COMMON-014",
        question=
        "Unit testing focuses on:",
        options=[
            "Small units of code",
            "Only the whole organization",
            "Network cables",
            "User salaries",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_TESTING,

        explanation=
        "Unit tests verify individual functions or components.",
    ),

    Question(
        question_code="COLLEGE-COMMON-015",
        question=
        "Which practice reduces merge conflicts in team development?",
        options=[
            "Frequent small commits and synchronization",
            "Long unshared branches forever",
            "Editing production only",
            "Avoiding version control",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Small frequent changes synchronized with the team reduce divergence.",
    ),

    Question(
        question_code="COLLEGE-COMMON-016",
        question=
        "A README file commonly explains:",
        options=[
            "How to understand and run a project",
            "CPU temperature",
            "Employee payroll",
            "Router firmware only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "README files document purpose, setup and usage.",
    ),

    Question(
        question_code="COLLEGE-COMMON-017",
        question=
        "Which model emphasizes short iterative development cycles?",
        options=[
            "Agile",
            "Waterfall only",
            "Big Bang",
            "Ad hoc",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Agile uses iterative and incremental development.",
    ),

    Question(
        question_code="COLLEGE-COMMON-018",
        question=
        "Code review is primarily used to:",
        options=[
            "Improve correctness, maintainability and knowledge sharing",
            "Replace all testing",
            "Increase file size",
            "Avoid collaboration",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Reviewers identify defects and improve code quality.",
    ),

    Question(
        question_code="COLLEGE-COMMON-019",
        question=
        "A REST API commonly identifies resources using:",
        options=[
            "URLs",
            "CPU registers",
            "Excel formulas",
            "Binary trees only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "REST resources are commonly addressed by URLs.",
    ),

    Question(
        question_code="COLLEGE-COMMON-020",
        question=
        "JSON is mainly used as a:",
        options=[
            "Data interchange format",
            "Programming language compiler",
            "Database engine",
            "Operating system",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "JSON is a lightweight structured data interchange format.",
    ),

    Question(
        question_code="COLLEGE-COMMON-021",
        question=
        "Which SQL statement retrieves rows?",
        options=[
            "SELECT",
            "INSERT",
            "UPDATE",
            "DROP",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SQL,

        explanation=
        "SELECT queries data from tables.",
    ),

    Question(
        question_code="COLLEGE-COMMON-022",
        question=
        "A primary key should:",
        options=[
            "Uniquely identify a row",
            "Contain duplicate values by design",
            "Always be a password",
            "Only store images",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "A primary key uniquely identifies each record.",
    ),

    Question(
        question_code="COLLEGE-COMMON-023",
        question=
        "Normalization in DBMS mainly reduces:",
        options=[
            "Redundancy and update anomalies",
            "Network bandwidth only",
            "CPU clock speed",
            "User count",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "Normalization organizes data to reduce redundancy and anomalies.",
    ),

    Question(
        question_code="COLLEGE-COMMON-024",
        question=
        "Which join returns matching rows from both tables?",
        options=[
            "INNER JOIN",
            "CROSS JOIN only",
            "FULL CARTESIAN only",
            "SELF JOIN only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "INNER JOIN returns rows satisfying the join condition.",
    ),

    Question(
        question_code="COLLEGE-COMMON-025",
        question=
        "A transaction property that ensures all-or-nothing behavior is:",
        options=[
            "Atomicity",
            "Availability",
            "Redundancy",
            "Partitioning",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "Atomicity means a transaction fully commits or fully rolls back.",
    ),

    Question(
        question_code="COLLEGE-COMMON-026",
        question=
        "Which structure stores key-value pairs in many languages?",
        options=[
            "Hash map",
            "Stack frame only",
            "Graph edge only",
            "Queue",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DSA,

        explanation=
        "Hash maps associate keys with values.",
    ),

    Question(
        question_code="COLLEGE-COMMON-027",
        question=
        "Big-O notation describes:",
        options=[
            "Asymptotic growth of resource usage",
            "Exact CPU temperature",
            "Variable names",
            "Network topology",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DSA,

        explanation=
        "Big-O expresses asymptotic upper growth.",
    ),

    Question(
        question_code="COLLEGE-COMMON-028",
        question=
        "A binary search requires data to be:",
        options=[
            "Ordered",
            "Encrypted",
            "Duplicated",
            "Stored only on disk",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SEARCHING,

        explanation=
        "Binary search relies on an ordered search space.",
    ),

    Question(
        question_code="COLLEGE-COMMON-029",
        question=
        "Which data structure is natural for breadth-first traversal?",
        options=[
            "Queue",
            "Stack",
            "Heap only",
            "Array only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DSA,

        explanation=
        "BFS processes vertices level by level using a queue.",
    ),

    Question(
        question_code="COLLEGE-COMMON-030",
        question=
        "Which skill is most useful when debugging an unfamiliar codebase?",
        options=[
            "Systematic problem decomposition",
            "Changing random lines",
            "Ignoring logs",
            "Deleting tests",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Decomposing the problem and using evidence makes debugging systematic.",
    ),

    Question(
        question_code="COLLEGE-COMMON-031",
        question=
        "A good internship project should demonstrate:",
        options=[
            "A clear problem, implementation and evidence of learning",
            "Only a fancy title",
            "Copied code without understanding",
            "No documentation",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Projects are strongest when they show meaningful work and understanding.",
    ),

    Question(
        question_code="COLLEGE-COMMON-032",
        question=
        "A resume bullet is stronger when it includes:",
        options=[
            "Action and measurable outcome",
            "Only a job title",
            "Long unrelated paragraphs",
            "Personal opinions only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.RESUME,

        explanation=
        "Action plus impact makes achievements concrete.",
    ),

    Question(
        question_code="COLLEGE-COMMON-033",
        question=
        "A technical interview usually evaluates:",
        options=[
            "Problem solving and technical understanding",
            "Only handwriting",
            "Only age",
            "Only social media followers",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.INTERVIEW,

        explanation=
        "Technical interviews commonly assess reasoning and technical knowledge.",
    ),

    Question(
        question_code="COLLEGE-COMMON-034",
        question=
        "Which is a good way to prepare for an interview?",
        options=[
            "Practice representative problems and explain reasoning",
            "Memorize answers without understanding",
            "Skip project review",
            "Avoid asking questions",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.INTERVIEW,

        explanation=
        "Practice plus explanation builds transferable interview skill.",
    ),

    Question(
        question_code="COLLEGE-COMMON-035",
        question=
        "A portfolio is useful because it can:",
        options=[
            "Provide evidence of skills through projects",
            "Replace all learning",
            "Guarantee a job",
            "Hide experience",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "A portfolio demonstrates practical work.",
    ),

    Question(
        question_code="COLLEGE-COMMON-036",
        question=
        "Which goal is measurable?",
        options=[
            "Learn coding someday",
            "Solve 50 practice problems this month",
            "Become better",
            "Study more",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "A numeric target can be tracked.",
    ),

    Question(
        question_code="COLLEGE-COMMON-037",
        question=
        "Technical debt refers to:",
        options=[
            "Future cost created by expedient technical choices",
            "A bank loan",
            "Cloud billing only",
            "Employee salary",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Technical debt is the future maintenance cost of shortcuts.",
    ),

    Question(
        question_code="COLLEGE-COMMON-038",
        question=
        "Continuous integration means:",
        options=[
            "Frequently integrating and testing changes",
            "Deploying once a year",
            "Avoiding automated tests",
            "Only manual coding",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "CI integrates changes frequently with automated validation.",
    ),

    Question(
        question_code="COLLEGE-COMMON-039",
        question=
        "A container image packages:",
        options=[
            "Application and its required runtime components",
            "Only a monitor",
            "Only source comments",
            "A physical server",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "Container images package software and its runtime dependencies.",
    ),

    Question(
        question_code="COLLEGE-COMMON-040",
        question=
        "Which practice protects secrets in software projects?",
        options=[
            "Use environment/secret management instead of committing keys",
            "Commit API keys to Git",
            "Put passwords in screenshots",
            "Share keys in README",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Secrets should be stored in secure secret-management systems.",
    ),

    Question(
        question_code="COLLEGE-COMMON-041",
        question=
        "A firewall primarily controls:",
        options=[
            "Network traffic based on rules",
            "CPU scheduling",
            "Database normalization",
            "Source formatting",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Firewalls filter network traffic according to configured rules.",
    ),

    Question(
        question_code="COLLEGE-COMMON-042",
        question=
        "What does DNS primarily resolve?",
        options=[
            "Domain names to network addresses",
            "Passwords to hashes",
            "SQL to Python",
            "Images to CSS",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER_NETWORK,

        explanation=
        "DNS maps domain names to IP addresses and related records.",
    ),

    Question(
        question_code="COLLEGE-COMMON-043",
        question=
        "TCP provides:",
        options=[
            "Reliable ordered byte-stream delivery",
            "Only broadcast video",
            "No sequencing",
            "Only local storage",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMPUTER_NETWORK,

        explanation=
        "TCP provides reliable ordered delivery with retransmission.",
    ),

    Question(
        question_code="COLLEGE-COMMON-044",
        question=
        "A process is:",
        options=[
            "A running instance of a program",
            "A source-code comment",
            "A database column",
            "A network cable",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OPERATING_SYSTEM,

        explanation=
        "A process is a program in execution.",
    ),

    Question(
        question_code="COLLEGE-COMMON-045",
        question=
        "A thread is generally:",
        options=[
            "A unit of execution within a process",
            "A hard disk partition",
            "A database table",
            "A compiler",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OPERATING_SYSTEM,

        explanation=
        "Threads are execution units within a process.",
    ),

    Question(
        question_code="COLLEGE-COMMON-046",
        question=
        "Encapsulation in OOP means:",
        options=[
            "Bundling data with methods and controlling access",
            "Multiple inheritance only",
            "Sorting objects",
            "Encrypting every file",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OOP,

        explanation=
        "Encapsulation bundles state and behavior while controlling access.",
    ),

    Question(
        question_code="COLLEGE-COMMON-047",
        question=
        "Polymorphism allows:",
        options=[
            "A common interface to have different implementations",
            "Only one class in a program",
            "No inheritance",
            "Only static data",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.OOP,

        explanation=
        "Polymorphism lets code use a common interface with varied implementations.",
    ),

    Question(
        question_code="COLLEGE-COMMON-048",
        question=
        "A software requirement should ideally be:",
        options=[
            "Clear and testable",
            "Ambiguous",
            "Impossible to verify",
            "Only verbal",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_ENGINEERING,

        explanation=
        "Good requirements are understandable and verifiable.",
    ),

    Question(
        question_code="COLLEGE-COMMON-049",
        question=
        "Version control provides:",
        options=[
            "History and collaboration around source changes",
            "Only antivirus protection",
            "Only cloud storage",
            "Only code compilation",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Version control tracks changes and supports collaboration.",
    ),

    Question(
        question_code="COLLEGE-COMMON-050",
        question=
        "A dependency lock file helps ensure:",
        options=[
            "Consistent dependency versions across environments",
            "Faster internet",
            "More RAM",
            "No source control",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Lock files record resolved dependency versions for reproducible installs.",
    ),
]