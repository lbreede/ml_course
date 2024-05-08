import math

graph = {
    "a": ["b"],
    "b": ["a","c","d","e"],
    "c": ["b","e"],
    "e": ["c","b","d","f"],
    "d": ["b","e","f"],
    "f": ["d","e","g"],
    "g": ["f"],
    "o": ["n"],
    "n": ["o"],
        }

def connectedGraphs(graph):
    visited = set()
    #for node in graph:
    #    graphTraversal(graph, node, visited)
    print(hasPath(graph, "a", "n", visited))

def graphTraversal(graph, source, visited):
    if source in visited:
        return False

    visited.add(source)
    print(source)
    for node in graph[source]:
        graphTraversal(graph, node, visited)

    return True

def hasPath(graph, source, dest, visited):
    if source == dest:
        return True
    if source in visited:
        return False
    visited.add(source)
    for node in graph[source]:
        if hasPath(graph, node, dest, visited):
            return True

    return False

connectedGraphs(graph)
