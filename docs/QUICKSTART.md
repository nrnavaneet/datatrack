# Quick Start Guide

Get up and running with Datatrack in under 5 minutes.

## Installation

```bash
pip install datatrack-core
```

## Basic Usage

### 1. Initialize Your Project

```bash
# Initialize datatrack in your project
datatrack init

# Connect to your database
datatrack connect "postgresql://user:password@localhost:5432/mydb"
```

### 2. Take Your First Snapshot

```bash
# Capture current schema
datatrack snapshot

# For large databases, use performance optimization
datatrack snapshot --parallel --max-workers 8
```

### 3. Track Changes

```bash
# Make some schema changes in your database, then...
datatrack snapshot

# See what changed
datatrack diff
```

### 4. Validate Schema Quality

```bash
# Check for naming conventions and best practices
datatrack lint

# Export schema for documentation
datatrack export --format json
```

## Example Workflow

```bash
# Day 1: Initial setup
datatrack init
datatrack connect "mysql://root:password@localhost:3306/ecommerce"
datatrack snapshot  # baseline snapshot

# Day 2: After adding new tables
datatrack snapshot
datatrack diff      # see changes
datatrack lint      # check quality

# Day 3: Before deployment
datatrack export --format yaml > schema_v1.2.yaml
```

## Performance Tips

- **Small databases** (< 50 tables): Standard mode works great
- **Medium databases** (50-200 tables): Use `--parallel` for 65-70% speed boost
- **Large databases** (200+ tables): Use `--parallel --batch-size 50` for 70-75% speed boost

## Next Steps

- [Complete Usage Guide](USAGE.md)
- [Installation Options](INSTALLATION.md)
- [Development Setup](DEVELOPMENT.md)
- [Contributing Guidelines](contribute/CONTRIBUTING.md)

## Need Help?

- 📖 [Full Documentation](../README.md)
- 🐛 [Report Issues](https://github.com/nrnavaneet/datatrack/issues)
- 💬 [Discussions](https://github.com/nrnavaneet/datatrack/discussions)
