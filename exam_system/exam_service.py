from typing import Dict, List

from .grading import grade_submission
from .models import Exam, Question, Submission


class ExamService:
    def __init__(self) -> None:
        self._exams: Dict[int, Exam] = {}
        self._submissions: List[Submission] = []

    def create_exam(self, exam_id: int, title: str, duration_minutes: int) -> Exam:
        if exam_id in self._exams:
            raise ValueError(f"Exam {exam_id} already exists")
        if duration_minutes <= 0:
            raise ValueError("Duration must be positive")
        exam = Exam(exam_id, title, duration_minutes)
        self._exams[exam_id] = exam
        return exam

    def add_question(self, exam_id: int, question: Question) -> None:
        exam = self.get_exam(exam_id)
        if not 0 <= question.correct_index < len(question.options):
            raise ValueError("correct_index is outside the options range")
        exam.questions.append(question)

    def get_exam(self, exam_id: int) -> Exam:
        try:
            return self._exams[exam_id]
        except KeyError:
            raise KeyError(f"Exam {exam_id} not found") from None

    def submit(self, student_id: str, exam_id: int, answers: Dict[int, int]) -> Submission:
        exam = self.get_exam(exam_id)
        if not exam.questions:
            raise ValueError("Cannot submit an exam with no questions")
        if any(s.student_id == student_id and s.exam_id == exam_id for s in self._submissions):
            raise ValueError("Student has already submitted this exam")
        submission = grade_submission(exam, Submission(student_id, exam_id, answers))
        self._submissions.append(submission)
        return submission

    def results_for(self, exam_id: int) -> List[Submission]:
        return [s for s in self._submissions if s.exam_id == exam_id]

    def average_score(self, exam_id: int) -> float:
        results = self.results_for(exam_id)
        if not results:
            return 0.0
        return round(sum(s.score for s in results) / len(results), 2)
