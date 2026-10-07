import pytest

from exam_system.exam_service import ExamService
from exam_system.models import Question


@pytest.fixture
def service():
    s = ExamService()
    s.create_exam(1, "Quiz", 20)
    s.add_question(1, Question(1, "Q1", ["a", "b"], 0))
    s.add_question(1, Question(2, "Q2", ["a", "b"], 1))
    return s


def test_duplicate_exam_rejected(service):
    with pytest.raises(ValueError):
        service.create_exam(1, "Again", 10)


def test_invalid_duration_rejected():
    with pytest.raises(ValueError):
        ExamService().create_exam(2, "Bad", 0)


def test_unknown_exam(service):
    with pytest.raises(KeyError):
        service.get_exam(99)


def test_invalid_correct_index(service):
    with pytest.raises(ValueError):
        service.add_question(1, Question(3, "Q3", ["a", "b"], 5))


def test_submit_and_results(service):
    result = service.submit("s1", 1, {1: 0, 2: 1})
    assert result.score == 2
    assert len(service.results_for(1)) == 1


def test_double_submission_rejected(service):
    service.submit("s1", 1, {1: 0})
    with pytest.raises(ValueError):
        service.submit("s1", 1, {1: 0})


def test_empty_exam_cannot_be_submitted():
    s = ExamService()
    s.create_exam(5, "Empty", 10)
    with pytest.raises(ValueError):
        s.submit("s1", 5, {})


def test_average_score(service):
    assert service.average_score(1) == 0.0
    service.submit("s1", 1, {1: 0, 2: 1})
    service.submit("s2", 1, {1: 0})
    assert service.average_score(1) == 1.5
