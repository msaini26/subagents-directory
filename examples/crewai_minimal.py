"""Minimal CrewAI example using the reusable agent catalog.

Replace `my_llm` with the LLM configured in your own private project.
"""

from __future__ import annotations

from pathlib import Path

from adapters.crewai.agent_factory import build_agent, load_catalog


ROOT = Path(__file__).resolve().parents[1]


def build_example_agents(my_llm):
    catalog = load_catalog(ROOT / "agents" / "catalog.yaml")
    return [
        build_agent(catalog["usability_evaluation_agent"], llm=my_llm),
        build_agent(catalog["ux_designer"], llm=my_llm),
        build_agent(catalog["software_engineer"], llm=my_llm),
    ]
