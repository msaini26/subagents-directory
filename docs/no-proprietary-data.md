# Public-Safe Publishing Checklist

Use this checklist before publishing or updating the repository.

## Do Not Include

- Proprietary product names, roadmap details, or release plans
- Customer, employee, partner, or stakeholder names
- Private research notes, interview excerpts, or datasets
- Screenshots, documents, exports, or source files from private projects
- Environment variables, API keys, model credentials, or service URLs
- Private branch names, ticket IDs, pull request details, or internal links

## Prefer

- Generic product terms
- Role-based personas
- Synthetic examples
- Publicly explainable workflows
- Adapter code that expects private context to be supplied by the consuming project

## Suggested Local Scan

Run a case-insensitive scan for terms you know should never appear in a public repo:

```bash
rg -i "company-name|project-code-name|customer-name|private-domain|api-key|secret|token"
```

Then review every match manually before publishing.
