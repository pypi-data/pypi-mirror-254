# Generated file. Do not edit.

import os
from typing import Dict, Tuple, Optional, List, Any

from itkwasm import (
    environment_dispatch,
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
    func = environment_dispatch("itkwasm_mesh_to_poly_data", "poly_data_to_mesh_async")
    output = await func(poly_data)
    return output
