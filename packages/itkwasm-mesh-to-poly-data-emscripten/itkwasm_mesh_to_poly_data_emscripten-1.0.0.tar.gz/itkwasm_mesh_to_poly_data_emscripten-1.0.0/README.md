# itkwasm-mesh-to-poly-data-emscripten

[![PyPI version](https://badge.fury.io/py/itkwasm-mesh-to-poly-data-emscripten.svg)](https://badge.fury.io/py/itkwasm-mesh-to-poly-data-emscripten)

Convert an ITK Mesh to a simple data structure compatible with vtkPolyData. Emscripten implementation.

This package provides the Emscripten WebAssembly implementation. It is usually not called directly. Please use the [`itkwasm-mesh-to-poly-data`](https://pypi.org/project/itkwasm-mesh-to-poly-data/) instead.


## Installation

```sh
import micropip
await micropip.install('itkwasm-mesh-to-poly-data-emscripten')
```

## Development

```sh
pip install hatch
hatch run download-pyodide
hatch run test
```
