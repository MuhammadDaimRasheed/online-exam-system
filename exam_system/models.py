from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Question:
    qid: int
    text: str
    options: List[str]
    correct_index: int
    marks: int = 1

    def is_correct(self, answer_index: int) -> bool:
        return answer_index == self.correct_index


@dataclass
class Exam:
    exam_id: int
    title: str
    duration_minutes: int
    questions: List[Question] = field(default_factory=list)

    @property
    def total_marks(self) -> int:
        return sum(q.marks for q in self.questions)


@dataclass
class Submission:
    student_id: str
    exam_id: int
    answers: Dict[int, int] = field(default_factory=dict)
    score: int = 0
    grade: str = ""
