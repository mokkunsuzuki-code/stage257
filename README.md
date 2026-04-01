Stage249: External Timestamp Anchoring (GitHub Actions)

## Overview

Stage249 introduces **external timestamp anchoring** by binding the latest
checkpoint state to a publicly observable GitHub Actions execution.

This stage does NOT claim a trusted timestamp authority (TSA) or blockchain anchoring.
Instead, it provides a **reproducible, verifiable, and externally observable timestamp binding**
based on CI execution metadata.

---

## What This Stage Achieves

- Binds checkpoint state → anchor request → external execution
- Generates deterministic anchor request with SHA256
- Records GitHub Actions execution metadata as a receipt
- Enables third-party verification of request ↔ receipt consistency

---

## Architecture


Review Log
↓
Checkpoint Chain (Stage248)
↓
Anchor Request (Stage249 local)
↓
GitHub Actions Run (external execution)
↓
Receipt (github_anchor_receipt.json)
↓
Verification


---

## Key Files

### Anchor Request

- `out/anchors/anchor_request.json`
- `out/anchors/anchor_request.sha256`
- `out/anchors/history/request_0001.json`

### External Receipt

- `github_anchor_receipt.json`
- `github_anchor_receipt.sha256`

### Tools

- `tools/generate_anchor_request.py`
- `tools/record_github_anchor.py`
- `tools/verify_external_anchor.py`

---

## How It Works

### 1. Generate Anchor Request

```bash
./tools/run_stage249_anchor.sh

This creates:

deterministic request JSON
SHA256 binding
request history
2. GitHub Actions Execution

Workflow:

.github/workflows/stage249-external-time-anchor.yml

Performs:

reconstruct transparency input
generate anchor request
record GitHub execution metadata
produce receipt
3. Verify External Anchor
python3 tools/verify_external_anchor.py \
  --request out/anchors/anchor_request.json \
  --receipt github_anchor_receipt.json
Example Verification Output
[OK] external anchor verified
[OK] request_sha256: <hash>
[OK] checkpoint_id: 1
[OK] run_url: https://github.com/.../actions/runs/<id>
Security Meaning

This stage proves:

the checkpoint state existed
the exact request was hashed
that hash appeared in a public CI execution
the execution time is externally observable
What This Is NOT
Not RFC3161 TSA
Not blockchain anchoring
Not absolute timestamp guarantee
Why This Matters
No hidden trust assumptions
Fully reproducible
Publicly observable
Verifiable by third parties
Design Philosophy

Do not claim stronger security than what can be verified.

Stage249 intentionally provides:

minimal assumptions
maximum transparency
reproducible verification
Next Steps
Stage250: Release Anchoring
Multi-anchor (CI / mirror / distributed)
External verification ecosystem
License

MIT License © 2025 Motohiro Suzuki