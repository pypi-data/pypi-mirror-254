import hppfcl
import numpy as np
from typing import Tuple

def extract_vertices_and_faces_from_geometry(geom: hppfcl.CollisionGeometry) -> Tuple[np.ndarray, np.ndarray]: ...
