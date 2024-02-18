from typing import Any, cast

from lark import Token, Tree


def get_ancestor(node: Tree, ancestor_name: str) -> Tree | None:
    while parent := cast(Any, node.meta).parent:
        if parent.data == ancestor_name:
            return parent
        node = cast(Any, node.meta).parent
    return None


def get_containing_query(node: Tree) -> Tree:
    """Gets the subquery that contains the given node."""
    query = get_ancestor(node, "full_query")
    assert query is not None
    return query


def in_subquery(node: Tree) -> bool:
    return (
        get_ancestor(node, "subquery") is not None
        or get_ancestor(node, "with_cte") is not None
    )


def has_subquery(node: Tree | Token) -> bool:
    """Determines if a node has a subquery as a child."""
    if isinstance(node, Token):
        return False

    try:
        next(node.find_data("full_query"))
    except StopIteration:
        return False
    else:
        return True
