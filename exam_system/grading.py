from .models import Exam, Submission

GRADE_BOUNDARIES = [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D")]


def calculate_score(exam: Exam, answers: dict) -> int:
    """Sum the marks of all correctly answered questions."""
    score = 0
    for question in exam.questions:
        if question.qid in answers and question.is_correct(answers[question.qid]):
            score += question.marks
    return score


def percentage(score: int, total: int) -> float:
    if total <= 0:
        raise ValueError("Total marks must be greater than zero")
    return round(score * 100 / total, 2)


def letter_grade(pct: float) -> str:
    for boundary, grade in GRADE_BOUNDARIES:
        if pct >= boundary:
            return grade
    return "F"


def grade_submission(exam: Exam, submission: Submission) -> Submission:
    submission.score = calculate_score(exam, submission.answers)
    submission.grade = letter_grade(percentage(submission.score, exam.total_marks))
    return submission
