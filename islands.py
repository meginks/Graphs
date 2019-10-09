# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

# island_counter(islands) # returns 4

# for node in array:
#   if node not in visited:
#       islands += 1
#       recurse_through(node) 

#Code from Brannan
def count_islands(islands):
    count = 0
    cache = {}
    def add_edges(i, j):
        if i > 0 and islands[i-1][j] == 1 and f"{i - 1}{j}" not in cache:
            cache[f"{i - 1}{j}"] = 1
            add_edges(i - 1, j)
        if i < len(islands) - 1 and islands[i+1][j] == 1 and f"{i + 1}{j}" not in cache:
            cache[f"{i + 1}{j}"] = 1
            add_edges(i + 1, j)
        if j > 0 and islands[i][j-1] == 1 and f"{i}{j -1}" not in cache:
            cache[f"{i}{j - 1}"] = 1
            add_edges(i, j - 1)
        if j < len(islands[0]) - 1 and islands[i][j+1] == 1 and f"{i}{j+1}" not in cache:
            cache[f"{i}{j + 1}"] = 1
            add_edges(i, j + 1)
    for i in range(len(islands)):
        for j in range(len(islands[0])):
            if islands[i][j] == 1 and f"{i}{j}" not in cache:
                cache[f"{i}{j}"] = 1
                count += 1
                add_edges(i, j)
    print(count)

count_islands(islands) 

# Code from Brian in class
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


# def island_counter(matrix):
#     # create a visited matrix
#     visited = []
#     for i in range(len(matrix)):
#         visited.append([False] * len(matrix[0]))
    
#     island_count = 0

#     for x in range(len(matrix[0])):
#         for y in range(len(matrix)):
#             # if not visited
#             if not visited[x][y]:
#                 if matrix[x][y] == 1:
#                     # Run some DFT and mark each as visited
#                     dft(x, y, matrix, visited)

#                     island_count += 1

#     return island_count


# def dft(x, y, matrix, visited):
#     s = Stack()
#     s.push((x, y))

#     while s.size() > 0:
#         v = s.pop()
#         x = v[0]
#         y = v[1]

#         if not visited[y][x]:
#             # mark as visited
#             visited[y][x] = True

#             for neighbor in get_neighbors((x, y), matrix):
#                 s.push(neighbor)

#     return visited


# def get_neighbors(vertex, graph_matrix):
#     x = vertex[0]
#     y = vertex[1]

#     neighbors = []

#     # North
#     if y > 0 and graph_matrix[y-1][x] == 1:
#         neighbors.append((x, y-1))

#     # South
#     if y < len(graph_matrix) - 1 and graph_matrix[y+1][x] == 1:
#         neighbors.append((x, y + 1))

#     # East
#     if x < len(graph_matrix[0]) - 1 and graph_matrix[y][x+1] == 1:
#         neighbors.append((x+1, y))

#     # West
#     if x > 0 and graph_matrix[y][x-1] == 1:
#         neighbors.append((x-1, y))

#     return neighbors



# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]


# print(island_counter(islands))