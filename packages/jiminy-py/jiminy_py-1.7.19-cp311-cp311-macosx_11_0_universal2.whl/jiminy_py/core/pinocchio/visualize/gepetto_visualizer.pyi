from . import BaseVisualizer
from _typeshed import Incomplete

__all__ = ['GepettoVisualizer']

class GepettoVisualizer(BaseVisualizer):
    def getViewerNodeName(self, geometry_object, geometry_type): ...
    viewer: Incomplete
    windowID: Incomplete
    sceneName: Incomplete
    def initViewer(self, viewer: Incomplete | None = None, windowName: str = 'python-pinocchio', sceneName: str = 'world', loadModel: bool = False) -> None: ...
    def loadPrimitive(self, meshName, geometry_object): ...
    def loadViewerGeometryObject(self, geometry_object, geometry_type) -> None: ...
    viewerRootNodeName: Incomplete
    viewerCollisionGroupName: Incomplete
    viewerVisualGroupName: Incomplete
    def loadViewerModel(self, rootNodeName: str = 'pinocchio') -> None: ...
    def display(self, q: Incomplete | None = None) -> None: ...
    display_collisions: Incomplete
    def displayCollisions(self, visibility) -> None: ...
    display_visuals: Incomplete
    def displayVisuals(self, visibility) -> None: ...
