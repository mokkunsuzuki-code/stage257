# Stage247: Review Transparency Log

MIT License © 2025 Motohiro Suzuki

## Overview

Stage247 adds **review transparency** to QSP.

Previous stages demonstrated that a review existed.

This stage goes one step further:

- the full review history is recorded
- the history is hashed
- the resulting log is signed
- the log can be independently verified

This turns review evidence into a **tamper-evident audit artifact**.

## Why this stage matters

Before Stage247:

- "a review happened"

After Stage247:

- "the review history itself is auditable"

This improves external trust for reviewers, organizations, and security auditors.

## What is included

### Review records

Source review records are stored in:

- `review_records/*.json`

### Review log artifacts

Generated artifacts are stored in:

- `out/review_log/review_log.json`
- `out/review_log/review_log_hash.txt`
- `out/review_log/review_log.sig`

### Tooling

- `tools/build_review_log.py`
- `tools/verify_review_log.py`
- `tools/run_stage247_review_transparency.sh`

### Tests

- `tests/test_review_log.py`

## Review transparency model

Stage247 uses the following model:

Review Records
↓
Leaf Hashes
↓
Merkle-style Root
↓
Canonical Review Log Hash
↓
Ed25519 Signature
↓
Independent Verification

## Repository structure

```text
review_records/
  review_001.json
  review_002.json
  review_003.json

tools/
  build_review_log.py
  verify_review_log.py
  run_stage247_review_transparency.sh

out/review_log/
  review_log.json
  review_log_hash.txt
  review_log.sig

tests/
  test_review_log.py

docs/
  review_transparency.md
How to run
1. Install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install cryptography pytest
2. Run Stage247
chmod +x tools/run_stage247_review_transparency.sh
./tools/run_stage247_review_transparency.sh
3. Run tests
pytest -q
Manual verification

You can also verify directly:

python3 tools/verify_review_log.py \
  --review-log out/review_log/review_log.json \
  --hash-file out/review_log/review_log_hash.txt \
  --sig-file out/review_log/review_log.sig \
  --public-key keys/owner_public.pem
Security properties
Integrity

If any review entry changes, verification fails.

Tamper Detection

If the review log or its hash is modified, the mismatch is detected.

Signature Binding

The review log hash is signed with an Ed25519 private key.

Auditability

A third party can verify the review history without trusting local claims.

Threat model note

Stage247 improves integrity and auditability of review history.

It does not prove that a reviewer is correct.
It proves that the recorded review history has not been silently changed.

Relationship to earlier stages
Stage245: review evidence exists
Stage246: reviewer process is structured
Stage247: review history becomes tamper-evident and independently verifiable
Intended external meaning

For external reviewers or organizations such as OpenSSF or infrastructure/security teams,
this stage changes the project from:

"interesting review evidence"

to:

"review history with audit properties"
Limitations

This is a lightweight Merkle-style construction for repository-level transparency.

It is not yet:

a public append-only service
a federated transparency network
a global transparency protocol

Those can come in later stages.

License

This project is licensed under the MIT License.
