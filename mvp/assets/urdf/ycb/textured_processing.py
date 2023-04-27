import pymeshlab
import os
from pathlib import Path
path = Path.cwd()
print(f"path is {path}")
ms = pymeshlab.MeshSet()

object_name = "003_cracker_box"
unfiltered_mesh = f"{path}/{object_name}/poisson/textured.obj"

ms.load_new_mesh(unfiltered_mesh)
ms.load_filter_script(f'{path}/nayesha_filtering.mlx')
ms.apply_filter_script()
ms.save_current_mesh('filtered_textured.obj')

#for generating collision mesh
filtered_mesh = f"{path}/{object_name}/filtered_textured.obj"
ms.load_new_mesh(filtered_mesh)
ms.load_filter_script(f'{path}/nayesha_collision_filtering.mlx')
ms.apply_filter_script()
ms.save_current_mesh('filtered_collision.obj')