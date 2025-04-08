#!/usr/bin/env python
from collections import defaultdict, deque

def alien_order(words):
    print(words)

    # Step 1: Create graph and in-degree map
    graph = defaultdict(set)
    print(graph)

    in_degree = {char: 0 for word in words for char in word}
    
    print(in_degree)
    
    # Step 2: Build the graph
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    in_degree[word2[j]] += 1
                break
        else:
            # Edge case: word2 is a prefix of word1 and comes after, invalid input
            if len(word2) < len(word1):
                return []
    
    print(in_degree)
    print(graph)
    
    # Step 3: Topological sort (Kahn's Algorithm)
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    print(queue)
    order = []

    while queue:
        char = queue.popleft()
        order.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all characters are in the order list, return it
    if len(order) == len(in_degree):
        return order
    else:
        # Cycle detected
        return []

# Example usage
words = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']
# Output: ['x', 'z', 'w', 'y']
print(f"{alien_order(words)}\n") 

words = ['abc', 'bcd', 'cde']
# Expected output: ['a', 'd', 'e', 'b', 'c']
print(f"{alien_order(words)}\n")

words = ['abc', 'abd']
# First difference: 'c' < 'd'
# Expected output: ['a', 'b', 'c', 'd']
print(f"{alien_order(words)}\n")

words = ['bat', 'cat', 'fat']
# Expected output: ['b', 'a', 't','c', 'f']
print(f"{alien_order(words)}\n")


