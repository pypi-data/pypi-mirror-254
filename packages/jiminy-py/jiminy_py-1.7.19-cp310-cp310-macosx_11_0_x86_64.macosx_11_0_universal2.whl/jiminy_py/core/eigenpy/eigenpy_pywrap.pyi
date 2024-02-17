import Boost.Python
from _typeshed import Incomplete
from typing import Any, ClassVar, overload

__eigen_version__: str
__raw_version__: str
__version__: str

class AngleAxis(Boost.Python.instance):
    angle: Incomplete
    axis: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def fromRotationMatrix(cls, *args, **kwargs): ...
    @classmethod
    def inverse(cls, Eigen) -> Any: ...
    @classmethod
    def isApprox(cls, *args, **kwargs): ...
    @classmethod
    def matrix(cls, Eigen) -> Any: ...
    @classmethod
    def toRotationMatrix(cls, Eigen) -> Any: ...
    @classmethod
    def __eq__(cls, other: object) -> bool: ...
    @classmethod
    def __mul__(cls, other): ...
    @classmethod
    def __ne__(cls, other: object) -> bool: ...
    @classmethod
    def __reduce__(cls): ...

class ComputationInfo(Boost.Python.enum):
    InvalidInput: ClassVar[ComputationInfo] = ...
    NoConvergence: ClassVar[ComputationInfo] = ...
    NumericalIssue: ClassVar[ComputationInfo] = ...
    Success: ClassVar[ComputationInfo] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class DecompositionOptions(Boost.Python.enum):
    ABx_lx: ClassVar[DecompositionOptions] = ...
    Ax_lBx: ClassVar[DecompositionOptions] = ...
    BAx_lx: ClassVar[DecompositionOptions] = ...
    ComputeEigenvectors: ClassVar[DecompositionOptions] = ...
    ComputeFullU: ClassVar[DecompositionOptions] = ...
    ComputeFullV: ClassVar[DecompositionOptions] = ...
    ComputeThinU: ClassVar[DecompositionOptions] = ...
    ComputeThinV: ClassVar[DecompositionOptions] = ...
    EigenvaluesOnly: ClassVar[DecompositionOptions] = ...
    names: ClassVar[dict] = ...
    values: ClassVar[dict] = ...

class EigenSolver(Boost.Python.instance):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def compute(cls, *args, **kwargs): ...
    @classmethod
    def eigenvalues(cls, *args, **kwargs): ...
    @classmethod
    def eigenvectors(cls, *args, **kwargs): ...
    @classmethod
    def getMaxIterations(cls, *args, **kwargs): ...
    @classmethod
    def info(cls, *args, **kwargs): ...
    @classmethod
    def pseudoEigenvalueMatrix(cls, *args, **kwargs): ...
    @classmethod
    def pseudoEigenvectors(cls, *args, **kwargs): ...
    @classmethod
    def setMaxIterations(cls, *args, **kwargs): ...
    @classmethod
    def __reduce__(cls): ...

