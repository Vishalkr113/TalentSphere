from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


PROFESSIONAL_TECHNICAL_QUESTIONS: list[Question] = [

    # =====================================================
    # PROFESSIONAL TECHNICAL (PROFESSIONAL-TECH-001–010)
    # =====================================================


    Question(

        question_code="PROFESSIONAL-TECH-001",

        question=
        "Which programming paradigm does Java mainly support?",

        options=[
            "Object-Oriented Programming",
            "Only Functional Programming",
            "Markup Programming",
            "Database Programming"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROGRAMMING,

        explanation=
        "Java is mainly based on Object-Oriented Programming concepts.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-002",

        question=
        "Which principle hides internal details of an object?",

        options=[
            "Encapsulation",
            "Inheritance",
            "Polymorphism",
            "Compilation"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.OOP,

        explanation=
        "Encapsulation hides data and implementation details.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-003",

        question=
        "Which database language is used to manage relational databases?",

        options=[
            "SQL",
            "HTML",
            "CSS",
            "XML"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DBMS,

        explanation=
        "SQL is used for managing relational database systems.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-004",

        question=
        "Which HTTP method is commonly used to retrieve data?",

        options=[
            "POST",
            "GET",
            "DELETE",
            "PATCH"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "GET method is used to request and retrieve data.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-005",

        question=
        "Which technology is used for containerization?",

        options=[
            "Docker",
            "Excel",
            "Photoshop",
            "Notepad"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "Docker is a popular containerization platform.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-006",

        question=
        "Which version control system is widely used in software development?",

        options=[
            "Git",
            "Paint",
            "Word",
            "Calculator"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Git is used for tracking code changes.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-007",

        question=
        "Which data structure is used for implementing BFS?",

        options=[
            "Stack",
            "Queue",
            "Heap",
            "Array"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.DSA,

        explanation=
        "BFS uses Queue for level-wise traversal.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-008",

        question=
        "Which cloud service model provides virtual machines?",

        options=[
            "IaaS",
            "SaaS",
            "PaaS",
            "DBaaS"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "Infrastructure as a Service provides virtualized computing resources.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-009",

        question=
        "Which testing checks individual software components?",

        options=[
            "Unit Testing",
            "System Testing",
            "Performance Testing",
            "Security Testing"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_TESTING,

        explanation=
        "Unit testing verifies individual modules or components.",
    ),



    Question(

        question_code="PROFESSIONAL-TECH-010",

        question=
        "API stands for:",

        options=[
            "Application Programming Interface",
            "Advanced Program Internet",
            "Application Process Integration",
            "Automatic Programming Input"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "API allows communication between different software systems.",
    ),



    Question(
        question_code="PROFESSIONAL-TECH-011",
        question=
        "A production API should validate input primarily to:",
        options=[
            "Prevent invalid or malicious data from reaching business logic",
            "Make UI prettier",
            "Increase font size",
            "Replace authentication",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Input validation protects correctness and reduces attack surface.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-012",
        question=
        "Rate limiting helps protect an API from:",
        options=[
            "Abusive request volume",
            "SQL joins",
            "Disk fragmentation",
            "CSS errors",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Rate limits constrain request frequency.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-013",
        question=
        "A cache is most useful when:",
        options=[
            "Data is read frequently and changes less often",
            "Every value is unique and never reused",
            "Consistency is irrelevant always",
            "Storage is unlimited",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SYSTEM_DESIGN,

        explanation=
        "Caching reduces repeated expensive reads when reuse is high.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-014",
        question=
        "A circuit breaker helps:",
        options=[
            "Prevent repeated calls to a failing dependency",
            "Encrypt databases",
            "Compile code",
            "Normalize tables",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SYSTEM_DESIGN,

        explanation=
        "Circuit breakers stop cascading failures by temporarily rejecting calls.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-015",
        question=
        "Horizontal scaling adds:",
        options=[
            "More instances",
            "More CPU to one instance only",
            "More SQL columns",
            "More passwords",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "Horizontal scaling increases capacity by adding instances.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-016",
        question=
        "Autoscaling typically responds to:",
        options=[
            "Load or resource metrics",
            "Source comments",
            "Git commit messages only",
            "User passwords",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "Autoscaling policies use observed metrics to adjust capacity.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-017",
        question=
        "A blue-green deployment uses:",
        options=[
            "Two production environments to reduce deployment risk",
            "Only one server",
            "No rollback path",
            "Only local builds",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Traffic can switch between two environments, enabling quick rollback.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-018",
        question=
        "Observability commonly includes:",
        options=[
            "Logs, metrics and traces",
            "Only screenshots",
            "Only source code",
            "Only backups",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "These signals help understand system behavior.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-019",
        question=
        "A distributed trace helps identify:",
        options=[
            "Where latency or errors occur across services",
            "Which user is richest",
            "Database schema only",
            "CSS color",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Traces follow a request across service boundaries.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-020",
        question=
        "A secret manager is preferable to:",
        options=[
            "Hard-coding credentials in source",
            "Environment-specific secret storage",
            "Access controls",
            "Rotation",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Secrets should not be embedded in source code.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-021",
        question=
        "Encryption at rest protects:",
        options=[
            "Stored data",
            "Only network traffic",
            "CPU scheduling",
            "Source formatting",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "At-rest encryption protects stored data if storage is accessed.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-022",
        question=
        "TLS protects data primarily:",
        options=[
            "In transit",
            "Only in RAM",
            "Only after deletion",
            "Only in source code",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "TLS secures network communication.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-023",
        question=
        "An access token should be:",
        options=[
            "Scoped and time-limited where appropriate",
            "Permanent and public",
            "Shared among users",
            "Stored in logs",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Least privilege and limited lifetime reduce token risk.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-024",
        question=
        "A database connection pool improves:",
        options=[
            "Reuse and management of database connections",
            "SQL syntax",
            "Password strength",
            "Disk capacity",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "Pools reuse established connections and bound concurrency.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-025",
        question=
        "Read replicas are useful for:",
        options=[
            "Scaling read workloads",
            "Guaranteeing zero latency",
            "Replacing backups",
            "Writing faster to one primary",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "Replicas can distribute read traffic.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-026",
        question=
        "A database transaction should be short when possible because:",
        options=[
            "Long transactions can hold locks and resources",
            "Short queries are always more correct",
            "It increases RAM",
            "It removes indexes",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "Short transactions reduce contention and resource retention.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-027",
        question=
        "An index can improve reads but may:",
        options=[
            "Increase write/storage overhead",
            "Eliminate all storage",
            "Remove constraints",
            "Guarantee every query is faster",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "Indexes require maintenance and storage and can slow writes.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-028",
        question=
        "A message queue provides:",
        options=[
            "Buffering and asynchronous decoupling",
            "Direct UI rendering",
            "Database normalization",
            "CPU instructions",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SYSTEM_DESIGN,

        explanation=
        "Queues decouple producers and consumers.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-029",
        question=
        "Eventual consistency means replicas may:",
        options=[
            "Temporarily disagree before converging",
            "Never converge",
            "Always be identical instantly",
            "Have no data",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SYSTEM_DESIGN,

        explanation=
        "Replicas can converge after propagation delay.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-030",
        question=
        "A unique constraint ensures:",
        options=[
            "No duplicate values for the constrained key",
            "Every value is null",
            "All rows are sorted",
            "Queries never fail",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "Unique constraints enforce uniqueness.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-031",
        question=
        "A service health check should be:",
        options=[
            "Fast and representative of service readiness",
            "A full database backup",
            "A long report",
            "A user login",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Health checks should be lightweight and meaningful.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-032",
        question=
        "A liveness check asks whether:",
        options=[
            "The process should be restarted if it cannot function",
            "A user has paid",
            "A query is indexed",
            "A deployment is pretty",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Liveness indicates whether restarting may recover the process.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-033",
        question=
        "A readiness check asks whether:",
        options=[
            "The instance can receive traffic",
            "The source code is open",
            "The database is normalized to 5NF",
            "A user is an admin",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Readiness controls whether traffic should be sent to an instance.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-034",
        question=
        "Least privilege is a principle of:",
        options=[
            "Security",
            "Compression",
            "Sorting",
            "Rendering",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Least privilege limits access to necessary permissions.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-035",
        question=
        "Defense in depth means:",
        options=[
            "Using multiple complementary security controls",
            "Using one perfect control",
            "Disabling logs",
            "Avoiding backups",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Layered controls reduce reliance on a single defense.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-036",
        question=
        "A dependency vulnerability should be handled by:",
        options=[
            "Assessing impact and upgrading/remediating appropriately",
            "Ignoring all alerts",
            "Deleting security tooling",
            "Publishing credentials",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Dependency vulnerabilities require risk assessment and remediation.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-037",
        question=
        "A rollback plan is important because:",
        options=[
            "Deployments can introduce unexpected failures",
            "All releases fail",
            "Testing is useless",
            "Users prefer old logos",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Rollback limits impact when a release causes problems.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-038",
        question=
        "A canary release sends:",
        options=[
            "A small portion of traffic to the new version",
            "All traffic immediately",
            "No traffic",
            "Only database writes",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Canarying limits blast radius while monitoring.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-039",
        question=
        "Idempotency keys are useful for:",
        options=[
            "Preventing duplicate effects from retried requests",
            "Faster CSS",
            "Sorting arrays",
            "Password hashing",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "They let servers recognize repeated attempts of the same operation.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-040",
        question=
        "Pagination helps APIs:",
        options=[
            "Limit response size for large collections",
            "Encrypt requests",
            "Remove authentication",
            "Replace indexes",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "Pagination prevents excessively large responses.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-041",
        question=
        "A cursor-based pagination scheme is often useful when:",
        options=[
            "Data changes and stable traversal is needed",
            "Only five rows exist",
            "No ordering exists",
            "All data is static forever",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "Cursors can provide more stable traversal than offsets under changes.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-042",
        question=
        "A webhook is typically:",
        options=[
            "An HTTP callback triggered by an event",
            "A database index",
            "A CPU interrupt only",
            "A CSS component",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "Webhooks deliver event notifications to a configured endpoint.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-043",
        question=
        "A reverse proxy can provide:",
        options=[
            "Routing, TLS termination and load balancing",
            "Only SQL joins",
            "Only source formatting",
            "Only file compression",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.WEB_DEVELOPMENT,

        explanation=
        "Reverse proxies commonly handle these edge responsibilities.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-044",
        question=
        "A CDN primarily improves delivery of:",
        options=[
            "Cacheable content closer to users",
            "Database transactions",
            "CPU instructions",
            "Private keys",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "CDNs cache and serve content from edge locations.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-045",
        question=
        "Object storage is suited to:",
        options=[
            "Files and large unstructured objects",
            "CPU registers",
            "Thread stacks",
            "SQL joins only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "Object storage handles blobs such as images and documents.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-046",
        question=
        "A backup is different from a replica because a backup:",
        options=[
            "Provides a recovery copy independent of live state",
            "Always serves traffic",
            "Replaces authentication",
            "Must be in memory",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CLOUD_COMPUTING,

        explanation=
        "Backups support recovery from deletion, corruption or other failures.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-047",
        question=
        "A zero-trust approach assumes:",
        options=[
            "Requests should be verified rather than trusted by network location",
            "Internal networks are always safe",
            "Passwords are unnecessary",
            "Encryption is forbidden",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Zero trust continuously verifies identity and authorization.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-048",
        question=
        "A secure software supply chain should include:",
        options=[
            "Dependency verification and controlled builds",
            "Unknown binaries from anywhere",
            "Shared credentials",
            "No provenance",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Supply-chain security depends on provenance and controlled dependencies.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-049",
        question=
        "A service-level objective defines:",
        options=[
            "A target level of reliability/performance",
            "A programming language",
            "A database row",
            "A password policy only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SYSTEM_DESIGN,

        explanation=
        "SLOs specify measurable service targets.",
    ),

    Question(
        question_code="PROFESSIONAL-TECH-050",
        question=
        "A bulkhead pattern helps by:",
        options=[
            "Isolating resource pools so one failure does not exhaust all capacity",
            "Encrypting all data",
            "Replacing caches",
            "Removing monitoring",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SYSTEM_DESIGN,

        explanation=
        "Bulkheads limit blast radius by isolating resources.",
    ),
]