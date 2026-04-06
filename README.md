# Stage254: Real QSP Integration

Stage254 replaces the Stage253 deterministic demo with real QSP execution integration.

This stage executes the real QSP implementation, normalizes the resulting session log, generates `session_manifest.json`, and anchors it with:

- local witness
- checkpoint witness
- GitHub anchor
- OpenTimestamps (OTS)
- cosign bundle

## Why this stage matters

Stage253 proved that the anchoring structure works.

Stage254 proves that the evidence chain is generated from real QSP execution output rather than a demo-only session.

The core chain is:

Real QSP execution  
→ session result  
→ session manifest  
→ anchored evidence  
→ independent verification

## What Stage254 does

1. Executes the real QSP implementation (default: `../stage226`)
2. Collects a real JSON session result
3. Normalizes the result into `qsp_session_result.json`
4. Extracts and binds:
   - transcript
   - transcript hash
   - policy
   - fail-closed result
5. Anchors the manifest with witnesses and external receipts

## Files

- `tools/run_real_qsp_session.py`  
  Runs and normalizes real QSP output

- `tools/build_session_manifest.py`  
  Builds `session_manifest.json`

- `tools/sign_session_manifest.py`  
  Creates local and checkpoint witnesses

- `tools/verify_session_anchor.py`  
  Verifies the complete evidence chain

- `.github/workflows/stage254-real-qsp-anchor.yml`  
  Produces GitHub / OTS / cosign anchors

## Local execution

```bash
./tools/run_stage254_real_qsp_anchor.sh
If your real QSP command differs

Set it explicitly:

export QSP_REAL_REPO=../stage226
export QSP_REAL_RUN_CMD="python3 tools/run_stage226_poc.py"
./tools/run_stage254_real_qsp_anchor.sh
Verification
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
Limitations
The adapter assumes the real QSP implementation emits JSON output
If your stage226 entrypoint differs, set QSP_REAL_RUN_CMD
This stage improves evidence integration, not cryptographic claims
License

MIT License

Copyright (c) 2025 Motohiro Suzuki
