# Stage250: Release Anchoring (GitHub Actions)

## Overview

Stage250 extends Stage249 by introducing **release-oriented anchoring**.

Instead of anchoring only to a CI execution, this stage binds the anchor artifacts
into a **release manifest**, and records that manifest in a publicly observable
GitHub Actions execution.

This provides a stronger, more explainable unit of evidence than CI-only anchoring.

---

## Architecture

Review Log  
↓  
Checkpoint Chain (Stage248)  
↓  
External Timestamp Anchor (Stage249)  
↓  
Release Manifest (Stage250)  
↓  
GitHub Actions Receipt  
↓  
Verification  

---

## What This Stage Achieves

- Binds Stage249 anchor artifacts into a release-level manifest
- Generates deterministic manifest with SHA256
- Records GitHub Actions execution metadata as a release receipt
- Enables third-party verification of manifest ↔ receipt consistency

---

## Key Files

### Release Manifest

- out/release_anchor/release_manifest.json
- out/release_anchor/release_manifest.sha256
- out/release_anchor/release_manifest_summary.json

### External Receipt

- github_release_anchor_receipt.json
- github_release_anchor_receipt.sha256

### Tools

- tools/generate_release_manifest.py
- tools/record_release_anchor_receipt.py
- tools/verify_release_anchor.py

---

## How It Works

### 1. Generate Release Manifest

```bash
./tools/run_stage250_release_anchor.sh

This binds:

anchor_request
anchor_summary
checkpoint reference

into a single release-oriented manifest.

2. GitHub Actions Execution

Workflow:

.github/workflows/stage250-release-anchor.yml

Performs:

reconstruct transparency input
regenerate anchor request
generate release manifest
record execution metadata
produce receipt
3. Verify Release Anchor
python3 tools/verify_release_anchor.py \
  --manifest release_manifest.json \
  --receipt github_release_anchor_receipt.json
Example Verification Output

[OK] release anchor verified
[OK] manifest_sha256: <hash>
[OK] release_tag: stage250-v1
[OK] checkpoint_id: 1
[OK] run_url: https://github.com/
...

Security Meaning

This stage proves:

Stage249 anchor artifacts existed
they were bound into a release manifest
that manifest appeared in a public CI execution
the relationship is reproducible and verifiable
What This Is NOT
Not RFC3161 TSA
Not blockchain anchoring
Not immutable global timestamping
Why This Matters
Moves from "execution-level proof" to "release-level proof"
Improves explainability for external reviewers
Maintains full reproducibility
Avoids unverifiable claims
Design Philosophy

Do not claim stronger security than what can be verified.

Next Steps
Stage251: Multi-anchor (eliminate single-point dependency)
External mirrors / distributed anchoring
Reviewer validation and audit
License

MIT License © 2025 Motohiro Suzuki
