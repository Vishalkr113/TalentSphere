"""
Aptitude Question Bank

Module:
- Quantitative Aptitude
- Percentage

Range:
APT-PERCENT-001 to APT-PERCENT-020
"""


from .enums import (
    Difficulty,
    QuestionType,
)

from .schemas import Question



APTITUDE_QUESTIONS: list[Question] = [


    Question(

        question_code="APT-PERCENT-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is increased by 20%. What is the new value of 500?",

        option_a="550",

        option_b="600",

        option_c="620",

        option_d="650",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="percentage_increase",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is decreased by 20%. What is the new value of 800?",

        option_a="620",

        option_b="640",

        option_c="680",

        option_d="700",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="percentage_decrease",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "20% of 450 is:",

        option_a="80",

        option_b="90",

        option_c="100",

        option_d="120",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="percentage",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A salary of ₹40000 is increased by 15%. What is the new salary?",

        option_a="44000",

        option_b="45000",

        option_c="46000",

        option_d="47000",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="percentage",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A value changes from 200 to 250. Percentage increase is:",

        option_a="20%",

        option_b="25%",

        option_c="30%",

        option_d="35%",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="percentage",

        skill="comparison",

    ),

        Question(

        question_code="APT-PERCENT-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A student scored 360 marks out of 500. What is his percentage?",

        option_a="62%",

        option_b="68%",

        option_c="72%",

        option_d="75%",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="percentage_conversion",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The price of a product increases from ₹800 to ₹960. Find the percentage increase.",

        option_a="15%",

        option_b="20%",

        option_c="25%",

        option_d="30%",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="percentage_increase",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is first increased by 10% and then decreased by 10%. What is the overall change?",

        option_a="No change",

        option_b="1% increase",

        option_c="1% decrease",

        option_d="2% decrease",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="successive_percentage",

        skill="logical_calculation",

    ),



    Question(

        question_code="APT-PERCENT-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If 40% of a number is 120, then the number is:",

        option_a="200",

        option_b="250",

        option_c="300",

        option_d="350",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="percentage_reverse",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A value decreases from 500 to 425. What is the percentage decrease?",

        option_a="10%",

        option_b="12%",

        option_c="15%",

        option_d="20%",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="percentage_decrease",

        skill="calculation",

    ),


    Question(

        question_code="APT-PERCENT-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is 25% more than 200. The number is:",

        option_a="225",

        option_b="250",

        option_c="275",

        option_d="300",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="percentage_increase",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is reduced by 30% and becomes 350. The original number was:",

        option_a="450",

        option_b="500",

        option_c="550",

        option_d="600",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="reverse_percentage",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "In an exam, a student gets 420 marks out of 600. Percentage obtained is:",

        option_a="60%",

        option_b="65%",

        option_c="70%",

        option_d="75%",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="marks_percentage",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The population of a city increases from 80000 to 92000. Percentage increase is:",

        option_a="10%",

        option_b="12%",

        option_c="15%",

        option_d="20%",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="population_percentage",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A shopkeeper gives 20% discount on an item priced at ₹1500. Selling price is:",

        option_a="1100",

        option_b="1200",

        option_c="1250",

        option_d="1300",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="discount",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If a number is increased by 50%, it becomes 450. Original number was:",

        option_a="250",

        option_b="300",

        option_c="350",

        option_d="400",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="reverse_percentage",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A person's income increases by 25% and expenses increase by 20%. If income was ₹40000, new income is:",

        option_a="45000",

        option_b="48000",

        option_c="50000",

        option_d="52000",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="income_percentage",

        skill="application",

    ),



    Question(

        question_code="APT-PERCENT-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A value decreases by 40%. If original value was 750, new value is:",

        option_a="400",

        option_b="450",

        option_c="500",

        option_d="550",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="percentage_decrease",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERCENT-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is increased by 30% and then increased by 20%. Total increase is:",

        option_a="50%",

        option_b="56%",

        option_c="60%",

        option_d="62%",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="successive_percentage",

        skill="logical_calculation",

    ),



    Question(

        question_code="APT-PERCENT-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is decreased by 20% and then increased by 20%. Overall change is:",

        option_a="No change",

        option_b="4% increase",

        option_c="4% decrease",

        option_d="8% decrease",

        correct_answer="C",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="percentage",

        sub_topic="successive_percentage",

        skill="logical_calculation",

    ),

        Question(

        question_code="APT-RATIO-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The ratio of two numbers is 3:5. If their sum is 64, the larger number is:",

        option_a="24",

        option_b="32",

        option_c="40",

        option_d="48",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="basic_ratio",

        skill="calculation",

    ),


    Question(

        question_code="APT-RATIO-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The ratio of boys and girls in a class is 5:3. If total students are 64, number of girls are:",

        option_a="20",

        option_b="24",

        option_c="32",

        option_d="40",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="division_of_quantity",

        skill="calculation",

    ),


    Question(

        question_code="APT-RATIO-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If A:B = 4:7 and B:C = 14:15, then A:B:C is:",

        option_a="4:7:15",

        option_b="8:14:15",

        option_c="14:7:15",

        option_d="8:7:15",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="compound_ratio",

        skill="logical_calculation",

    ),


    Question(

        question_code="APT-RATIO-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Divide ₹900 in the ratio 2:3. The smaller share is:",

        option_a="300",

        option_b="360",

        option_c="400",

        option_d="540",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="division_ratio",

        skill="calculation",

    ),


    Question(

        question_code="APT-RATIO-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The ages of A and B are in the ratio 4:5. If their total age is 45 years, age of B is:",

        option_a="20",

        option_b="25",

        option_c="30",

        option_d="35",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="age_ratio",

        skill="calculation",

    ),


    Question(

        question_code="APT-RATIO-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If 5 pens cost ₹100, then cost of 8 pens is:",

        option_a="120",

        option_b="140",

        option_c="160",

        option_d="180",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="direct_proportion",

        skill="calculation",

    ),


    Question(

        question_code="APT-RATIO-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If x:y = 2:3 and y:z = 4:5, then x:y:z is:",

        option_a="8:12:15",

        option_b="2:3:5",

        option_c="4:6:5",

        option_d="8:6:15",

        correct_answer="A",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="combined_ratio",

        skill="logical_calculation",

    ),


    Question(

        question_code="APT-RATIO-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The ratio of income and expenditure of a person is 5:3. If savings are ₹8000, income is:",

        option_a="15000",

        option_b="20000",

        option_c="25000",

        option_d="30000",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="income_ratio",

        skill="application",

    ),


    Question(

        question_code="APT-RATIO-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Two numbers are in ratio 7:9 and their difference is 18. The smaller number is:",

        option_a="42",

        option_b="54",

        option_c="63",

        option_d="72",

        correct_answer="A",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="difference_ratio",

        skill="calculation",

    ),


    Question(

        question_code="APT-RATIO-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If 12 workers complete a work in 10 days, 15 workers will complete it in:",

        option_a="6 days",

        option_b="8 days",

        option_c="10 days",

        option_d="12 days",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="inverse_proportion",

        skill="application",

    ),

        Question(

        question_code="APT-PROFIT-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "An article is bought for ₹800 and sold for ₹960. What is the profit percentage?",

        option_a="15%",

        option_b="20%",

        option_c="25%",

        option_d="30%",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="profit_percentage",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROFIT-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A product is purchased for ₹500 and sold for ₹450. Find the loss percentage.",

        option_a="5%",

        option_b="10%",

        option_c="15%",

        option_d="20%",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="loss_percentage",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROFIT-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A shopkeeper buys an item for ₹1200 and gains 25%. Selling price is:",

        option_a="1400",

        option_b="1450",

        option_c="1500",

        option_d="1600",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="selling_price",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROFIT-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "An item is sold for ₹720 after a loss of 10%. What was its cost price?",

        option_a="700",

        option_b="750",

        option_c="800",

        option_d="850",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="cost_price",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROFIT-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A trader buys a watch for ₹2000 and sells it at 15% profit. Selling price is:",

        option_a="2200",

        option_b="2300",

        option_c="2400",

        option_d="2500",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="profit_calculation",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROFIT-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If cost price is ₹1500 and selling price is ₹1800, profit is:",

        option_a="200",

        option_b="250",

        option_c="300",

        option_d="350",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="profit_amount",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROFIT-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A seller earns 20% profit by selling an item for ₹600. Cost price is:",

        option_a="450",

        option_b="500",

        option_c="550",

        option_d="580",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="reverse_profit",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROFIT-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A book is sold at ₹540 with 10% profit. Cost price of book is:",

        option_a="450",

        option_b="480",

        option_c="500",

        option_d="520",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="cost_price",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROFIT-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A trader sells an item for ₹960 with 20% loss. Cost price is:",

        option_a="1100",

        option_b="1200",

        option_c="1250",

        option_d="1300",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="loss_calculation",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROFIT-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A man buys an article for ₹2500 and sells it for ₹3000. Profit percentage is:",

        option_a="15%",

        option_b="18%",

        option_c="20%",

        option_d="25%",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="profit_percentage",

        skill="calculation",

    ),

    Question(

        question_code="APT-PROFIT-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A trader buys an article for ₹1500 and sells it for ₹1800. The profit percentage is:",

        option_a="15%",

        option_b="18%",

        option_c="20%",

        option_d="25%",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="profit_percentage",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROFIT-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "An item is sold for ₹960 after making a profit of 20%. The cost price is:",

        option_a="700",

        option_b="800",

        option_c="850",

        option_d="900",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="cost_price",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROFIT-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A shopkeeper marks an article at ₹1000 and gives a discount of 10%. If the cost price is ₹800, the profit percentage is:",

        option_a="10%",

        option_b="12.5%",

        option_c="15%",

        option_d="20%",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="discount_profit",

        skill="application",

    ),



    Question(

        question_code="APT-PROFIT-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A man sells an article at 25% profit. If the cost price is ₹2400, selling price is:",

        option_a="2800",

        option_b="3000",

        option_c="3200",

        option_d="3500",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="selling_price",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROFIT-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "An article bought for ₹1200 is sold at a loss of 15%. Selling price is:",

        option_a="980",

        option_b="1000",

        option_c="1020",

        option_d="1050",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="loss_percentage",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROFIT-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A dealer buys a product for ₹4000 and spends ₹500 on repair. If he sells it for ₹5400, his profit percentage is:",

        option_a="10%",

        option_b="15%",

        option_c="20%",

        option_d="25%",

        correct_answer="A",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="effective_cost_price",

        skill="application",

    ),



    Question(

        question_code="APT-PROFIT-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A shopkeeper sells an item for ₹750 and gains 25%. Cost price of the item is:",

        option_a="500",

        option_b="550",

        option_c="600",

        option_d="650",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="reverse_profit",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROFIT-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A trader wants to earn 30% profit on an item costing ₹2000. The selling price should be:",

        option_a="2400",

        option_b="2500",

        option_c="2600",

        option_d="2800",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="profit_target",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROFIT-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A product is sold for ₹1380 with a profit of 15%. The cost price is:",

        option_a="1100",

        option_b="1200",

        option_c="1250",

        option_d="1300",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="reverse_profit",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROFIT-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A seller gains 12% by selling an article for ₹2240. The cost price is:",

        option_a="1800",

        option_b="1900",

        option_c="2000",

        option_d="2100",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="profit_loss",

        sub_topic="profit_percentage",

        skill="calculation",

    ),

    Question(

        question_code="APT-AVERAGE-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of 5 numbers is 20. Their total sum is:",

        option_a="80",

        option_b="90",

        option_c="100",

        option_d="120",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="basic_average",

        skill="calculation",

    ),


    Question(

        question_code="APT-AVERAGE-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of 8 numbers is 15. The sum of these numbers is:",

        option_a="100",

        option_b="120",

        option_c="140",

        option_d="160",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="basic_average",

        skill="calculation",

    ),


    Question(

        question_code="APT-AVERAGE-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average age of 4 students is 18 years. Their total age is:",

        option_a="64",

        option_b="72",

        option_c="76",

        option_d="80",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="average_sum",

        skill="calculation",

    ),


    Question(

        question_code="APT-AVERAGE-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of three numbers is 25. If two numbers are 20 and 30, the third number is:",

        option_a="20",

        option_b="25",

        option_c="30",

        option_d="35",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="missing_number",

        skill="calculation",

    ),


    Question(

        question_code="APT-AVERAGE-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average marks of 6 subjects is 75. Total marks obtained are:",

        option_a="400",

        option_b="425",

        option_c="450",

        option_d="475",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="marks_average",

        skill="calculation",

    ),


    Question(

        question_code="APT-AVERAGE-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of 10 numbers is 45. If one number is removed, average becomes 40. Removed number is:",

        option_a="80",

        option_b="85",

        option_c="90",

        option_d="95",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="removal_average",

        skill="logical_calculation",

    ),


    Question(

        question_code="APT-AVERAGE-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average weight of 5 persons is 60 kg. If one person leaves, average becomes 55 kg. Weight of the person who left is:",

        option_a="70 kg",

        option_b="75 kg",

        option_c="80 kg",

        option_d="85 kg",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="removal_average",

        skill="application",

    ),


    Question(

        question_code="APT-AVERAGE-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of first 10 natural numbers is:",

        option_a="5",

        option_b="5.5",

        option_c="6",

        option_d="6.5",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="natural_numbers",

        skill="calculation",

    ),


    Question(

        question_code="APT-AVERAGE-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of 7 consecutive numbers is 30. The middle number is:",

        option_a="28",

        option_b="29",

        option_c="30",

        option_d="31",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="consecutive_numbers",

        skill="logical_calculation",

    ),


    Question(

        question_code="APT-AVERAGE-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average salary of 20 employees is ₹30000. Total salary is:",

        option_a="500000",

        option_b="550000",

        option_c="600000",

        option_d="650000",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="salary_average",

        skill="calculation",

    ),

        Question(

        question_code="APT-AVERAGE-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of 6 numbers is 35. If one number is added, the average becomes 40. The added number is:",

        option_a="60",

        option_b="65",

        option_c="70",

        option_d="75",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="addition_average",

        skill="calculation",

    ),


    Question(

        question_code="APT-AVERAGE-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average marks of 30 students is 60. If the average marks of boys is 70 and girls is 50, the ratio of boys to girls is:",

        option_a="1:1",

        option_b="2:1",

        option_c="1:2",

        option_d="3:2",

        correct_answer="A",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="weighted_average",

        skill="logical_calculation",

    ),


    Question(

        question_code="APT-AVERAGE-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of 12 numbers is 25. If each number is increased by 5, the new average will be:",

        option_a="25",

        option_b="30",

        option_c="35",

        option_d="40",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="average_change",

        skill="concept",

    ),


    Question(

        question_code="APT-AVERAGE-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average temperature of Monday to Wednesday is 30°C and Wednesday to Friday is 32°C. If Wednesday temperature is 31°C, average temperature of all five days is:",

        option_a="30°C",

        option_b="31°C",

        option_c="32°C",

        option_d="33°C",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="combined_average",

        skill="logical_calculation",

    ),


    Question(

        question_code="APT-AVERAGE-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average age of 8 players is 24 years. A new player joins and average becomes 25 years. Age of new player is:",

        option_a="30",

        option_b="32",

        option_c="33",

        option_d="35",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="joining_average",

        skill="calculation",

    ),


    Question(

        question_code="APT-AVERAGE-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of 15 numbers is 40. The average of first 8 numbers is 35 and last 8 numbers is 45. The middle number is:",

        option_a="35",

        option_b="40",

        option_c="45",

        option_d="50",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="overlapping_average",

        skill="logical_calculation",

    ),


    Question(

        question_code="APT-AVERAGE-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of 9 numbers is 50. If one number 70 is replaced by 88, the new average is:",

        option_a="51",

        option_b="52",

        option_c="53",

        option_d="54",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="replacement_average",

        skill="calculation",

    ),


    Question(

        question_code="APT-AVERAGE-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A batsman has an average score of 45 runs in 10 innings. How many runs must he score in the 11th inning to make average 50?",

        option_a="90",

        option_b="95",

        option_c="100",

        option_d="105",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="target_average",

        skill="application",

    ),


    Question(

        question_code="APT-AVERAGE-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average weight of 10 students increases by 2 kg when one student weighing 40 kg is replaced. The new student's weight is:",

        option_a="55 kg",

        option_b="60 kg",

        option_c="65 kg",

        option_d="70 kg",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="replacement_average",

        skill="application",

    ),


    Question(

        question_code="APT-AVERAGE-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of 20 numbers is 18. If two numbers 12 and 16 are removed, the average of remaining numbers is:",

        option_a="18",

        option_b="18.2",

        option_c="18.5",

        option_d="19",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="average",

        sub_topic="removal_average",

        skill="logical_calculation",

    ),

        Question(

        question_code="APT-TIME-WORK-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A can complete a work in 10 days. How many days will A take to complete half of the work?",

        option_a="3 days",

        option_b="5 days",

        option_c="7 days",

        option_d="10 days",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="basic_work",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If A completes a work in 12 days, his one day work is:",

        option_a="1/6",

        option_b="1/10",

        option_c="1/12",

        option_d="12",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="work_efficiency",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A can do a work in 15 days and B can do it in 20 days. Together they can complete the work in:",

        option_a="8 days",

        option_b="9 days",

        option_c="10 days",

        option_d="12 days",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="combined_work",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A and B together complete a work in 12 days. If A alone takes 20 days, B alone will take:",

        option_a="25 days",

        option_b="30 days",

        option_c="35 days",

        option_d="40 days",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="combined_work",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "10 workers complete a work in 15 days. How many workers are required to complete the same work in 5 days?",

        option_a="20",

        option_b="25",

        option_c="30",

        option_d="35",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="worker_efficiency",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A can do a work in 8 days and B can do it in 24 days. Their efficiency ratio is:",

        option_a="1:2",

        option_b="2:3",

        option_c="3:1",

        option_d="4:1",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="efficiency_ratio",

        skill="logical_calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If 5 men complete a work in 20 days, 10 men will complete it in:",

        option_a="5 days",

        option_b="10 days",

        option_c="15 days",

        option_d="20 days",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="men_days",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A can finish a work in 18 days. After working for 6 days, remaining work is:",

        option_a="1/2",

        option_b="2/3",

        option_c="1/3",

        option_d="1/4",

        correct_answer="A",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="remaining_work",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A and B can complete a work in 6 days. If A alone can do it in 10 days, B alone can do it in:",

        option_a="12 days",

        option_b="15 days",

        option_c="18 days",

        option_d="20 days",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="combined_efficiency",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "12 workers complete a work in 18 days. After 6 days, 6 more workers join. Remaining work will complete in:",

        option_a="6 days",

        option_b="8 days",

        option_c="10 days",

        option_d="12 days",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="multiple_workers",

        skill="application",

    ),

        Question(

        question_code="APT-TIME-WORK-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A can do a work in 16 days and B can do the same work in 24 days. Together they will complete the work in:",

        option_a="8 days",

        option_b="9.6 days",

        option_c="10 days",

        option_d="12 days",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="combined_work",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A and B together can complete a work in 8 days. B alone can complete it in 12 days. A alone can complete it in:",

        option_a="18 days",

        option_b="20 days",

        option_c="24 days",

        option_d="30 days",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="combined_work",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "15 workers complete a work in 12 days. After 4 days, 5 workers leave. Remaining work will be completed in:",

        option_a="8 days",

        option_b="10 days",

        option_c="12 days",

        option_d="15 days",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="worker_change",

        skill="application",

    ),



    Question(

        question_code="APT-TIME-WORK-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A takes 30 days to complete a work. B is 50% more efficient than A. B alone can complete the work in:",

        option_a="15 days",

        option_b="20 days",

        option_c="25 days",

        option_d="30 days",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="efficiency",

        skill="logical_calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A, B and C can complete a work in 10, 15 and 30 days respectively. Together they can complete the work in:",

        option_a="4 days",

        option_b="5 days",

        option_c="6 days",

        option_d="8 days",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="three_person_work",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If 20 men can build a wall in 15 days, 25 men can build the same wall in:",

        option_a="10 days",

        option_b="12 days",

        option_c="15 days",

        option_d="18 days",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="men_days",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A completes 40% of a work in 8 days. Total time required to complete the work is:",

        option_a="16 days",

        option_b="18 days",

        option_c="20 days",

        option_d="24 days",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="percentage_work",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A and B together finish a work in 15 days. They work together for 5 days. Remaining work is:",

        option_a="1/2",

        option_b="2/3",

        option_c="1/3",

        option_d="1/4",

        correct_answer="A",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="remaining_work",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "8 workers complete a work in 24 days. How many days will 12 workers take to complete the same work?",

        option_a="12 days",

        option_b="14 days",

        option_c="16 days",

        option_d="18 days",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="inverse_proportion",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-WORK-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A can complete a work in 25 days and B can complete it in 50 days. If they work on alternate days starting with A, the work will be completed in:",

        option_a="15 days",

        option_b="16 days",

        option_c="17 days",

        option_d="18 days",

        correct_answer="C",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="time_work",

        sub_topic="alternate_work",

        skill="application",

    ),

        Question(

        question_code="APT-TIME-DISTANCE-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A car travels 240 km in 4 hours. What is its speed?",

        option_a="50 km/hr",

        option_b="60 km/hr",

        option_c="70 km/hr",

        option_d="80 km/hr",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="basic_speed",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A train covers 360 km in 6 hours. Its average speed is:",

        option_a="50 km/hr",

        option_b="60 km/hr",

        option_c="70 km/hr",

        option_d="80 km/hr",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="average_speed",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A man walks at 5 km/hr and reaches his destination in 6 hours. Distance travelled is:",

        option_a="25 km",

        option_b="30 km",

        option_c="35 km",

        option_d="40 km",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="distance_calculation",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A train moving at 72 km/hr covers a distance in 5 hours. Distance covered is:",

        option_a="320 km",

        option_b="340 km",

        option_c="360 km",

        option_d="380 km",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="distance_calculation",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If a car speed is increased from 40 km/hr to 60 km/hr, the ratio of speeds is:",

        option_a="1:2",

        option_b="2:3",

        option_c="3:4",

        option_d="4:5",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="speed_ratio",

        skill="comparison",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A person travels 150 km in 3 hours. If speed remains same, distance covered in 5 hours is:",

        option_a="200 km",

        option_b="225 km",

        option_c="250 km",

        option_d="300 km",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="direct_proportion",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A train runs at 90 km/hr. How much distance will it cover in 20 minutes?",

        option_a="20 km",

        option_b="25 km",

        option_c="30 km",

        option_d="35 km",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="time_conversion",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A person increases his speed by 25%. Time taken for the same distance will:",

        option_a="Increase by 25%",

        option_b="Decrease by 20%",

        option_c="Decrease by 25%",

        option_d="Remain same",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="speed_time_relation",

        skill="concept",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A bus covers 480 km at a speed of 80 km/hr. Time taken is:",

        option_a="4 hours",

        option_b="5 hours",

        option_c="6 hours",

        option_d="7 hours",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="time_calculation",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A train covers 600 km in 10 hours. Its speed in m/s is:",

        option_a="15 m/s",

        option_b="16.67 m/s",

        option_c="18 m/s",

        option_d="20 m/s",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="unit_conversion",

        skill="calculation",

    ),

        Question(

        question_code="APT-TIME-DISTANCE-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Two cars travel the same distance at speeds of 40 km/hr and 60 km/hr. The ratio of time taken is:",

        option_a="2:3",

        option_b="3:2",

        option_c="1:2",

        option_d="4:5",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="speed_time_relation",

        skill="logical_calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A train 200 meters long crosses a pole in 10 seconds. Speed of the train is:",

        option_a="15 m/s",

        option_b="20 m/s",

        option_c="25 m/s",

        option_d="30 m/s",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="train_speed",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A train moving at 54 km/hr crosses a platform in 30 seconds. Total distance covered is:",

        option_a="400 m",

        option_b="450 m",

        option_c="500 m",

        option_d="550 m",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="train_platform",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A boat covers 30 km downstream in 3 hours. Speed of boat in downstream is:",

        option_a="5 km/hr",

        option_b="8 km/hr",

        option_c="10 km/hr",

        option_d="12 km/hr",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="boat_stream",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A boat moves at 12 km/hr in still water and stream speed is 3 km/hr. Downstream speed is:",

        option_a="9 km/hr",

        option_b="12 km/hr",

        option_c="15 km/hr",

        option_d="18 km/hr",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="boat_stream",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A person travels half distance at 40 km/hr and remaining half at 60 km/hr. Average speed is:",

        option_a="45 km/hr",

        option_b="48 km/hr",

        option_c="50 km/hr",

        option_d="55 km/hr",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="average_speed",

        skill="logical_calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A cyclist travels at 12 km/hr. How much time will he take to cover 36 km?",

        option_a="2 hours",

        option_b="3 hours",

        option_c="4 hours",

        option_d="5 hours",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="time_calculation",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A train running at 72 km/hr crosses a man standing on platform in 15 seconds. Length of train is:",

        option_a="250 m",

        option_b="300 m",

        option_c="350 m",

        option_d="400 m",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="train_problem",

        skill="calculation",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A man covers a distance in 8 hours. If his speed increases by 5 km/hr, he takes 6 hours. Original speed is:",

        option_a="10 km/hr",

        option_b="12 km/hr",

        option_c="15 km/hr",

        option_d="20 km/hr",

        correct_answer="C",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="speed_difference",

        skill="problem_solving",

    ),



    Question(

        question_code="APT-TIME-DISTANCE-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A train travels first 120 km at 60 km/hr and next 120 km at 40 km/hr. Average speed for entire journey is:",

        option_a="45 km/hr",

        option_b="48 km/hr",

        option_c="50 km/hr",

        option_d="55 km/hr",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="time_speed_distance",

        sub_topic="average_speed",

        skill="logical_calculation",

    ),

        Question(

        question_code="APT-NUMBER-SYSTEM-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The smallest prime number is:",

        option_a="0",

        option_b="1",

        option_c="2",

        option_d="3",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="prime_number",

        skill="concept",

    ),


    Question(

        question_code="APT-NUMBER-SYSTEM-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The HCF of 12 and 18 is:",

        option_a="3",

        option_b="6",

        option_c="9",

        option_d="12",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="hcf",

        skill="calculation",

    ),


    Question(

        question_code="APT-NUMBER-SYSTEM-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The LCM of 8 and 12 is:",

        option_a="16",

        option_b="20",

        option_c="24",

        option_d="36",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="lcm",

        skill="calculation",

    ),


    Question(

        question_code="APT-NUMBER-SYSTEM-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Which of the following is an even number?",

        option_a="37",

        option_b="49",

        option_c="52",

        option_d="75",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="even_odd",

        skill="concept",

    ),


    Question(

        question_code="APT-NUMBER-SYSTEM-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The remainder when 25 is divided by 4 is:",

        option_a="0",

        option_b="1",

        option_c="2",

        option_d="3",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="remainder",

        skill="calculation",

    ),


    Question(

        question_code="APT-NUMBER-SYSTEM-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The sum of first 10 natural numbers is:",

        option_a="45",

        option_b="50",

        option_c="55",

        option_d="60",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="natural_numbers",

        skill="calculation",

    ),


    Question(

        question_code="APT-NUMBER-SYSTEM-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The greatest two digit number is:",

        option_a="90",

        option_b="98",

        option_c="99",

        option_d="100",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="number_properties",

        skill="concept",

    ),


    Question(

        question_code="APT-NUMBER-SYSTEM-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The smallest composite number is:",

        option_a="1",

        option_b="2",

        option_c="3",

        option_d="4",

        correct_answer="D",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="composite_number",

        skill="concept",

    ),


    Question(

        question_code="APT-NUMBER-SYSTEM-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number divisible by both 2 and 3 is also divisible by:",

        option_a="4",

        option_b="5",

        option_c="6",

        option_d="9",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="divisibility",

        skill="concept",

    ),


    Question(

        question_code="APT-NUMBER-SYSTEM-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of 2³ × 2² is:",

        option_a="16",

        option_b="24",

        option_c="32",

        option_d="64",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="powers",

        skill="calculation",

    ),

        Question(

        question_code="APT-NUMBER-SYSTEM-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The number of factors of 12 is:",

        option_a="4",

        option_b="5",

        option_c="6",

        option_d="8",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="factors",

        skill="logical_calculation",

    ),



    Question(

        question_code="APT-NUMBER-SYSTEM-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Which of the following numbers is divisible by 9?",

        option_a="124",

        option_b="135",

        option_c="146",

        option_d="157",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="divisibility_rule",

        skill="concept",

    ),



    Question(

        question_code="APT-NUMBER-SYSTEM-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The unit digit of 7² is:",

        option_a="7",

        option_b="8",

        option_c="9",

        option_d="4",

        correct_answer="D",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="unit_digit",

        skill="calculation",

    ),



    Question(

        question_code="APT-NUMBER-SYSTEM-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The sum of first 20 natural numbers is:",

        option_a="200",

        option_b="210",

        option_c="220",

        option_d="230",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="natural_numbers",

        skill="calculation",

    ),



    Question(

        question_code="APT-NUMBER-SYSTEM-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If a number is multiplied by 5 and then divided by 5, the result is:",

        option_a="Same number",

        option_b="Double number",

        option_c="Half number",

        option_d="Zero",

        correct_answer="A",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="basic_operation",

        skill="concept",

    ),



    Question(

        question_code="APT-NUMBER-SYSTEM-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The difference between the greatest and smallest two digit numbers is:",

        option_a="88",

        option_b="89",

        option_c="90",

        option_d="91",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="number_properties",

        skill="calculation",

    ),



    Question(

        question_code="APT-NUMBER-SYSTEM-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of 3⁴ is:",

        option_a="27",

        option_b="64",

        option_c="81",

        option_d="100",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="powers",

        skill="calculation",

    ),



    Question(

        question_code="APT-NUMBER-SYSTEM-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number when divided by 5 gives remainder 3. Which can be the number?",

        option_a="10",

        option_b="13",

        option_c="15",

        option_d="20",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="remainder",

        skill="problem_solving",

    ),



    Question(

        question_code="APT-NUMBER-SYSTEM-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of first five odd numbers is:",

        option_a="3",

        option_b="5",

        option_c="7",

        option_d="9",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="odd_numbers",

        skill="calculation",

    ),



    Question(

        question_code="APT-NUMBER-SYSTEM-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The smallest number which is divisible by 12, 15 and 20 is:",

        option_a="40",

        option_b="50",

        option_c="60",

        option_d="120",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="number_system",

        sub_topic="lcm",

        skill="calculation",

    ),

        Question(

        question_code="APT-SIMPLIFICATION-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: 25 + 35 × 2",

        option_a="120",

        option_b="95",

        option_c="85",

        option_d="75",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="basic_operation",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: 48 ÷ 6 × 4",

        option_a="8",

        option_b="24",

        option_c="32",

        option_d="40",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="division_multiplication",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Find the value of: 15% of 200",

        option_a="20",

        option_b="25",

        option_c="30",

        option_d="35",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="percentage",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: (25 × 4) + (36 ÷ 6)",

        option_a="100",

        option_b="106",

        option_c="110",

        option_d="120",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="mixed_operation",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Find the value of: √144 + √81",

        option_a="19",

        option_b="20",

        option_c="21",

        option_d="22",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="square_root",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: 2³ + 3²",

        option_a="15",

        option_b="17",

        option_c="18",

        option_d="20",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="powers",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Find the value of: 40% of 500",

        option_a="150",

        option_b="180",

        option_c="200",

        option_d="250",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="percentage",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: 100 - 25 × 2",

        option_a="50",

        option_b="60",

        option_c="70",

        option_d="75",

        correct_answer="A",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="operator_precedence",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Find the value of: 7 × 8 + 12",

        option_a="56",

        option_b="64",

        option_c="68",

        option_d="72",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="basic_operation",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: (18 + 12) ÷ 5",

        option_a="5",

        option_b="6",

        option_c="7",

        option_d="8",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="brackets",

        skill="calculation",

    ),

        Question(

        question_code="APT-SIMPLIFICATION-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: 45 + 36 ÷ 6 × 5",

        option_a="65",

        option_b="70",

        option_c="75",

        option_d="80",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="operator_precedence",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Find the value of: (15² - 10²)",

        option_a="100",

        option_b="125",

        option_c="150",

        option_d="175",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="square_difference",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: 3/4 of 200",

        option_a="100",

        option_b="120",

        option_c="150",

        option_d="175",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="fraction",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Find the value of: 2.5 × 4 + 10",

        option_a="15",

        option_b="18",

        option_c="20",

        option_d="25",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="decimal_operation",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: 125 ÷ 5 + 15",

        option_a="35",

        option_b="40",

        option_c="45",

        option_d="50",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="division",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Find the value of: 5³ - 4³",

        option_a="31",

        option_b="61",

        option_c="81",

        option_d="125",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="cube",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: 18% of 250",

        option_a="35",

        option_b="40",

        option_c="45",

        option_d="50",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="percentage",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Find the value of: √225 + √25",

        option_a="15",

        option_b="18",

        option_c="20",

        option_d="25",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="square_root",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: (24 × 5) ÷ 8",

        option_a="10",

        option_b="12",

        option_c="15",

        option_d="20",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="mixed_operation",

        skill="calculation",

    ),


    Question(

        question_code="APT-SIMPLIFICATION-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Find the value of: 10² + 5² - 25",

        option_a="75",

        option_b="90",

        option_c="100",

        option_d="110",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="simplification",

        sub_topic="square_operation",

        skill="calculation",

    ),

        Question(

        question_code="APT-ALGEBRA-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If x + 5 = 12, then the value of x is:",

        option_a="5",

        option_b="6",

        option_c="7",

        option_d="8",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="linear_equation",

        skill="problem_solving",

    ),


    Question(

        question_code="APT-ALGEBRA-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Solve: 2x = 20",

        option_a="5",

        option_b="10",

        option_c="15",

        option_d="20",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="linear_equation",

        skill="calculation",

    ),


    Question(

        question_code="APT-ALGEBRA-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If 3x + 4 = 19, then x is:",

        option_a="3",

        option_b="4",

        option_c="5",

        option_d="6",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="linear_equation",

        skill="calculation",

    ),


    Question(

        question_code="APT-ALGEBRA-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Find the value of x if x² = 49:",

        option_a="5",

        option_b="6",

        option_c="7",

        option_d="8",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="quadratic_basic",

        skill="calculation",

    ),


    Question(

        question_code="APT-ALGEBRA-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If x = 5, find the value of 2x + 10:",

        option_a="15",

        option_b="20",

        option_c="25",

        option_d="30",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="substitution",

        skill="calculation",

    ),


    Question(

        question_code="APT-ALGEBRA-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Solve: x/5 = 8",

        option_a="30",

        option_b="35",

        option_c="40",

        option_d="45",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="linear_equation",

        skill="calculation",

    ),


    Question(

        question_code="APT-ALGEBRA-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If a + b = 10 and a = 6, then b is:",

        option_a="2",

        option_b="3",

        option_c="4",

        option_d="5",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="variables",

        skill="calculation",

    ),


    Question(

        question_code="APT-ALGEBRA-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: 5x + 3x",

        option_a="5x",

        option_b="6x",

        option_c="8x",

        option_d="10x",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="simplification",

        skill="concept",

    ),


    Question(

        question_code="APT-ALGEBRA-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If x - 7 = 15, value of x is:",

        option_a="20",

        option_b="21",

        option_c="22",

        option_d="23",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="linear_equation",

        skill="calculation",

    ),


    Question(

        question_code="APT-ALGEBRA-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of (a+b)² when a=2 and b=3 is:",

        option_a="20",

        option_b="25",

        option_c="30",

        option_d="35",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="identity",

        skill="calculation",

    ),

        Question(

        question_code="APT-ALGEBRA-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If 4x + 8 = 24, then value of x is:",

        option_a="2",

        option_b="3",

        option_c="4",

        option_d="5",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="linear_equation",

        skill="calculation",

    ),



    Question(

        question_code="APT-ALGEBRA-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If x² - 16 = 0, then the positive value of x is:",

        option_a="2",

        option_b="3",

        option_c="4",

        option_d="8",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="quadratic_equation",

        skill="calculation",

    ),



    Question(

        question_code="APT-ALGEBRA-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If 2x + 5 = 15, value of x is:",

        option_a="3",

        option_b="4",

        option_c="5",

        option_d="6",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="linear_equation",

        skill="calculation",

    ),



    Question(

        question_code="APT-ALGEBRA-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Simplify: 3a + 5a - 2a",

        option_a="4a",

        option_b="5a",

        option_c="6a",

        option_d="8a",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="simplification",

        skill="concept",

    ),



    Question(

        question_code="APT-ALGEBRA-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If y = 3x + 2 and x = 4, value of y is:",

        option_a="12",

        option_b="14",

        option_c="16",

        option_d="18",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="substitution",

        skill="calculation",

    ),



    Question(

        question_code="APT-ALGEBRA-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The solution of equation x + x + 10 = 30 is:",

        option_a="5",

        option_b="10",

        option_c="15",

        option_d="20",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="linear_equation",

        skill="calculation",

    ),



    Question(

        question_code="APT-ALGEBRA-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Find the value of x if 5x = 45:",

        option_a="7",

        option_b="8",

        option_c="9",

        option_d="10",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="linear_equation",

        skill="calculation",

    ),



    Question(

        question_code="APT-ALGEBRA-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If a = 5 and b = 4, then value of a² + b² is:",

        option_a="35",

        option_b="40",

        option_c="41",

        option_d="45",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="substitution",

        skill="calculation",

    ),



    Question(

        question_code="APT-ALGEBRA-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Solve: 3x - 9 = 12",

        option_a="5",

        option_b="6",

        option_c="7",

        option_d="8",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="linear_equation",

        skill="calculation",

    ),



    Question(

        question_code="APT-ALGEBRA-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If x = 2, find the value of x³ + x²:",

        option_a="10",

        option_b="12",

        option_c="14",

        option_d="16",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="algebra",

        sub_topic="powers",

        skill="calculation",

    ),

        Question(

        question_code="APT-PROBABILITY-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A coin is tossed once. Probability of getting a head is:",

        option_a="1/4",

        option_b="1/2",

        option_c="3/4",

        option_d="1",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="basic_probability",

        skill="concept",

    ),


    Question(

        question_code="APT-PROBABILITY-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A dice is rolled once. Probability of getting 6 is:",

        option_a="1/2",

        option_b="1/3",

        option_c="1/6",

        option_d="5/6",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="dice",

        skill="concept",

    ),


    Question(

        question_code="APT-PROBABILITY-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A bag contains 5 red balls and 5 blue balls. Probability of selecting a red ball is:",

        option_a="1/5",

        option_b="1/2",

        option_c="2/5",

        option_d="3/5",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="selection",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROBABILITY-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The probability of an impossible event is:",

        option_a="0",

        option_b="1",

        option_c="1/2",

        option_d="2",

        correct_answer="A",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="basic_probability",

        skill="concept",

    ),


    Question(

        question_code="APT-PROBABILITY-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The probability of a certain event is:",

        option_a="0",

        option_b="1/2",

        option_c="1",

        option_d="2",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="basic_probability",

        skill="concept",

    ),


    Question(

        question_code="APT-PROBABILITY-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A card is drawn from a standard deck. Probability of getting an ace is:",

        option_a="1/13",

        option_b="1/26",

        option_c="4/13",

        option_d="1/52",

        correct_answer="A",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="cards",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROBABILITY-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Probability of getting an even number on a dice is:",

        option_a="1/6",

        option_b="1/3",

        option_c="1/2",

        option_d="2/3",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="dice",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROBABILITY-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Two coins are tossed together. Total possible outcomes are:",

        option_a="2",

        option_b="3",

        option_c="4",

        option_d="6",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="coin",

        skill="concept",

    ),


    Question(

        question_code="APT-PROBABILITY-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Probability of getting two heads when two coins are tossed is:",

        option_a="1/2",

        option_b="1/3",

        option_c="1/4",

        option_d="3/4",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="coin",

        skill="calculation",

    ),


    Question(

        question_code="APT-PROBABILITY-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A dice is rolled. Probability of getting a number greater than 4 is:",

        option_a="1/6",

        option_b="1/3",

        option_c="1/2",

        option_d="2/3",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="dice",

        skill="calculation",

    ),

        Question(

        question_code="APT-PROBABILITY-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A bag contains 4 white and 6 black balls. Probability of selecting a black ball is:",

        option_a="2/5",

        option_b="3/5",

        option_c="1/2",

        option_d="4/5",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="selection",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROBABILITY-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is selected randomly from 1 to 10. Probability that it is even is:",

        option_a="1/5",

        option_b="2/5",

        option_c="1/2",

        option_d="3/5",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="number_selection",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROBABILITY-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A card is drawn from a deck of 52 cards. Probability of getting a king is:",

        option_a="1/13",

        option_b="1/26",

        option_c="4/52",

        option_d="1/52",

        correct_answer="A",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="cards",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROBABILITY-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Two dice are thrown together. Total possible outcomes are:",

        option_a="12",

        option_b="24",

        option_c="36",

        option_d="48",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="dice",

        skill="concept",

    ),



    Question(

        question_code="APT-PROBABILITY-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "When a dice is rolled, probability of getting a number less than 3 is:",

        option_a="1/6",

        option_b="1/3",

        option_c="1/2",

        option_d="2/3",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="dice",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROBABILITY-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A coin is tossed three times. Total possible outcomes are:",

        option_a="4",

        option_b="6",

        option_c="8",

        option_d="10",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="coin",

        skill="concept",

    ),



    Question(

        question_code="APT-PROBABILITY-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Probability of getting at least one head when two coins are tossed is:",

        option_a="1/4",

        option_b="1/2",

        option_c="3/4",

        option_d="1",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="coin",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROBABILITY-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A box contains 3 red, 2 blue and 5 green balls. Probability of selecting a blue ball is:",

        option_a="1/5",

        option_b="1/4",

        option_c="1/3",

        option_d="2/5",

        correct_answer="A",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="selection",

        skill="calculation",

    ),



    Question(

        question_code="APT-PROBABILITY-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If probability of an event is 0.25, probability of its complementary event is:",

        option_a="0.25",

        option_b="0.50",

        option_c="0.75",

        option_d="1.25",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="complementary_event",

        skill="concept",

    ),



    Question(

        question_code="APT-PROBABILITY-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is chosen from 1 to 20. Probability that it is a multiple of 5 is:",

        option_a="1/10",

        option_b="1/5",

        option_c="1/4",

        option_d="1/2",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="probability",

        sub_topic="number_selection",

        skill="calculation",

    ),

        Question(

        question_code="APT-PERMUTATION-COMBINATION-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of 5! is:",

        option_a="60",

        option_b="100",

        option_c="120",

        option_d="150",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="factorial",

        skill="calculation",

    ),


    Question(

        question_code="APT-PERMUTATION-COMBINATION-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of 0! is:",

        option_a="0",

        option_b="1",

        option_c="10",

        option_d="undefined",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="factorial",

        skill="concept",

    ),


    Question(

        question_code="APT-PERMUTATION-COMBINATION-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Number of arrangements of letters in word CAT is:",

        option_a="3",

        option_b="6",

        option_c="9",

        option_d="12",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="permutation",

        skill="calculation",

    ),


    Question(

        question_code="APT-PERMUTATION-COMBINATION-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of 4P2 is:",

        option_a="8",

        option_b="10",

        option_c="12",

        option_d="16",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="permutation",

        skill="calculation",

    ),


    Question(

        question_code="APT-PERMUTATION-COMBINATION-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of 5C2 is:",

        option_a="5",

        option_b="10",

        option_c="15",

        option_d="20",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="combination",

        skill="calculation",

    ),


    Question(

        question_code="APT-PERMUTATION-COMBINATION-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "How many ways can 3 students be selected from 5 students?",

        option_a="5",

        option_b="10",

        option_c="15",

        option_d="20",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="selection",

        skill="calculation",

    ),


    Question(

        question_code="APT-PERMUTATION-COMBINATION-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Number of ways to arrange 4 different books on a shelf is:",

        option_a="12",

        option_b="24",

        option_c="36",

        option_d="48",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="arrangement",

        skill="calculation",

    ),


    Question(

        question_code="APT-PERMUTATION-COMBINATION-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of 6P1 is:",

        option_a="1",

        option_b="6",

        option_c="12",

        option_d="36",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="permutation",

        skill="calculation",

    ),


    Question(

        question_code="APT-PERMUTATION-COMBINATION-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The number of combinations of choosing 2 objects from 4 objects is:",

        option_a="4",

        option_b="5",

        option_c="6",

        option_d="8",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="combination",

        skill="calculation",

    ),


    Question(

        question_code="APT-PERMUTATION-COMBINATION-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "How many 2-digit numbers can be formed using digits 1,2,3 without repetition?",

        option_a="3",

        option_b="6",

        option_c="9",

        option_d="12",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="number_formation",

        skill="calculation",

    ),

        Question(

        question_code="APT-PERMUTATION-COMBINATION-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "How many ways can 5 people sit in a row?",

        option_a="60",

        option_b="100",

        option_c="120",

        option_d="150",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="arrangement",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERMUTATION-COMBINATION-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of 6C2 is:",

        option_a="10",

        option_b="12",

        option_c="15",

        option_d="20",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="combination",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERMUTATION-COMBINATION-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "In how many ways can 3 different prizes be given to 3 students?",

        option_a="3",

        option_b="6",

        option_c="9",

        option_d="12",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="distribution",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERMUTATION-COMBINATION-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of 7P2 is:",

        option_a="21",

        option_b="42",

        option_c="49",

        option_d="56",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="permutation",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERMUTATION-COMBINATION-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of 7C1 is:",

        option_a="1",

        option_b="5",

        option_c="7",

        option_d="14",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="combination",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERMUTATION-COMBINATION-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "How many arrangements are possible for letters of the word DOG?",

        option_a="3",

        option_b="6",

        option_c="9",

        option_d="12",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="word_arrangement",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERMUTATION-COMBINATION-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "How many ways can 2 students be selected from 6 students?",

        option_a="10",

        option_b="12",

        option_c="15",

        option_d="20",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="selection",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERMUTATION-COMBINATION-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The value of 8P3 is:",

        option_a="168",

        option_b="336",

        option_c="512",

        option_d="720",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="permutation",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERMUTATION-COMBINATION-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The number of ways to choose a committee of 3 members from 8 members is:",

        option_a="28",

        option_b="36",

        option_c="56",

        option_d="64",

        correct_answer="C",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="committee_selection",

        skill="calculation",

    ),



    Question(

        question_code="APT-PERMUTATION-COMBINATION-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "How many different arrangements can be made using all letters of the word LEVEL?",

        option_a="20",

        option_b="30",

        option_c="60",

        option_d="120",

        correct_answer="C",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="permutation_combination",

        sub_topic="repeated_letters",

        skill="calculation",

    ),

        Question(

        question_code="APT-DATA-INTERPRETATION-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A company has sales of 100, 150, 200 and 250 units in four quarters. Total sales are:",

        option_a="600",

        option_b="650",

        option_c="700",

        option_d="750",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="table_based",

        skill="data_analysis",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average sales of the above four quarters is:",

        option_a="150",

        option_b="160",

        option_c="175",

        option_d="200",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="average",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A student scored 70, 80, 90 and 60 marks in four subjects. Total marks obtained are:",

        option_a="280",

        option_b="290",

        option_c="300",

        option_d="310",

        correct_answer="A",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="marks_analysis",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "Using previous data, average marks scored by the student are:",

        option_a="70",

        option_b="75",

        option_c="80",

        option_d="85",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="average",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A shop sold 40, 60, 80 and 100 products in four months. Highest sales exceeded lowest sales by:",

        option_a="40",

        option_b="50",

        option_c="60",

        option_d="70",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="comparison",

        skill="data_analysis",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A population increased from 5000 to 6000. Percentage increase is:",

        option_a="10%",

        option_b="15%",

        option_c="20%",

        option_d="25%",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="percentage_change",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A company produced 1200 units in January and 1500 units in February. Increase in production is:",

        option_a="200",

        option_b="300",

        option_c="400",

        option_d="500",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="comparison",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The ratio of 200 to 500 is:",

        option_a="1:2",

        option_b="2:5",

        option_c="3:5",

        option_d="5:2",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="ratio",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A survey shows 40% people prefer tea and 60% prefer coffee. If total people are 500, coffee lovers are:",

        option_a="200",

        option_b="250",

        option_c="300",

        option_d="350",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="percentage",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A company revenue was 50 lakh in 2024 and 75 lakh in 2025. Increase in revenue is:",

        option_a="25 lakh",

        option_b="30 lakh",

        option_c="35 lakh",

        option_d="40 lakh",

        correct_answer="A",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="growth_analysis",

        skill="calculation",

    ),

        Question(

        question_code="APT-DATA-INTERPRETATION-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The sales of a company are 120, 180, 240 and 300 units in four months. The highest sales are how many times the lowest sales?",

        option_a="1.5 times",

        option_b="2 times",

        option_c="2.5 times",

        option_d="3 times",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="comparison",

        skill="data_analysis",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A student's marks in five subjects are 75, 80, 65, 90 and 70. The highest marks are:",

        option_a="75",

        option_b="80",

        option_c="85",

        option_d="90",

        correct_answer="D",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="marks_analysis",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average production of a factory for three years is 5000 units. Total production is:",

        option_a="10000",

        option_b="12000",

        option_c="15000",

        option_d="18000",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="average",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A company's profit increased from 20 lakh to 30 lakh. Percentage increase is:",

        option_a="25%",

        option_b="40%",

        option_c="50%",

        option_d="60%",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="percentage_change",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "In a survey of 800 people, 45% liked product A. Number of people who liked product A are:",

        option_a="320",

        option_b="360",

        option_c="400",

        option_d="450",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="percentage",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A bar graph shows values 50, 70, 90 and 110. The difference between maximum and minimum value is:",

        option_a="40",

        option_b="50",

        option_c="60",

        option_d="70",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="bar_graph",

        skill="data_analysis",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A company has expenses of 30%, 25%, 20% and 25% in four departments. Total percentage is:",

        option_a="90%",

        option_b="95%",

        option_c="100%",

        option_d="110%",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="percentage_distribution",

        skill="concept",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The ratio of male and female employees is 3:2. If total employees are 500, female employees are:",

        option_a="150",

        option_b="200",

        option_c="250",

        option_d="300",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="ratio_analysis",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A store sold 200, 250, 300 and 350 items in four months. Average monthly sales are:",

        option_a="250",

        option_b="275",

        option_c="300",

        option_d="325",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="average",

        skill="calculation",

    ),



    Question(

        question_code="APT-DATA-INTERPRETATION-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A company revenue increased from 80 lakh to 100 lakh. The increase amount is:",

        option_a="10 lakh",

        option_b="15 lakh",

        option_c="20 lakh",

        option_d="25 lakh",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="data_interpretation",

        topic="data_interpretation",

        sub_topic="growth_analysis",

        skill="calculation",

    ),

        Question(

        question_code="APT-MIXED-ADVANCED-001",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is increased by 20% and then decreased by 20%. The overall change is:",

        option_a="No change",

        option_b="4% increase",

        option_c="4% decrease",

        option_d="8% decrease",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="percentage",

        skill="calculation",

    ),


    Question(

        question_code="APT-MIXED-ADVANCED-002",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A sum becomes double in 8 years at simple interest. The rate of interest is:",

        option_a="10%",

        option_b="12.5%",

        option_c="15%",

        option_d="20%",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="simple_interest",

        skill="calculation",

    ),


    Question(

        question_code="APT-MIXED-ADVANCED-003",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A man buys an article for 500 and sells it for 600. Profit percentage is:",

        option_a="10%",

        option_b="15%",

        option_c="20%",

        option_d="25%",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="profit_loss",

        skill="calculation",

    ),


    Question(

        question_code="APT-MIXED-ADVANCED-004",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The average of 10 numbers is 25. Their total sum is:",

        option_a="200",

        option_b="225",

        option_c="250",

        option_d="275",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="average",

        skill="calculation",

    ),


    Question(

        question_code="APT-MIXED-ADVANCED-005",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If 12 men complete a work in 15 days, 20 men will complete it in:",

        option_a="8 days",

        option_b="9 days",

        option_c="10 days",

        option_d="12 days",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="time_work",

        skill="calculation",

    ),


    Question(

        question_code="APT-MIXED-ADVANCED-006",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A train covers 420 km in 7 hours. Its speed is:",

        option_a="50 km/hr",

        option_b="60 km/hr",

        option_c="70 km/hr",

        option_d="80 km/hr",

        correct_answer="B",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="speed_distance",

        skill="calculation",

    ),


    Question(

        question_code="APT-MIXED-ADVANCED-007",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The ratio of ages of A and B is 3:5. If their sum is 40, age of B is:",

        option_a="15",

        option_b="20",

        option_c="25",

        option_d="30",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="ratio",

        skill="problem_solving",

    ),


    Question(

        question_code="APT-MIXED-ADVANCED-008",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A discount of 10% is given on an article of 1000. Selling price is:",

        option_a="800",

        option_b="850",

        option_c="900",

        option_d="950",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="discount",

        skill="calculation",

    ),


    Question(

        question_code="APT-MIXED-ADVANCED-009",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If 25% of a number is 50, the number is:",

        option_a="100",

        option_b="150",

        option_c="200",

        option_d="250",

        correct_answer="C",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="percentage",

        skill="calculation",

    ),


    Question(

        question_code="APT-MIXED-ADVANCED-010",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The compound interest on 1000 at 10% per annum for 2 years is:",

        option_a="200",

        option_b="210",

        option_c="220",

        option_d="250",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="compound_interest",

        skill="calculation",

    ),

        Question(

        question_code="APT-MIXED-ADVANCED-011",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A shopkeeper marks an item at 800 and gives a discount of 15%. Selling price is:",

        option_a="650",

        option_b="680",

        option_c="700",

        option_d="720",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="discount",

        skill="calculation",

    ),



    Question(

        question_code="APT-MIXED-ADVANCED-012",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The difference between compound interest and simple interest on 1000 at 10% for 2 years is:",

        option_a="5",

        option_b="10",

        option_c="15",

        option_d="20",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="interest",

        skill="calculation",

    ),



    Question(

        question_code="APT-MIXED-ADVANCED-013",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is first increased by 10% and then increased by 20%. Total increase is:",

        option_a="25%",

        option_b="30%",

        option_c="32%",

        option_d="35%",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="percentage",

        skill="calculation",

    ),



    Question(

        question_code="APT-MIXED-ADVANCED-014",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A can complete a work in 20 days. After working 5 days, remaining work is:",

        option_a="1/2",

        option_b="3/4",

        option_c="2/3",

        option_d="1/4",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="time_work",

        skill="calculation",

    ),



    Question(

        question_code="APT-MIXED-ADVANCED-015",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A car covers first 100 km at 50 km/hr and next 100 km at 100 km/hr. Average speed is:",

        option_a="60 km/hr",

        option_b="66.67 km/hr",

        option_c="75 km/hr",

        option_d="80 km/hr",

        correct_answer="B",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="average_speed",

        skill="calculation",

    ),



    Question(

        question_code="APT-MIXED-ADVANCED-016",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "If the average of 8 numbers is 15, and one number is removed, average becomes 14. Removed number is:",

        option_a="20",

        option_b="21",

        option_c="22",

        option_d="23",

        correct_answer="C",

        difficulty=Difficulty.HARD,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="average",

        skill="problem_solving",

    ),



    Question(

        question_code="APT-MIXED-ADVANCED-017",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "The probability of getting a prime number on a dice is:",

        option_a="1/6",

        option_b="1/3",

        option_c="1/2",

        option_d="2/3",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="probability",

        skill="calculation",

    ),



    Question(

        question_code="APT-MIXED-ADVANCED-018",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "How many ways can 4 people be arranged in a row?",

        option_a="12",

        option_b="18",

        option_c="24",

        option_d="36",

        correct_answer="C",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="permutation",

        skill="calculation",

    ),



    Question(

        question_code="APT-MIXED-ADVANCED-019",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A number is divided by 5 and gives remainder 2. Which number satisfies this?",

        option_a="12",

        option_b="15",

        option_c="20",

        option_d="25",

        correct_answer="A",

        difficulty=Difficulty.EASY,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="number_system",

        skill="concept",

    ),



    Question(

        question_code="APT-MIXED-ADVANCED-020",

        assessment_type="aptitude",

        question_type=QuestionType.APTITUDE,

        question_text=
        "A student scores 80, 75, 90 and 85 marks. Percentage obtained out of 400 is:",

        option_a="80%",

        option_b="82.5%",

        option_c="85%",

        option_d="87.5%",

        correct_answer="B",

        difficulty=Difficulty.MEDIUM,

        category="quantitative_aptitude",

        topic="mixed_advanced",

        sub_topic="percentage",

        skill="calculation",

    ),
    
]

