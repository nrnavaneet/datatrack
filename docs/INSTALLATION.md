# Installation Guide

Datatrack is a high-performance CLI tool for tracking database schema changes. Choose the installation method that best fits your use case.

## Install from PyPI (Recommended)

For most users, install from PyPI:

```bash
# Basic installation
pip install datatrack-core

# With development dependencies (for contributors)
pip install datatrack-core[dev]
```

## Install from Source

For development or contributing:

```bash
git clone https://github.com/nrnavaneet/datatrack.git
cd datatrack

# Install in development mode
pip install -e .[dev]
```

## Quick Setup

Initialize a new project:

```bash
datatrack init
```

This creates a `.datatrack/` folder with configuration files.

## Performance Features

Datatrack automatically optimizes processing based on schema size:

- **Small schemas (1-49 tables)**: Standard processing
- **Medium schemas (50-199 tables)**: Parallel processing (65-70% faster)
- **Large schemas (200+ tables)**: Parallel + batched processing (70-75% faster)
## Manual Performance Configuration

For specific performance needs:

```bash
# Enable parallel processing
datatrack snapshot --parallel

# Custom worker count
datatrack snapshot --parallel --max-workers 8

# Custom batch size
datatrack snapshot --batch-size 50
```

## Verification

Test your installation:

```bash
# Run basic tests
pytest tests/

# Run performance tests
pytest tests/test_performance.py

# Test CLI functionality
datatrack --help
```

## System Requirements

- **Python**: 3.8 or higher
- **Memory**: Minimum 512MB RAM (2GB+ recommended for large schemas)
- **CPU**: Multi-core recommended for parallel processing benefits
- **Storage**: ~10MB for installation + database snapshot storage

## Troubleshooting

### Common Issues

**Import Errors**: Ensure you're in the correct virtual environment
```bash
which python
pip list | grep datatrack
```

**Database Connection Issues**: Check your connection string format
```bash
datatrack connect --test postgresql://user:pass@localhost:5432/db
```

**Performance Issues**: For large schemas, ensure sufficient memory
```bash
datatrack snapshot --batch-size 25  # Reduce batch size
```

## Next Steps

After installation:

1. [Quick Start Guide](../USAGE.md) - Learn basic commands
2. [Database Connections](../USAGE.md#database-connections) - Connect to your database
3. [Performance Tuning](../USAGE.md#performance-optimization) - Optimize for your workload

For issues, visit [GitHub Issues](https://github.com/nrnavaneet/datatrack/issues).

# For development installations, run tests with coverage
pytest tests/ --cov=datatrack --cov-report=term-missing --cov-report=html

# Test performance optimizations specifically
pytest tests/test_performance.py -v

# Benchmark performance improvements
python performance_demo.py

# Run linting and formatting checks (dev dependencies required)
black --check datatrack/
ruff check datatrack/
mypy datatrack/
```

## System Requirements

- **Python**: 3.8 or higher
- **Memory**: Minimum 512MB RAM (2GB+ recommended for large schemas)
- **CPU**: Multi-core recommended for parallel processing benefits
- **Storage**: ~10MB for installation + database snapshot storage

## Performance Benchmarks

On typical systems, expect these performance improvements:

| Schema Size   | Processing Method    | Improvement   |
|---------------|----------------------|---------------|
| 10-49 tables  | Standard | Baseline  |               |
| 50-199 tables | Parallel (4 workers) | 65-70% faster |
| 200+ tables   | Parallel + Batched   | 70-75% faster |

For any issues, refer to [https://github.com/nrnavaneet/datatrack/issues](https://github.com/nrnavaneet/datatrack/issues).
