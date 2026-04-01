import subprocess
from pathlib import Path

def test_real_review_record_exists():
    assert Path("review_records/real_review_record.json").exists()

def test_sign_and_verify_review_record():
    sign_result = subprocess.run(
        [
            "python3",
            "tools/sign_review_record.py",
            "--input",
            "review_records/real_review_record.json",
            "--signature-output",
            "review_records/real_review_record.sig",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert sign_result.returncode == 0

    verify_result = subprocess.run(
        [
            "python3",
            "tools/verify_signed_review_record.py",
            "--input",
            "review_records/real_review_record.json",
            "--signature",
            "review_records/real_review_record.sig",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert verify_result.returncode == 0
    assert "[OK] signed review record is valid" in verify_result.stdout
