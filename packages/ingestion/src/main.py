"""Entry point for Helm post-install ingest Job."""

from __future__ import annotations

import os
import sys


def main() -> None:
    kb_dir = os.environ.get("KNOWLEDGE_BASE_DIR", "data/knowledge-base")
    print(f"Ingestion scaffold: knowledge base dir={kb_dir!r}")
    print("Implement chunking, embedding, and pgvector upsert in rh-qs-implement.")


if __name__ == "__main__":
    main()
    sys.exit(0)
