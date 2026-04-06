# Stage256: External Execution Record (QSP)

## Overview

Stage256 records independently executed QSP runs.

A third party can:

- run QSP in their own environment
- generate an anchor from their execution
- record that execution as a verifiable receipt
- verify the entire execution history later

---

## Key Concept

Stage255:

- third party execution

Stage256:

- third party execution + recorded + verifiable

---

## Quick Start

```bash
git clone https://github.com/mokkunsuzuki-code/stage256.git
cd stage256

export QSP_EXTERNAL_COMMAND="python tools/run_stage255_qsp.py"
bash tools/run_stage256_external_record.sh
Outputs

out/external_execution_record/

review_log.json
review_log.json.sha256
receipts/*.json
Example Record
{
  "reviewer_id": "reviewer_local",
  "executed_at_utc": "...",
  "bundle_manifest_sha256": "...",
  "anchor_sha256": "...",
  "qsp_result_sha256": "...",
  "receipt_sha256": "..."
}
Security Meaning

This stage upgrades:

"external execution"

to:

"externally recorded and verifiable execution history"

Next Steps
Stage257: Multi-party execution chain
License

MIT License
