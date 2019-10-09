# from collections import defaultdict
# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)
        
# def dfs(starting_vertex, ancestors):
#     visited = []
#     stack = Stack()
#     stack.push([starting_vertex])
#     while stack.size() > 0:
#         path = stack.pop()
#         vertex = path[-1]
#         if vertex not in visited:
#             visited.append(vertex)
#         for neighbor in ancestors[vertex]:
#             path_copy = [*path]
#             path_copy.append(neighbor)
#             stack.push(path_copy)
#     return visited[-1]

# def earliest_ancestor(ancestors, starting_node):
#     family = defaultdict(list)
#     for parent, child in ancestors:
#         family[child].append(parent)
#     if starting_node not in family:
#         return -1
#     earliest_ancestor = dfs(starting_node, family)
#     return earliest_ancestor
class Queue():
  def __init__(self):
    self.queue = []
  def enqueue(self, value):
    self.queue.append(value)
  def dequeue(self):
    if self.size() > 0:
      return self.queue.pop(0)
    else:
      return None
  def size(self):
    return len(self.queue)
class Graph:
  def __init__(self):
    self.vertices = {}
  
  def add_vertex(self, vertex_id):
    if vertex_id not in self.vertices:
      self.vertices[vertex_id] = set()
  def add_edges(self, v1, v2):
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)
    else:
      raise IndexError("That vertex does not exist!")
def earliest_ancestor(ancestors, starting_node):
  graph = Graph()
  for pair in ancestors:
    graph.add_vertex(pair[0])
    graph.add_vertex(pair[1])
    graph.add_edges(pair[1], pair[0])
  queue = Queue()
  queue.enqueue([starting_node])
  max_path_length = 1
  earliest_ancestor = -1
  while queue.size() > 0:
    path = queue.dequeue()
    v = path[-1]
    if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
      earliest_ancestor = v
      max_path_length = len(path)
    for neighbor in graph.vertices[v]:
      path_copy = list(path)
      path_copy.append(neighbor)
      queue.enqueue(path_copy)
  return earliest_ancestor