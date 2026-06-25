#!/usr/bin/env python3
import os
from pathlib import Path


def load_env_file(project_root: Path, env_filename: str = ".env") -> dict[str, str]:
    env_path = project_root / env_filename
    values: dict[str, str] = {}
    if not env_path.exists():
        return values

    for raw_line in env_path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        cleaned_key = key.strip()
        cleaned_value = value.strip().strip("'").strip('"')
        values[cleaned_key] = cleaned_value
        if cleaned_key not in os.environ:
            os.environ[cleaned_key] = cleaned_value
    return values
