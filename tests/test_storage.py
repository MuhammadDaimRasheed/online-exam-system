from exam_system.models import Submission
from exam_system.storage import load_submissions, save_submissions


def test_save_and_load_roundtrip(tmp_path):
    path = tmp_path / "subs.json"
    original = [Submission("s1", 1, {1: 0, 2: 1}, score=3, grade="A")]
    save_submissions(str(path), original)
    assert load_submissions(str(path)) == original
