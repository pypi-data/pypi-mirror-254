"""Test sprauta."""

import random

import pytest
from typing_extensions import Annotated


def test_call_no_dependencies():
    """Test calling a function with no dependencies."""

    from sprauta import call

    def f():
        return 42

    assert call(f) == 42


def test_call_with_dependencies():
    """Test calling a function with dependencies"""

    from sprauta import Depends, call

    def get_a() -> int:
        return 42

    def get_b(a: Annotated[int, Depends(get_a)]) -> int:
        return a**2

    def f(b: Annotated[int, Depends(get_b)]) -> str:
        return str(b)

    assert call(f) == str(42**2)


def test_unresolved_dependency():
    """Test calling a function with an unresolved dependency."""

    from sprauta import call

    def f(x):
        return x  # pragma: no cover

    def g(x: Annotated[int, float, str]):
        return x  # pragma: no cover

    with pytest.raises(RuntimeError):
        call(f)

    with pytest.raises(RuntimeError):
        call(g)


def test_dependency_caching():
    """Test caching of dependencies."""

    from sprauta import Depends, call

    def f(
        r1: Annotated[float, Depends(random.random)],
        r2: Annotated[float, Depends(random.random)],
        r3: Annotated[float, Depends(random.random, use_cache=False)],
    ):
        assert r1 == r2
        assert r1 != r3

    call(f)


def test_cache_cleared_between_calls():
    """Test that the cache is cleared between function calls."""

    from sprauta import Depends, call

    def f(r: Annotated[float, Depends(random.random)]):
        return r

    assert call(f) != call(f)


def test_dependency_overwrites():
    """Test dependency overwrites."""

    from sprauta import Depends, call

    def get_a() -> int:
        return 42

    def f(a: Annotated[int, Depends(get_a)]):
        return a

    assert call(f) == 42
    assert call(f, overwrites={get_a: lambda: 1337}) == 1337


def test_caching_overwrites():
    """Test caching of overwritten dependencies."""

    from sprauta import Depends, call

    def get_r() -> float:
        return 4.2  # pragma: no cover

    def f(
        r1: Annotated[float, Depends(get_r)],
        r2: Annotated[float, Depends(get_r)],
        r3: Annotated[float, Depends(get_r, use_cache=False)],
    ):
        assert r1 == r2
        assert r1 != r3

    call(f, overwrites={get_r: random.random})


def test_parameter_types():
    """Test different types of parameters."""

    from sprauta import Depends, call

    def f(
        pos_only: Annotated[int, Depends(lambda: 1)],
        /,
        pos_or_kw: Annotated[int, Depends(lambda: 2)],
        *,
        kw_only: Annotated[int, Depends(lambda: 3)],
    ):
        return (pos_only, pos_or_kw, kw_only)

    assert call(f) == (1, 2, 3)


def test_resource_dependencies():
    """Test resource dependencies."""

    from sprauta import Depends, call

    events = []

    def get_resource_1():
        events.append("init 1")
        yield 1
        events.append("cleanup 1")

    def get_resource_2():
        events.append("init 2")
        yield 2
        events.append("cleanup 2")

    def f(
        r1: Annotated[int, Depends(get_resource_1)],
        r2: Annotated[int, Depends(get_resource_2)],
    ):
        events.append(f"result: {r1 + r2}")

    call(f)

    assert events == [
        "init 1",
        "init 2",
        "result: 3",
        "cleanup 2",
        "cleanup 1",
    ]


def test_exception_with_resources():
    """Test resource management with exceptions."""

    from sprauta import Depends, call

    events = []

    def get_resource_1():
        events.append("init 1")
        try:
            yield 1
        finally:
            events.append("cleanup 1")

    def get_resource_2():
        events.append("init 2")
        try:
            yield 2
        finally:
            events.append("cleanup 2")

    def f(
        r1: Annotated[int, Depends(get_resource_1)],
        r2: Annotated[int, Depends(get_resource_2)],
    ):
        raise Exception(r1 + r2)

    with pytest.raises(Exception, match="3"):
        call(f)

    assert events == [
        "init 1",
        "init 2",
        "cleanup 2",
        "cleanup 1",
    ]


def test_exception_in_resource_dependencies():
    """Test handling of exceptions in resource dependencies."""

    from sprauta import Depends, call

    events = []

    def get_resource_1():
        events.append("init 1")
        try:
            yield 1
        except KeyError:
            events.append("error handler 1")

    def get_resource_2():
        events.append("init 2")
        try:
            yield 2
        except KeyError:
            events.append("error handler 2")
            msg = "will not overwrite KeyError in resource 1"
            raise IndexError(msg) from None

    def get_resource_3():
        events.append("error 3")
        msg = "foobar"
        raise KeyError(msg)

    def f(
        _r1: Annotated[int, Depends(get_resource_1)],
        _r2: Annotated[int, Depends(get_resource_2)],
        _r3: Annotated[int, Depends(get_resource_3)],
    ):
        events.append("f called")  # pragma: no cover

    with pytest.raises(KeyError, match="foobar"):
        call(f)

    assert events == [
        "init 1",
        "init 2",
        "error 3",
        "error handler 2",
        "error handler 1",
    ]


def test_caching_resource_dependencies():
    """Test resource dependency caching and re-use."""

    from sprauta import Depends, call

    events = []

    def get_random_resource():
        """Resource returning random number."""

        events.append("init")
        yield random.random()
        events.append("cleanup")

    def f(
        r1: Annotated[float, Depends(get_random_resource)],
        r2: Annotated[float, Depends(get_random_resource)],
        r3: Annotated[float, Depends(get_random_resource, use_cache=False)],
    ):
        assert r1 == r2
        assert r1 != r3

    call(f)

    assert events == ["init", "init", "cleanup", "cleanup"]


def test_invalid_resources():
    """Test invalid resoruces."""

    from sprauta import Depends, call

    def get_resource_1():
        if False:
            yield 1

    def f1(_r: Annotated[int, Depends(get_resource_1)]):
        pass  # pragma: no cover

    def get_resource_2():
        yield 2
        yield 2

    def f2(_r: Annotated[int, Depends(get_resource_2)]):
        pass

    with pytest.raises(RuntimeError):
        call(f1)

    with pytest.raises(RuntimeError):
        call(f2)


def test_type_dependency_callback():
    """Test type dependencies."""

    from sprauta import Depends, call, type_dependency_callback

    def get_a():
        return 1

    def get_b():
        return 2

    def f1(
        a: int,
        b: Annotated[int, Depends(get_b)],
    ):
        return a + b

    def f2(
        x: Annotated[int, "some", "unrelated", "metadata"],
    ):
        return x

    with pytest.raises(RuntimeError):
        call(f1)

    callback = type_dependency_callback({int: Depends(get_a)})

    assert call(f1, callback=callback) == 3

    with pytest.raises(RuntimeError):
        call(f2)

    assert call(f2, callback=callback) == 1


def test_visit():
    """Test sprauta.visit."""

    from sprauta import visit, Depends

    def get_b(c: float):
        assert False  # should not be called, pragma: no cover

    def f(a: int, b: Annotated[int, Depends(get_b)]):
        assert False  # should not be called, pragma: no cover

    calls = []

    def callback(func, param):
        calls.append((func, param.name))

    visit(f, callback=callback)

    assert calls == [
        (f, "a"),
        (get_b, "c"),
    ]
