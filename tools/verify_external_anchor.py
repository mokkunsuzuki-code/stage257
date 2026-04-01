#!/usr/bin/env python3
# MIT License
# Copyright (c) 2025 Motohiro Suzuki

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify external timestamp anchor")
    parser.add_argument(
        "--request",
        default="out/anchors/anchor_request.json",
        help="Path to anchor request JSON",
    )
    parser.add_argument(
        "--receipt",
        default="out/anchors/github_anchor_receipt.json",
        help="Path to GitHub anchor receipt JSON",
    )
    args = parser.parse_args()

    request_path = Path(args.request)
    receipt_path = Path(args.receipt)

    if not request_path.exists():
        raise FileNotFoundError(f"Missing request file: {request_path}")
    if not receipt_path.exists():
        raise FileNotFoundError(f"Missing receipt file: {receipt_path}")

    request = read_json(request_path)
    receipt = read_json(receipt_path)

    request_sha256 = sha256_file(request_path)
    receipt_request_sha256 = receipt.get("request_sha256")
    if request_sha256 != receipt_request_sha256:
        raise ValueError(
            f"Request hash mismatch: computed={request_sha256} receipt={receipt_request_sha256}"
        )

    if receipt.get("stage") != "stage249":
        raise ValueError("Receipt stage is not stage249")

    if receipt.get("anchor_type") != "github_actions_external_timestamp_receipt":
        raise ValueError("Unexpected receipt anchor_type")

    if request.get("sequence") != receipt.get("request_sequence"):
        raise ValueError("Request sequence does not match receipt request_sequence")

    request_checkpoint_id = request.get("semantic_binding", {}).get("checkpoint_id")
    receipt_checkpoint_id = receipt.get("checkpoint_id")
    if request_checkpoint_id != receipt_checkpoint_id:
        raise ValueError("Checkpoint ID mismatch between request and receipt")

    request_checkpoint_seq = request.get("semantic_binding", {}).get("checkpoint_latest_history_sequence")
    receipt_checkpoint_seq = receipt.get("checkpoint_sequence")
    if request_checkpoint_seq != receipt_checkpoint_seq:
        raise ValueError("Checkpoint sequence mismatch between request and receipt")

    run_url = receipt.get("run_url")
    if not run_url or "/actions/runs/" not in run_url:
        raise ValueError("Receipt run_url is missing or malformed")

    print("[OK] external anchor verified")
    print(f"[OK] request_sha256: {request_sha256}")
    print(f"[OK] checkpoint_id: {request_checkpoint_id}")
    print(f"[OK] checkpoint_sequence: {request_checkpoint_seq}")
    print(f"[OK] run_url: {run_url}")


if __name__ == "__main__":
    main()
