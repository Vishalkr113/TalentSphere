from enum import Enum


class UserType(str, Enum):
    HIGH_SCHOOL = "high_school"
    COLLEGE = "college"
    PROFESSIONAL = "professional"


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class QuestionType(str, Enum):
    APTITUDE = "aptitude"
    REASONING = "reasoning"
    CODING = "coding"
    TECHNICAL = "technical"
    CAREER = "career"
    SITUATIONAL = "situational"
    SUBJECT = "subject"


class Topic(str, Enum):
    # Aptitude
    NUMBER_SERIES = "number_series"
    PERCENTAGE = "percentage"
    RATIO_PROPORTION = "ratio_proportion"
    AVERAGE = "average"
    PROFIT_LOSS = "profit_loss"
    TIME_WORK = "time_work"
    TIME_DISTANCE = "time_speed_distance"
    SIMPLE_INTEREST = "simple_interest"
    COMPOUND_INTEREST = "compound_interest"
    PROBABILITY = "probability"
    PERMUTATION_COMBINATION = "permutation_combination"
    DATA_INTERPRETATION = "data_interpretation"

    # Reasoning
    ANALOGY = "analogy"
    CLASSIFICATION = "classification"
    CODING_DECODING = "coding_decoding"
    BLOOD_RELATION = "blood_relation"
    DIRECTION = "direction"
    CALENDAR = "calendar"
    CLOCK = "clock"
    RANKING = "ranking"
    PUZZLE = "puzzle"
    SYLLOGISM = "syllogism"
    STATEMENT_CONCLUSION = "statement_conclusion"

    # Coding
    C = "c"
    CPP = "cpp"
    JAVA = "java"
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    SQL = "sql"

    # High School
    MATHEMATICS = "mathematics"
    PHYSICS = "physics"
    CHEMISTRY = "chemistry"
    BIOLOGY = "biology"
    ENGLISH = "english"
    COMPUTER = "computer"
    ACCOUNTANCY = "accountancy"
    ECONOMICS = "economics"
    BUSINESS_STUDIES = "business_studies"
    HISTORY = "history"
    GEOGRAPHY = "geography"
    POLITICAL_SCIENCE = "political_science"
    SOCIOLOGY = "sociology"

    # College
    DBMS = "dbms"
    OPERATING_SYSTEM = "operating_system"
    COMPUTER_NETWORK = "computer_network"
    DSA = "dsa"
    OOP = "oop"
    SOFTWARE_ENGINEERING = "software_engineering"

    # Professional
    SYSTEM_DESIGN = "system_design"
    CLOUD = "cloud"
    DEVOPS = "devops"
    CYBER_SECURITY = "cyber_security"
    COMMUNICATION = "communication"
    LEADERSHIP = "leadership"
    TEAMWORK = "teamwork"