"""Minimal smoke test -- run with: python tests/smoke_test.py"""

import json
from pathlib import Path


def test_config_parses() -> None:
    cfg = Path(__file__).resolve().parent.parent / "assets" / "config.json"
    if cfg.exists():
        data = json.loads(cfg.read_text(encoding="utf-8"))
        assert isinstance(data, dict)


def main() -> int:
    test_config_parses()
    print("all checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
