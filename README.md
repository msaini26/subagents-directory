# Reusable AI Subagents

A public-safe library of reusable agent definitions for product, design, engineering, research, review, and quality workflows.

These agents are intentionally generic. They do not include proprietary product details, customer names, internal terminology, private roadmaps, or company-specific process language. Use them as starting points and customize them inside your own private workspace.

## What's Included

| Agent | Use When You Need |
| --- | --- |
| Product Strategy Partner | Scope, prioritization, requirements, acceptance criteria |
| UX Designer | Flows, hierarchy, copy, interaction patterns, design handoff |
| Usability Evaluation Agent | Persona-driven usability testing and heuristic evaluation |
| Research Synthesis Analyst | Turning mixed evidence into themes, risks, and decisions |
| Technical Architect | System shape, data flow, component boundaries, implementation risks |
| Software Engineer | Concrete implementation plans and code-oriented execution |
| Code Reviewer | Quality, security, accessibility, maintainability review |
| QA Readiness Analyst | Test planning, release confidence, scenario coverage |
| Documentation Steward | Documentation audits, stale-doc fixes, onboarding clarity |

## Repository Layout

```text
agents/
  catalog.yaml             # Machine-readable agent definitions
  *.md                     # Human-readable agent cards
adapters/crewai/
  agent_factory.py         # Minimal CrewAI adapter
examples/
  crewai_minimal.py        # Example workflow using the catalog
docs/
  no-proprietary-data.md   # Safety checklist for keeping this repo public-safe
```

## Use With CrewAI

Install CrewAI in your own project environment, then import the adapter:

```python
from adapters.crewai.agent_factory import build_agent, load_catalog

catalog = load_catalog("agents/catalog.yaml")
ux_designer = build_agent(catalog["ux_designer"], llm=my_llm)
```

The adapter expects you to provide your own LLM object. This keeps model choice, credentials, and private environment configuration outside this repository.

## Customization Guidance

Keep public versions generic:

- Replace private project names with neutral terms like "the product" or "the workflow".
- Replace customer or employee names with role-based personas.
- Keep examples synthetic.
- Put private prompts, source files, datasets, and implementation context in your own private repo.
- Before publishing changes, run the safety scan in `docs/no-proprietary-data.md`.

## License

MIT. Use, adapt, and share these agents freely.
