Stage251: Multi-Anchor Verification (Threshold-based Trust Model)

## Overview

Stage251 introduces a **multi-anchor verification model** that removes single-point dependency on GitHub.

Instead of relying on a single source of truth, this stage implements:

- Multiple independent anchors
- Threshold-based verification (2-of-3)
- Distributed trust model

---

## Why This Matters

Previous stages relied on:

- GitHub Release as the primary anchor

This creates a **single point of failure**.

Stage251 solves this by introducing:

- Multiple anchors
- Independent verification paths
- Threshold-based acceptance

---

## Architecture

### Anchors

| Anchor Type | Description |
|------------|------------|
| GitHub Release Anchor | External reference (Stage250) |
| Local Witness | Ed25519 signature |
| Checkpoint Witness | Append-only checkpoint chain |

---

### Policy

```json
{
  "threshold": 2,
  "accepted_anchor_types": [
    "github_release_anchor",
    "local_witness",
    "checkpoint_witness"
  ]
}
Verification Model

Verification succeeds if:

👉 At least 2 independent anchors agree

Example:

GitHub + Local → OK
Local + Checkpoint → OK
GitHub only → NG
How It Works
Step 1: Build request
python3 tools/build_multi_anchor_request.py \
  --subject downloaded_stage250_release_anchor/release_manifest.json \
  --output out/multi_anchor/request.json
Step 2: Generate anchors
./tools/run_stage251_multi_anchor.sh

This will:

Create request
Generate local witness signature
Generate checkpoint anchor
Import GitHub anchor
Verify all anchors
Output
out/multi_anchor/

Includes:

request.json
local_witness_receipt.json
checkpoint_witness_receipt.json
github_release_anchor_normalized.json
checkpoint history
Security Properties
1. No Single Point of Trust

Verification does not depend on GitHub alone.

2. Threshold-Based Trust

Requires multiple independent confirmations.

3. Tamper Detection

Any mismatch in hash breaks verification.

4. Auditability

All anchors are verifiable independently.

Limitations
Local witness and checkpoint anchors are controlled by the same operator
Not yet a fully independent third-party trust system
Next Step

👉 Stage252: External Anchor Integration

RFC3161 timestamp
Sigstore / Rekor
Third-party witness
Conclusion

Stage251 transforms verification from:

👉 Single-anchor trust

to

👉 Distributed, threshold-based trust

License

MIT License

Copyright (c) 2025 Motohiro Suzuki

Permission is hereby granted, free of charge, to any person obtaining a copy...