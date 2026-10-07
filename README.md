# Online Examination System

Small Python project built for **SQE Lab 5 - Software Metrics**.
It supports creating exams, adding MCQ questions, submitting answers, automatic grading and saving results to JSON.

## Run
```bash
pip install -r requirements.txt
python main.py
pytest --cov=exam_system --cov-report=term-missing
```

## Structure
- `exam_system/models.py` - Question, Exam, Submission
- `exam_system/grading.py` - scoring and letter grades
- `exam_system/exam_service.py` - exam workflow
- `exam_system/storage.py` - JSON persistence
- `tests/` - unit tests (pytest)
- Run tests using: pytest
Check coverage using pytest-cov
   ## Future Work
   - Add more unit tests
   - Add input validation
