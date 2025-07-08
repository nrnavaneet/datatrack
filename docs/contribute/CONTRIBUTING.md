# Contributing to Datatracker

Thank you for your interest in contributing!
Datatracker is a lightweight CLI tool to track schema changes across database versions. Your contributions—big or small—help make this project better for everyone.


## How to Contribute

### 1. Fork the Repo

Click the "Fork" button at the top right of [the repository](https://github.com/nrnavaneet/datatrack) and clone your fork:

```bash
git clone https://github.com/your-username/datatrack.git
cd datatrack
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 3. Make Your Changes

- Create a new branch:
  ```bash
  git checkout -b your-feature-name
  ```

- Follow code style (PEP8, Black) and ensure changes are meaningful.

### 4. Test Your Changes

Make sure everything still works:

Initialise it
```bash
datatrack init
```

```bash
datatrack pipeline run --source sqlite:///.databases/example.db
```

Add or update unit tests if necessary.

### 5. Run Pre-commit Hooks

Install and run pre-commit checks:

```bash
pre-commit install
pre-commit run --all-files
```

### 6. Commit and Push

```bash
git add .
git commit -m " Add new feature or fix bug"
git push origin your-feature-name
```

### 7. Open a Pull Request

Go to your fork and open a **Pull Request (PR)** to `main`.
Describe your changes clearly, and link any related issues.


## Code of Conduct

Please be kind and respectful in all interactions.
We follow the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) code of conduct.


## Need Help?

Open an [issue](https://github.com/nrnavaneet/datatrack/issues), or reach out via GitHub Discussions if you have questions.

Thanks for helping improve Datatracker! 💙
