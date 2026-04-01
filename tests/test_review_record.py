import json
import subprocess
from pathlib import Path

def test_example_review_record_exists():
    path = Path("review_records/example_external_review.json")
    assert path.exists()

def test_example_review_record_has_valid_verdict():
    path = Path("review_records/example_external_review.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["verdict"] in {"observed", "reproduced", "reviewed", "approved"}

def test_verify_review_record_script():
    result = subprocess.run(
        ["python3", "tools/verify_review_record.py", "--input", "review_records/example_external_review.json"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "[OK] review record is valid" in result.stdout
