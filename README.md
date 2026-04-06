# Stage253: QSP Session Anchoring

Stage253 binds anchoring evidence directly to QSP session execution output.

This stage generates `session_manifest.json` from a QSP session result and fixes:

- transcript hash
- policy
- fail-closed result

The generated session manifest can then be verified through:

- local witness
- checkpoint witness
- GitHub anchor
- OpenTimestamps (OTS)
- cosign bundle

## Why this stage matters

The main value of Stage253 is not adding more external signatures first.

The main value is proving that the evidence structure is born directly from QSP itself.

That makes later external review stronger, because the reviewer can see:

QSP execution  
→ session result  
→ session manifest  
→ anchored evidence  
→ independent verification

## Files

- `tools/run_qsp_session_demo.py`  
  Minimal deterministic QSP session execution output

- `tools/build_session_manifest.py`  
  Builds `session_manifest.json` from QSP session result

- `tools/sign_session_manifest.py`  
  Creates local witness and checkpoint witness

- `tools/verify_session_anchor.py`  
  Verifies manifest binding and anchor artifacts

- `.github/workflows/stage253-session-anchor.yml`  
  Produces GitHub anchor receipt, OTS, and cosign bundle

## Quickstart

### 1. Local build

```bash
./tools/run_stage253_qsp_session_anchor.sh
2. Push to GitHub
git add .
git commit -m "Stage253: add QSP session anchoring"
git push
3. Download workflow artifacts
gh run list --workflow "stage253-session-anchor" --limit 5
gh run download <RUN_ID> -n stage253-session-anchor-artifacts -D downloaded_stage253_session_anchor
4. Verify
python3 tools/verify_session_anchor.py \
  --manifest downloaded_stage253_session_anchor/session_manifest.json \
  --session-result downloaded_stage253_session_anchor/qsp_session_result.json \
  --local-witness downloaded_stage253_session_anchor/local_witness.json \
  --local-public downloaded_stage253_session_anchor/local_witness_public.pem \
  --checkpoint-witness downloaded_stage253_session_anchor/checkpoint_witness.json \
  --checkpoint-public downloaded_stage253_session_anchor/checkpoint_witness_public.pem \
  --github-receipt downloaded_stage253_session_anchor/github_session_anchor_receipt.json \
  --ots downloaded_stage253_session_anchor/session_manifest.json.ots \
  --cosign-bundle downloaded_stage253_session_anchor/session_manifest.json.cosign.bundle
Verification meaning

This stage demonstrates:

the manifest is derived directly from QSP session execution output
transcript hash is fixed
policy is fixed
fail-closed result is fixed
witness and anchor artifacts point to the same manifest
Security note

This stage does not claim a new cryptographic proof.

It claims a stronger evidence chain:

QSP session execution output
→ session manifest
→ witness / checkpoint / external anchor artifacts
→ independent verification

License

MIT License

Copyright (c) 2025 Motohiro Suzuki
