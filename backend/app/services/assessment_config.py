"""
Assessment Configuration
------------------------

Centralized configuration for:
- Question distribution
- Difficulty ratios
- Assessment duration
- User type mapping

No business logic should be written here.
"""

from __future__ import annotations

from dataclasses import dataclass


# ==========================================================
# Assessment Duration (Minutes)
# ==========================================================

ASSESSMENT_DURATION = {
    "high_school": 45,
    "college": 60,
    "professional": 75,
}


# ==========================================================
# Default Question Count
# ==========================================================

QUESTION_COUNT = {
    "high_school": 40,
    "college": 50,
    "professional": 60,
}


# ==========================================================
# Difficulty Distribution
# ==========================================================

DIFFICULTY_DISTRIBUTION = {
    "easy": {
        "easy": 70,
        "medium": 30,
        "hard": 0,
    },
    "medium": {
        "easy": 30,
        "medium": 50,
        "hard": 20,
    },
    "hard": {
        "easy": 10,
        "medium": 30,
        "hard": 60,
    },
}


# ==========================================================
# Question Distribution
# ==========================================================

QUESTION_DISTRIBUTION = {

    "high_school": {
        "aptitude": 8,
        "reasoning": 8,
        "common": 12,
        "stream": 12,
    },

    "college": {
        "aptitude": 10,
        "reasoning": 8,
        "coding": 8,
        "dsa": 8,
        "technical": 10,
        "career": 6,
    },

    "professional": {
        "aptitude": 10,
        "reasoning": 8,
        "coding": 8,
        "dsa": 8,
        "technical": 14,
        "situational": 12,
    },
}


# ==========================================================
# Question Bank Mapping
# ==========================================================

QUESTION_BANKS = {

    "high_school": [
        "aptitude",
        "reasoning",
        "common",
        "stream",
    ],

    "college": [
        "aptitude",
        "reasoning",
        "coding",
        "dsa",
        "technical",
        "career",
    ],

    "professional": [
        "aptitude",
        "reasoning",
        "coding",
        "dsa",
        "technical",
        "situational",
    ],
}


# ==========================================================
# Assessment Rules
# ==========================================================

@dataclass(frozen=True)
class AssessmentRules:

    shuffle_questions: bool = True

    shuffle_options: bool = True

    remove_answers: bool = True

    validate_questions: bool = True

    prevent_duplicates: bool = True

    auto_generate_session_id: bool = True


RULES = AssessmentRules()