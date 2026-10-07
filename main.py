from exam_system.exam_service import ExamService
from exam_system.models import Question


def main() -> None:
    service = ExamService()
    service.create_exam(1, "Software Quality Engineering Quiz", 30)
    service.add_question(1, Question(1, "What does SQE stand for?",
                                     ["Software Quality Engineering", "Simple Query Engine"], 0))
    service.add_question(1, Question(2, "Cyclomatic complexity measures...",
                                     ["Code size", "Independent paths"], 1, marks=2))

    result = service.submit("student-001", 1, {1: 0, 2: 1})
    print(f"Score: {result.score}, Grade: {result.grade}")


if __name__ == "__main__":
    main()