class Exception(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(cls): ...
    @property
    def message(self): ...

class LDLT(Boost.Python.instance):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def adjoint(cls, *args, **kwargs): ...
    @classmethod
    def compute(cls, *args, **kwargs): ...
    @classmethod
    def info(cls, *args, **kwargs): ...
    @classmethod
    def isNegative(cls, *args, **kwargs): ...
    @classmethod
    def isPositive(cls, *args, **kwargs): ...
    @classmethod
    def matrixL(cls, *args, **kwargs): ...
    @classmethod
    def matrixLDLT(cls, *args, **kwargs): ...
    @classmethod
    def matrixU(cls, *args, **kwargs): ...
    @classmethod
    def rankUpdate(cls, *args, **kwargs): ...
    @classmethod
    def rcond(cls, *args, **kwargs): ...
    @classmethod
    def reconstructedMatrix(cls, *args, **kwargs): ...
    @classmethod
    def setZero(cls, *args, **kwargs): ...
    @classmethod
    def solve(cls, *args, **kwargs): ...
    @classmethod
    def transpositionsP(cls, *args, **kwargs): ...
    @classmethod
    def vectorD(cls, *args, **kwargs): ...
    @classmethod
    def __reduce__(cls): ...

class LLT(Boost.Python.instance):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def adjoint(cls, *args, **kwargs): ...
    @classmethod
    def compute(cls, *args, **kwargs): ...
    @classmethod
    def info(cls, *args, **kwargs): ...
    @classmethod
    def matrixL(cls, *args, **kwargs): ...
    @classmethod
    def matrixLLT(cls, *args, **kwargs): ...
    @classmethod
    def matrixU(cls, *args, **kwargs): ...
    @classmethod
    def rankUpdate(cls, *args, **kwargs): ...
    @classmethod
    def rcond(cls, *args, **kwargs): ...
    @classmethod
    def reconstructedMatrix(cls, *args, **kwargs): ...
    @classmethod
    def solve(cls, *args, **kwargs): ...
    @classmethod
    def __reduce__(cls): ...

class MINRES(Boost.Python.instance):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def analyzePattern(cls, *args, **kwargs): ...
    @classmethod
    def cols(cls, *args, **kwargs): ...
    @classmethod
    def compute(cls, *args, **kwargs): ...
    @classmethod
    def error(cls, *args, **kwargs): ...
    @classmethod
    def factorize(cls, *args, **kwargs): ...
    @classmethod
    def info(cls, *args, **kwargs): ...
    @classmethod
    def iterations(cls, *args, **kwargs): ...
    @classmethod
    def maxIterations(cls, *args, **kwargs): ...
    @classmethod
    def preconditioner(cls, *args, **kwargs): ...
    @classmethod
    def rows(cls, *args, **kwargs): ...
    @classmethod
    def setMaxIterations(cls, *args, **kwargs): ...
    @classmethod
    def setTolerance(cls, *args, **kwargs): ...
    @classmethod
    def solve(cls, *args, **kwargs): ...
    @classmethod
    def solveWithGuess(cls, *args, **kwargs): ...
    @classmethod
    def tolerance(cls, *args, **kwargs): ...
    @classmethod
    def __reduce__(cls): ...

class Quaternion(Boost.Python.instance):
    w: Incomplete
    x: Incomplete
    y: Incomplete
    z: Incomplete
    @overload
    @classmethod
    def __init__(cls, boost, Eigen) -> Any: ...
    @overload
    @classmethod
    def __init__(cls, boost) -> Any: ...
    @classmethod
    def FromTwoVectors(cls, *args, **kwargs): ...
    @classmethod
    def Identity(cls) -> Any: ...
    @classmethod
    def angularDistance(cls, *args, **kwargs): ...
    @classmethod
    def assign(cls, *args, **kwargs): ...
    @classmethod
    def coeffs(cls, *args, **kwargs): ...
    @classmethod
    def conjugate(cls, *args, **kwargs): ...
    @classmethod
    def dot(cls, *args, **kwargs): ...
    @classmethod
    def inverse(cls, *args, **kwargs): ...
    @classmethod
    def isApprox(cls, *args, **kwargs): ...
    @classmethod
    def matrix(cls, *args, **kwargs): ...
    @classmethod
    def norm(cls, *args, **kwargs): ...
    @classmethod
    def normalize(cls, *args, **kwargs): ...
    @classmethod
    def normalized(cls, *args, **kwargs): ...
    @classmethod
    def setFromTwoVectors(cls, *args, **kwargs): ...
    @classmethod
    def setIdentity(cls, *args, **kwargs): ...
    @classmethod
    def slerp(cls, *args, **kwargs): ...
    @classmethod
    def squaredNorm(cls, *args, **kwargs): ...
    @classmethod
    def toRotationMatrix(cls, *args, **kwargs): ...
    @classmethod
    def vec(cls, *args, **kwargs): ...
    @classmethod
    def __abs__(cls): ...
    @classmethod
    def __eq__(cls, other: object) -> bool: ...
    @classmethod
    def __getitem__(cls, index): ...
    @classmethod
    def __imul__(cls, other): ...
    @classmethod
    def __len__(cls) -> Any: ...
    @classmethod
    def __mul__(cls, other): ...
    @classmethod
    def __ne__(cls, other: object) -> bool: ...
    @classmethod
    def __reduce__(cls): ...
    @classmethod
    def __setitem__(cls, index, object) -> None: ...

class SelfAdjointEigenSolver(Boost.Python.instance):
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def compute(cls, *args, **kwargs): ...
    @classmethod
    def computeDirect(cls, *args, **kwargs): ...
    @classmethod
    def eigenvalues(cls, *args, **kwargs): ...
    @classmethod
    def eigenvectors(cls, *args, **kwargs): ...
    @classmethod
    def info(cls, *args, **kwargs): ...
    @classmethod
    def operatorInverseSqrt(cls, *args, **kwargs): ...
    @classmethod
    def operatorSqrt(cls, *args, **kwargs): ...
    @classmethod
    def __reduce__(cls): ...

class StdVec_MatrixXd(Boost.Python.instance):
    __getstate_manages_dict__: ClassVar[bool] = ...
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def append(cls, *args, **kwargs): ...
    @classmethod
    def copy(cls, *args, **kwargs): ...
    @classmethod
    def extend(cls, *args, **kwargs): ...
    @classmethod
    def reserve(cls, *args, **kwargs): ...
    @classmethod
    def tolist(cls, *args, **kwargs): ...
    @classmethod
    def __contains__(cls, other) -> bool: ...
    @classmethod
    def __copy__(cls): ...
    @classmethod
    def __deepcopy__(cls): ...
    @classmethod
    def __delitem__(cls, other) -> None: ...
    @classmethod
    def __getinitargs__(cls): ...
    @classmethod
    def __getitem__(cls, index): ...
    @classmethod
    def __iter__(cls): ...
    @classmethod
    def __len__(cls) -> int: ...
    @classmethod
    def __reduce__(cls): ...
    @classmethod
    def __setitem__(cls, index, object) -> None: ...

class StdVec_MatrixXi(Boost.Python.instance):
    __getstate_manages_dict__: ClassVar[bool] = ...
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def append(cls, *args, **kwargs): ...
    @classmethod
    def copy(cls, *args, **kwargs): ...
    @classmethod
    def extend(cls, *args, **kwargs): ...
    @classmethod
    def reserve(cls, *args, **kwargs): ...
    @classmethod
    def tolist(cls, *args, **kwargs): ...
    @classmethod
    def __contains__(cls, other) -> bool: ...
    @classmethod
    def __copy__(cls): ...
    @classmethod
    def __deepcopy__(cls): ...
    @classmethod
    def __delitem__(cls, other) -> None: ...
    @classmethod
    def __getinitargs__(cls): ...
    @classmethod
    def __getitem__(cls, index): ...
    @classmethod
    def __iter__(cls): ...
    @classmethod
    def __len__(cls) -> int: ...
    @classmethod
    def __reduce__(cls): ...
    @classmethod
    def __setitem__(cls, index, object) -> None: ...

class StdVec_VectorXd(Boost.Python.instance):
    __getstate_manages_dict__: ClassVar[bool] = ...
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def append(cls, *args, **kwargs): ...
    @classmethod
    def copy(cls, *args, **kwargs): ...
    @classmethod
    def extend(cls, *args, **kwargs): ...
    @classmethod
    def reserve(cls, *args, **kwargs): ...
    @classmethod
    def tolist(cls, *args, **kwargs): ...
    @classmethod
    def __contains__(cls, other) -> bool: ...
    @classmethod
    def __copy__(cls): ...
    @classmethod
    def __deepcopy__(cls): ...
    @classmethod
    def __delitem__(cls, other) -> None: ...
    @classmethod
    def __getinitargs__(cls): ...
    @classmethod
    def __getitem__(cls, index): ...
    @classmethod
    def __iter__(cls): ...
    @classmethod
    def __len__(cls) -> int: ...
    @classmethod
    def __reduce__(cls): ...
    @classmethod
    def __setitem__(cls, index, object) -> None: ...

class StdVec_VectorXi(Boost.Python.instance):
    __getstate_manages_dict__: ClassVar[bool] = ...
    __instance_size__: ClassVar[int] = ...
    __safe_for_unpickling__: ClassVar[bool] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def append(cls, *args, **kwargs): ...
    @classmethod
    def copy(cls, *args, **kwargs): ...
    @classmethod
    def extend(cls, *args, **kwargs): ...
    @classmethod
    def reserve(cls, *args, **kwargs): ...
    @classmethod
    def tolist(cls, *args, **kwargs): ...
    @classmethod
    def __contains__(cls, other) -> bool: ...
    @classmethod
    def __copy__(cls): ...
    @classmethod
    def __deepcopy__(cls): ...
    @classmethod
    def __delitem__(cls, other) -> None: ...
    @classmethod
    def __getinitargs__(cls): ...
    @classmethod
    def __getitem__(cls, index): ...
    @classmethod
    def __iter__(cls): ...
    @classmethod
    def __len__(cls) -> int: ...
    @classmethod
    def __reduce__(cls): ...
    @classmethod
    def __setitem__(cls, index, object) -> None: ...

class solvers(Boost.Python.instance):
    class ComputationInfo(Boost.Python.enum):
        InvalidInput: ClassVar[ComputationInfo] = ...
        NoConvergence: ClassVar[ComputationInfo] = ...
        NumericalIssue: ClassVar[ComputationInfo] = ...
        Success: ClassVar[ComputationInfo] = ...
        names: ClassVar[dict] = ...
        values: ClassVar[dict] = ...

    class ConjugateGradient(Boost.Python.instance):
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        @classmethod
        def analyzePattern(cls, *args, **kwargs): ...
        @classmethod
        def compute(cls, *args, **kwargs): ...
        @classmethod
        def error(cls, *args, **kwargs): ...
        @classmethod
        def factorize(cls, *args, **kwargs): ...
        @classmethod
        def info(cls, *args, **kwargs): ...
        @classmethod
        def iterations(cls, *args, **kwargs): ...
        @classmethod
        def maxIterations(cls, *args, **kwargs): ...
        @classmethod
        def preconditioner(cls, *args, **kwargs): ...
        @classmethod
        def setMaxIterations(cls, *args, **kwargs): ...
        @classmethod
        def setTolerance(cls, *args, **kwargs): ...
        @classmethod
        def solve(cls, *args, **kwargs): ...
        @classmethod
        def solveWithGuess(cls, *args, **kwargs): ...
        @classmethod
        def tolerance(cls, *args, **kwargs): ...
        @classmethod
        def __reduce__(cls): ...

    class DiagonalPreconditioner(Boost.Python.instance):
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        @classmethod
        def __reduce__(cls): ...

    class IdentityConjugateGradient(Boost.Python.instance):
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        @classmethod
        def analyzePattern(cls, *args, **kwargs): ...
        @classmethod
        def compute(cls, *args, **kwargs): ...
        @classmethod
        def error(cls, *args, **kwargs): ...
        @classmethod
        def factorize(cls, *args, **kwargs): ...
        @classmethod
        def info(cls, *args, **kwargs): ...
        @classmethod
        def iterations(cls, *args, **kwargs): ...
        @classmethod
        def maxIterations(cls, *args, **kwargs): ...
        @classmethod
        def preconditioner(cls, *args, **kwargs): ...
        @classmethod
        def setMaxIterations(cls, *args, **kwargs): ...
        @classmethod
        def setTolerance(cls, *args, **kwargs): ...
        @classmethod
        def solve(cls, *args, **kwargs): ...
        @classmethod
        def solveWithGuess(cls, *args, **kwargs): ...
        @classmethod
        def tolerance(cls, *args, **kwargs): ...
        @classmethod
        def __reduce__(cls): ...

    class IdentityPreconditioner(Boost.Python.instance):
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        @classmethod
        def compute(cls, *args, **kwargs): ...
        @classmethod
        def factorize(cls, *args, **kwargs): ...
        @classmethod
        def info(cls, Eigen) -> Any: ...
        @classmethod
        def solve(cls, *args, **kwargs): ...
        @classmethod
        def __reduce__(cls): ...

    class LeastSquareDiagonalPreconditioner(Boost.Python.instance):
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        @classmethod
        def compute(cls, *args, **kwargs): ...
        @classmethod
        def factorize(cls, *args, **kwargs): ...
        @classmethod
        def info(cls, Eigen) -> Any: ...
        @classmethod
        def solve(cls, *args, **kwargs): ...
        @classmethod
        def __reduce__(cls): ...

    class LeastSquaresConjugateGradient(Boost.Python.instance):
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        @classmethod
        def analyzePattern(cls, *args, **kwargs): ...
        @classmethod
        def compute(cls, *args, **kwargs): ...
        @classmethod
        def error(cls, *args, **kwargs): ...
        @classmethod
        def factorize(cls, *args, **kwargs): ...
        @classmethod
        def info(cls, *args, **kwargs): ...
        @classmethod
        def iterations(cls, *args, **kwargs): ...
        @classmethod
        def maxIterations(cls, *args, **kwargs): ...
        @classmethod
        def preconditioner(cls, *args, **kwargs): ...
        @classmethod
        def setMaxIterations(cls, *args, **kwargs): ...
        @classmethod
        def setTolerance(cls, *args, **kwargs): ...
        @classmethod
        def solve(cls, *args, **kwargs): ...
        @classmethod
        def solveWithGuess(cls, *args, **kwargs): ...
        @classmethod
        def tolerance(cls, *args, **kwargs): ...
        @classmethod
        def __reduce__(cls): ...
    __instance_size__: ClassVar[int] = ...
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    @classmethod
    def __reduce__(cls): ...

def SimdInstructionSetsInUse() -> Any: ...
def checkVersionAtLeast(*args, **kwargs): ...
def fromEulerAngles(*args, **kwargs): ...
def is_approx(*args, **kwargs): ...
def seed(unsignedint) -> Any: ...
@overload
def sharedMemory(bool) -> Any: ...
@overload
def sharedMemory() -> Any: ...
def toEulerAngles(*args, **kwargs): ...
