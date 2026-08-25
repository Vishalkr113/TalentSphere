from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


PROFESSIONAL_COMMON_QUESTIONS: list[Question] = [

    # =====================================================
    # PROFESSIONAL COMMON (PROFESSIONAL-COMMON-001–010)
    # =====================================================


    Question(

        question_code="PROFESSIONAL-COMMON-001",

        question=
        "Professional communication mainly focuses on:",

        options=[
            "Clear exchange of information",
            "Avoiding discussion",
            "Ignoring feedback",
            "Using difficult words only"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Professional communication requires clear and effective information sharing.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-002",

        question=
        "Teamwork means:",

        options=[
            "Working together to achieve a goal",
            "Working alone always",
            "Avoiding responsibilities",
            "Ignoring team members"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Teamwork involves collaboration among team members.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-003",

        question=
        "A good leader should have:",

        options=[
            "Decision making ability",
            "No responsibility",
            "Poor communication",
            "No planning"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.LEADERSHIP,

        explanation=
        "Leadership requires decision making and responsibility.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-004",

        question=
        "Time management helps to:",

        options=[
            "Complete tasks efficiently",
            "Delay work",
            "Avoid planning",
            "Reduce productivity"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Time management improves productivity and task completion.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-005",

        question=
        "Feedback is useful because it:",

        options=[
            "Improves performance",
            "Creates confusion only",
            "Stops learning",
            "Avoids improvement"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Constructive feedback helps improve skills and performance.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-006",

        question=
        "A professional should maintain:",

        options=[
            "Work ethics",
            "Negative attitude",
            "Poor communication",
            "Irresponsibility"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Work ethics are important for professional behavior.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-007",

        question=
        "Problem solving requires:",

        options=[
            "Logical thinking",
            "Ignoring problems",
            "Random decisions",
            "Avoiding analysis"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Logical thinking helps identify and solve problems.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-008",

        question=
        "Adaptability means:",

        options=[
            "Ability to adjust with changes",
            "Rejecting changes",
            "Avoiding learning",
            "Stopping improvement"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Adaptability helps professionals handle changing situations.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-009",

        question=
        "A professional resume should be:",

        options=[
            "Clear and relevant",
            "Very lengthy with unnecessary details",
            "Without skills",
            "Incomplete"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "A resume should clearly highlight relevant skills and experience.",
    ),



    Question(

        question_code="PROFESSIONAL-COMMON-010",

        question=
        "Continuous learning helps professionals to:",

        options=[
            "Stay updated with skills",
            "Stop growth",
            "Avoid technology",
            "Reduce knowledge"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Continuous learning keeps professionals updated and competitive.",
    ),



    Question(
        question_code="PROFESSIONAL-COMMON-011",
        question=
        "A senior engineer should communicate risk by:",
        options=[
            "Stating impact, likelihood and mitigation",
            "Hiding uncertainty",
            "Only reporting after failure",
            "Blaming a teammate",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Clear risk communication supports informed decisions.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-012",
        question=
        "A professional disagreement is best handled by:",
        options=[
            "Focusing on evidence and shared goals",
            "Making it personal",
            "Avoiding all discussion",
            "Escalating immediately",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Evidence and shared goals keep disagreements constructive.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-013",
        question=
        "When a deadline is at risk, the best action is to:",
        options=[
            "Communicate early with options and impact",
            "Wait until the deadline passes",
            "Hide the delay",
            "Delete the task",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "Early communication creates options for mitigation.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-014",
        question=
        "A good status update should include:",
        options=[
            "Progress, blockers and next steps",
            "Only 'working on it'",
            "Personal opinions",
            "No dates",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Concise status updates help teams coordinate.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-015",
        question=
        "Delegating a task effectively requires:",
        options=[
            "Clear outcome, authority and context",
            "Giving a vague instruction",
            "No follow-up ever",
            "Taking the task back immediately",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LEADERSHIP,

        explanation=
        "Effective delegation includes clarity and appropriate autonomy.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-016",
        question=
        "A retrospective should focus on:",
        options=[
            "Process improvements rather than blame",
            "Finding one person to blame",
            "Only successes",
            "Only metrics",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Blameless retrospectives encourage learning and improvement.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-017",
        question=
        "A professional email subject should be:",
        options=[
            "Specific and informative",
            "Blank",
            "Very long and vague",
            "Only an emoji",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Specific subjects help recipients understand the purpose quickly.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-018",
        question=
        "Meeting notes are valuable because they capture:",
        options=[
            "Decisions, owners and action items",
            "Only attendance",
            "Private opinions",
            "Every spoken word",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Actionable records preserve accountability.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-019",
        question=
        "When requirements are ambiguous, you should:",
        options=[
            "Ask targeted clarifying questions",
            "Guess silently",
            "Implement everything",
            "Ignore the requirement",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Clarification reduces rework and misalignment.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-020",
        question=
        "A strong estimate should include:",
        options=[
            "Assumptions and uncertainty",
            "False precision",
            "No explanation",
            "Only a single number",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Assumptions make estimates reviewable.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-021",
        question=
        "A conflict of interest should be:",
        options=[
            "Disclosed appropriately",
            "Hidden",
            "Used for personal gain",
            "Ignored",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Disclosure supports ethical decision-making.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-022",
        question=
        "Confidential company information should be:",
        options=[
            "Shared only with authorized parties",
            "Posted publicly",
            "Sent to competitors",
            "Stored in public repositories",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Confidential information requires controlled access.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-023",
        question=
        "A good mentor asks questions to:",
        options=[
            "Help the learner reason and grow",
            "Provide every answer instantly",
            "Control every decision",
            "Avoid feedback",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LEADERSHIP,

        explanation=
        "Questions can develop independent problem solving.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-024",
        question=
        "A useful one-on-one meeting should cover:",
        options=[
            "Progress, blockers, feedback and goals",
            "Only personal gossip",
            "Only status once a year",
            "No agenda",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Regular one-on-ones support alignment and development.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-025",
        question=
        "When receiving negative feedback, first:",
        options=[
            "Listen, clarify and identify actionable points",
            "Argue immediately",
            "Ignore it",
            "Forward it publicly",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Understanding feedback helps turn it into improvement.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-026",
        question=
        "Ownership means:",
        options=[
            "Following a problem through to an outcome",
            "Doing every task alone",
            "Never asking for help",
            "Avoiding accountability",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LEADERSHIP,

        explanation=
        "Ownership is responsibility for outcomes, including coordination.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-027",
        question=
        "A high-quality handoff includes:",
        options=[
            "Context, current state, risks and next steps",
            "Only a file name",
            "No documentation",
            "Only a verbal 'done'",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Good handoffs preserve context and reduce continuity risk.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-028",
        question=
        "A professional should respond to an incident by:",
        options=[
            "Stabilizing, communicating and learning from it",
            "Hiding logs",
            "Blaming first",
            "Deleting evidence",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Incident response prioritizes safety, communication and learning.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-029",
        question=
        "Prioritization should consider:",
        options=[
            "Impact, urgency and dependencies",
            "Only who asks first",
            "Only task size",
            "Only personal preference",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "Multiple factors determine sensible priority.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-030",
        question=
        "Saying 'no' professionally is best done with:",
        options=[
            "Reason and an alternative when possible",
            "Silence",
            "Personal criticism",
            "False promises",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "A clear reason and alternative preserves trust.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-031",
        question=
        "A career development plan should contain:",
        options=[
            "Target skills, actions and review points",
            "Only a title",
            "No timeline",
            "Only salary goals",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Concrete development actions make progress trackable.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-032",
        question=
        "A promotion case is strongest when supported by:",
        options=[
            "Evidence of sustained impact and scope",
            "Only tenure",
            "Only self-confidence",
            "A single compliment",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Evidence of impact supports advancement decisions.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-033",
        question=
        "A technical lead should balance:",
        options=[
            "Delivery, quality, people and risk",
            "Only coding speed",
            "Only meetings",
            "Only architecture diagrams",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LEADERSHIP,

        explanation=
        "Leadership balances technical and organizational outcomes.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-034",
        question=
        "When two urgent tasks conflict, you should:",
        options=[
            "Clarify business impact and negotiate priority",
            "Do both halfway silently",
            "Ignore one",
            "Choose randomly",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "Explicit prioritization avoids hidden trade-offs.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-035",
        question=
        "A good escalation contains:",
        options=[
            "Facts, impact, options and requested decision",
            "Only frustration",
            "No evidence",
            "Personal blame",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Decision-makers need concise context and options.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-036",
        question=
        "A reliable teammate is someone who:",
        options=[
            "Communicates commitments and changes early",
            "Never speaks",
            "Accepts everything",
            "Hides blockers",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Reliability includes transparent commitment management.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-037",
        question=
        "Documentation is most valuable when it:",
        options=[
            "Explains decisions and operational knowledge",
            "Duplicates every line of code",
            "Contains secrets",
            "Is never updated",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Useful documentation captures knowledge that is hard to infer.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-038",
        question=
        "A good code review comment should be:",
        options=[
            "Specific, respectful and actionable",
            "Personal",
            "Vague",
            "All caps",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Actionable technical feedback improves code without personal criticism.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-039",
        question=
        "Psychological safety helps teams:",
        options=[
            "Raise concerns and learn from mistakes",
            "Avoid all accountability",
            "Hide defects",
            "Stop feedback",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Safety encourages people to surface issues early.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-040",
        question=
        "When mentoring, giving a learner a small challenge helps:",
        options=[
            "Build independent capability",
            "Create dependency",
            "Avoid learning",
            "Replace all feedback",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LEADERSHIP,

        explanation=
        "Gradual challenges build autonomy.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-041",
        question=
        "A useful KPI should:",
        options=[
            "Measure an outcome aligned with a goal",
            "Be easy but irrelevant",
            "Change every hour",
            "Have no owner",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Useful metrics connect measurement to desired outcomes.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-042",
        question=
        "Burnout risk can be reduced by:",
        options=[
            "Sustainable workload, recovery and realistic priorities",
            "Working longer indefinitely",
            "Ignoring workload",
            "Removing breaks",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "Sustainable practices reduce prolonged overload.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-043",
        question=
        "A professional presentation should:",
        options=[
            "Lead with the key message and evidence",
            "Hide the conclusion",
            "Use every slide for text",
            "Avoid questions",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Clear structure and evidence improve decision-making.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-044",
        question=
        "If a teammate makes a mistake, a constructive response is to:",
        options=[
            "Address impact, help fix it and improve the process",
            "Publicly shame them",
            "Hide the issue",
            "Repeat the mistake",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Constructive responses fix both immediate and systemic issues.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-045",
        question=
        "Ethical decision-making should consider:",
        options=[
            "Stakeholders, consequences and applicable policies",
            "Only personal benefit",
            "Only speed",
            "Only popularity",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Ethical choices consider impact and obligations.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-046",
        question=
        "A good manager creates clarity by:",
        options=[
            "Defining outcomes, ownership and constraints",
            "Changing goals daily without notice",
            "Avoiding decisions",
            "Keeping context secret",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LEADERSHIP,

        explanation=
        "Clarity enables teams to execute independently.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-047",
        question=
        "A postmortem is useful because it:",
        options=[
            "Identifies causes and preventive actions",
            "Assigns blame only",
            "Deletes incident history",
            "Replaces monitoring",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Postmortems turn incidents into learning and prevention.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-048",
        question=
        "A professional network is strongest when:",
        options=[
            "Relationships are built through genuine value and follow-up",
            "Only referrals are requested",
            "Messages are automated spam",
            "Contacts are never maintained",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Sustainable networking is based on mutual value.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-049",
        question=
        "A good career pivot begins with:",
        options=[
            "Transferable skills and target-role gap analysis",
            "Deleting previous experience",
            "Ignoring market needs",
            "Only changing a title",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CAREER,

        explanation=
        "Gap analysis identifies how existing skills transfer and what to learn.",
    ),

    Question(
        question_code="PROFESSIONAL-COMMON-050",
        question=
        "A strong remote-work practice is:",
        options=[
            "Clear async communication and documented decisions",
            "Assuming everyone is online",
            "No written context",
            "Meetings for every question",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Good async habits reduce coordination friction.",
    ),
]