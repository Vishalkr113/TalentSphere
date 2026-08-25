from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


COLLEGE_CAREER_QUESTIONS: list[Question] = [

    # =====================================================
    # COLLEGE CAREER (COLLEGE-CAREER-001–010)
    # =====================================================


    Question(

        question_code="COLLEGE-CAREER-001",

        question=
        "Which platform is commonly used for professional networking?",

        options=[
            "LinkedIn",
            "Calculator",
            "Paint",
            "Notepad"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "LinkedIn is a professional networking platform.",
    ),



    Question(

        question_code="COLLEGE-CAREER-002",

        question=
        "A good resume should mainly contain:",

        options=[
            "Skills and achievements",
            "Only personal photos",
            "Random information",
            "Unrelated details"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Resume should highlight education, skills and achievements.",
    ),



    Question(

        question_code="COLLEGE-CAREER-003",

        question=
        "Which skill is important for software developers?",

        options=[
            "Problem Solving",
            "Ignoring errors",
            "Avoiding practice",
            "No communication"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Problem solving is a core skill for software development.",
    ),



    Question(

        question_code="COLLEGE-CAREER-004",

        question=
        "Mock interviews help students to:",

        options=[
            "Improve interview confidence",
            "Avoid preparation",
            "Remove skills",
            "Skip learning"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Mock interviews improve communication and confidence.",
    ),



    Question(

        question_code="COLLEGE-CAREER-005",

        question=
        "Which is important for career growth?",

        options=[
            "Learning new skills",
            "Stopping improvement",
            "Ignoring technology",
            "Avoiding projects"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Continuous skill development helps career growth.",
    ),



    Question(

        question_code="COLLEGE-CAREER-006",

        question=
        "A technical portfolio contains:",

        options=[
            "Projects and work samples",
            "Only marksheet",
            "Only certificates",
            "Only personal details"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Portfolio demonstrates practical skills through projects.",
    ),



    Question(

        question_code="COLLEGE-CAREER-007",

        question=
        "Internships provide:",

        options=[
            "Industry experience",
            "Only attendance",
            "No learning",
            "Only exams"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Internships expose students to real industry environments.",
    ),



    Question(

        question_code="COLLEGE-CAREER-008",

        question=
        "Which communication skill is important during interviews?",

        options=[
            "Clear explanation",
            "Avoiding answers",
            "Ignoring questions",
            "No interaction"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Clear communication helps express ideas effectively.",
    ),



    Question(

        question_code="COLLEGE-CAREER-009",

        question=
        "Which website is commonly used for code hosting?",

        options=[
            "GitHub",
            "YouTube",
            "Calculator",
            "WordPad"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "GitHub is used to store and manage code repositories.",
    ),



    Question(

        question_code="COLLEGE-CAREER-010",

        question=
        "Networking helps students to:",

        options=[
            "Find opportunities and connections",
            "Avoid learning",
            "Reduce skills",
            "Skip projects"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Professional networking helps discover career opportunities.",
    ),



    Question(
        question_code="COLLEGE-CAREER-011",
        question=
        "A strong project description should start with:",
        options=[
            "The problem and your contribution",
            "A list of random technologies",
            "A personal biography",
            "Only screenshots",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Recruiters need context, contribution and outcomes.",
    ),

    Question(
        question_code="COLLEGE-CAREER-012",
        question=
        "A measurable project outcome could be:",
        options=[
            "Reduced response time by 30%",
            "Made it nice",
            "Worked hard",
            "Used many tools",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Quantified outcomes provide evidence of impact.",
    ),

    Question(
        question_code="COLLEGE-CAREER-013",
        question=
        "A GitHub README should ideally include:",
        options=[
            "Setup, usage and project overview",
            "Private passwords",
            "Only a logo",
            "No instructions",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.RESUME,

        explanation=
        "Good README documentation helps others understand and run the project.",
    ),

    Question(
        question_code="COLLEGE-CAREER-014",
        question=
        "STAR in interviews stands for:",
        options=[
            "Situation, Task, Action, Result",
            "Skill, Time, Answer, Review",
            "Study, Test, Apply, Repeat",
            "System, Tool, API, Runtime",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.INTERVIEW,

        explanation=
        "STAR structures behavioral interview answers.",
    ),

    Question(
        question_code="COLLEGE-CAREER-015",
        question=
        "When asked about a project, you should be able to explain:",
        options=[
            "Why it exists and key design decisions",
            "Only its color scheme",
            "Only the library names",
            "Nothing beyond the title",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.INTERVIEW,

        explanation=
        "Understanding decisions demonstrates ownership.",
    ),

    Question(
        question_code="COLLEGE-CAREER-016",
        question=
        "A tailored resume changes content to match:",
        options=[
            "The target role and requirements",
            "The weather",
            "Random companies",
            "Only font size",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.RESUME,

        explanation=
        "Tailoring emphasizes relevant evidence for the target role.",
    ),

    Question(
        question_code="COLLEGE-CAREER-017",
        question=
        "A skills section should prioritize:",
        options=[
            "Relevant skills you can demonstrate",
            "Every technology ever seen",
            "Unverified claims",
            "Only buzzwords",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.RESUME,

        explanation=
        "Relevant demonstrable skills are more credible.",
    ),

    Question(
        question_code="COLLEGE-CAREER-018",
        question=
        "Networking can help students by:",
        options=[
            "Learning about roles and opportunities",
            "Guaranteeing employment",
            "Replacing skills",
            "Avoiding interviews",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Professional networking provides information, relationships and opportunities.",
    ),

    Question(
        question_code="COLLEGE-CAREER-019",
        question=
        "An internship goal should be:",
        options=[
            "Specific and reviewable",
            "Completely undefined",
            "Only salary-based",
            "Impossible to measure",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Clear goals make learning progress easier to evaluate.",
    ),

    Question(
        question_code="COLLEGE-CAREER-020",
        question=
        "A good learning roadmap usually orders topics by:",
        options=[
            "Prerequisites and increasing difficulty",
            "Random selection",
            "Alphabetical order only",
            "Popularity only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.EDUCATION,

        explanation=
        "Prerequisites help learners build skills progressively.",
    ),

    Question(
        question_code="COLLEGE-CAREER-021",
        question=
        "A technical portfolio should demonstrate:",
        options=[
            "Evidence of practical ability",
            "Only certificates",
            "Only copied tutorials",
            "No source code",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Projects demonstrate applied skill.",
    ),

    Question(
        question_code="COLLEGE-CAREER-022",
        question=
        "A certificate is strongest when it is supported by:",
        options=[
            "Projects or demonstrated skills",
            "A profile picture",
            "A long title",
            "No practice",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CERTIFICATION,

        explanation=
        "Certificates are more meaningful when supported by evidence.",
    ),

    Question(
        question_code="COLLEGE-CAREER-023",
        question=
        "A good interview question to ask an employer is about:",
        options=[
            "Role expectations and success criteria",
            "Private employee data",
            "Guaranteed promotion date",
            "Competitor secrets",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.INTERVIEW,

        explanation=
        "Role expectations help candidates understand fit.",
    ),

    Question(
        question_code="COLLEGE-CAREER-024",
        question=
        "If you do not know an interview answer, a good response is to:",
        options=[
            "Explain what you know and reason toward an answer",
            "Invent a fact confidently",
            "Refuse to think",
            "Blame the interviewer",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.INTERVIEW,

        explanation=
        "Transparent reasoning is better than fabricated certainty.",
    ),

    Question(
        question_code="COLLEGE-CAREER-025",
        question=
        "A resume should usually avoid:",
        options=[
            "Unrelated personal details",
            "Relevant achievements",
            "Project links",
            "Contact information",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.RESUME,

        explanation=
        "Space should focus on role-relevant evidence.",
    ),

    Question(
        question_code="COLLEGE-CAREER-026",
        question=
        "A good LinkedIn headline should communicate:",
        options=[
            "Role/skills and career direction",
            "A random quote only",
            "Private information",
            "A password",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "A concise professional headline helps clarify positioning.",
    ),

    Question(
        question_code="COLLEGE-CAREER-027",
        question=
        "Career exploration is improved by:",
        options=[
            "Comparing role requirements with your current skills",
            "Choosing only by title",
            "Ignoring job descriptions",
            "Avoiding projects",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Skill-gap comparison makes career exploration concrete.",
    ),

    Question(
        question_code="COLLEGE-CAREER-028",
        question=
        "A skill gap is:",
        options=[
            "A capability required for a goal but not yet sufficiently developed",
            "A salary difference",
            "A resume font",
            "A company logo",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Skill gaps guide targeted learning.",
    ),

    Question(
        question_code="COLLEGE-CAREER-029",
        question=
        "Mock interviews are useful because they:",
        options=[
            "Provide practice and feedback",
            "Guarantee an offer",
            "Replace technical study",
            "Remove uncertainty completely",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.INTERVIEW,

        explanation=
        "Practice and feedback improve interview performance.",
    ),

    Question(
        question_code="COLLEGE-CAREER-030",
        question=
        "A coding project with tests demonstrates:",
        options=[
            "Ability to validate behavior",
            "Only UI design",
            "Only documentation",
            "No engineering practice",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_TESTING,

        explanation=
        "Tests provide evidence that behavior is validated.",
    ),

    Question(
        question_code="COLLEGE-CAREER-031",
        question=
        "Version control history can demonstrate:",
        options=[
            "Iterative development and collaboration",
            "Only typing speed",
            "Salary",
            "Academic grades",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Commit history can show how work evolved.",
    ),

    Question(
        question_code="COLLEGE-CAREER-032",
        question=
        "A bug report is strongest when it includes:",
        options=[
            "Reproduction steps and expected vs actual behavior",
            "Only 'it doesn't work'",
            "A screenshot with no context",
            "No environment details",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Reproducible details help developers diagnose issues.",
    ),

    Question(
        question_code="COLLEGE-CAREER-033",
        question=
        "Prioritizing tasks by impact and urgency helps with:",
        options=[
            "Time management",
            "Database indexing",
            "Encryption",
            "Compilation",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "Impact and urgency are useful prioritization dimensions.",
    ),

    Question(
        question_code="COLLEGE-CAREER-034",
        question=
        "Breaking a large goal into milestones makes it:",
        options=[
            "Easier to track and execute",
            "Impossible to change",
            "Less measurable",
            "Only theoretical",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "Milestones provide manageable checkpoints.",
    ),

    Question(
        question_code="COLLEGE-CAREER-035",
        question=
        "A good technical blog post should:",
        options=[
            "Explain a problem, approach and lessons",
            "Hide all reasoning",
            "Copy documentation verbatim",
            "Only show a title",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Technical writing demonstrates understanding and communication.",
    ),

    Question(
        question_code="COLLEGE-CAREER-036",
        question=
        "Open-source contribution can demonstrate:",
        options=[
            "Collaboration and real-world engineering practice",
            "Guaranteed employment",
            "Only social activity",
            "No technical skill",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Contributions can show collaboration, tooling and engineering practices.",
    ),

    Question(
        question_code="COLLEGE-CAREER-037",
        question=
        "Before applying for a role, comparing the job description with your skills helps:",
        options=[
            "Target learning and application quality",
            "Guarantee selection",
            "Avoid all interviews",
            "Remove the need for a resume",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Gap analysis helps prioritize relevant preparation.",
    ),

    Question(
        question_code="COLLEGE-CAREER-038",
        question=
        "A good project README should state how to:",
        options=[
            "Install dependencies and run the project",
            "Bypass security",
            "Access private credentials",
            "Delete production data",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Reproducible setup is a key part of useful documentation.",
    ),

    Question(
        question_code="COLLEGE-CAREER-039",
        question=
        "When receiving constructive criticism, the best first step is to:",
        options=[
            "Understand the evidence and clarify expectations",
            "Defend every decision immediately",
            "Ignore it",
            "Delete the work",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Understanding feedback supports improvement.",
    ),

    Question(
        question_code="COLLEGE-CAREER-040",
        question=
        "A career objective should be:",
        options=[
            "Specific enough to guide choices",
            "A generic motivational quote",
            "Unrelated to skills",
            "Impossible to measure",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "A useful objective guides role and learning decisions.",
    ),

    Question(
        question_code="COLLEGE-CAREER-041",
        question=
        "An ATS-friendly resume benefits from:",
        options=[
            "Clear standard headings and relevant keywords",
            "Images for every skill",
            "Hidden text",
            "Unusual layouts only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.RESUME,

        explanation=
        "Standard structure and relevant terms improve machine readability.",
    ),

    Question(
        question_code="COLLEGE-CAREER-042",
        question=
        "A cover letter is strongest when it:",
        options=[
            "Connects your evidence to the role",
            "Repeats the resume word for word",
            "Uses generic text only",
            "Discusses unrelated hobbies",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.RESUME,

        explanation=
        "A tailored letter explains role fit and motivation.",
    ),

    Question(
        question_code="COLLEGE-CAREER-043",
        question=
        "A portfolio case study should include:",
        options=[
            "Problem, constraints, decisions, result and lessons",
            "Only final screenshots",
            "Only source code",
            "No context",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Case studies show engineering thinking and outcomes.",
    ),

    Question(
        question_code="COLLEGE-CAREER-044",
        question=
        "If a job requires a skill you lack, a sensible response is to:",
        options=[
            "Assess the gap and create a focused learning plan",
            "Claim expertise you don't have",
            "Ignore the requirement",
            "Change the resume secretly",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Honest gap analysis enables targeted improvement.",
    ),

    Question(
        question_code="COLLEGE-CAREER-045",
        question=
        "A technical assessment should be approached by:",
        options=[
            "Clarifying requirements, testing assumptions and managing time",
            "Coding immediately without reading",
            "Ignoring edge cases",
            "Submitting without testing",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.INTERVIEW,

        explanation=
        "Structured reasoning improves assessment quality.",
    ),

    Question(
        question_code="COLLEGE-CAREER-046",
        question=
        "Career decisions should consider:",
        options=[
            "Interests, strengths, market requirements and learning path",
            "Salary only",
            "Titles only",
            "Friends' choices only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Balanced career decisions consider fit and opportunity.",
    ),

    Question(
        question_code="COLLEGE-CAREER-047",
        question=
        "A good mentor relationship benefits from:",
        options=[
            "Clear goals, questions and feedback loops",
            "Expecting answers without effort",
            "No communication",
            "Only asking for referrals",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Clear goals and active learning make mentoring effective.",
    ),

    Question(
        question_code="COLLEGE-CAREER-048",
        question=
        "Professional reputation is strengthened by:",
        options=[
            "Reliable delivery and transparent communication",
            "Overpromising",
            "Hiding delays",
            "Ignoring commitments",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Reliability and communication build trust.",
    ),

    Question(
        question_code="COLLEGE-CAREER-049",
        question=
        "A learning retrospective asks:",
        options=[
            "What worked, what didn't, and what to change next",
            "Only who is responsible",
            "Only the final score",
            "Nothing about process",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.EDUCATION,

        explanation=
        "Retrospectives turn experience into improvements.",
    ),

    Question(
        question_code="COLLEGE-CAREER-050",
        question=
        "A strong internship application should emphasize:",
        options=[
            "Relevant evidence, learning and contribution",
            "Only marks",
            "Only hobbies",
            "Unverified claims",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Relevant evidence makes an application credible.",
    ),
]