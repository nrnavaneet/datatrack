# Performance and benchmarks

[← Documentation home](README.md)

Datatrack’s snapshot pipeline can run **serially** or with **parallel batching** for larger schemas. The numbers below are indicative: always measure against your own engines and hardware.

## Reference results

Benchmarks were run on a MacBook Pro M2, Python 3.11, using SQLite and PostgreSQL (August 2025).

| Database size | Tables | Serial time | Parallel time | Speedup | Time saved (per 1k runs) | Time saved (per 50k runs) |
|--------------:|-------:|------------:|--------------:|--------:|-------------------------:|--------------------------:|
| Small         | 12     | 0.18 s      | 0.09 s        | 2×      | 90 s                     | 75 min                    |
| Medium        | 75     | 0.95 s      | 0.32 s        | 3×      | 630 s (10.5 min)         | 8.75 hrs                  |
| Large         | 250    | 2.80 s      | 0.80 s        | 3.5×    | 2,000 s (~33 min)        | 27 hrs                    |

### Takeaways

- Snapshot wall time often drops **65–75%** for medium and large databases when parallel introspection is enabled.
- Savings scale with how often you snapshot in CI or data pipelines.

## Reproducing

See `benchmark_tests/README.md` and `benchmark_tests/parallel_processing.py` in the repository for the harness used to generate comparable figures. Those scripts intentionally stay **out of CI**; run them locally when validating performance work.

Hand-maintained YAML under [`examples/`](../examples/README.md) is useful for diffing tiny schemas without a live database.

## When I/O dominates

If your database is remote, network latency may overshadow local CPU parallelism. Prefer running benchmarks close to the server or against a restored copy when tuning.

Terminology for **snapshot**, **lint**, and **verify** is summarised in the [Glossary](GLOSSARY.md). A hand-maintained YAML example lives under [`examples/`](../examples/README.md) for diff experiments.
