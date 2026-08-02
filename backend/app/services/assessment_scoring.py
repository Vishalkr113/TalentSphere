"""
Assessment Scoring Service

Responsibilities
----------------
- Calculate score
- Topic performance
- Skill performance
- Percentage
- Grade
- Strengths
- Weaknesses
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any


class AssessmentScorer:

    def __init__(
        self,
        correct_marks: float = 1.0,
        negative_marks: float = 0.0,
    ):
        self.correct_marks = correct_marks
        self.negative_marks = negative_marks


    def evaluate(
        self,
        questions: list,
        answers: dict[int, str],
    ) -> dict[str, Any]:

        total_questions = len(questions)

        obtained_score = 0.0

        topic_scores = defaultdict(float)
        topic_total = defaultdict(float)

        skill_scores = defaultdict(float)
        skill_total = defaultdict(float)

        correct_answers = 0
        wrong_answers = 0
        skipped = 0


        for question in questions:

            question_id = str(question.id)


            topic = (
                question.category
                or "General"
            )

            skill = (
                question.skill
                or "General Skill"
            )


            topic_total[topic] += self.correct_marks
            skill_total[skill] += self.correct_marks


            selected = answers.get(question_id)


            if selected is None:
                skipped += 1
                continue


            correct = question.correct_answer


            option_map = {
                "A": question.option_a,
                "B": question.option_b,
                "C": question.option_c,
                "D": question.option_d,
            }


            # Check answer
            if correct in option_map:

                selected_is_correct = (
                    selected == correct
                    or
                    selected.strip().lower()
                    ==
                    str(option_map[correct]).strip().lower()
                )

            else:

                selected_is_correct = (
                    selected.strip().lower()
                    ==
                    str(correct).strip().lower()
                )


            if selected_is_correct:

                correct_answers += 1

                obtained_score += (
                    self.correct_marks
                )

                topic_scores[topic] += (
                    self.correct_marks
                )

                skill_scores[skill] += (
                    self.correct_marks
                )


            else:

                wrong_answers += 1

                obtained_score -= (
                    self.negative_marks
                )


        obtained_score = max(
            obtained_score,
            0
        )


        percentage = round(
            (
                obtained_score /
                (total_questions * self.correct_marks)
            )
            * 100,
            2,
        )


        skill_percentage = {

            skill: round(
                (
                    skill_scores[skill]
                    /
                    skill_total[skill]
                )
                * 100,
                2,
            )

            for skill in skill_total

        }


        return {

            "total_questions":
                total_questions,

            "correct":
                correct_answers,

            "wrong":
                wrong_answers,

            "skipped":
                skipped,

            "score":
                round(obtained_score, 2),

            "percentage":
                percentage,

            "grade":
                self._grade(
                    percentage
                ),

            "topic_scores":
                dict(topic_scores),

            "skill_scores":
                skill_percentage,

            "strengths":
                self._strengths(
                    topic_scores,
                    topic_total,
                ),

            "weaknesses":
                self._weaknesses(
                    topic_scores,
                    topic_total,
                ),
        }



    def _grade(
        self,
        percentage: float,
    ):

        if percentage >= 90:
            return "A+"

        if percentage >= 80:
            return "A"

        if percentage >= 70:
            return "B+"

        if percentage >= 60:
            return "B"

        if percentage >= 50:
            return "C"

        if percentage >= 40:
            return "D"

        return "F"



    def _strengths(
        self,
        score,
        total,
    ):

        result = []

        for topic in total:

            percentage = (
                score[topic]
                /
                total[topic]
            ) * 100


            if percentage >= 75:
                result.append(topic)


        return sorted(result)



    def _weaknesses(
        self,
        score,
        total,
    ):

        result = []


        for topic in total:

            percentage = (
                score[topic]
                /
                total[topic]
            ) * 100


            if percentage < 50:
                result.append(topic)


        return sorted(result)