# Generated file. To retain edits, remove this comment.

from pathlib import Path, PurePosixPath
import os
from typing import Dict, Tuple, Optional, List, Any

from importlib_resources import files as file_resources

_pipeline = None

from itkwasm import (
    InterfaceTypes,
    PipelineOutput,
    PipelineInput,
    Pipeline,
    Mesh,
    PolyData,
)

def mesh_to_poly_data(
    mesh: Mesh,
) -> PolyData:
    """Convert an itk::Mesh to an itk::PolyData

    :param mesh: Input mesh
    :type  mesh: Mesh

    :return: Output polydata
    :rtype:  PolyData
    """
    global _pipeline
    if _pipeline is None:
        _pipeline = Pipeline(file_resources('itkwasm_mesh_to_poly_data_wasi').joinpath(Path('wasm_modules') / Path('mesh-to-poly-data.wasi.wasm')))

    pipeline_outputs: List[PipelineOutput] = [
        PipelineOutput(InterfaceTypes.PolyData),
    ]

    pipeline_inputs: List[PipelineInput] = [
        PipelineInput(InterfaceTypes.Mesh, mesh),
    ]

    args: List[str] = ['--memory-io',]
    # Inputs
    args.append('0')
    # Outputs
    poly_data_name = '0'
    args.append(poly_data_name)

    # Options
    input_count = len(pipeline_inputs)

    outputs = _pipeline.run(args, pipeline_outputs, pipeline_inputs)

    result = outputs[0].data
    return result

