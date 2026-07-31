"""
Assessment Report Service

Responsibilities
----------------
- Generate assessment report
- Create summary
- Skill matrix
- Topic analysis
- Career summary
- Placement readiness
"""

from __future__ import annotations

from typing import Any


class AssessmentReportService:

    def generate(
        self,
        assessment_result: dict[str, Any],
        recommendation: dict[str, Any],
    ) -> dict[str, Any]:

        return {

            "summary": self._summary(assessment_result),

            "performance": self._performance(assessment_result),

            "skill_matrix": self._skill_matrix(
                assessment_result,
            ),

            "career": recommendation,

            "placement_readiness":
                self._placement_readiness(
                    assessment_result["percentage"],
                ),

            "interview_readiness":
                self._interview_readiness(
                    assessment_result["percentage"],
                ),

            "next_steps":
                self._next_steps(
                    recommendation,
                ),
        }

    # --------------------------------------------------

    def _summary(
        self,
        result: dict[str, Any],
    ) -> dict[str, Any]:

        return {

            "score": result["score"],

            "percentage": result["percentage"],

            "grade": result["grade"],

            "correct": result["correct"],

            "wrong": result["wrong"],

            "skipped": result["skipped"],
        }

    # --------------------------------------------------

    def _performance(
        self,
        result: dict[str, Any],
    ) -> dict[str, Any]:

        return {

            "strengths": result["strengths"],

            "weaknesses": result["weaknesses"],

            "topic_scores": result["topic_scores"],

            "skill_scores": result["skill_scores"],
        }

    # --------------------------------------------------

    def _skill_matrix(
        self,
        result: dict[str, Any],
    ) -> list[dict]:

        matrix = []

        for skill, score in result["skill_scores"].items():

            matrix.append({

                "skill": skill,

                "score": score,

            })

        return matrix

    # --------------------------------------------------

    def _placement_readiness(
        self,
        percentage: float,
    ) -> str:

        if percentage >= 90:
            return "Excellent"

        if percentage >= 80:
            return "Very Good"

        if percentage >= 70:
            return "Good"

        if percentage >= 60:
            return "Average"

        return "Needs Improvement"

    # --------------------------------------------------

    def _interview_readiness(
        self,
        percentage: float,
    ) -> str:

        if percentage >= 85:
            return "Ready"

        if percentage >= 70:
            return "Almost Ready"

        if percentage >= 50:
            return "Needs Practice"

        return "Not Ready"

    # --------------------------------------------------

    def _next_steps(
        self,
        recommendation: dict[str, Any],
    ) -> list[str]:

        steps = []

        for item in recommendation["learning_path"]:

            steps.append(item)

        return steps