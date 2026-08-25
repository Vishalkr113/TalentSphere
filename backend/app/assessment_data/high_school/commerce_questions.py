from ..enums import Difficulty, QuestionType, Topic
from ..schemas import Question


COMMERCE_QUESTIONS: list[Question] = [

    # =====================================================
    # COMMERCE QUESTIONS (HS-COMMERCE-001–010)
    # =====================================================


    Question(

        question_code="HS-COMMERCE-001",

        question=
        "Accounting is mainly concerned with:",

        options=[
            "Recording financial transactions",
            "Manufacturing products",
            "Selling goods",
            "Hiring employees"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.COMMERCE,

        student_class="11-12",

        stream="COMMERCE",

        explanation=
        "Accounting records, classifies and summarizes financial transactions.",
    ),



    Question(

        question_code="HS-COMMERCE-002",

        question=
        "The basic accounting equation is:",

        options=[
            "Assets = Liabilities + Capital",
            "Assets = Income + Expense",
            "Profit = Assets",
            "Capital = Expense"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ACCOUNTING,

        student_class="11-12",

        stream="COMMERCE",

        explanation=
        "The accounting equation is Assets = Liabilities + Owner's Equity.",
    ),



    Question(

        question_code="HS-COMMERCE-003",

        question=
        "Which book records daily transactions in accounting?",

        options=[
            "Ledger",
            "Journal",
            "Balance Sheet",
            "Cash Flow"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ACCOUNTING,

        student_class="11-12",

        stream="COMMERCE",

        explanation=
        "Journal is used for recording daily financial transactions.",
    ),



    Question(

        question_code="HS-COMMERCE-004",

        question=
        "A person who starts and manages a business is called:",

        options=[
            "Consumer",
            "Entrepreneur",
            "Employee",
            "Manager"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BUSINESS,

        student_class="11-12",

        stream="COMMERCE",

        explanation=
        "An entrepreneur starts and manages a business venture.",
    ),



    Question(

        question_code="HS-COMMERCE-005",

        question=
        "GDP stands for:",

        options=[
            "Gross Domestic Product",
            "General Development Plan",
            "Gross Demand Price",
            "Government Development Process"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ECONOMICS,

        student_class="11-12",

        stream="COMMERCE",

        explanation=
        "GDP represents total value of goods and services produced in a country.",
    ),



    Question(

        question_code="HS-COMMERCE-006",

        question=
        "Demand and supply are concepts of:",

        options=[
            "Physics",
            "Economics",
            "Biology",
            "Computer Science"
        ],

        answer="B",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ECONOMICS,

        student_class="11-12",

        stream="COMMERCE",

        explanation=
        "Demand and supply are fundamental concepts in economics.",
    ),



    Question(

        question_code="HS-COMMERCE-007",

        question=
        "Which document shows financial position of a business?",

        options=[
            "Journal",
            "Balance Sheet",
            "Invoice",
            "Receipt"
        ],

        answer="B",

        difficulty=Difficulty.MEDIUM,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ACCOUNTING,

        student_class="11-12",

        stream="COMMERCE",

        explanation=
        "Balance Sheet shows assets, liabilities and capital.",
    ),



    Question(

        question_code="HS-COMMERCE-008",

        question=
        "Marketing mainly focuses on:",

        options=[
            "Customer needs",
            "Only production",
            "Machine repair",
            "Accounting records"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.BUSINESS,

        student_class="11-12",

        stream="COMMERCE",

        explanation=
        "Marketing identifies and satisfies customer needs.",
    ),



    Question(

        question_code="HS-COMMERCE-009",

        question=
        "Profit is calculated as:",

        options=[
            "Income - Expenses",
            "Assets - Liabilities",
            "Sales + Cost",
            "Capital - Assets"
        ],

        answer="A",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ACCOUNTING,

        student_class="11-12",

        stream="COMMERCE",

        explanation=
        "Profit equals total income minus total expenses.",
    ),



    Question(

        question_code="HS-COMMERCE-010",

        question=
        "Banking is a part of which sector?",

        options=[
            "Primary Sector",
            "Secondary Sector",
            "Service Sector",
            "Agriculture Sector"
        ],

        answer="C",

        difficulty=Difficulty.EASY,

        question_type=QuestionType.ASSESSMENT,

        topic=Topic.ECONOMICS,

        student_class="11-12",

        stream="COMMERCE",

        explanation=
        "Banking comes under the service sector.",
    ),


    # =====================================================
    # ADDITIONAL QUESTIONS (011–020)
    # =====================================================

    Question(
        question_code="HS-COMMERCE-011",
        question="A trial balance is mainly prepared to check:",
        options=[
            "Arithmetic accuracy of ledger postings",
            "Market demand",
            "Cash sales only",
            "Employee performance"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,
        student_class="11-12",
        stream="COMMERCE",
        explanation="A trial balance checks the arithmetical accuracy of debit and credit balances.",
    ),
    Question(
        question_code="HS-COMMERCE-012",
        question="The amount invested by the owner in a business is called:",
        options=[
            "Revenue",
            "Capital",
            "Expense",
            "Drawings"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,
        student_class="11-12",
        stream="COMMERCE",
        explanation="Owner's investment in the business is called capital.",
    ),
    Question(
        question_code="HS-COMMERCE-013",
        question="Goods returned by a customer are recorded as:",
        options=[
            "Purchase return",
            "Sales return",
            "Capital receipt",
            "Expense"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,
        student_class="11-12",
        stream="COMMERCE",
        explanation="Goods returned by customers are recorded as sales returns.",
    ),
    Question(
        question_code="HS-COMMERCE-014",
        question="Which financial statement shows profit or loss for an accounting period?",
        options=[
            "Balance Sheet",
            "Profit and Loss Account",
            "Cash Book",
            "Trial Balance"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,
        student_class="11-12",
        stream="COMMERCE",
        explanation="The Profit and Loss Account reports income, expenses and resulting profit or loss.",
    ),
    Question(
        question_code="HS-COMMERCE-015",
        question="The law of demand generally states that, other things being equal:",
        options=[
            "Demand rises when price rises",
            "Demand falls when price rises",
            "Demand is always constant",
            "Supply falls when price rises"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,
        student_class="11-12",
        stream="COMMERCE",
        explanation="Normally, quantity demanded decreases as price increases, other factors remaining constant.",
    ),
    Question(
        question_code="HS-COMMERCE-016",
        question="Inflation means a sustained increase in the:",
        options=[
            "General price level",
            "Population only",
            "Production of one product",
            "Exchange rate only"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,
        student_class="11-12",
        stream="COMMERCE",
        explanation="Inflation is a sustained rise in the general price level.",
    ),
    Question(
        question_code="HS-COMMERCE-017",
        question="Which institution is the central bank of India?",
        options=[
            "State Bank of India",
            "Reserve Bank of India",
            "SEBI",
            "NABARD"
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,
        student_class="11-12",
        stream="COMMERCE",
        explanation="The Reserve Bank of India is India's central bank.",
    ),
    Question(
        question_code="HS-COMMERCE-018",
        question="A business plan is primarily used to:",
        options=[
            "Guide and evaluate a business venture",
            "Record only daily expenses",
            "Replace all employees",
            "Calculate school marks"
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BUSINESS,
        student_class="11-12",
        stream="COMMERCE",
        explanation="A business plan outlines objectives, strategy, resources and expected performance.",
    ),
    Question(
        question_code="HS-COMMERCE-019",
        question="The process of dividing a market into groups of similar customers is called:",
        options=[
            "Market segmentation",
            "Market expansion",
            "Product costing",
            "Book keeping"
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BUSINESS,
        student_class="11-12",
        stream="COMMERCE",
        explanation="Market segmentation divides a broad market into groups with similar characteristics or needs.",
    ),
    Question(
        question_code="HS-COMMERCE-020",
        question="A debenture generally represents:",
        options=[
            "A long-term debt instrument",
            "Owner's personal expense",
            "A cash discount",
            "A type of inventory"
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,
        student_class="11-12",
        stream="COMMERCE",
        explanation="A debenture is generally a long-term borrowing/debt instrument issued by a company.",
    ),


    Question(
        question_code="HS-COMMERCE-021",
        question=
        "The accounting equation is:",
        options=[
            "Assets = Liabilities + Capital",
            "Assets = Revenue - Expense",
            "Capital = Assets + Liabilities",
            "Assets = Expenses + Profit",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "The fundamental accounting equation is Assets = Liabilities + Capital.",
    ),

    Question(
        question_code="HS-COMMERCE-022",
        question=
        "A debit entry generally increases:",
        options=[
            "Assets and expenses",
            "Liabilities only",
            "Capital only",
            "Revenue only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "Debits normally increase assets and expenses.",
    ),

    Question(
        question_code="HS-COMMERCE-023",
        question=
        "Revenue received in advance is treated initially as:",
        options=[
            "Asset",
            "Liability",
            "Expense",
            "Drawings",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "Advance revenue creates an obligation to provide goods or services.",
    ),

    Question(
        question_code="HS-COMMERCE-024",
        question=
        "Depreciation is charged to account for:",
        options=[
            "Increase in cash",
            "Loss of useful value of an asset",
            "Increase in capital",
            "New revenue",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "Depreciation allocates the depreciable cost of an asset over its useful life.",
    ),

    Question(
        question_code="HS-COMMERCE-025",
        question=
        "A trial balance primarily checks:",
        options=[
            "Profitability",
            "Arithmetical equality of debits and credits",
            "Cash flow only",
            "Market value",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "Trial balance checks the equality of debit and credit totals.",
    ),

    Question(
        question_code="HS-COMMERCE-026",
        question=
        "Gross profit equals:",
        options=[
            "Sales - Cost of goods sold",
            "Sales - Operating expenses",
            "Revenue + Expenses",
            "Assets - Liabilities",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "Gross profit is sales minus cost of goods sold.",
    ),

    Question(
        question_code="HS-COMMERCE-027",
        question=
        "Which financial statement shows assets and liabilities?",
        options=[
            "Income statement",
            "Balance sheet",
            "Cash book",
            "Trial balance only",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "The balance sheet reports financial position.",
    ),

    Question(
        question_code="HS-COMMERCE-028",
        question=
        "Working capital is commonly:",
        options=[
            "Current assets - Current liabilities",
            "Fixed assets - Capital",
            "Sales - Purchases",
            "Profit - Tax",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "Working capital measures short-term operating liquidity.",
    ),

    Question(
        question_code="HS-COMMERCE-029",
        question=
        "A cash budget estimates:",
        options=[
            "Only profit",
            "Expected cash inflows and outflows",
            "Employee attendance",
            "Market share",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "Cash budgets forecast cash receipts and payments.",
    ),

    Question(
        question_code="HS-COMMERCE-030",
        question=
        "Break-even point occurs when:",
        options=[
            "Profit is maximum",
            "Total revenue equals total cost",
            "Sales are zero",
            "Fixed cost is zero",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "At break-even, there is no profit or loss.",
    ),

    Question(
        question_code="HS-COMMERCE-031",
        question=
        "Opportunity cost means:",
        options=[
            "Accounting expense",
            "Value of the next best alternative forgone",
            "Tax paid",
            "Interest earned",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,

        explanation=
        "Opportunity cost is the value of the next best alternative.",
    ),

    Question(
        question_code="HS-COMMERCE-032",
        question=
        "Demand generally falls when price rises, other things equal, because of:",
        options=[
            "Law of demand",
            "Law of supply",
            "Inflation only",
            "Accounting rule",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,

        explanation=
        "The law of demand describes the inverse price-demand relationship, ceteris paribus.",
    ),

    Question(
        question_code="HS-COMMERCE-033",
        question=
        "Inflation means:",
        options=[
            "Fall in general price level",
            "Sustained rise in general price level",
            "Rise in one product only",
            "Fall in money supply only",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,

        explanation=
        "Inflation is a sustained increase in the general price level.",
    ),

    Question(
        question_code="HS-COMMERCE-034",
        question=
        "GDP measures the value of:",
        options=[
            "All second-hand sales",
            "Final goods and services produced within an economy",
            "Only exports",
            "Only government spending",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,

        explanation=
        "GDP measures final production within a geographic boundary.",
    ),

    Question(
        question_code="HS-COMMERCE-035",
        question=
        "A market with a single seller is called:",
        options=[
            "Perfect competition",
            "Monopoly",
            "Oligopoly",
            "Monopsony",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,

        explanation=
        "A monopoly has one dominant seller.",
    ),

    Question(
        question_code="HS-COMMERCE-036",
        question=
        "Fiscal policy primarily uses:",
        options=[
            "Government spending and taxation",
            "Interest rates only",
            "Bank reserves only",
            "Exchange rates only",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,

        explanation=
        "Fiscal policy concerns government revenue and expenditure.",
    ),

    Question(
        question_code="HS-COMMERCE-037",
        question=
        "Monetary policy is generally conducted by:",
        options=[
            "Central bank",
            "Retailer",
            "Household",
            "Stock exchange",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,

        explanation=
        "Central banks use monetary policy tools to influence money and credit conditions.",
    ),

    Question(
        question_code="HS-COMMERCE-038",
        question=
        "Price elasticity of demand measures responsiveness of quantity demanded to:",
        options=[
            "Income",
            "Price",
            "Advertising only",
            "Population",
        ],
        answer="B",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,

        explanation=
        "Price elasticity relates quantity demanded to price changes.",
    ),

    Question(
        question_code="HS-COMMERCE-039",
        question=
        "A business plan mainly helps an entrepreneur:",
        options=[
            "Avoid all risk",
            "Define goals, strategy and resources",
            "Guarantee profit",
            "Eliminate competition",
        ],
        answer="B",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BUSINESS,

        explanation=
        "A business plan structures objectives, strategy, market and resource requirements.",
    ),

    Question(
        question_code="HS-COMMERCE-040",
        question=
        "Marketing mix is commonly summarized as:",
        options=[
            "4Ps",
            "4Cs only",
            "3Rs",
            "5Es",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BUSINESS,

        explanation=
        "The traditional marketing mix includes product, price, place and promotion.",
    ),

    Question(
        question_code="HS-COMMERCE-041",
        question=
        "Branding primarily helps a company:",
        options=[
            "Differentiate its offering",
            "Eliminate costs",
            "Avoid customers",
            "Stop innovation",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BUSINESS,

        explanation=
        "Branding creates identity and differentiation.",
    ),

    Question(
        question_code="HS-COMMERCE-042",
        question=
        "Market segmentation means:",
        options=[
            "Dividing a market into groups with similar needs",
            "Increasing prices randomly",
            "Removing products",
            "Ignoring customers",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BUSINESS,

        explanation=
        "Segmentation groups customers by shared characteristics or needs.",
    ),

    Question(
        question_code="HS-COMMERCE-043",
        question=
        "A sole proprietorship is owned by:",
        options=[
            "One person",
            "Shareholders only",
            "Government only",
            "Two corporations",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BUSINESS,

        explanation=
        "A sole proprietorship has a single owner.",
    ),

    Question(
        question_code="HS-COMMERCE-044",
        question=
        "Delegation means:",
        options=[
            "Assigning authority and responsibility to others",
            "Avoiding responsibility",
            "Removing all controls",
            "Doing every task alone",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.LEADERSHIP,

        explanation=
        "Delegation distributes work while retaining accountability.",
    ),

    Question(
        question_code="HS-COMMERCE-045",
        question=
        "A SMART goal should be:",
        options=[
            "Specific and measurable",
            "Secret and random",
            "Only ambitious",
            "Without a deadline",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.BUSINESS,

        explanation=
        "SMART goals are specific, measurable, achievable, relevant and time-bound.",
    ),

    Question(
        question_code="HS-COMMERCE-046",
        question=
        "Cash flow from operations relates mainly to:",
        options=[
            "Core business activities",
            "Only buying shares",
            "Only borrowing",
            "Only dividends",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "Operating cash flow comes from the company's main revenue-generating activities.",
    ),

    Question(
        question_code="HS-COMMERCE-047",
        question=
        "Inventory is classified as a:",
        options=[
            "Current asset",
            "Long-term liability",
            "Revenue",
            "Capital reserve",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "Inventory is normally a current asset.",
    ),

    Question(
        question_code="HS-COMMERCE-048",
        question=
        "A balance sheet is prepared to show:",
        options=[
            "Financial position at a point in time",
            "Only monthly sales",
            "Only employee salaries",
            "Only cash receipts",
        ],
        answer="A",
        difficulty=Difficulty.EASY,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ACCOUNTING,

        explanation=
        "It reports assets, liabilities and equity at a specific date.",
    ),

    Question(
        question_code="HS-COMMERCE-049",
        question=
        "Consumer surplus is the difference between:",
        options=[
            "Willingness to pay and actual price",
            "Revenue and cost",
            "Price and tax",
            "Assets and liabilities",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,

        explanation=
        "Consumer surplus measures the benefit from paying less than willingness to pay.",
    ),

    Question(
        question_code="HS-COMMERCE-050",
        question=
        "A decrease in supply, with demand unchanged, generally causes equilibrium price to:",
        options=[
            "Rise",
            "Fall",
            "Become zero",
            "Stay always unchanged",
        ],
        answer="A",
        difficulty=Difficulty.MEDIUM,
        question_type=QuestionType.ASSESSMENT,
        topic=Topic.ECONOMICS,

        explanation=
        "A leftward supply shift tends to raise equilibrium price.",
    ),
]