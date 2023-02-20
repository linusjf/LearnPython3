#!/usr/bin/env python
"""Graphviz test."""
from graphviz import Digraph


def main():
    """Execute main."""
    dot = Digraph(comment="The Round Table", format="png", node_attr={"shape": "plaintext"})
    dot.node("A", "King Arthur")
    dot.node("B", "Sir Bedevere the Wise")
    dot.node("L", "Sir Lancelot the Brave")

    dot.edges(["AB", "AL"])
    dot.edge("B", "L", constraint="false")
    print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
    dot.render("round-table.gv", view=False)


if __name__ == "__main__":
    main()
