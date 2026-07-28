import ast as _ast
import builtins as _builtins
import os as _os
import sys
from collections.abc import Iterator as _Iterator
from typing import ClassVar as _ClassVar
from typing import Literal as _Literal
from typing import NoReturn as _Never
from typing import TypeVar as _TypeVar
from typing import overload as _overload

if sys.version_info >= (3, 10):
    from types import EllipsisType as _EllipsisType
else:
    from builtins import ellipsis as _EllipsisType

from ast import (
    AST as AST,
    boolop as boolop,
    cmpop as cmpop,
    excepthandler as excepthandler,
    expr as expr,
    expr_context as expr_context,
    mod as mod,
    operator as operator,
    slice as slice,
    stmt as stmt,
    unaryop as unaryop,
)

if sys.version_info >= (3, 8):
    from ast import TypeIgnore as TypeIgnore
else:
    class TypeIgnore(AST): ...

if sys.version_info >= (3, 10):
    from ast import pattern as pattern
else:
    class pattern(AST): ...

if sys.version_info >= (3, 12):
    from ast import type_param as type_param
else:
    class type_param(AST): ...

if sys.version_info >= (3, 14):
    from typing import Self as _Self
    from typing import TypedDict as _TypedDict
    from typing import Unpack as _Unpack

    class _LocationAttributes(_TypedDict, total=False):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None

    class _TypeIgnoreAttributes(_TypedDict, total=False):
        lineno: int | None
        tag: str

_T = _TypeVar("_T", bound=AST)
_Pattern = pattern

_Source = str | bytes | bytearray | memoryview
_Filename = str | bytes | _os.PathLike[str] | _os.PathLike[bytes]
_LiteralValue = (
    str
    | bytes
    | int
    | float
    | complex
    | bool
    | None
    | _EllipsisType
    | tuple["_LiteralValue", ...]
    | list["_LiteralValue"]
    | set["_LiteralValue"]
    | dict["_LiteralValue", "_LiteralValue"]
)

class Module(mod):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    body: list[stmt]
    type_ignores: list[TypeIgnore | type_ignore]
    @_overload
    def __init__(self, *, body: list[stmt] = ..., type_ignores: list[TypeIgnore | type_ignore] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], /, *, type_ignores: list[TypeIgnore | type_ignore] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], type_ignores: list[TypeIgnore | type_ignore], /, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, *, body: list[stmt] = ..., type_ignores: list[TypeIgnore | type_ignore] = ...) -> _Self: ...

class Interactive(mod):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    body: list[stmt]
    @_overload
    def __init__(self, *, body: list[stmt] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], /, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, *, body: list[stmt] = ...) -> _Self: ...

class Expression(mod):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    body: expr
    @_overload
    def __init__(self, *, body: expr = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: expr, /, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, *, body: expr = ...) -> _Self: ...

class FunctionType(mod):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    argtypes: list[expr]
    returns: expr
    @_overload
    def __init__(self, *, argtypes: list[expr] = ..., returns: expr = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, argtypes: list[expr], /, *, returns: expr = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, argtypes: list[expr], returns: expr, /, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, *, argtypes: list[expr] = ..., returns: expr = ...) -> _Self: ...

class Suite(mod):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    body: list[stmt]
    @_overload
    def __init__(self, *, body: list[stmt] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], /, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, *, body: list[stmt] = ...) -> _Self: ...

