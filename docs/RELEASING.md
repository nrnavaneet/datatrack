# Releasing Datatrack

[← Documentation home](README.md)

This document is for **maintainers** cutting a PyPI release of `datatrack-core`. End users install with `pip install datatrack-core` and do not need these steps.

The shorter **`pypiREADME.md`** file ships on PyPI; it now includes a compact **Contributing** section that points back to these longer guides on GitHub.

PyPI readers should follow links from that readme to **Roadmap**, **Compatibility**, and **Support** pages when planning larger changes.

1. Ensure `main` is green (push CI and weekly schedule).
2. Update **`pyproject.toml`** `version = "x.y.z"`.
3. Add a matching **`CHANGELOG.md`** section with the release date and bullet points.
4. Confirm `requirements.txt` matches any dependency changes in **`pyproject.toml`** so CI caches stay valid, then run **`make test`** and **`pre-commit run --all-files`** locally.
5. Tag the release commit: `git tag -s vX.Y.Z -m "Release X.Y.Z"` (maintainer GPG optional but preferred).
6. Build and upload with **Twine** after reviewing the sdist/wheel contents:

```bash
python3 -m pip install build twine
python3 -m build
python3 -m twine check dist/*
python3 -m twine upload dist/datatrack_core-X.Y.Z*
```

`MANIFEST.in` ensures long-form docs and policy files ship in the **sdist** alongside the Python package; skim the generated `dist/*.tar.gz` before upload. Confirm the root `LICENSE` still carries the SPDX identifier line expected by compliance scanners.

## After release

- Verify the [PyPI project page](https://pypi.org/project/datatrack-core/) shows the new version.
- If the release fixes a security issue, follow **SECURITY.md** disclosure timing before announcing details publicly.
- Update [Credits](CREDITS.md) if maintainer contact metadata changed in the same release.
- If you are announcing a notable public adoption, consider adding an entry to [Adopters](ADOPTERS.md) in a follow-up PR after the release dust settles.
