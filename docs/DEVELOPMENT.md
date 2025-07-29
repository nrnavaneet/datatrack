# Development Guide

This guide provides information for developers working on the Datatrack project.

## Development Setup

### 1. Clone and Setup

```bash
git clone https://github.com/nrnavaneet/datatrack.git
cd datatrack

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### 2. Install Pre-commit Hooks

```bash
pre-commit install
```

## Project Structure

```
datatrack/
├── datatrack/           # Main package
│   ├── cli.py          # CLI interface
│   ├── tracker.py      # Schema introspection engine
│   ├── diff.py         # Schema comparison
│   ├── linter.py       # Schema quality checks
│   └── ...
├── tests/              # Test suite
│   ├── test_tracker.py
│   ├── test_performance.py
│   └── ...
└── docs/               # Documentation
```

## Performance Architecture

Datatrack includes performance optimizations:

### Core Components

1. **Parallel Processing** (`tracker.py`):
   - ThreadPoolExecutor-based table introspection
   - Configurable worker pools
   - Error handling for concurrent operations

2. **Memory Management**:
   - Batched processing for large schemas
   - Memory-efficient data structures
   - Intelligent strategy selection

3. **Performance Testing** (`test_performance.py`):
   - Mocked timing tests for consistent CI/CD
   - Benchmark validation
   - Performance regression detection

## Testing

## Testing

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test categories
pytest tests/test_performance.py -v    # Performance tests
pytest tests/test_tracker.py -v       # Core functionality
pytest tests/test_cli.py -v           # CLI interface

# Run with coverage
pytest tests/ --cov=datatrack --cov-report=term-missing

# Run performance benchmarks
python performance_demo.py
```

### Test Structure

```
tests/
├── conftest.py              # Shared fixtures
├── test_cli.py             # CLI command tests
├── test_tracker.py         # Schema tracking tests
├── test_performance.py     # Performance optimization tests
└── ...
```

### Writing Tests

```python
def test_feature():
    """Test description."""
    # Arrange
    data = create_test_data()

    # Act
    result = function_under_test(data)

    # Assert
    assert result == expected_value
```

### Running Tests

#### Basic Test Commands

```bash
# Run all tests (including performance tests)
pytest tests/

# Run performance benchmarks
python performance_demo.py
```

#### Specific Test Categories

```bash
# Run specific test file
pytest tests/test_cli.py

# Run performance tests
pytest tests/test_performance.py -v

# Run specific test class
pytest tests/test_cli.py::TestCLI

# Run specific test method
pytest tests/test_cli.py::TestCLI::test_init_command_success

# Test performance regression
pytest tests/test_performance.py::test_parallel_performance_improvement -v
```

## Code Quality

### Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

### Code Formatting

```bash
# Format code with Black
black datatrack/ tests/

# Lint with Ruff
ruff check datatrack/ tests/
```

### Type Checking

```bash
# Run mypy (if configured)
mypy datatrack/
```

## Development Workflow

### 1. Feature Development

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes
# ... code changes ...

# Run tests
pytest tests/

# Run pre-commit checks
pre-commit run --all-files

# Commit changes
git commit -m "Add: your feature description"
```

### 2. Testing Changes

```bash
# Test specific functionality
pytest tests/test_module.py -v

# Test with coverage (including performance tests)
pytest tests/ --cov=datatrack --cov-report=term-missing

# Test edge cases
pytest tests/ -k "error or exception" -v

# Performance regression testing
pytest tests/test_performance.py -v --tb=short

# Benchmark current performance
python performance_demo.py
```

### 3. Performance Testing & Benchmarking

```bash
# Test performance optimizations
pytest tests/test_performance.py -v

# Run benchmark demonstration
python performance_demo.py

# Test with large mock schemas
pytest tests/test_performance.py::test_batch_processing_large_schemas -v

# Validate parallel processing
pytest tests/test_performance.py::test_parallel_vs_sequential_processing -v
```

## Test Data and Fixtures

### Common Fixtures (conftest.py)

- `tmp_path`: Temporary directory for tests
- `mock_datatrack_dir`: Mocked datatrack configuration
- `sample_schema_data`: Sample database schema for testing
- `in_memory_sqlite_engine`: SQLite engine for testing

### Creating Test Data

```python
# Example: Creating test schema data
def create_test_schema():
    return {
        "tables": [
            {
                "name": "users",
                "columns": [
                    {"name": "id", "type": "INTEGER", "nullable": False},
                    {"name": "name", "type": "VARCHAR(100)", "nullable": False}
                ],
                "primary_key": ["id"],
                "foreign_keys": [],
                "indexes": []
            }
        ],
        "views": [],
        "triggers": []
    }
```

## Debugging Tests

### Debugging Failed Tests

```bash
# Run with detailed output
pytest tests/test_file.py::test_method -vvv

# Drop into debugger on failure
pytest tests/test_file.py::test_method --pdb

# Show local variables in traceback
pytest tests/test_file.py::test_method --tb=long -vv
```

### Mock Debugging

```python
# Debug mock calls
mock_function.assert_called_with(expected_args)
print(mock_function.call_args_list)  # See all calls
print(mock_function.return_value)    # Check return value
```

## Continuous Integration

Tests run automatically on:
- Pull requests
- Pushes to main branch
- Scheduled runs (if configured)

Local commands mirror CI environment:

```bash
# Run the same checks as CI
pytest tests/ --cov=datatrack --cov-fail-under=80
pre-commit run --all-files
```

## Performance Testing

```bash
# Run with performance profiling
pytest tests/ --profile

# Time test execution
pytest tests/ --durations=10
```

## Test Coverage Goals

- **Unit tests**: Aim for >90% coverage
- **Integration tests**: Cover main user workflows
- **Edge cases**: Test error conditions and edge cases
- **Regression tests**: Add tests for bug fixes

### Coverage Reporting

```bash
# Generate coverage report
pytest tests/ --cov=datatrack --cov-report=html

# View coverage report
open htmlcov/index.html  # Opens in browser
```

## Adding New Tests

When adding new functionality:

1. **Write tests first** (TDD approach)
2. **Test happy path and error cases**
3. **Mock external dependencies**
4. **Update fixtures if needed**
5. **Ensure tests are isolated and repeatable**

## Troubleshooting Common Issues

### Import Errors
```bash
# Ensure package is installed in development mode
pip install -e .
```

### Path Issues
```bash
# Run tests from project root
cd /path/to/datatrack
pytest tests/
```

### Mock Issues
```python
# Use proper patch targets
@patch('datatrack.module.function')  # Target where it's used
# not @patch('original.module.function')  # Not where it's defined
```

This comprehensive testing setup ensures reliable, maintainable code and catches issues early in development.
