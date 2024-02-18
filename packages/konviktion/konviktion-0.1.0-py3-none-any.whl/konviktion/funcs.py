""" This module provides helpers for the mikro rath api
they are wrapped functions for the turms generated api"""
from .rath import KonviktionRath, get_current_konviktion_rath
from koil.helpers import unkoil, unkoil_gen
from typing import Optional, Type, Dict, Any, TypeVar, Iterator, AsyncIterator


T = TypeVar("T")


async def aexecute(
    operation: Type[T],
    variables: Dict[str, Any],
    rath: Optional[KonviktionRath] = None,
) -> T:
    """Execute a graphql operation (asynchronous)

    This is a proxy function for rath query, it is referenced defined
    in the graphql.config.yaml file and is used to execute the auto
    generated graphql operations.

    Parameters
    ----------
    operation : Type[T]
        The graphql operation to execute
    variables : Dict[str, Any]
        The variables for the graphql operation
    rath : Optional[KonviktionRath], optional
        The rath client to use, by default None

    Returns
    -------
    T
        The result of the graphql operation
    """
    rath = rath or get_current_konviktion_rath()

    x = await rath.aquery(
        operation.Meta.document,  # type: ignore
        operation.Arguments(**variables).dict(by_alias=True),  # type: ignore
    )  # type: ignore
    return operation(**x.data)


def execute(
    operation: Type[T],
    variables: Dict[str, Any],
    rath: Optional[KonviktionRath] = None,
) -> T:
    """Execute a graphql operation (synchronous)

    This is a proxy function for rath query, it is referenced defined
    in the graphql.config.yaml file and is used to execute the auto
    generated graphql operations.

    Parameters
    ----------
    operation : Type[T]
        The graphql operation to execute
    variables : Dict[str, Any]
        The variables for the graphql operation
    rath : Optional[KonviktionRath], optional
        The rath client to use, by default None

    Returns
    -------
    T
        The result of the graphql operation
    """
    return unkoil(aexecute, operation, variables, rath=rath)


def subscribe(
    operation: Type[T],
    variables: Dict[str, Any],
    rath: Optional[KonviktionRath] = None,
) -> Iterator[T]:
    """Subscribe to a graphql operation (synchronous)

    This is a proxy function for rath subscribe, it is referenced defined
    in the graphql.config.yaml file and is used to execute the auto
    generated graphql operations.

    Parameters
    ----------
    operation : Type[T]
        The graphql operation to execute
    variables : Dict[str, Any]
        The variables for the graphql operation
    rath : Optional[KonviktionRath], optional
        The rath client to use, by default None

    Yields
    -------
    T
        The result of the graphql operation
    """

    return unkoil_gen(asubscribe, operation, variables, rath=rath)


async def asubscribe(
    operation: Type[T],
    variables: Dict[str, Any],
    rath: Optional[KonviktionRath] = None,
) -> AsyncIterator[T]:
    """Subscribe to a graphql operation (asynchronous)

    This is a proxy function for rath asubscribe, it is referenced defined
    in the graphql.config.yaml file and is used to execute the auto
    generated graphql operations.

    Parameters
    ----------
    operation : Type[T]
        The graphql operation to execute
    variables : Dict[str, Any]
        The variables for the graphql operation
    rath : Optional[KonviktionRath], optional
        The rath client to use, by default None

    Yields
    -------
    T
        The result of the graphql operation
    """
    rath = rath or get_current_konviktion_rath()
    async for event in rath.asubscribe(
        operation.Meta.document,  # type: ignore
        operation.Arguments(**variables).dict(by_alias=True),  # type: ignore
    ):
        yield operation(**event.data)
