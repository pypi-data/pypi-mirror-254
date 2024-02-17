import numpy as np
from . import core as jiminy
from .dynamics import State as State, TrajectoryDataType as TrajectoryDataType
from _typeshed import Incomplete
from typing import Any, Callable, Dict, List, Literal, Optional, Sequence, Type, Union, overload

ENGINE_NAMESPACE: str
SENSORS_FIELDS: Dict[Type[jiminy.AbstractSensor], Union[List[str], Dict[str, List[str]]]]
FieldNested: Incomplete
read_log: Incomplete

@overload
def extract_variables_from_log(log_vars: Dict[str, np.ndarray], fieldnames: FieldNested, namespace: Optional[str] = ..., *, as_dict: Literal[False] = False) -> List[np.ndarray]: ...
@overload
def extract_variables_from_log(log_vars: Dict[str, np.ndarray], fieldnames: FieldNested, namespace: Optional[str] = ..., *, as_dict: Literal[True]) -> Dict[str, np.ndarray]: ...
def build_robot_from_log(log_data: Dict[str, Any], mesh_path_dir: Optional[str] = None, mesh_package_dirs: Sequence[str] = ()) -> jiminy.Robot: ...
def extract_trajectory_from_log(log_data: Dict[str, Any], robot: Optional[jiminy.Model] = None) -> TrajectoryDataType: ...
def update_sensors_data_from_log(log_data: Dict[str, Any], robot: jiminy.Model) -> Callable[[float, np.ndarray, np.ndarray], None]: ...
