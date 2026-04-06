# Stage253: QSP Session Anchoring

Stage253 introduces **Session Anchoring** for QSP.

This stage proves that a verifiable evidence chain can be derived directly from QSP-style session execution output.

---

## Overview

In this stage, we:

1. Execute a QSP session (deterministic demo)
2. Generate `session_manifest.json`
3. Bind critical security properties:
   - transcript hash
   - policy
   - fail-closed result
4. Anchor the manifest with:
   - local witness
   - checkpoint witness (append-only)
   - GitHub Actions (anchor receipt)
   - OpenTimestamps (OTS)
   - cosign bundle (Sigstore)

---

## Why this matters

The key idea is:

> Evidence is not added later.  
> Evidence is generated from the session itself.

This creates a direct chain:

QSP execution  
→ session result  
→ session manifest  
→ anchored evidence  
→ independent verification

---

## What is verified

This stage ensures:

- The manifest is derived from session execution output
- Transcript integrity is fixed via `transcript_hash`
- Security policy is fixed
- Fail-closed behavior is explicitly recorded
- All witnesses and anchors refer to the same manifest

---

## Architecture


QSP session execution
↓
qsp_session_result.json
↓
session_manifest.json
↓
├── local_witness.json
├── checkpoint_witness.json
├── GitHub anchor (receipt)
├── OTS (timestamp)
└── cosign bundle


---

## Files

- `tools/run_qsp_session_demo.py`  
  Minimal deterministic QSP session output

- `tools/build_session_manifest.py`  
  Builds `session_manifest.json`

- `tools/sign_session_manifest.py`  
  Creates local & checkpoint witnesses

- `tools/verify_session_anchor.py`  
  Verifies the entire anchor chain

- `.github/workflows/stage253-session-anchor.yml`  
  Produces external anchors (GitHub / OTS / cosign)

---

## Quickstart

### 1. Local execution

```bash
./tools/run_stage253_qsp_session_anchor.sh
2. Push and run CI
git add .
git commit -m "Stage253: QSP session anchoring"
git push
3. Download artifacts
gh run list --workflow "stage253-session-anchor" --limit 5

gh run download <RUN_ID> \
  -n stage253-session-anchor-artifacts \
  -D downloaded_stage253_session_anchor
4. Verify
python3 tools/verify_session_anchor.py \
  --manifest downloaded_stage253_session_anchor/out/session/session_manifest.json \
  --session-result downloaded_stage253_session_anchor/out/session/qsp_session_result.json \
  --local-witness downloaded_stage253_session_anchor/out/witnesses/local_witness.json \
  --local-public downloaded_stage253_session_anchor/keys/local_witness_public.pem \
  --checkpoint-witness downloaded_stage253_session_anchor/out/checkpoints/checkpoint_witness.json \
  --checkpoint-public downloaded_stage253_session_anchor/keys/checkpoint_witness_public.pem \
  --github-receipt downloaded_stage253_session_anchor/out/anchors/github_session_anchor_receipt.json \
  --ots downloaded_stage253_session_anchor/out/session/session_manifest.json.ots \
  --cosign-bundle downloaded_stage253_session_anchor/out/anchors/session_manifest.json.cosign.bundle
Interpretation

This stage demonstrates:

Evidence is derived from session execution
Security-relevant properties are fixed and verifiable
Anchors (GitHub / OTS / cosign) all bind to the same data
Verification can be reproduced independently
Limitations
This stage uses a deterministic demo session (not full QSP integration yet)
It does not introduce new cryptographic proofs
It focuses on evidence structure and verifiability
Next step

Stage254:

👉 Direct integration with real QSP implementation
👉 Session output is no longer simulated
👉 Evidence is generated from real execution

License

MIT License

Copyright (c) 2025 Motohiro Suzuki