class FunctionDef(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    name: str
    args: arguments
    body: list[stmt]
    decorator_list: list[expr]
    returns: expr | None
    type_comment: str | None
    type_params: list[type_param]
    @_overload
    def __init__(self, *, name: str = ..., args: arguments = ..., body: list[stmt] = ..., decorator_list: list[expr] = ..., returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, /, *, args: arguments = ..., body: list[stmt] = ..., decorator_list: list[expr] = ..., returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, /, *, body: list[stmt] = ..., decorator_list: list[expr] = ..., returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, body: list[stmt], /, *, decorator_list: list[expr] = ..., returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, body: list[stmt], decorator_list: list[expr], /, *, returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, body: list[stmt], decorator_list: list[expr], returns: expr | None, /, *, type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, body: list[stmt], decorator_list: list[expr], returns: expr | None, type_comment: str | None, /, *, type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, body: list[stmt], decorator_list: list[expr], returns: expr | None, type_comment: str | None, type_params: list[type_param], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, name: str = ..., args: arguments = ..., body: list[stmt] = ..., decorator_list: list[expr] = ..., returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class AsyncFunctionDef(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    name: str
    args: arguments
    body: list[stmt]
    decorator_list: list[expr]
    returns: expr | None
    type_comment: str | None
    type_params: list[type_param]
    @_overload
    def __init__(self, *, name: str = ..., args: arguments = ..., body: list[stmt] = ..., decorator_list: list[expr] = ..., returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, /, *, args: arguments = ..., body: list[stmt] = ..., decorator_list: list[expr] = ..., returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, /, *, body: list[stmt] = ..., decorator_list: list[expr] = ..., returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, body: list[stmt], /, *, decorator_list: list[expr] = ..., returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, body: list[stmt], decorator_list: list[expr], /, *, returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, body: list[stmt], decorator_list: list[expr], returns: expr | None, /, *, type_comment: str | None = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, body: list[stmt], decorator_list: list[expr], returns: expr | None, type_comment: str | None, /, *, type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, args: arguments, body: list[stmt], decorator_list: list[expr], returns: expr | None, type_comment: str | None, type_params: list[type_param], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, name: str = ..., args: arguments = ..., body: list[stmt] = ..., decorator_list: list[expr] = ..., returns: expr | None = ..., type_comment: str | None = ..., type_params: list[type_param] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class ClassDef(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    name: str
    bases: list[expr]
    keywords: list[keyword]
    body: list[stmt]
    decorator_list: list[expr]
    type_params: list[type_param]
    @_overload
    def __init__(self, *, name: str = ..., bases: list[expr] = ..., keywords: list[keyword] = ..., body: list[stmt] = ..., decorator_list: list[expr] = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, /, *, bases: list[expr] = ..., keywords: list[keyword] = ..., body: list[stmt] = ..., decorator_list: list[expr] = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, bases: list[expr], /, *, keywords: list[keyword] = ..., body: list[stmt] = ..., decorator_list: list[expr] = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, bases: list[expr], keywords: list[keyword], /, *, body: list[stmt] = ..., decorator_list: list[expr] = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, bases: list[expr], keywords: list[keyword], body: list[stmt], /, *, decorator_list: list[expr] = ..., type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, bases: list[expr], keywords: list[keyword], body: list[stmt], decorator_list: list[expr], /, *, type_params: list[type_param] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, bases: list[expr], keywords: list[keyword], body: list[stmt], decorator_list: list[expr], type_params: list[type_param], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, name: str = ..., bases: list[expr] = ..., keywords: list[keyword] = ..., body: list[stmt] = ..., decorator_list: list[expr] = ..., type_params: list[type_param] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Return(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr | None
    @_overload
    def __init__(self, *, value: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Delete(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    targets: list[expr]
    @_overload
    def __init__(self, *, targets: list[expr] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, targets: list[expr], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, targets: list[expr] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Assign(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    targets: list[expr]
    value: expr
    type_comment: str | None
    @_overload
    def __init__(self, *, targets: list[expr] = ..., value: expr = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, targets: list[expr], /, *, value: expr = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, targets: list[expr], value: expr, /, *, type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, targets: list[expr], value: expr, type_comment: str | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, targets: list[expr] = ..., value: expr = ..., type_comment: str | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class TypeAlias(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    name: expr
    type_params: list[type_param]
    value: expr
    @_overload
    def __init__(self, *, name: expr = ..., type_params: list[type_param] = ..., value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: expr, /, *, type_params: list[type_param] = ..., value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: expr, type_params: list[type_param], /, *, value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: expr, type_params: list[type_param], value: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, name: expr = ..., type_params: list[type_param] = ..., value: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class AugAssign(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    target: expr
    op: operator
    value: expr
    @_overload
    def __init__(self, *, target: expr = ..., op: operator = ..., value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, /, *, op: operator = ..., value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, op: operator, /, *, value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, op: operator, value: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, target: expr = ..., op: operator = ..., value: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class AnnAssign(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    target: expr
    annotation: expr
    value: expr | None
    simple: int
    @_overload
    def __init__(self, *, target: expr = ..., annotation: expr = ..., value: expr | None = ..., simple: int = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, /, *, annotation: expr = ..., value: expr | None = ..., simple: int = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, annotation: expr, /, *, value: expr | None = ..., simple: int = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, annotation: expr, value: expr | None, /, *, simple: int = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, annotation: expr, value: expr | None, simple: int, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, target: expr = ..., annotation: expr = ..., value: expr | None = ..., simple: int = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Print(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    dest: expr | None
    values: list[expr]
    nl: bool
    @_overload
    def __init__(self, *, dest: expr | None = ..., values: list[expr] = ..., nl: bool = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, dest: expr | None, /, *, values: list[expr] = ..., nl: bool = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, dest: expr | None, values: list[expr], /, *, nl: bool = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, dest: expr | None, values: list[expr], nl: bool, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, dest: expr | None = ..., values: list[expr] = ..., nl: bool = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class For(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    target: expr
    iter: expr
    body: list[stmt]
    orelse: list[stmt]
    type_comment: str | None
    @_overload
    def __init__(self, *, target: expr = ..., iter: expr = ..., body: list[stmt] = ..., orelse: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, /, *, iter: expr = ..., body: list[stmt] = ..., orelse: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, iter: expr, /, *, body: list[stmt] = ..., orelse: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, iter: expr, body: list[stmt], /, *, orelse: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, iter: expr, body: list[stmt], orelse: list[stmt], /, *, type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, iter: expr, body: list[stmt], orelse: list[stmt], type_comment: str | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, target: expr = ..., iter: expr = ..., body: list[stmt] = ..., orelse: list[stmt] = ..., type_comment: str | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class AsyncFor(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    target: expr
    iter: expr
    body: list[stmt]
    orelse: list[stmt]
    type_comment: str | None
    @_overload
    def __init__(self, *, target: expr = ..., iter: expr = ..., body: list[stmt] = ..., orelse: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, /, *, iter: expr = ..., body: list[stmt] = ..., orelse: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, iter: expr, /, *, body: list[stmt] = ..., orelse: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, iter: expr, body: list[stmt], /, *, orelse: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, iter: expr, body: list[stmt], orelse: list[stmt], /, *, type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, iter: expr, body: list[stmt], orelse: list[stmt], type_comment: str | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, target: expr = ..., iter: expr = ..., body: list[stmt] = ..., orelse: list[stmt] = ..., type_comment: str | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class While(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    test: expr
    body: list[stmt]
    orelse: list[stmt]
    @_overload
    def __init__(self, *, test: expr = ..., body: list[stmt] = ..., orelse: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, test: expr, /, *, body: list[stmt] = ..., orelse: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, test: expr, body: list[stmt], /, *, orelse: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, test: expr, body: list[stmt], orelse: list[stmt], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, test: expr = ..., body: list[stmt] = ..., orelse: list[stmt] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class If(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    test: expr
    body: list[stmt]
    orelse: list[stmt]
    @_overload
    def __init__(self, *, test: expr = ..., body: list[stmt] = ..., orelse: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, test: expr, /, *, body: list[stmt] = ..., orelse: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, test: expr, body: list[stmt], /, *, orelse: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, test: expr, body: list[stmt], orelse: list[stmt], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, test: expr = ..., body: list[stmt] = ..., orelse: list[stmt] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class With(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    items: list[withitem]
    body: list[stmt]
    type_comment: str | None
    @_overload
    def __init__(self, *, items: list[withitem] = ..., body: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, items: list[withitem], /, *, body: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, items: list[withitem], body: list[stmt], /, *, type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, items: list[withitem], body: list[stmt], type_comment: str | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, items: list[withitem] = ..., body: list[stmt] = ..., type_comment: str | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class AsyncWith(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    items: list[withitem]
    body: list[stmt]
    type_comment: str | None
    @_overload
    def __init__(self, *, items: list[withitem] = ..., body: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, items: list[withitem], /, *, body: list[stmt] = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, items: list[withitem], body: list[stmt], /, *, type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, items: list[withitem], body: list[stmt], type_comment: str | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, items: list[withitem] = ..., body: list[stmt] = ..., type_comment: str | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Match(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    subject: expr
    cases: list[match_case]
    @_overload
    def __init__(self, *, subject: expr = ..., cases: list[match_case] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, subject: expr, /, *, cases: list[match_case] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, subject: expr, cases: list[match_case], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, subject: expr = ..., cases: list[match_case] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Raise(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    exc: expr | None
    cause: expr | None
    @_overload
    def __init__(self, *, exc: expr | None = ..., cause: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, exc: expr | None, /, *, cause: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, exc: expr | None, cause: expr | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, exc: expr | None = ..., cause: expr | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Try(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    body: list[stmt]
    handlers: list[ExceptHandler]
    orelse: list[stmt]
    finalbody: list[stmt]
    @_overload
    def __init__(self, *, body: list[stmt] = ..., handlers: list[ExceptHandler] = ..., orelse: list[stmt] = ..., finalbody: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], /, *, handlers: list[ExceptHandler] = ..., orelse: list[stmt] = ..., finalbody: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], handlers: list[ExceptHandler], /, *, orelse: list[stmt] = ..., finalbody: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], handlers: list[ExceptHandler], orelse: list[stmt], /, *, finalbody: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], handlers: list[ExceptHandler], orelse: list[stmt], finalbody: list[stmt], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, body: list[stmt] = ..., handlers: list[ExceptHandler] = ..., orelse: list[stmt] = ..., finalbody: list[stmt] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class TryStar(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    body: list[stmt]
    handlers: list[ExceptHandler]
    orelse: list[stmt]
    finalbody: list[stmt]
    @_overload
    def __init__(self, *, body: list[stmt] = ..., handlers: list[ExceptHandler] = ..., orelse: list[stmt] = ..., finalbody: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], /, *, handlers: list[ExceptHandler] = ..., orelse: list[stmt] = ..., finalbody: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], handlers: list[ExceptHandler], /, *, orelse: list[stmt] = ..., finalbody: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], handlers: list[ExceptHandler], orelse: list[stmt], /, *, finalbody: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: list[stmt], handlers: list[ExceptHandler], orelse: list[stmt], finalbody: list[stmt], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, body: list[stmt] = ..., handlers: list[ExceptHandler] = ..., orelse: list[stmt] = ..., finalbody: list[stmt] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Assert(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    test: expr
    msg: expr | None
    @_overload
    def __init__(self, *, test: expr = ..., msg: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, test: expr, /, *, msg: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, test: expr, msg: expr | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, test: expr = ..., msg: expr | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Import(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    names: list[alias]
    @_overload
    def __init__(self, *, names: list[alias] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, names: list[alias], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, names: list[alias] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class ImportFrom(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    module: str | None
    names: list[alias]
    level: int | None
    @_overload
    def __init__(self, *, module: str | None = ..., names: list[alias] = ..., level: int | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, module: str | None, /, *, names: list[alias] = ..., level: int | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, module: str | None, names: list[alias], /, *, level: int | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, module: str | None, names: list[alias], level: int | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, module: str | None = ..., names: list[alias] = ..., level: int | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Exec(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    body: expr
    globals: expr | None
    locals: expr | None
    @_overload
    def __init__(self, *, body: expr = ..., globals: expr | None = ..., locals: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: expr, /, *, globals: expr | None = ..., locals: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: expr, globals: expr | None, /, *, locals: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, body: expr, globals: expr | None, locals: expr | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, body: expr = ..., globals: expr | None = ..., locals: expr | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Global(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    names: list[str]
    @_overload
    def __init__(self, *, names: list[str] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, names: list[str], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, names: list[str] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Nonlocal(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    names: list[str]
    @_overload
    def __init__(self, *, names: list[str] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, names: list[str], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, names: list[str] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Expr(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr
    @_overload
    def __init__(self, *, value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Pass(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Break(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Continue(stmt):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class BoolOp(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    op: boolop
    values: list[expr]
    @_overload
    def __init__(self, *, op: boolop = ..., values: list[expr] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, op: boolop, /, *, values: list[expr] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, op: boolop, values: list[expr], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, op: boolop = ..., values: list[expr] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class NamedExpr(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    target: expr
    value: expr
    @_overload
    def __init__(self, *, target: expr = ..., value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, /, *, value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, value: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, target: expr = ..., value: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class BinOp(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    left: expr
    op: operator
    right: expr
    @_overload
    def __init__(self, *, left: expr = ..., op: operator = ..., right: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, left: expr, /, *, op: operator = ..., right: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, left: expr, op: operator, /, *, right: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, left: expr, op: operator, right: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, left: expr = ..., op: operator = ..., right: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class UnaryOp(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    op: unaryop
    operand: expr
    @_overload
    def __init__(self, *, op: unaryop = ..., operand: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, op: unaryop, /, *, operand: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, op: unaryop, operand: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, op: unaryop = ..., operand: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Lambda(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    args: arguments
    body: expr
    @_overload
    def __init__(self, *, args: arguments = ..., body: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, args: arguments, /, *, body: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, args: arguments, body: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, args: arguments = ..., body: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class IfExp(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    test: expr
    body: expr
    orelse: expr
    @_overload
    def __init__(self, *, test: expr = ..., body: expr = ..., orelse: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, test: expr, /, *, body: expr = ..., orelse: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, test: expr, body: expr, /, *, orelse: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, test: expr, body: expr, orelse: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, test: expr = ..., body: expr = ..., orelse: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Dict(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    keys: list[expr | None]
    values: list[expr]
    @_overload
    def __init__(self, *, keys: list[expr | None] = ..., values: list[expr] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, keys: list[expr | None], /, *, values: list[expr] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, keys: list[expr | None], values: list[expr], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, keys: list[expr | None] = ..., values: list[expr] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Set(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    elts: list[expr]
    @_overload
    def __init__(self, *, elts: list[expr] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, elts: list[expr], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, elts: list[expr] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class ListComp(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    elt: expr
    generators: list[comprehension]
    @_overload
    def __init__(self, *, elt: expr = ..., generators: list[comprehension] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, elt: expr, /, *, generators: list[comprehension] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, elt: expr, generators: list[comprehension], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, elt: expr = ..., generators: list[comprehension] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class SetComp(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    elt: expr
    generators: list[comprehension]
    @_overload
    def __init__(self, *, elt: expr = ..., generators: list[comprehension] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, elt: expr, /, *, generators: list[comprehension] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, elt: expr, generators: list[comprehension], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, elt: expr = ..., generators: list[comprehension] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class DictComp(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    key: expr
    value: expr
    generators: list[comprehension]
    @_overload
    def __init__(self, *, key: expr = ..., value: expr = ..., generators: list[comprehension] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, key: expr, /, *, value: expr = ..., generators: list[comprehension] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, key: expr, value: expr, /, *, generators: list[comprehension] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, key: expr, value: expr, generators: list[comprehension], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, key: expr = ..., value: expr = ..., generators: list[comprehension] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class GeneratorExp(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    elt: expr
    generators: list[comprehension]
    @_overload
    def __init__(self, *, elt: expr = ..., generators: list[comprehension] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, elt: expr, /, *, generators: list[comprehension] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, elt: expr, generators: list[comprehension], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, elt: expr = ..., generators: list[comprehension] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Await(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr
    @_overload
    def __init__(self, *, value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Yield(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr | None
    @_overload
    def __init__(self, *, value: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class YieldFrom(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr
    @_overload
    def __init__(self, *, value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Compare(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    left: expr
    ops: list[cmpop]
    comparators: list[expr]
    @_overload
    def __init__(self, *, left: expr = ..., ops: list[cmpop] = ..., comparators: list[expr] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, left: expr, /, *, ops: list[cmpop] = ..., comparators: list[expr] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, left: expr, ops: list[cmpop], /, *, comparators: list[expr] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, left: expr, ops: list[cmpop], comparators: list[expr], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, left: expr = ..., ops: list[cmpop] = ..., comparators: list[expr] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Call(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    func: expr
    args: list[expr]
    keywords: list[keyword]
    @_overload
    def __init__(self, *, func: expr = ..., args: list[expr] = ..., keywords: list[keyword] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, func: expr, /, *, args: list[expr] = ..., keywords: list[keyword] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, func: expr, args: list[expr], /, *, keywords: list[keyword] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, func: expr, args: list[expr], keywords: list[keyword], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, func: expr = ..., args: list[expr] = ..., keywords: list[keyword] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Repr(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr
    @_overload
    def __init__(self, *, value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class FormattedValue(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr
    conversion: int
    format_spec: expr | None
    @_overload
    def __init__(self, *, value: expr = ..., conversion: int = ..., format_spec: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, /, *, conversion: int = ..., format_spec: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, conversion: int, /, *, format_spec: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, conversion: int, format_spec: expr | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr = ..., conversion: int = ..., format_spec: expr | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Interpolation(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr
    str: _builtins.str | None
    conversion: int
    format_spec: expr | None
    @_overload
    def __init__(self, *, value: expr = ..., str: _builtins.str | None = ..., conversion: int = ..., format_spec: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, /, *, str: _builtins.str | None = ..., conversion: int = ..., format_spec: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, str: _builtins.str | None, /, *, conversion: int = ..., format_spec: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, str: _builtins.str | None, conversion: int, /, *, format_spec: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, str: _builtins.str | None, conversion: int, format_spec: expr | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr = ..., str: _builtins.str | None = ..., conversion: int = ..., format_spec: expr | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class JoinedStr(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    values: list[expr]
    @_overload
    def __init__(self, *, values: list[expr] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, values: list[expr], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, values: list[expr] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class TemplateStr(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    values: list[expr]
    @_overload
    def __init__(self, *, values: list[expr] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, values: list[expr], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, values: list[expr] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Constant(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: object
    kind: str | None
    @_overload
    def __init__(self, *, value: object = ..., kind: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: object, /, *, kind: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: object, kind: str | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: object = ..., kind: str | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Attribute(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr
    attr: str
    ctx: expr_context
    @_overload
    def __init__(self, *, value: expr = ..., attr: str = ..., ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, /, *, attr: str = ..., ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, attr: str, /, *, ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, attr: str, ctx: expr_context, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr = ..., attr: str = ..., ctx: expr_context = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Subscript(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr
    slice: expr | _ast.slice
    ctx: expr_context
    @_overload
    def __init__(self, *, value: expr = ..., slice: expr | _ast.slice = ..., ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, /, *, slice: expr | _ast.slice = ..., ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, slice: expr | _ast.slice, /, *, ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, slice: expr | _ast.slice, ctx: expr_context, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr = ..., slice: expr | _ast.slice = ..., ctx: expr_context = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Starred(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr
    ctx: expr_context
    @_overload
    def __init__(self, *, value: expr = ..., ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, /, *, ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, ctx: expr_context, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr = ..., ctx: expr_context = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Name(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    id: str
    ctx: expr_context
    annotation: expr | None
    type_comment: str | None
    @_overload
    def __init__(self, *, id: str = ..., ctx: expr_context = ..., annotation: expr | None = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, id: str, /, *, ctx: expr_context = ..., annotation: expr | None = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, id: str, ctx: expr_context, /, *, annotation: expr | None = ..., type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, id: str, ctx: expr_context, annotation: expr | None, /, *, type_comment: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, id: str, ctx: expr_context, annotation: expr | None, type_comment: str | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, id: str = ..., ctx: expr_context = ..., annotation: expr | None = ..., type_comment: str | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class List(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    elts: list[expr]
    ctx: expr_context
    @_overload
    def __init__(self, *, elts: list[expr] = ..., ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, elts: list[expr], /, *, ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, elts: list[expr], ctx: expr_context, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, elts: list[expr] = ..., ctx: expr_context = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Tuple(expr):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    elts: list[expr]
    ctx: expr_context
    @_overload
    def __init__(self, *, elts: list[expr] = ..., ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, elts: list[expr], /, *, ctx: expr_context = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, elts: list[expr], ctx: expr_context, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, elts: list[expr] = ..., ctx: expr_context = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class Load(expr_context):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Store(expr_context):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Del(expr_context):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class AugLoad(expr_context):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class AugStore(expr_context):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Param(expr_context):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Slice(slice):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    lower: expr | None
    upper: expr | None
    step: expr | None
    lineno: int | None
    col_offset: int | None
    end_lineno: int | None
    end_col_offset: int | None
    @_overload
    def __init__(self, *, lower: expr | None = ..., upper: expr | None = ..., step: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, lower: expr | None, /, *, upper: expr | None = ..., step: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, lower: expr | None, upper: expr | None, /, *, step: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, lower: expr | None, upper: expr | None, step: expr | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, lower: expr | None = ..., upper: expr | None = ..., step: expr | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class And(boolop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Or(boolop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Add(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Sub(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Mult(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class MatMult(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Div(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Mod(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Pow(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class LShift(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class RShift(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class BitOr(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class BitXor(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class BitAnd(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class FloorDiv(operator):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Invert(unaryop, AST):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Not(unaryop, AST):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class UAdd(unaryop, AST):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class USub(unaryop, AST):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Eq(cmpop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class NotEq(cmpop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Lt(cmpop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class LtE(cmpop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Gt(cmpop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class GtE(cmpop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class Is(cmpop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class IsNot(cmpop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class In(cmpop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class NotIn(cmpop):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    def __init__(self, *args: _Never, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self) -> _Self: ...

class comprehension(AST):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    target: expr
    iter: expr
    ifs: list[expr]
    is_async: int
    @_overload
    def __init__(self, *, target: expr = ..., iter: expr = ..., ifs: list[expr] = ..., is_async: int = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, /, *, iter: expr = ..., ifs: list[expr] = ..., is_async: int = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, iter: expr, /, *, ifs: list[expr] = ..., is_async: int = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, iter: expr, ifs: list[expr], /, *, is_async: int = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, target: expr, iter: expr, ifs: list[expr], is_async: int, /, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, *, target: expr = ..., iter: expr = ..., ifs: list[expr] = ..., is_async: int = ...) -> _Self: ...

class ExceptHandler(excepthandler):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    type: expr | None
    name: Name | None
    body: list[stmt]
    @_overload
    def __init__(self, *, type: expr | None = ..., name: Name | None = ..., body: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, type: expr | None, /, *, name: Name | None = ..., body: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, type: expr | None, name: Name | None, /, *, body: list[stmt] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, type: expr | None, name: Name | None, body: list[stmt], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, type: expr | None = ..., name: Name | None = ..., body: list[stmt] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class arguments(AST):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    args: list[Name]
    posonlyargs: list[Name]
    vararg: Name | None
    kwonlyargs: list[Name]
    kw_defaults: list[expr | None]
    kwarg: Name | None
    defaults: list[expr]
    @_overload
    def __init__(self, *, args: list[Name] = ..., posonlyargs: list[Name] = ..., vararg: Name | None = ..., kwonlyargs: list[Name] = ..., kw_defaults: list[expr | None] = ..., kwarg: Name | None = ..., defaults: list[expr] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, args: list[Name], /, *, posonlyargs: list[Name] = ..., vararg: Name | None = ..., kwonlyargs: list[Name] = ..., kw_defaults: list[expr | None] = ..., kwarg: Name | None = ..., defaults: list[expr] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, args: list[Name], posonlyargs: list[Name], /, *, vararg: Name | None = ..., kwonlyargs: list[Name] = ..., kw_defaults: list[expr | None] = ..., kwarg: Name | None = ..., defaults: list[expr] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, args: list[Name], posonlyargs: list[Name], vararg: Name | None, /, *, kwonlyargs: list[Name] = ..., kw_defaults: list[expr | None] = ..., kwarg: Name | None = ..., defaults: list[expr] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, args: list[Name], posonlyargs: list[Name], vararg: Name | None, kwonlyargs: list[Name], /, *, kw_defaults: list[expr | None] = ..., kwarg: Name | None = ..., defaults: list[expr] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, args: list[Name], posonlyargs: list[Name], vararg: Name | None, kwonlyargs: list[Name], kw_defaults: list[expr | None], /, *, kwarg: Name | None = ..., defaults: list[expr] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, args: list[Name], posonlyargs: list[Name], vararg: Name | None, kwonlyargs: list[Name], kw_defaults: list[expr | None], kwarg: Name | None, /, *, defaults: list[expr] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, args: list[Name], posonlyargs: list[Name], vararg: Name | None, kwonlyargs: list[Name], kw_defaults: list[expr | None], kwarg: Name | None, defaults: list[expr], /, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, *, args: list[Name] = ..., posonlyargs: list[Name] = ..., vararg: Name | None = ..., kwonlyargs: list[Name] = ..., kw_defaults: list[expr | None] = ..., kwarg: Name | None = ..., defaults: list[expr] = ...) -> _Self: ...

class keyword(AST):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    arg: str | None
    value: expr
    lineno: int | None
    col_offset: int | None
    end_lineno: int | None
    end_col_offset: int | None
    @_overload
    def __init__(self, *, arg: str | None = ..., value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, arg: str | None, /, *, value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, arg: str | None, value: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, arg: str | None = ..., value: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class alias(AST):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    name: str
    asname: str | None
    lineno: int | None
    col_offset: int | None
    end_lineno: int | None
    end_col_offset: int | None
    @_overload
    def __init__(self, *, name: str = ..., asname: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, /, *, asname: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, asname: str | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, name: str = ..., asname: str | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class withitem(AST):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    context_expr: expr
    optional_vars: expr | None
    @_overload
    def __init__(self, *, context_expr: expr = ..., optional_vars: expr | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, context_expr: expr, /, *, optional_vars: expr | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, context_expr: expr, optional_vars: expr | None, /, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, *, context_expr: expr = ..., optional_vars: expr | None = ...) -> _Self: ...

class match_case(AST):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    pattern: _Pattern
    guard: expr | None
    body: list[stmt]
    @_overload
    def __init__(self, *, pattern: _Pattern = ..., guard: expr | None = ..., body: list[stmt] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, pattern: _Pattern, /, *, guard: expr | None = ..., body: list[stmt] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, pattern: _Pattern, guard: expr | None, /, *, body: list[stmt] = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, pattern: _Pattern, guard: expr | None, body: list[stmt], /, **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, *, pattern: _Pattern = ..., guard: expr | None = ..., body: list[stmt] = ...) -> _Self: ...

class MatchValue(pattern):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: expr
    if sys.version_info < (3, 10):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None
    @_overload
    def __init__(self, *, value: expr = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: expr, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: expr = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class MatchSingleton(pattern):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    value: object
    if sys.version_info < (3, 10):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None
    @_overload
    def __init__(self, *, value: object = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, value: object, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, value: object = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class MatchSequence(pattern):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    patterns: list[pattern]
    if sys.version_info < (3, 10):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None
    @_overload
    def __init__(self, *, patterns: list[pattern] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, patterns: list[pattern], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, patterns: list[pattern] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class MatchMapping(pattern):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    keys: list[expr]
    patterns: list[pattern]
    rest: str | None
    if sys.version_info < (3, 10):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None
    @_overload
    def __init__(self, *, keys: list[expr] = ..., patterns: list[pattern] = ..., rest: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, keys: list[expr], /, *, patterns: list[pattern] = ..., rest: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, keys: list[expr], patterns: list[pattern], /, *, rest: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, keys: list[expr], patterns: list[pattern], rest: str | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, keys: list[expr] = ..., patterns: list[pattern] = ..., rest: str | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class MatchClass(pattern):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    cls: expr
    patterns: list[pattern]
    kwd_attrs: list[str]
    kwd_patterns: list[pattern]
    if sys.version_info < (3, 10):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None
    @_overload
    def __init__(self, *, cls: expr = ..., patterns: list[pattern] = ..., kwd_attrs: list[str] = ..., kwd_patterns: list[pattern] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, cls: expr, /, *, patterns: list[pattern] = ..., kwd_attrs: list[str] = ..., kwd_patterns: list[pattern] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, cls: expr, patterns: list[pattern], /, *, kwd_attrs: list[str] = ..., kwd_patterns: list[pattern] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, cls: expr, patterns: list[pattern], kwd_attrs: list[str], /, *, kwd_patterns: list[pattern] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, cls: expr, patterns: list[pattern], kwd_attrs: list[str], kwd_patterns: list[pattern], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, cls: expr = ..., patterns: list[pattern] = ..., kwd_attrs: list[str] = ..., kwd_patterns: list[pattern] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class MatchStar(pattern):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    name: str | None
    if sys.version_info < (3, 10):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None
    @_overload
    def __init__(self, *, name: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, name: str | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class MatchAs(pattern):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    pattern: _Pattern | None
    name: str | None
    if sys.version_info < (3, 10):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None
    @_overload
    def __init__(self, *, pattern: _Pattern | None = ..., name: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, pattern: _Pattern | None, /, *, name: str | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, pattern: _Pattern | None, name: str | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, pattern: _Pattern | None = ..., name: str | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class MatchOr(pattern):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    patterns: list[pattern]
    if sys.version_info < (3, 10):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None
    @_overload
    def __init__(self, *, patterns: list[pattern] = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, patterns: list[pattern], /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, patterns: list[pattern] = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class type_ignore(TypeIgnore):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    if sys.version_info < (3, 8):
        lineno: int | None
        tag: str
    def __init__(self, *args: _Never, lineno: int | None = ..., tag: str = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        def __replace__(self, **attributes: _Unpack[_TypeIgnoreAttributes]) -> _Self: ...

class TypeVar(type_param):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    name: str
    bound: expr | None
    default_value: expr | None
    if sys.version_info < (3, 12):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None
    @_overload
    def __init__(self, *, name: str = ..., bound: expr | None = ..., default_value: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, /, *, bound: expr | None = ..., default_value: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, bound: expr | None, /, *, default_value: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, bound: expr | None, default_value: expr | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, name: str = ..., bound: expr | None = ..., default_value: expr | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class ParamSpec(type_param):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    name: str
    default_value: expr | None
    if sys.version_info < (3, 12):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None
    @_overload
    def __init__(self, *, name: str = ..., default_value: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, /, *, default_value: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, default_value: expr | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, name: str = ..., default_value: expr | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

class TypeVarTuple(type_param):
    _fields: _ClassVar[tuple[str, ...]]
    _field_types: _ClassVar[dict[str, object]]
    _attributes: _ClassVar[tuple[str, ...]]
    name: str
    default_value: expr | None
    if sys.version_info < (3, 12):
        lineno: int | None
        col_offset: int | None
        end_lineno: int | None
        end_col_offset: int | None
    @_overload
    def __init__(self, *, name: str = ..., default_value: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, /, *, default_value: expr | None = ..., lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    @_overload
    def __init__(self, name: str, default_value: expr | None, /, *, lineno: int | None = ..., col_offset: int | None = ..., end_lineno: int | None = ..., end_col_offset: int | None = ..., **attributes: object) -> None: ...
    if sys.version_info >= (3, 15):
        def __replace__(self, **attributes: object) -> _Self: ...
    elif sys.version_info >= (3, 14):
        @_overload
        def __replace__(self, **attributes: _Unpack[_LocationAttributes]) -> _Self: ...
        @_overload
        def __replace__(self, *, name: str = ..., default_value: expr | None = ..., **attributes: _Unpack[_LocationAttributes]) -> _Self: ...

_CoreGAstNode = (
    Module
    | Interactive
    | Expression
    | Suite
    | FunctionDef
    | AsyncFunctionDef
    | ClassDef
    | Return
    | Delete
    | Assign
    | AugAssign
    | AnnAssign
    | For
    | AsyncFor
    | While
    | If
    | With
    | AsyncWith
    | Raise
    | Try
    | Assert
    | Import
    | ImportFrom
    | Global
    | Nonlocal
    | Expr
    | Pass
    | Break
    | Continue
    | BoolOp
    | BinOp
    | UnaryOp
    | Lambda
    | IfExp
    | Dict
    | Set
    | ListComp
    | SetComp
    | DictComp
    | GeneratorExp
    | Await
    | Yield
    | YieldFrom
    | Compare
    | Call
    | FormattedValue
    | JoinedStr
    | Constant
    | Attribute
    | Subscript
    | Starred
    | Name
    | List
    | Tuple
    | Load
    | Store
    | Del
    | AugLoad
    | AugStore
    | Param
    | Slice
    | And
    | Or
    | Add
    | Sub
    | Mult
    | MatMult
    | Div
    | Mod
    | Pow
    | LShift
    | RShift
    | BitOr
    | BitXor
    | BitAnd
    | FloorDiv
    | Invert
    | Not
    | UAdd
    | USub
    | Eq
    | NotEq
    | Lt
    | LtE
    | Gt
    | GtE
    | Is
    | IsNot
    | In
    | NotIn
    | comprehension
    | ExceptHandler
    | arguments
    | keyword
    | alias
    | withitem
)
_LegacyGAstNode = (
    Print
    | Exec
    | Repr
)
_Py38GAstNode = (
    FunctionType
    | NamedExpr
    | type_ignore
)
_Py310GAstNode = (
    Match
    | match_case
    | MatchValue
    | MatchSingleton
    | MatchSequence
    | MatchMapping
    | MatchClass
    | MatchStar
    | MatchAs
    | MatchOr
)
_Py311GAstNode = (
    TryStar
)
_Py312GAstNode = (
    TypeAlias
    | TypeVar
    | ParamSpec
    | TypeVarTuple
)
_Py314GAstNode = (
    Interpolation
    | TemplateStr
)
_TypeIgnoreGAstNode = TypeIgnore
_CoreAstNode = (
    _ast.Module
    | _ast.Interactive
    | _ast.Expression
    | _ast.Suite
    | _ast.FunctionDef
    | _ast.AsyncFunctionDef
    | _ast.ClassDef
    | _ast.Return
    | _ast.Delete
    | _ast.Assign
    | _ast.AugAssign
    | _ast.AnnAssign
    | _ast.For
    | _ast.AsyncFor
    | _ast.While
    | _ast.If
    | _ast.With
    | _ast.AsyncWith
    | _ast.Raise
    | _ast.Try
    | _ast.Assert
    | _ast.Import
    | _ast.ImportFrom
    | _ast.Global
    | _ast.Nonlocal
    | _ast.Expr
    | _ast.Pass
    | _ast.Break
    | _ast.Continue
    | _ast.BoolOp
    | _ast.BinOp
    | _ast.UnaryOp
    | _ast.Lambda
    | _ast.IfExp
    | _ast.Dict
    | _ast.Set
    | _ast.ListComp
    | _ast.SetComp
    | _ast.DictComp
    | _ast.GeneratorExp
    | _ast.Await
    | _ast.Yield
    | _ast.YieldFrom
    | _ast.Compare
    | _ast.Call
    | _ast.FormattedValue
    | _ast.JoinedStr
    | _ast.Constant
    | _ast.Attribute
    | _ast.Subscript
    | _ast.Starred
    | _ast.Name
    | _ast.List
    | _ast.Tuple
    | _ast.Load
    | _ast.Store
    | _ast.Del
    | _ast.AugLoad
    | _ast.AugStore
    | _ast.Param
    | _ast.Slice
    | _ast.And
    | _ast.Or
    | _ast.Add
    | _ast.Sub
    | _ast.Mult
    | _ast.MatMult
    | _ast.Div
    | _ast.Mod
    | _ast.Pow
    | _ast.LShift
    | _ast.RShift
    | _ast.BitOr
    | _ast.BitXor
    | _ast.BitAnd
    | _ast.FloorDiv
    | _ast.Invert
    | _ast.Not
    | _ast.UAdd
    | _ast.USub
    | _ast.Eq
    | _ast.NotEq
    | _ast.Lt
    | _ast.LtE
    | _ast.Gt
    | _ast.GtE
    | _ast.Is
    | _ast.IsNot
    | _ast.In
    | _ast.NotIn
    | _ast.comprehension
    | _ast.ExceptHandler
    | _ast.arguments
    | _ast.keyword
    | _ast.alias
    | _ast.withitem
)
_AstArgNode = _ast.arg
if sys.version_info < (3, 9):
    _LegacySliceAstNode = _ast.Index | _ast.ExtSlice
if sys.version_info >= (3, 8):
    _Py38AstNode = (
        _ast.FunctionType
        | _ast.NamedExpr
        | _ast.type_ignore
    )
    _TypeIgnoreAstNode = _ast.TypeIgnore
if sys.version_info >= (3, 10):
    _Py310AstNode = (
        _ast.Match
        | _ast.match_case
        | _ast.MatchValue
        | _ast.MatchSingleton
        | _ast.MatchSequence
        | _ast.MatchMapping
        | _ast.MatchClass
        | _ast.MatchStar
        | _ast.MatchAs
        | _ast.MatchOr
    )
if sys.version_info >= (3, 11):
    _Py311AstNode = (
        _ast.TryStar
    )
if sys.version_info >= (3, 12):
    _Py312AstNode = (
        _ast.TypeAlias
        | _ast.TypeVar
        | _ast.ParamSpec
        | _ast.TypeVarTuple
    )
if sys.version_info >= (3, 14):
    _Py314AstNode = (
        _ast.Interpolation
        | _ast.TemplateStr
    )
_GAstNode = (
    _CoreGAstNode
    | _LegacyGAstNode
    | _Py38GAstNode
    | _Py310GAstNode
    | _Py311GAstNode
    | _Py312GAstNode
    | _Py314GAstNode
    | _TypeIgnoreGAstNode
)

if sys.version_info >= (3, 14):
    _SupportedGAstNode = (
        _CoreGAstNode | _Py38GAstNode | _Py310GAstNode
        | _Py311GAstNode | _Py312GAstNode | _Py314GAstNode
        | _TypeIgnoreGAstNode
    )
    _UnsupportedGAstNode = _LegacyGAstNode
    _SupportedAstNode = (
        _CoreAstNode | _Py38AstNode | _Py310AstNode | _Py311AstNode
        | _Py312AstNode | _Py314AstNode | _TypeIgnoreAstNode
        | _AstArgNode
    )
elif sys.version_info >= (3, 12):
    _SupportedGAstNode = (
        _CoreGAstNode | _Py38GAstNode | _Py310GAstNode
        | _Py311GAstNode | _Py312GAstNode | _TypeIgnoreGAstNode
    )
    _UnsupportedGAstNode = _LegacyGAstNode | _Py314GAstNode
    _SupportedAstNode = (
        _CoreAstNode | _Py38AstNode | _Py310AstNode | _Py311AstNode
        | _Py312AstNode | _TypeIgnoreAstNode | _AstArgNode
    )
elif sys.version_info >= (3, 11):
    _SupportedGAstNode = (
        _CoreGAstNode | _Py38GAstNode | _Py310GAstNode
        | _Py311GAstNode | _TypeIgnoreGAstNode
    )
    _UnsupportedGAstNode = (
        _LegacyGAstNode | _Py312GAstNode | _Py314GAstNode
    )
    _SupportedAstNode = (
        _CoreAstNode | _Py38AstNode | _Py310AstNode | _Py311AstNode
        | _TypeIgnoreAstNode | _AstArgNode
    )
elif sys.version_info >= (3, 10):
    _SupportedGAstNode = (
        _CoreGAstNode | _Py38GAstNode | _Py310GAstNode
        | _TypeIgnoreGAstNode
    )
    _UnsupportedGAstNode = (
        _LegacyGAstNode | _Py311GAstNode | _Py312GAstNode
        | _Py314GAstNode
    )
    _SupportedAstNode = (
        _CoreAstNode | _Py38AstNode | _Py310AstNode
        | _TypeIgnoreAstNode | _AstArgNode
    )
elif sys.version_info >= (3, 9):
    _SupportedGAstNode = (
        _CoreGAstNode | _Py38GAstNode | _TypeIgnoreGAstNode
    )
    _UnsupportedGAstNode = (
        _LegacyGAstNode | _Py310GAstNode | _Py311GAstNode
        | _Py312GAstNode | _Py314GAstNode
    )
    _SupportedAstNode = (
        _CoreAstNode | _Py38AstNode | _TypeIgnoreAstNode | _AstArgNode
    )
elif sys.version_info >= (3, 8):
    _SupportedGAstNode = (
        _CoreGAstNode | _Py38GAstNode | _TypeIgnoreGAstNode
    )
    _UnsupportedGAstNode = (
        _LegacyGAstNode | _Py310GAstNode | _Py311GAstNode
        | _Py312GAstNode | _Py314GAstNode
    )
    _SupportedAstNode = (
        _CoreAstNode | _Py38AstNode | _TypeIgnoreAstNode | _AstArgNode
        | _LegacySliceAstNode
    )
else:
    _SupportedGAstNode = _CoreGAstNode
    _UnsupportedGAstNode = (
        _LegacyGAstNode | _Py38GAstNode | _Py310GAstNode
        | _Py311GAstNode | _Py312GAstNode | _Py314GAstNode
        | _TypeIgnoreGAstNode
    )
    _SupportedAstNode = _CoreAstNode | _AstArgNode | _LegacySliceAstNode

@_overload
def ast_to_gast(node: _SupportedAstNode) -> _SupportedGAstNode: ...
@_overload
def ast_to_gast(node: _ast.AST) -> _ast.AST | None: ...
@_overload
def gast_to_ast(node: _SupportedGAstNode) -> _ast.AST: ...
@_overload
def gast_to_ast(node: _UnsupportedGAstNode) -> None: ...

if sys.version_info >= (3, 15):
    @_overload
    def parse(
        source: _SupportedAstNode,
        filename: _Filename = ...,
        mode: str = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
        module: str | None = ...,
    ) -> _SupportedGAstNode: ...
    @_overload
    def parse(
        source: _ast.AST,
        filename: _Filename = ...,
        mode: str = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
        module: str | None = ...,
    ) -> _ast.AST | None: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        mode: _Literal["exec"] = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
        module: str | None = ...,
    ) -> Module: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename,
        mode: _Literal["eval"],
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
        module: str | None = ...,
    ) -> Expression: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        *,
        mode: _Literal["eval"],
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
        module: str | None = ...,
    ) -> Expression: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename,
        mode: _Literal["single"],
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
        module: str | None = ...,
    ) -> Interactive: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        *,
        mode: _Literal["single"],
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
        module: str | None = ...,
    ) -> Interactive: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename,
        mode: _Literal["func_type"],
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
        module: str | None = ...,
    ) -> FunctionType: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        *,
        mode: _Literal["func_type"],
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
        module: str | None = ...,
    ) -> FunctionType: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        mode: str = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
        module: str | None = ...,
    ) -> mod: ...
elif sys.version_info >= (3, 13):
    @_overload
    def parse(
        source: _SupportedAstNode,
        filename: _Filename = ...,
        mode: str = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
    ) -> _SupportedGAstNode: ...
    @_overload
    def parse(
        source: _ast.AST,
        filename: _Filename = ...,
        mode: str = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
    ) -> _ast.AST | None: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        mode: _Literal["exec"] = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
    ) -> Module: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename,
        mode: _Literal["eval"],
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
    ) -> Expression: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        *,
        mode: _Literal["eval"],
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
    ) -> Expression: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename,
        mode: _Literal["single"],
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
    ) -> Interactive: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        *,
        mode: _Literal["single"],
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
    ) -> Interactive: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename,
        mode: _Literal["func_type"],
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
    ) -> FunctionType: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        *,
        mode: _Literal["func_type"],
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
    ) -> FunctionType: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        mode: str = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
        optimize: _Literal[-1, 0, 1, 2] = ...,
    ) -> mod: ...
elif sys.version_info >= (3, 8):
    @_overload
    def parse(
        source: _SupportedAstNode,
        filename: _Filename = ...,
        mode: str = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
    ) -> _SupportedGAstNode: ...
    @_overload
    def parse(
        source: _ast.AST,
        filename: _Filename = ...,
        mode: str = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
    ) -> _ast.AST | None: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        mode: _Literal["exec"] = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
    ) -> Module: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename,
        mode: _Literal["eval"],
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
    ) -> Expression: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        *,
        mode: _Literal["eval"],
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
    ) -> Expression: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename,
        mode: _Literal["single"],
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
    ) -> Interactive: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        *,
        mode: _Literal["single"],
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
    ) -> Interactive: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename,
        mode: _Literal["func_type"],
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
    ) -> FunctionType: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        *,
        mode: _Literal["func_type"],
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
    ) -> FunctionType: ...
    @_overload
    def parse(
        source: _Source,
        filename: _Filename = ...,
        mode: str = ...,
        *,
        type_comments: bool = ...,
        feature_version: int | tuple[int, int] | None = ...,
    ) -> mod: ...
else:
    @_overload
    def parse(
        source: _SupportedAstNode,
        filename: str | bytes = ...,
        mode: str = ...,
    ) -> _SupportedGAstNode: ...
    @_overload
    def parse(
        source: _ast.AST,
        filename: str | bytes = ...,
        mode: str = ...,
    ) -> _ast.AST | None: ...
    @_overload
    def parse(
        source: str | bytes,
        filename: str | bytes = ...,
        mode: _Literal["exec"] = ...,
    ) -> Module: ...
    @_overload
    def parse(
        source: str | bytes,
        filename: str | bytes,
        mode: _Literal["eval"],
    ) -> Expression: ...
    @_overload
    def parse(
        source: str | bytes,
        filename: str | bytes = ...,
        *,
        mode: _Literal["eval"],
    ) -> Expression: ...
    @_overload
    def parse(
        source: str | bytes,
        filename: str | bytes,
        mode: _Literal["single"],
    ) -> Interactive: ...
    @_overload
    def parse(
        source: str | bytes,
        filename: str | bytes = ...,
        *,
        mode: _Literal["single"],
    ) -> Interactive: ...
    @_overload
    def parse(
        source: str | bytes,
        filename: str | bytes = ...,
        mode: str = ...,
    ) -> mod: ...

def unparse(gast_obj: _GAstNode) -> str: ...
@_overload
def literal_eval(node_or_string: str) -> _LiteralValue: ...
@_overload
def literal_eval(node_or_string: _GAstNode) -> object: ...
def get_docstring(
    node: AsyncFunctionDef | FunctionDef | ClassDef | Module,
    clean: bool = ...,
) -> str | None: ...
def copy_location(new_node: _T, old_node: AST) -> _T: ...
def fix_missing_locations(node: _T) -> _T: ...
if sys.version_info >= (3, 8):
    def get_source_segment(source: str, node: AST, *, padded: bool = ...) -> str | None: ...
else:
    def get_source_segment(source: str, node: AST, padded: bool = ...) -> None: ...
def increment_lineno(node: _T, n: int = ...) -> _T: ...
def dump(
    node: AST,
    annotate_fields: bool = ...,
    include_attributes: bool = ...,
    color: bool = ...,
    indent: int | str | None = ...,
    show_empty: bool = ...,
) -> str: ...
def iter_child_nodes(node: AST) -> _Iterator[AST]: ...
def walk(node: AST) -> _Iterator[AST]: ...

del sys
