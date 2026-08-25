from enum import Enum


# =========================================================
# User Type
# =========================================================

class UserType(str, Enum):

    HIGH_SCHOOL = "high_school"

    COLLEGE = "college"

    PROFESSIONAL = "professional"


# =========================================================
# Difficulty
# =========================================================

class Difficulty(str, Enum):

    EASY = "easy"

    MEDIUM = "medium"

    HARD = "hard"


# =========================================================
# Question Type
# =========================================================

class QuestionType(str, Enum):

    # General Assessment
    ASSESSMENT = "assessment"

    # Aptitude
    APTITUDE = "aptitude"

    # Reasoning
    REASONING = "reasoning"

    # Coding
    CODING = "coding"

    # DSA
    DSA = "dsa"

    # Technical
    TECHNICAL = "technical"

    # Career
    CAREER = "career"

    # Situational
    SITUATIONAL = "situational"

    # Subject Based
    SUBJECT = "subject"




# =========================================================
#                       Topic Mapping
# =========================================================

class Topic(str, Enum):


    # =====================================================
    #                       Aptitude
    # =====================================================

    NUMBER_SYSTEM = "number_system"

    NUMBER_SERIES = "number_series"

    SIMPLIFICATION = "simplification"

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

    ALGEBRA = "algebra"

    QUANTITATIVE_APTITUDE = "quantitative_aptitude"

    MIXED_ADVANCED = "mixed_advanced"

   

    # =====================================================
    # Reasoning
    # =====================================================

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



    # =====================================================
    # Programming Languages
    # =====================================================

    C = "c"

    CPP = "cpp"

    JAVA = "java"

    PYTHON = "python"

    JAVASCRIPT = "javascript"

    SQL = "sql"



    # =====================================================
    # General Programming
    # =====================================================

    PROGRAMMING = "programming"

    SOFTWARE_DEVELOPMENT = "software_development"

    WEB_DEVELOPMENT = "web_development"

    SOFTWARE_TESTING = "software_testing"



    # =====================================================
    # DSA
    # =====================================================

    DSA = "dsa"

    ARRAY = "array"

    STRING = "string"

    LINKED_LIST = "linked_list"

    STACK = "stack"

    QUEUE = "queue"

    TREE = "tree"

    GRAPH = "graph"

    SORTING = "sorting"

    SEARCHING = "searching"

    RECURSION = "recursion"

    BACKTRACKING = "backtracking"

    DYNAMIC_PROGRAMMING = "dynamic_programming"

    HASHING = "hashing"

    HEAP = "heap"

    GREEDY = "greedy"

    BIT_MANIPULATION = "bit_manipulation"

    ADVANCED_DSA = "advanced_dsa"

# =====================================================
# High School
# =====================================================

    MATHEMATICS = "mathematics"

    PHYSICS = "physics"

    CHEMISTRY = "chemistry"

    BIOLOGY = "biology"

    GENERAL_SCIENCE = "general_science"

    ENGLISH = "english"

    COMPUTER = "computer"

    ACCOUNTANCY = "accountancy"

    ACCOUNTING = "accounting"

    ECONOMICS = "economics"

    BUSINESS_STUDIES = "business_studies"

    BUSINESS = "business"

    COMMERCE = "commerce"

    HISTORY = "history"

    GEOGRAPHY = "geography"

    POLITICAL_SCIENCE = "political_science"

    SOCIOLOGY = "sociology"

    PSYCHOLOGY = "psychology"


# =====================================================
# College Technical
# =====================================================

    DBMS = "dbms"

    OPERATING_SYSTEM = "operating_system"

    COMPUTER_NETWORK = "computer_network"

    OOP = "oop"

    SOFTWARE_ENGINEERING = "software_engineering"

    COMPUTER_ARCHITECTURE = "computer_architecture"


    # =====================================================
    # Career
    # =====================================================

    CAREER = "career"

    EDUCATION = "education"

    PROFESSIONAL_SKILLS = "professional_skills"

    PROBLEM_SOLVING = "problem_solving"

    TIME_MANAGEMENT = "time_management"

    TEAMWORK = "teamwork"

    LEADERSHIP = "leadership"


    # =====================================================
    # Cloud / Security
    # =====================================================

    SYSTEM_DESIGN = "system_design"

    CLOUD = "cloud"

    CLOUD_COMPUTING = "cloud_computing"

    DEVOPS = "devops"

    CYBER_SECURITY = "cyber_security"


    # =====================================================
    # Professional
    # =====================================================

    COMMUNICATION = "communication"

    INTERVIEW = "interview"

    RESUME = "resume"

    CERTIFICATION = "certification"