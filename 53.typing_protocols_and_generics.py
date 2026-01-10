"""Small, commented examples: Protocols, Generics and ParamSpec.

Keep this file short and runnable. Intended as a quick demo for contributors.
"""

from typing import Protocol, runtime_checkable, TypeVar, Generic, Callable, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")


@runtime_checkable
class SupportsClose(Protocol):
    """Structural type: any object with a close() method fits."""
    def close(self) -> None: ...


class Socket:
    """Simple object that implements close()."""
    def __init__(self, name: str) -> None:
        self.name = name

    def close(self) -> None:
        print(f"Socket {self.name} closed")


def close_if_supported(obj: SupportsClose) -> None:
    """Call .close() on anything that matches the Protocol.

    This shows structural typing: no inheritance required.
    """
    obj.close()


class Box(Generic[T]):
    """Tiny generic container.

    Static type checkers will remember the element type.
    """
    def __init__(self, value: T) -> None:
        self._v = value

    def get(self) -> T:
        return self._v


# ParamSpec decorator: preserves caller signature for typing tools.
def make_logged(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:  # type: ignore[misc]
        print(f"[log] {func.__name__} args={args} kwargs={kwargs}")
        res = func(*args, **kwargs)
        print(f"[log] {func.__name__} -> {res}")
        return res

    return wrapper


@make_logged
def greet(name: str, excited: bool = False) -> str:
    return "Hello, " + name + ("!!!" if excited else ".")


if __name__ == "__main__":
    # Protocol demo
    s = Socket("A")
    close_if_supported(s)

    # Generic demo
    bi = Box[int](10)
    bs = Box[str]("ok")
    print(type(bi.get()), bi.get())
    print(type(bs.get()), bs.get())

    # ParamSpec demo (runtime logs and preserved signature for mypy)
    print(greet("World"))
    print(greet("Lin", excited=True))
