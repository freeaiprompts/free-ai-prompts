#!/usr/bin/env python3
"""Checks data/prompts.json: required fields, unique ids/slugs, balanced [brackets]."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ["id", "title", "slug", "type", "categories", "tools", "prompt", "description"]
TYPES = {"photo", "video", "text", "code"}

data = json.loads((ROOT / "data" / "prompts.json").read_text(encoding="utf-8"))
errors, ids, slugs = [], set(), set()

for p in data["prompts"]:
    name = p.get("title", "?")
    for key in REQUIRED:
        if not p.get(key):
            errors.append(f"{name}: missing '{key}'")
    if p.get("type") not in TYPES:
        errors.append(f"{name}: type must be one of {sorted(TYPES)}")
    if p.get("id") in ids:
        errors.append(f"{name}: duplicate id {p.get('id')}")
    if p.get("slug") in slugs:
        errors.append(f"{name}: duplicate slug {p.get('slug')}")
    ids.add(p.get("id"))
    slugs.add(p.get("slug"))
    text = p.get("prompt", "")
    if text.count("[") != text.count("]"):
        errors.append(f"{name}: unbalanced [brackets]")
    if len(p.get("title", "")) > 80:
        errors.append(f"{name}: title longer than 80 characters")
    if not re.match(r"^[a-z0-9-]+$", p.get("slug", "")):
        errors.append(f"{name}: slug must be lowercase letters, numbers and dashes")

if data.get("count") != len(data["prompts"]):
    errors.append(f"count is {data.get('count')} but there are {len(data['prompts'])} prompts")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK - {len(data['prompts'])} prompts valid")
