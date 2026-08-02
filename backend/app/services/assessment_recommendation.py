"""
Assessment Recommendation Service

Responsibilities
----------------
- Analyze assessment performance
- Recommend career path
- Generate learning roadmap
- Suggest projects
- Suggest certifications
"""


from __future__ import annotations

from typing import Any


class AssessmentRecommendationService:


    def generate(
        self,
        assessment_result: dict[str, Any],
    ) -> dict[str, Any]:


        percentage = (
            assessment_result.get(
                "percentage",
                0
            )
        )


        strengths = (
            assessment_result.get(
                "strengths",
                []
            )
        )


        weaknesses = (
            assessment_result.get(
                "weaknesses",
                []
            )
        )


        skill_scores = (
            assessment_result.get(
                "skill_scores",
                {}
            )
        )


        career = self._recommend_career(
            skill_scores,
            percentage,
        )


        skill_gaps = self._skill_gaps(
            skill_scores
        )


        return {

            "career": career,


            "learning_path":
                self._learning_path(
                    skill_gaps
                ),


            "recommended_projects":
                self._projects(
                    career
                ),


            "recommended_certifications":
                self._certifications(
                    career
                ),


            "skill_gaps":
                skill_gaps,


            "next_goal":
                self._next_goal(
                    percentage
                ),
        }


    # --------------------------------------------------

    def _recommend_career(
        self,
        skill_scores: dict,
        percentage: float,
    ):


        reasoning = (
            skill_scores.get(
                "logical_reasoning",
                0
            )
        )


        problem_solving = (
            skill_scores.get(
                "problem_solving",
                0
            )
        )


        data = (
            skill_scores.get(
                "data_interpretation",
                0
            )
        )


        verbal = (
            skill_scores.get(
                "verbal_ability",
                0
            )
        )


        if (
            reasoning >= 75
            and problem_solving >= 75
        ):
            return "Software Developer"


        if data >= 75:
            return "Data Analyst"


        if verbal >= 80:
            return "Business Analyst"


        if percentage >= 80:
            return "Technology Professional"


        return "Explore Multiple Domains"



    # --------------------------------------------------

    def _skill_gaps(
        self,
        skill_scores: dict,
    ):

        gaps = []


        for skill, score in skill_scores.items():

            if score < 60:
                gaps.append(skill)


        return gaps



    # --------------------------------------------------

    def _learning_path(
        self,
        gaps:list[str],
    ):

        roadmap = []


        mapping = {

            "logical_reasoning":
                "Practice logical reasoning and DSA problems",

            "problem_solving":
                "Build problem solving skills using coding challenges",

            "quantitative_aptitude":
                "Practice quantitative aptitude daily",

            "data_interpretation":
                "Learn data analysis and visualization",

            "verbal_ability":
                "Improve communication and interview skills",

        }


        for skill in gaps:

            roadmap.append(
                mapping.get(
                    skill,
                    f"Improve {skill}"
                )
            )


        return roadmap



    # --------------------------------------------------

    def _projects(
        self,
        career:str,
    ):


        projects = {


            "Software Developer":[

                "Full Stack Web Application",

                "AI Career Assistant",

                "Portfolio Website",

            ],


            "Data Analyst":[

                "Sales Analytics Dashboard",

                "Student Performance Analyzer",

                "Power BI Dashboard",

            ],


            "Business Analyst":[

                "Market Research Dashboard",

                "Business Intelligence Report",

            ],


        }


        return projects.get(
            career,
            [
                "Personal Portfolio"
            ],
        )



    # --------------------------------------------------

    def _certifications(
        self,
        career:str,
    ):


        certifications = {


            "Software Developer":[

                "DSA Certification",

                "Cloud Fundamentals",

                "Backend Development",

            ],


            "Data Analyst":[

                "SQL Certification",

                "Power BI Certification",

                "Data Analytics",

            ],

        }


        return certifications.get(
            career,
            [],
        )



    # --------------------------------------------------

    def _next_goal(
        self,
        percentage:float,
    ):


        if percentage >= 90:
            return (
                "Prepare for Product Based Companies"
            )


        if percentage >= 75:
            return (
                "Practice Interview Level Problems"
            )


        if percentage >= 60:
            return (
                "Improve Weak Skills"
            )


        return (
            "Build Strong Fundamentals"
        )