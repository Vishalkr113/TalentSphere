"""
Assessment Recommendation Service

Responsibilities
----------------
- Analyze assessment result
- Identify strengths
- Identify weaknesses
- Recommend career paths
- Recommend learning roadmap
- Recommend projects
- Recommend certifications
"""

from __future__ import annotations

from typing import Any


class AssessmentRecommendationService:

    def generate(
        self,
        assessment_result: dict[str, Any],
    ) -> dict[str, Any]:

        percentage = assessment_result["percentage"]

        strengths = assessment_result["strengths"]

        weaknesses = assessment_result["weaknesses"]

        career = self._recommend_career(
            percentage,
            strengths,
        )

        return {

            "career": career,

            "learning_path": self._learning_path(weaknesses),

            "recommended_projects": self._projects(career),

            "recommended_certifications": self._certifications(career),

            "skill_gaps": weaknesses,

            "next_goal": self._next_goal(percentage),

        }

    # ----------------------------------------------------

    def _recommend_career(
        self,
        percentage: float,
        strengths: list[str],
    ) -> str:

        if "Python" in strengths:
            return "Python Developer"

        if "Java" in strengths:
            return "Java Developer"

        if "JavaScript" in strengths:
            return "Frontend Developer"

        if "React" in strengths:
            return "React Developer"

        if "Node.js" in strengths:
            return "Backend Developer"

        if "SQL" in strengths:
            return "Data Analyst"

        if "DSA" in strengths:
            return "Software Engineer"

        if percentage >= 90:
            return "Full Stack Developer"

        if percentage >= 75:
            return "Software Developer"

        return "Explore Multiple Domains"

    # ----------------------------------------------------

    def _learning_path(
        self,
        weaknesses: list[str],
    ) -> list[str]:

        roadmap = []

        for skill in weaknesses:

            roadmap.append(
                f"Improve {skill}"
            )

        return roadmap

    # ----------------------------------------------------

    def _projects(
        self,
        career: str,
    ) -> list[str]:

        mapping = {

            "Python Developer": [

                "REST API",

                "Automation Tool",

                "Web Scraper",

            ],

            "Frontend Developer": [

                "Portfolio",

                "Admin Dashboard",

                "E-commerce UI",

            ],

            "React Developer": [

                "Task Manager",

                "Chat App",

                "Analytics Dashboard",

            ],

            "Backend Developer": [

                "Authentication API",

                "Inventory System",

                "Blog API",

            ],

            "Software Engineer": [

                "DSA Practice Platform",

                "Compiler",

                "System Design Project",

            ],

            "Data Analyst": [

                "Sales Dashboard",

                "Excel Analytics",

                "Power BI Dashboard",

            ],

        }

        return mapping.get(
            career,
            ["Personal Portfolio"],
        )

    # ----------------------------------------------------

    def _certifications(
        self,
        career: str,
    ) -> list[str]:

        mapping = {

            "Python Developer": [

                "Python",

                "FastAPI",

                "SQL",

            ],

            "Frontend Developer": [

                "JavaScript",

                "React",

                "HTML/CSS",

            ],

            "Backend Developer": [

                "FastAPI",

                "Docker",

                "PostgreSQL",

            ],

            "Software Engineer": [

                "DSA",

                "System Design",

                "OOP",

            ],

            "Data Analyst": [

                "Excel",

                "Power BI",

                "SQL",

            ],

        }

        return mapping.get(
            career,
            [],
        )

    # ----------------------------------------------------

    def _next_goal(
        self,
        percentage: float,
    ) -> str:

        if percentage >= 90:
            return "Prepare for Product-Based Companies"

        if percentage >= 80:
            return "Practice Medium-Level Interview Questions"

        if percentage >= 70:
            return "Strengthen Weak Skills"

        if percentage >= 60:
            return "Complete One Real Project"

        return "Build Strong Fundamentals"