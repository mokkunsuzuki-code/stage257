# Stage242: Multi-Party Approval (2-of-3 with External Reviewer)

MIT License © 2025 Motohiro Suzuki

---

## Overview

Stage242 introduces **multi-party approval with enforced independence**.

It upgrades the trust model from:

- multiple keys (Stage241)

to:

- **multiple independent human approvals**

---

## Core Policy

The repository enforces:

- **At least 2 valid signatures required (2-of-3)**
- **At least 1 external signer required**
- **Approvals must span ≥2 independence groups**

Defined in:


docs/stage242_policy.yaml


---

## Roles

| Role        | Description              | Group       |
|------------|--------------------------|------------|
| developer  | artifact creator         | owner      |
| auditor    | internal reviewer        | owner      |
| reviewer   | external reviewer        | external   |

---

## Why Stage242 Matters

Stage241:

- 2-of-2 signatures
- but both controlled by same person

Stage242:

- separates authority across **independent actors**
- prevents self-approval

---

## Example

### ❌ Not Enough


developer ✔
auditor ✔
reviewer ✖


- threshold satisfied (2)
- but no external signer
- ❌ verification fails

---

### ✅ Valid


developer ✔
reviewer ✔


- threshold satisfied (2)
- external signer present
- independence satisfied
- ✅ verification succeeds

---

## Demo

Run the full demonstration:

```bash
./tools/run_stage242_demo.sh

Expected behavior:

Fails without external reviewer
Passes after reviewer signs
Verification
python tools/verify_stage242_threshold.py \
  --config docs/stage242_policy.yaml \
  --signatures-dir signatures
Security Model

This stage extends the pipeline:

Assumption
→ Claim
→ Evidence
→ Approval Policy
→ Verification

Key property:

A single actor cannot approve their own output.

What Changed from Stage241
Stage	Model	Meaning
241	2-of-2 keys	technical threshold
242	2-of-3 people	distributed trust
Significance

Stage242 is not only stronger cryptography.

It introduces:

governance enforcement
independence verification
human-layer security guarantees
Next Direction
Stage243: real external reviewers (non-local keys)
public audit participation
research / standardization readiness