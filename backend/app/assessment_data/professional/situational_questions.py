from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


PROFESSIONAL_SITUATIONAL_QUESTIONS: list[Question] = [

    # =====================================================
    # PROFESSIONAL SITUATIONAL (PROFESSIONAL-SITUATIONAL-001–010)
    # =====================================================


    Question(

        question_code="PROFESSIONAL-SITUATIONAL-001",

        question=
        "If a team member disagrees with your idea, you should:",

        options=[
            "Listen and discuss the concern",
            "Ignore the person",
            "Force your decision",
            "Leave the team"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Good professionals respect different opinions and discuss solutions.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-002",

        question=
        "If you miss a project deadline, the best action is:",

        options=[
            "Inform the team and explain the reason",
            "Hide the issue",
            "Blame others",
            "Stop working"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Transparency and communication help solve deadline issues.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-003",

        question=
        "When receiving negative feedback, you should:",

        options=[
            "Accept it and improve",
            "Argue immediately",
            "Ignore feedback",
            "Quit the task"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Constructive feedback helps improve performance.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-004",

        question=
        "A colleague needs help with a task. You should:",

        options=[
            "Support and guide them",
            "Ignore them",
            "Create problems",
            "Avoid communication"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.TEAMWORK,

        explanation=
        "Helping teammates improves collaboration.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-005",

        question=
        "If you find a bug in production, you should:",

        options=[
            "Report and fix it properly",
            "Ignore it",
            "Delete the project",
            "Hide the problem"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Production issues should be handled responsibly.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-006",

        question=
        "When working in a team, communication should be:",

        options=[
            "Clear and regular",
            "Avoided",
            "Only during problems",
            "Unnecessary"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.TEAMWORK,

        explanation=
        "Regular communication keeps teams aligned.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-007",

        question=
        "If you do not know a technology required for a task, you should:",

        options=[
            "Learn and ask for guidance",
            "Reject the task",
            "Pretend to know",
            "Ignore it"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.CAREER,

        explanation=
        "Learning attitude helps professionals grow.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-008",

        question=
        "During a meeting, a professional should:",

        options=[
            "Listen actively and contribute",
            "Interrupt everyone",
            "Avoid participation",
            "Ignore discussion"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Active participation improves workplace communication.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-009",

        question=
        "When multiple tasks are assigned, you should:",

        options=[
            "Prioritize tasks based on importance",
            "Do random tasks",
            "Ignore deadlines",
            "Stop working"
        ],

        answer="A",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "Prioritization helps complete important tasks efficiently.",
    ),



    Question(

        question_code="PROFESSIONAL-SITUATIONAL-010",

        question=
        "A professional conflict should be resolved through:",

        options=[
            "Discussion and solution finding",
            "Arguments",
            "Avoidance forever",
            "Personal attacks"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Healthy discussion helps resolve workplace conflicts.",
    ),



    Question(
        question_code="PROFESSIONAL-SITUATIONAL-011",
        question=
        "A critical production alert fires during your shift. What should you do first?",
        options=[
            "Assess impact and follow the incident process",
            "Ignore it until morning",
            "Delete the alert",
            "Restart random services",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Incident response starts with impact assessment and the established process.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-012",
        question=
        "A teammate proposes a risky change without tests. You should:",
        options=[
            "Discuss risk and ask for validation before release",
            "Approve immediately",
            "Block all future changes",
            "Publicly criticize them",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Risk should be addressed constructively with evidence.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-013",
        question=
        "A client requests an urgent feature that conflicts with a committed deadline. You should:",
        options=[
            "Clarify priority and negotiate scope/timeline",
            "Promise both silently",
            "Ignore the client",
            "Cancel the deadline",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Explicit trade-offs prevent hidden commitments.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-014",
        question=
        "You discover a security vulnerability in production. You should:",
        options=[
            "Report and contain it through the security process",
            "Hide it",
            "Post details publicly",
            "Wait for a customer to find it",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Security incidents require prompt responsible handling.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-015",
        question=
        "A requirement changes after implementation begins. You should:",
        options=[
            "Assess impact and update the plan with stakeholders",
            "Reject every change",
            "Implement without telling anyone",
            "Delete the old work",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Change management requires impact assessment and alignment.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-016",
        question=
        "A teammate is overloaded while you have capacity. A good response is:",
        options=[
            "Offer specific help after aligning priorities",
            "Take their work without asking",
            "Ignore it",
            "Tell management they are failing",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Specific collaboration helps the team while preserving ownership.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-017",
        question=
        "A reviewer points out a defect in your code. You should:",
        options=[
            "Thank them, understand the issue and fix it",
            "Argue automatically",
            "Remove the reviewer",
            "Ignore the comment",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Constructive review improves quality.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-018",
        question=
        "A deployment causes elevated errors. You have a tested rollback. You should:",
        options=[
            "Follow the rollback/incident plan and communicate impact",
            "Keep deploying unrelated changes",
            "Hide the errors",
            "Delete monitoring",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Rollback can quickly reduce impact when a release is faulty.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-019",
        question=
        "You are asked to estimate an unfamiliar task. You should:",
        options=[
            "State assumptions and provide a range or confidence",
            "Invent exact certainty",
            "Refuse every estimate",
            "Use another task's estimate blindly",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Uncertainty-aware estimates are more useful.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-020",
        question=
        "A meeting has no clear objective. You should:",
        options=[
            "Clarify the desired outcome and agenda",
            "Talk until time ends",
            "Cancel all meetings forever",
            "Invite everyone",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "A clear outcome improves meeting effectiveness.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-021",
        question=
        "A colleague takes credit for your work. You should:",
        options=[
            "Discuss it directly and factually, escalating if needed",
            "Retaliate publicly",
            "Delete the work",
            "Spread rumors",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Professional resolution starts with facts and direct communication.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-022",
        question=
        "You notice a repeated manual task causing errors. You should:",
        options=[
            "Measure it and propose automation or process improvement",
            "Accept it forever",
            "Blame users",
            "Hide the errors",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Recurring error-prone work is a candidate for improvement.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-023",
        question=
        "A stakeholder disagrees with your technical recommendation. You should:",
        options=[
            "Explain trade-offs using evidence and listen to constraints",
            "Use jargon to win",
            "Ignore their concerns",
            "Escalate immediately",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Good decisions combine technical evidence with stakeholder constraints.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-024",
        question=
        "A production database query is slow. You should first:",
        options=[
            "Measure/query-plan the problem before changing indexes blindly",
            "Add indexes everywhere",
            "Delete data",
            "Restart the database repeatedly",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DBMS,

        explanation=
        "Diagnosis should precede optimization.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-025",
        question=
        "A user reports a bug you cannot reproduce. You should:",
        options=[
            "Collect environment, steps and evidence",
            "Close the ticket immediately",
            "Blame the user",
            "Change random code",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "More reproduction evidence is needed.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-026",
        question=
        "A deadline is tomorrow and testing is incomplete. You should:",
        options=[
            "Communicate risk and prioritize critical validation",
            "Skip testing silently",
            "Ship without telling anyone",
            "Delete tests",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "Transparent risk management enables informed decisions.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-027",
        question=
        "A teammate is repeatedly missing handoffs. You should:",
        options=[
            "Discuss the pattern and agree on a concrete process",
            "Complain to everyone",
            "Stop communicating",
            "Take over permanently",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Addressing the process directly can improve reliability.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-028",
        question=
        "You receive a request for confidential data from an unauthorized person. You should:",
        options=[
            "Decline and follow access policy",
            "Send it because they sound senior",
            "Post it publicly",
            "Forward credentials",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Authorization controls must be respected.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-029",
        question=
        "A new tool looks popular but does not solve your team's problem. You should:",
        options=[
            "Evaluate it against actual requirements",
            "Adopt it immediately",
            "Ban all new tools",
            "Use it for marketing only",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Tool selection should follow needs and evidence.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-030",
        question=
        "Two incidents compete for attention. You should prioritize based on:",
        options=[
            "User/business impact and risk",
            "Who reported first only",
            "Personal preference",
            "Which alert looks louder",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Impact and risk provide a rational priority basis.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-031",
        question=
        "You make a mistake in a customer-facing change. You should:",
        options=[
            "Acknowledge, mitigate and communicate appropriately",
            "Hide it",
            "Blame the customer",
            "Delete logs",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Ownership and timely mitigation preserve trust.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-032",
        question=
        "A junior engineer asks for help. You should:",
        options=[
            "Guide them with questions and context, then let them implement",
            "Do everything for them",
            "Ignore them",
            "Tell them to search forever",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LEADERSHIP,

        explanation=
        "Coaching should build independent capability.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-033",
        question=
        "A product requirement is technically impossible under current constraints. You should:",
        options=[
            "Explain the constraint and propose alternatives",
            "Promise it anyway",
            "Stop the project",
            "Hide the issue",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Alternatives allow stakeholders to choose among feasible options.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-034",
        question=
        "A service repeatedly runs out of memory. You should:",
        options=[
            "Measure memory behavior and identify the cause before tuning",
            "Increase memory indefinitely",
            "Restart forever",
            "Disable alerts",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Root-cause analysis avoids masking leaks or unbounded usage.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-035",
        question=
        "A coworker suggests committing an API key for convenience. You should:",
        options=[
            "Reject it and use secure secret management",
            "Commit it temporarily",
            "Put it in a public gist",
            "Email it to everyone",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.CYBER_SECURITY,

        explanation=
        "Credentials should never be committed to source control.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-036",
        question=
        "A customer is angry about an outage. You should:",
        options=[
            "Acknowledge impact, communicate facts and recovery steps",
            "Argue with them",
            "Promise impossible dates",
            "Blame infrastructure",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Empathy plus factual updates helps manage incident communication.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-037",
        question=
        "A project is growing in scope without a schedule change. You should:",
        options=[
            "Surface scope creep and agree on priorities",
            "Accept everything silently",
            "Work unlimited overtime",
            "Hide the new requirements",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TIME_MANAGEMENT,

        explanation=
        "Scope, time and resources need explicit trade-offs.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-038",
        question=
        "A teammate proposes a simpler design that meets requirements. You should:",
        options=[
            "Evaluate it fairly rather than favoring complexity",
            "Reject simple solutions automatically",
            "Add features anyway",
            "Ignore constraints",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "The simplest adequate solution is often preferable.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-039",
        question=
        "You find duplicated logic across services. You should:",
        options=[
            "Assess duplication cost and propose a safe refactor",
            "Copy it more",
            "Delete one service",
            "Ignore all maintenance",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.SOFTWARE_DEVELOPMENT,

        explanation=
        "Refactoring should be driven by maintainability and risk.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-040",
        question=
        "A release has no monitoring for a critical path. You should:",
        options=[
            "Add appropriate observability before or alongside release",
            "Release blind",
            "Disable logs",
            "Assume success",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Critical changes need feedback signals.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-041",
        question=
        "A stakeholder asks you to hide a known defect from a report. You should:",
        options=[
            "Report accurately and escalate ethical concerns if needed",
            "Hide it",
            "Change the data",
            "Delete evidence",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROFESSIONAL_SKILLS,

        explanation=
        "Accurate reporting is an ethical and operational requirement.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-042",
        question=
        "A task is blocked by another team. You should:",
        options=[
            "Communicate the dependency, owner and required date",
            "Wait silently",
            "Blame the other team",
            "Duplicate their system",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Explicit dependency management reduces delays.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-043",
        question=
        "A code review becomes personal. You should:",
        options=[
            "Return discussion to code, evidence and shared standards",
            "Respond personally",
            "Close the review angrily",
            "Ignore all comments",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Professional review focuses on technical issues.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-044",
        question=
        "A recurring deployment failure happens every Friday. You should:",
        options=[
            "Analyze patterns and automate/prevent the failure",
            "Accept it as normal",
            "Blame Friday",
            "Stop deploying forever",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Patterns can reveal process or automation defects.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-045",
        question=
        "You need to choose between two implementation approaches. You should compare:",
        options=[
            "Requirements, trade-offs, risks and maintenance",
            "Only initial coding speed",
            "Only popularity",
            "Only line count",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Engineering choices require multi-dimensional trade-off analysis.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-046",
        question=
        "A colleague asks for feedback on a presentation. You should:",
        options=[
            "Give specific strengths and actionable improvements",
            "Say only 'good'",
            "Rewrite everything without consent",
            "Avoid honesty",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.COMMUNICATION,

        explanation=
        "Specific feedback is actionable and respectful.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-047",
        question=
        "A project has no clear owner for a critical task. You should:",
        options=[
            "Clarify ownership with the team/manager",
            "Assume someone will do it",
            "Do it secretly",
            "Ignore the task",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LEADERSHIP,

        explanation=
        "Explicit ownership prevents dropped work.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-048",
        question=
        "A production fix is urgent but risky. You should:",
        options=[
            "Use the safest validated mitigation and document the decision",
            "Push untested changes blindly",
            "Wait without communicating",
            "Disable monitoring",
        ],
        answer="A",
        difficulty=Difficulty.HARD,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.DEVOPS,

        explanation=
        "Urgent changes still require controlled risk management.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-049",
        question=
        "A teammate is struggling with a new technology. You should:",
        options=[
            "Pair on a small task and provide resources",
            "Take all their tasks permanently",
            "Tell them to learn alone",
            "Exclude them",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.TEAMWORK,

        explanation=
        "Targeted pairing supports learning and delivery.",
    ),

    Question(
        question_code="PROFESSIONAL-SITUATIONAL-050",
        question=
        "A stakeholder changes a key acceptance criterion late in testing. You should:",
        options=[
            "Document the change, assess impact and agree on revised acceptance",
            "Pretend the old criterion still applies",
            "Delete failing tests",
            "Release without alignment",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.PROBLEM_SOLVING,

        explanation=
        "Acceptance changes should be explicit, assessed and agreed.",
    ),
]