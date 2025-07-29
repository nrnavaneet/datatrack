# Contributing to Datatrack

Thank you for your interest in contributing to Datatrack. We welcome contributions from the community to help make database schema management better for everyone.

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/datatrack.git
cd datatrack

# Add upstream remote
git remote add upstream https://github.com/nrnavaneet/datatrack.git
```

### 2. Development Environment

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with all dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

### 3. Verify Setup

```bash
# Run tests to ensure everything works
pytest tests/ -v

# Run performance tests
pytest tests/test_performance.py -v

# Check code quality
pre-commit run --all-files
```

## How to Contribute

### Bug Reports

Found a bug? Please check existing issues first, then create a new issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, database type)

### Feature Requests

Have an idea for improvement? Please:
- Check existing discussions and issues
- Describe the use case and expected behavior
- Explain why this would benefit other users

### Code Contributions

Ready to contribute code? Great! Please:
- Check for good first issues or help wanted labels
- Discuss major changes in issues first
- Follow our development workflow

## Development Workflow

### 1. Create a Feature Branch

```bash
# Update your fork
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/your-feature-name
```

### 2. Make Changes

- Write clean, well-documented code
- Follow existing code style and patterns
- Consider performance impact for database operations
- Add tests for new functionality

### 3. Test Your Changes

```bash
# Run full test suite
pytest tests/

# Run specific test categories
pytest tests/test_performance.py -v    # Performance tests
pytest tests/test_tracker.py -v       # Core functionality
pytest tests/test_cli.py -v           # CLI interface

# Test with coverage
pytest tests/ --cov=datatrack --cov-report=term-missing
```

### 4. Quality Checks

```bash
# Format code
black datatrack/ tests/

# Lint code
ruff check datatrack/ tests/

# Type checking
mypy datatrack/

# Run all pre-commit hooks
pre-commit run --all-files
```

### 5. Commit and Push

```bash
# Stage your changes
git add .

# Commit with descriptive message
git commit -m "feat: add parallel processing for large schemas"

# Push to your fork
git push origin feature/your-feature-name
```

### 6. Create Pull Request

- Use clear, descriptive title and description
- Link related issues and discussions
- Include screenshots for UI changes
- Ensure all checks pass

## Code Guidelines

### Python Style
- Follow PEP 8 style guide
- Use Black for code formatting
- Use Ruff for linting
- Add type hints for new functions

### Commit Messages
```
type: brief description

Longer explanation if needed

Closes #123
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### Testing
- Write tests for new functionality
- Maintain existing test coverage
- Use descriptive test names
- Mock external dependencies

## Getting Help

Need help? We're here for you:

- GitHub Discussions for general questions
- GitHub Issues for bug reports and feature requests
- Email maintainer for sensitive issues

## Code of Conduct

Please be respectful and inclusive in all interactions. We follow the Contributor Covenant code of conduct.

Thank you for contributing to Datatrack!
