import json
from dataclasses import asdict
from typing import List

from .models import Submission


def save_submissions(path: str, submissions: List[Submission]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump([asdict(s) for s in submissions], f, indent=2)


def load_submissions(path: str) -> List[Submission]:
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    return [
        Submission(
            student_id=item["student_id"],
            exam_id=item["exam_id"],
            answers={int(k): v for k, v in item["answers"].items()},
            score=item["score"],
            grade=item["grade"],
        )
        for item in raw
    ]
