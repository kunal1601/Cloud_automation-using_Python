#!/usr/bin/env bash
# Load environment variables from .env into current shell
set -a
if [ -f ".env" ]; then
  source .env
  echo "Loaded .env"
else
  echo ".env not found. Copy env.example.txt to .env and edit."
fi
set +a
