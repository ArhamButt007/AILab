graph = {
  'A' : {'B': 4, 'C': 3},
  'B' : {'A': 4, 'C': 2, 'D': 5},
  'C' : {'A': 3, 'B': 2, 'D': 1},
  'D' : {'B': 5, 'C': 1, 'E': 2},
  'E' : {'D': 2},
}

heu = {
  'A' : 3,
  'B' : 2,
  'C' : 2,
  'D' : 1,
  'E' : 0,
}

def custom_sort(open_list):
    return sorted(open_list, key=lambda x: x[0])

def astar(graph, start, goal, heuristics):
    open_list = [(0, start)]
    closed_list = set()
    g_values = {node: float('inf') for node in graph}
    g_values[start] = 0

    while open_list:
        open_list = custom_sort(open_list)
        current_cost, current_node = open_list.pop(0)

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from.get(current_node)
            return path[::-1]

        closed_list.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor in closed_list:
                continue

            tentative_g = g_values[current_node] + cost
            if tentative_g < g_values[neighbor]:
                g_values[neighbor] = tentative_g
                f_value = tentative_g + heuristics[neighbor]
                open_list.append((f_value, neighbor))
                came_from[neighbor] = current_node

    return None

# Find the shortest path from A to E
came_from = {}
path = astar(graph, 'A', 'E', heu)

if path:
    print("Shortest path:", " -> ".join(path))
else:
    print("No path found")















# graph = {
#   'A' : ['B','E','C'],
#   'B' : ['A', 'E','D'],
#   'C' : ['A','F','G'], 
#   'D' : ['B', 'E'],
#   'E' : ['A', 'B','F'],
#   'F' : ['C'],
#   'G' : ['C'], 
# }

# visited = [] 
# queue = []    

# def bfs(visited, graph, node): 
#   visited.append(node)
#   queue.append(node)

#   while queue:          
#     val = queue.pop(0) 
#     print (val, end = " ") 

#     for adjacent in graph[val]:
#       if adjacent not in visited:
#         visited.append(adjacent)
#         queue.append(adjacent)


# print("Breadth-First Search Traversal")
# bfs(visited, graph, 'C')    
