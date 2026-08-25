"""
Assessment Report Service

Responsibilities
----------------
- Generate assessment report
- Create summary
- Skill matrix
- Performance analysis
- Career summary
- Placement readiness
- Interview readiness
"""


from __future__ import annotations

from typing import Any



class AssessmentReportService:


    def generate(
        self,
        assessment_result: dict[str, Any],
        recommendation: dict[str, Any],
    ) -> dict[str, Any]:


        percentage = (
            assessment_result.get(
                "percentage",
                0
            )
        )


        return {


            "summary":
                self._summary(
                    assessment_result
                ),



            "performance":
                self._performance(
                    assessment_result
                ),



            "skill_matrix":
                self._skill_matrix(
                    assessment_result
                ),



            "career":
                recommendation,



            "placement_readiness":
                self._placement_readiness(
                    percentage,
                    assessment_result,
                ),



            "interview_readiness":
                self._interview_readiness(
                    percentage,
                    assessment_result,
                ),



            "next_steps":
                self._next_steps(
                    recommendation
                ),

        }



    # --------------------------------------------------


    def _summary(
        self,
        result,
    ):


        return {


            "score":
                result.get(
                    "score",
                    0
                ),


            "percentage":
                result.get(
                    "percentage",
                    0
                ),


            "grade":
                result.get(
                    "grade",
                    "F"
                ),


            "correct":
                result.get(
                    "correct",
                    0
                ),


            "wrong":
                result.get(
                    "wrong",
                    0
                ),


            "skipped":
                result.get(
                    "skipped",
                    0
                ),

        }



    # --------------------------------------------------


    def _performance(
        self,
        result,
    ):


        return {


            "strengths":
                result.get(
                    "strengths",
                    []
                ),


            "weaknesses":
                result.get(
                    "weaknesses",
                    []
                ),


            "topic_scores":
                result.get(
                    "topic_scores",
                    {}
                ),


            "skill_scores":
                result.get(
                    "skill_scores",
                    {}
                ),

        }



    # --------------------------------------------------


    def _skill_matrix(
        self,
        result,
    ):


        skill_scores = (
            result.get(
                "skill_scores",
                {}
            )
        )


        matrix = []


        for skill, score in skill_scores.items():

            matrix.append(

                {

                    "skill": skill,

                    "score": score,

                    "level":
                        self._skill_level(
                            score
                        )

                }

            )


        return sorted(
            matrix,
            key=lambda x:x["score"],
            reverse=True
        )



    # --------------------------------------------------


    def _skill_level(
        self,
        score,
    ):


        if score >= 80:
            return "Strong"


        if score >= 60:
            return "Average"


        return "Needs Improvement"



    # --------------------------------------------------


    def _placement_readiness(
        self,
        percentage,
        result,
    ):


        weaknesses = (
            result.get(
                "weaknesses",
                []
            )
        )


        if percentage >= 85 and not weaknesses:

            return "Placement Ready"


        if percentage >= 70:

            return "Almost Ready"


        return "Needs Improvement"



    # --------------------------------------------------


    def _interview_readiness(
        self,
        percentage,
        result,
    ):


        if percentage >= 85:

            return "Ready"


        if percentage >= 70:

            return "Practice Required"


        return "Not Ready"



    # --------------------------------------------------


    def _next_steps(
        self,
        recommendation,
    ):


        steps = (
            recommendation.get(
                "learning_path",
                []
            )
        )


        if steps:

            return steps



        return [

            "Build practical projects",

            "Practice interview questions",

            "Improve technical skills",

        ]