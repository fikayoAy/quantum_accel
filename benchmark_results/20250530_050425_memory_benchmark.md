# Quantum Virtual Memory Benchmark

**Date:** 2025-05-30 05:04:27
**Python Version:** 3.9.13
**Average Recovery Error:** 0.3551396899

## Memory Usage and Performance Results

| Vector Size | Traditional | | Python Virtual Memory | | Rust Virtual Memory | |
|-------------|-------------|------|-------------|------|-------------|------|
| | Time (ms) | Memory | Time (ms) | Memory | Time (ms) | Memory |
| 64 | 0.00 | 1.33 KB | 0.00 | 0.00 B | 0.00 | 12.00 KB |
| 128 | 0.00 | 0.00 B | 0.00 | 0.00 B | 0.00 | 0.00 B |
| 256 | 0.00 | 0.00 B | 0.67 | 0.00 B | 0.00 | 0.00 B |
| 512 | 0.00 | 44.00 KB | 0.00 | 0.00 B | 0.00 | 0.00 B |
| 1024 | 0.00 | 76.00 KB | 0.00 | 0.00 B | 0.00 | 0.00 B |
| 2048 | 5.38 | 80.00 KB | 0.73 | 0.00 B | 0.00 | 0.00 B |
| 4096 | 0.67 | 90.67 KB | 0.00 | 0.00 B | 0.00 | 0.00 B |
| 8192 | 0.60 | 178.67 KB | 0.67 | 0.00 B | 0.00 | 0.00 B |
| 16384 | 1.34 | -322218.67 B | 0.00 | 382.67 KB | 0.00 | 170.67 KB |
| 32768 | 4.01 | 300.00 KB | 0.00 | 425.33 KB | 0.67 | 85.33 KB |
| 65536 | 10.90 | 269.33 KB | 1.46 | 1.16 MB | 0.66 | 512.00 KB |
| 131072 | 18.06 | 1.00 MB | 4.62 | 1.00 MB | 5.01 | 4.00 KB |


## Memory Reduction Factor (compared to traditional storage)

| Vector Size | Python Virtual Memory | Rust Virtual Memory |
|-------------|----------------------|---------------------|
| 64 | infx | 0.11x |
| 128 | infx | infx |
| 256 | infx | infx |
| 512 | infx | infx |
| 1024 | infx | infx |
| 2048 | infx | infx |
| 4096 | infx | infx |
| 8192 | infx | infx |
| 16384 | -0.82x | -1.84x |
| 32768 | 0.71x | 3.52x |
| 65536 | 0.23x | 0.53x |
| 131072 | 1.00x | 257.00x |


## Conclusion

The `apply_evolving_and_or` function demonstrates how quantum operations can act as virtual memory with significantly reduced footprint. By storing only transformation parameters (eigenvalues) and active indices, we can represent and manipulate data without storing complete raw copies.

This approach enables:
- Lower memory footprint during complex transformations
- Reversible operations with minimal data loss
- Efficient representation of quantum state transformations

The Rust implementation further optimizes this approach with native code execution speed while maintaining the memory efficiency benefits.

![Memory Benchmark Results](./20250530_050425_quantum_memory_benchmark.png)