## What changed

<!-- Short description for reviewers -->

## Risk / rollout notes

<!-- Call out migrations, breaking CLI flags, or anything that should ship behind a major bump -->

## How to test

```bash
python3 -m pytest tests/ -q
# or: make test
```

## Checklist

- [ ] Docs updated if user-facing behaviour changed
- [ ] `pre-commit run --all-files` passes locally (or `make lint`)
- [ ] No secrets or production URIs in commits
- [ ] `CHANGELOG.md` and `pyproject.toml` versions updated if this PR is release-worthy
