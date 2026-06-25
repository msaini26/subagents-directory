"""Build CrewAI agents from the reusable catalog.

This adapter intentionally does not create or configure an LLM. Keep model
choice, credentials, and private project context in your consuming project.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from crewai import Agent


def load_catalog(path: str | Path) -> dict[str, dict[str, Any]]:
    """Load agent definitions from the YAML catalog."""
    catalog_path = Path(path)
    data = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    return data["agents"]


def build_agent(definition: dict[str, Any], *, llm: Any) -> Agent:
    """Create a CrewAI Agent from one catalog entry."""
    return Agent(
        role=definition["role"],
        goal=definition["goal"],
        backstory=definition["backstory"],
        llm=llm,
        verbose=True,
        allow_delegation=definition.get("allow_delegation", False),
        memory=definition.get("memory", False),
    )
