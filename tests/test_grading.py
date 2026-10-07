import pytest

from exam_system.grading import calculate_score, grade_submission, letter_grade, percentage
from exam_system.models import Exam, Question, Submission


@pytest.fixture
def exam():
    e = Exam(1, "Quiz", 10)
    e.questions = [Question(1, "Q1", ["a", "b"], 0), Question(2, "Q2", ["a", "b"], 1, marks=3)]
    return e


def test_calculate_score_all_correct(exam):
    assert calculate_score(exam, {1: 0, 2: 1}) == 4


def test_calculate_score_partial_and_missing(exam):
    assert calculate_score(exam, {1: 0}) == 1


def test_percentage_and_zero_total():
    assert percentage(3, 4) == 75.0
    with pytest.raises(ValueError):
        percentage(1, 0)


@pytest.mark.parametrize("pct,expected", [(95, "A+"), (85, "A"), (72, "B"), (60, "C"), (50, "D"), (10, "F")])
def test_letter_grade(pct, expected):
    assert letter_grade(pct) == expected


def test_grade_submission(exam):
    result = grade_submission(exam, Submission("s1", 1, {1: 0, 2: 1}))
    assert (result.score, result.grade) == (4, "A+")
