# itkwasm-mesh-to-poly-data-wasi

[![PyPI version](https://badge.fury.io/py/itkwasm-mesh-to-poly-data-wasi.svg)](https://badge.fury.io/py/itkwasm-mesh-to-poly-data-wasi)

Convert an ITK Mesh to a simple data structure compatible with vtkPolyData. WASI implementation.

This package provides the WASI WebAssembly implementation. It is usually not called directly. Please use [`itkwasm-mesh-to-poly-data`](https://pypi.org/project/itkwasm-mesh-to-poly-data/) instead.


## Installation

```sh
pip install itkwasm-mesh-to-poly-data-wasi
```

## Development

```sh
pip install pytest
pip install -e .
pytest

# or
pip install hatch
hatch run test
```
