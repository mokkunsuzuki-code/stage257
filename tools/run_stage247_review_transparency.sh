#!/usr/bin/env bash
set -euo pipefail

mkdir -p keys out/review_log

if [ ! -f keys/owner_private.pem ]; then
  echo "[INFO] owner_private.pem not found. Generating new Ed25519 keypair..."
  openssl genpkey -algorithm Ed25519 -out keys/owner_private.pem
  openssl pkey -in keys/owner_private.pem -pubout -out keys/owner_public.pem
fi

if [ ! -f keys/owner_public.pem ]; then
  echo "[INFO] owner_public.pem not found. Deriving public key from private key..."
  openssl pkey -in keys/owner_private.pem -pubout -out keys/owner_public.pem
fi

python3 tools/build_review_log.py \
  --source-dir review_records \
  --output-dir out/review_log \
  --private-key keys/owner_private.pem

python3 tools/verify_review_log.py \
  --review-log out/review_log/review_log.json \
  --hash-file out/review_log/review_log_hash.txt \
  --sig-file out/review_log/review_log.sig \
  --public-key keys/owner_public.pem

echo "[OK] Stage247 review transparency completed."
