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
    PolyData,
    Mesh,
)

def poly_data_to_mesh(
    poly_data: PolyData,
) -> Mesh:
    """Convert an itk::PolyData to an itk::Mesh

    :param poly_data: Input polydata
    :type  poly_data: PolyData

    :return: Output mesh
    :rtype:  Mesh
    """
    global _pipeline
    if _pipeline is None:
        _pipeline = Pipeline(file_resources('itkwasm_mesh_to_poly_data_wasi').joinpath(Path('wasm_modules') / Path('poly-data-to-mesh.wasi.wasm')))

    pipeline_outputs: List[PipelineOutput] = [
        PipelineOutput(InterfaceTypes.Mesh),
    ]

    pipeline_inputs: List[PipelineInput] = [
        PipelineInput(InterfaceTypes.PolyData, poly_data),
    ]

    args: List[str] = ['--memory-io',]
    # Inputs
    args.append('0')
    # Outputs
    mesh_name = '0'
    args.append(mesh_name)

    # Options
    input_count = len(pipeline_inputs)

    outputs = _pipeline.run(args, pipeline_outputs, pipeline_inputs)

    result = outputs[0].data
    return result

