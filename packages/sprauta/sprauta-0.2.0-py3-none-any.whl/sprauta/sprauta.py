"""Sprauta."""

import contextlib
import functools
import inspect
import sys
from typing import (
    Callable,
    ContextManager,
    Dict,
    List,
    Optional,
    TypeVar,
    Protocol,
    Any,
)

from typing_extensions import Annotated, TypeAlias, get_args, get_origin

if sys.version_info < (3, 10):
    get_signature = inspect.signature
else:
    get_signature = functools.partial(inspect.signature, eval_str=True)

T = TypeVar("T")

DependencyOverwritesT: TypeAlias = Dict[Callable[..., T], Callable[..., T]]


class Depends:
    def __init__(self, dependency: Callable[..., T], *, use_cache: bool = True):
        self.dependency = dependency
        self.use_cache = use_cache


class DependencyCallbackT(Protocol):
    """Dependency callback type."""

    def __call__(
        self,
        func: Callable[..., Any],
        param: inspect.Parameter,
    ) -> Optional[Depends]:
        """Optionally creates a dependency from the given parameter.

        Args:
            func: The function the parameter belongs to
            param: The parameter as returned by inspect.signature(func)
        """


def type_dependency_callback(
    type_dependencies: Dict[type, Depends],
) -> DependencyCallbackT:
    """Create callback that chooses dependencies based on parameter types."""

    def callback(
        func: Callable[..., Any], param: inspect.Parameter
    ) -> Optional[Depends]:
        annotation = param.annotation
        if get_origin(annotation) is Annotated:
            annotation = get_args(annotation)[0]

        return type_dependencies.get(annotation)

    return callback


def get_parameter_annotation_dependency(param: inspect.Parameter) -> Optional[Depends]:
    for meta in get_args(param.annotation):
        if isinstance(meta, Depends):
            return meta
    return None


def _call(
    func: Callable[..., T],
    *,
    cache: Dict,
    overwrites: Dict,
    callback: Optional[DependencyCallbackT] = None,
    resources: list,
) -> T:
    """Call func with dependency injection."""

    args = []
    kwargs = {}

    for param in get_signature(func).parameters.values():
        dep = get_parameter_annotation_dependency(param)

        if dep is None and callback:
            dep = callback(func, param)

        if dep is None:
            msg = f"unresolved dependency: {func!r}:{param!r}"
            raise RuntimeError(msg)

        dep_func = overwrites.get(dep.dependency, dep.dependency)

        if dep.use_cache and dep_func in cache:
            value = cache[dep_func]
        else:
            if inspect.isgeneratorfunction(dep_func):
                resource = _call(
                    contextlib.contextmanager(dep_func),
                    cache=cache,
                    overwrites=overwrites,
                    callback=callback,
                    resources=resources,
                )
                value = resource.__enter__()
                resources.append(resource)
            else:
                value = _call(
                    dep_func,
                    cache=cache,
                    overwrites=overwrites,
                    callback=callback,
                    resources=resources,
                )

            if dep.use_cache:
                cache[dep_func] = value

        if param.kind == inspect.Parameter.POSITIONAL_ONLY:
            args.append(value)

        else:
            kwargs[param.name] = value

    return func(*args, **kwargs)


def _visit(
    func: Callable[..., T],
    *,
    overwrites: dict,
    callback: Optional[DependencyCallbackT],
) -> None:
    for param in get_signature(func).parameters.values():
        dep = get_parameter_annotation_dependency(param)

        if dep is None and callback:
            dep = callback(func, param)

        if dep is not None:
            dep_func = overwrites.get(dep.dependency, dep.dependency)

            _visit(
                dep_func,
                overwrites=overwrites,
                callback=callback,
            )


def visit(
    func: Callable[..., T],
    *,
    overwrites: Optional[Dict] = None,
    callback: DependencyCallbackT,
) -> None:
    _visit(func, overwrites=overwrites or {}, callback=callback)


def call(
    func: Callable[..., T],
    *,
    overwrites: Optional[Dict] = None,
    callback: Optional[DependencyCallbackT] = None,
) -> T:
    """Call func after resolving its dependencies."""

    resources: List[ContextManager] = []

    try:
        value = _call(
            func,
            cache={},
            overwrites=overwrites or {},
            callback=callback,
            resources=resources,
        )

        while resources:
            resources.pop().__exit__(None, None, None)

        return value

    except BaseException:
        exc_info = sys.exc_info()

        while resources:
            with contextlib.suppress(BaseException):
                resources.pop().__exit__(*exc_info)
        raise
