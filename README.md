Stage254: Real QSP Integration (Session Anchoring)

This stage integrates the QSP execution itself into the evidence chain.

Unlike previous stages, the session manifest is not generated from a demo,
but directly derived from a real QSP execution.

---

## What this stage demonstrates

- Real QSP execution (Stage226)
- Extraction of:
  - transcript hash
  - policy
  - fail-closed result
- Generation of `session_manifest.json` from actual execution
- Multi-layer anchoring:
  - Local witness (Ed25519)
  - Checkpoint witness (append-only)
  - GitHub Actions anchor
  - OpenTimestamps (OTS)
  - cosign bundle (Sigstore)

---

## Architecture


Real QSP execution (stage226)
↓
qsp_session_result.json
↓
session_manifest.json
↓
witness / checkpoint / external anchors
↓
independent verification


---

## Key property

The evidence is now **directly derived from the protocol execution**.

This removes the gap between:

- protocol behavior
- evidence artifacts

---

## How to reproduce (local)

```bash
cd stage254

export QSP_REAL_REPO=../stage226
export QSP_REAL_RUN_CMD="python3 poc/run_poc.py"

./tools/run_stage254_real_qsp_anchor.sh
How to verify (GitHub Actions)
gh run list --workflow "stage254-real-qsp-anchor"

gh run download <RUN_ID> \
  -n stage254-real-qsp-anchor-artifacts \
  -D downloaded_stage254_session_anchor

python3 tools/verify_session_anchor.py \
  --manifest downloaded_stage254_session_anchor/out/session/session_manifest.json \
  --session-result downloaded_stage254_session_anchor/out/session/qsp_session_result.json \
  --local-witness downloaded_stage254_session_anchor/out/witnesses/local_witness.json \
  --local-public downloaded_stage254_session_anchor/keys/local_witness_public.pem \
  --checkpoint-witness downloaded_stage254_session_anchor/out/checkpoints/checkpoint_witness.json \
  --checkpoint-public downloaded_stage254_session_anchor/keys/checkpoint_witness_public.pem \
  --github-receipt downloaded_stage254_session_anchor/out/anchors/github_session_anchor_receipt.json \
  --ots downloaded_stage254_session_anchor/out/session/session_manifest.json.ots \
  --cosign-bundle downloaded_stage254_session_anchor/out/anchors/session_manifest.json.cosign.bundle
Verification guarantees
manifest integrity (SHA256)
transcript binding
fail-closed result consistency
witness signatures (local / checkpoint)
GitHub run binding
external timestamp (OTS)
Sigstore transparency (cosign)
Important note

This stage does NOT introduce a new cryptographic proof.

It strengthens the evidence chain:

QSP execution
→ manifest
→ anchors
→ independent verification
Why this matters

Previous stages proved:

reproducibility
transparency
verifiability

Stage254 proves:

👉 the evidence originates from real protocol execution

Limitations
Assumes QSP implementation outputs JSON
Depends on Stage226 structure
OTS verification may be pending until blockchain confirmation
License

MIT License

Copyright (c) 2025 Motohiro Suzuki