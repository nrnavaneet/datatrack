# Releasing Datatrack

[← Documentation home](README.md)

This document is for **maintainers** cutting a PyPI release of `datatrack-core`. End users install with `pip install datatrack-core` and do not need these steps.

The shorter **`pypiREADME.md`** file ships on PyPI; it now includes a compact **Contributing** section that points back to these longer guides on GitHub.

## Checklist

1. Ensure `main` is green (push CI and weekly schedule).
2. Update **`pyproject.toml`** `version = "x.y.z"`.
3. Add a matching **`CHANGELOG.md`** section with the release date and bullet points.
4. Run **`make test`** and **`pre-commit run --all-files`** locally.
5. Tag the release commit: `git tag -s vX.Y.Z -m "Release X.Y.Z"` (maintainer GPG optional but preferred).
6. Build and upload with **Twine** after reviewing the sdist/wheel contents:

```bash
python3 -m pip install build twine
python3 -m build
python3 -m twine upload dist/datatrack_core-X.Y.Z*
```

## After release

- Verify the [PyPI project page](https://pypi.org/project/datatrack-core/) shows the new version.
- If the release fixes a security issue, follow **SECURITY.md** disclosure timing before announcing details publicly.
