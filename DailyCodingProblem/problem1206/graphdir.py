#!/usr/bin/env python
from collections import defaultdict

def direction_to_constraints(direction):
    # Map directions to x and y constraints
    constraints = []
    if 'N' in direction:
        constraints.append(('y', 1))  # A.y > B.y => A.y - B.y > 0
    if 'S' in direction:
        constraints.append(('y', -1)) # A.y < B.y => B.y - A.y > 0
    if 'E' in direction:
        constraints.append(('x', 1))  # A.x > B.x
    if 'W' in direction:
        constraints.append(('x', -1)) # A.x < B.x
    return constraints

def validate_rules(rules):
    variables = set()
    edges = {'x': [], 'y': []}

    for rule in rules:
        a, dirn, b = rule.split()
        variables.update([a, b])
        constraints = direction_to_constraints(dirn)
        for axis, sign in constraints:
            # A > B → A - B > 0 → B - A < 0 (edge from A to B with weight -1)
            if sign == 1:
                edges[axis].append((b, a, -1))  # a > b => b - a < 0
            else:
                edges[axis].append((a, b, -1))  # a < b => a - b < 0

    def bellman_ford(nodes, edges):
        dist = {node: 0 for node in nodes}
        for _ in range(len(nodes)):
            updated = False
            for u, v, weight in edges:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    updated = True
            if not updated:
                return True
        return False  # Negative cycle → contradiction

    return bellman_ford(variables, edges['x']) and bellman_ford(variables, edges['y'])

# Example usage:
rules1 = [
    "A N B",
    "B NE C",
    "C N A"
]

rules2 = [
    "A NW B",
    "A N B"
]

print(validate_rules(rules1))  # Output: False
print(validate_rules(rules2))  # Output: True
