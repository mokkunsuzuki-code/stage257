#!/usr/bin/env bash
set -e

python3 tools/create_third_party_chain_record.py \
  --executor A \
  --bundle-path bundle_v1 \
  --result success

python3 tools/create_third_party_chain_record.py \
  --executor B \
  --bundle-path bundle_v1 \
  --result success

python3 tools/create_third_party_chain_record.py \
  --executor C \
  --bundle-path bundle_v1 \
  --result success

python3 tools/verify_third_party_chain.py

echo "[DONE] Stage257 completed"
