# Generated file. To retain edits, remove this comment.

from pathlib import Path
import os
from typing import Dict, Tuple, Optional, List, Any

from .js_package import js_package

from itkwasm.pyodide import (
    to_js,
    to_py,
    js_resources
)
from itkwasm import (
    InterfaceTypes,
    PolyData,
    Mesh,
)

async def poly_data_to_mesh_async(
    poly_data: PolyData,
) -> Mesh:
    """Convert an itk::PolyData to an itk::Mesh

    :param poly_data: Input polydata
    :type  poly_data: PolyData

    :return: Output mesh
    :rtype:  Mesh
    """
    js_module = await js_package.js_module
    web_worker = js_resources.web_worker

    kwargs = {}

    outputs = await js_module.polyDataToMesh(to_js(poly_data), webWorker=web_worker, noCopy=True, **kwargs)

    output_web_worker = None
    output_list = []
    outputs_object_map = outputs.as_object_map()
    for output_name in outputs.object_keys():
        if output_name == 'webWorker':
            output_web_worker = outputs_object_map[output_name]
        else:
            output_list.append(to_py(outputs_object_map[output_name]))

    js_resources.web_worker = output_web_worker

    if len(output_list) == 1:
        return output_list[0]
    return tuple(output_list)
