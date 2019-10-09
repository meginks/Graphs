from collections import defaultdict
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
        
def dfs(starting_vertex, ancestors):
    visited = []
    stack = Stack()
    stack.push([starting_vertex])
    while stack.size() > 0:
        path = stack.pop()
        vertex = path[-1]
        if vertex not in visited:
            visited.append(vertex)
        for neighbor in ancestors[vertex]:
            path_copy = [*path]
            path_copy.append(neighbor)
            stack.push(path_copy)
    return visited[-1]

def earliest_ancestor(ancestors, starting_node):
    family = defaultdict(list)
    for parent, child in ancestors:
        family[child].append(parent)
    if starting_node not in family:
        return -1
    ancestor = dfs(starting_node, family)
    return ancestor
