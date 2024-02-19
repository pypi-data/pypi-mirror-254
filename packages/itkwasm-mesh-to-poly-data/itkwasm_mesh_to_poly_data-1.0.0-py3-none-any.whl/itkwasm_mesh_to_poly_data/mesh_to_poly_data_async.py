# Generated file. Do not edit.

import os
from typing import Dict, Tuple, Optional, List, Any

from itkwasm import (
    environment_dispatch,
    Mesh,
    PolyData,
)

async def mesh_to_poly_data_async(
    mesh: Mesh,
) -> PolyData:
    """Convert an itk::Mesh to an itk::PolyData

    :param mesh: Input mesh
    :type  mesh: Mesh

    :return: Output polydata
    :rtype:  PolyData
    """
    func = environment_dispatch("itkwasm_mesh_to_poly_data", "mesh_to_poly_data_async")
    output = await func(mesh)
    return output
