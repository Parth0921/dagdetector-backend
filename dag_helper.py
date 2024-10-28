from models import Edge

# These are helper functions to check if the graph is DAG or not
# Returns node at which cycle is detected or empty string

# Recursive helper for dag_dfs
def is_cyclic_dfs(node, adjaceny_list, visited, pathVisited):
    visited[node] = True
    pathVisited[node] = True
    
    # print("node:-" + node)
    for neighbour in adjaceny_list[node]:
        if not visited[neighbour]:
            result = is_cyclic_dfs(neighbour, adjaceny_list, visited, pathVisited)
            if result != "":
                return neighbour 
        elif pathVisited[neighbour]:
            return neighbour 


    pathVisited[node] = False
    return ""

# DFS implementation to check DAG
def dag_dfs(nodes: list[str], edges: list[Edge]):
    adjaceny_list, _ = build_adjacency_and_indegree_list(nodes, edges)

    visited = {}
    pathVisited = {}

    for node in nodes:
        visited[node] = False
        pathVisited[node] = False

    for node in nodes:
        if not visited[node]:
            result = is_cyclic_dfs(node, adjaceny_list, visited, pathVisited)
            if result != "":
               return result 

    return ""

# Kahn's algorithm to check DAG --> slight modification of topological sort --> BFS
def dag_bfs(nodes, edges):
    adjaceny_list, indegree_list = build_adjacency_and_indegree_list(nodes, edges)

    queue = []
    for node in nodes:
        if indegree_list[node] == 0:
            queue.append(node)

    count = 0
    while queue:
        node = queue.pop(0)
        count += 1

        for neighbour in adjaceny_list[node]:
            indegree_list[neighbour] -= 1
            if indegree_list[neighbour] == 0:
                queue.append(neighbour)

    if count == len(nodes):
        return ""

    cycle_node = ""
    for node in nodes:
        if indegree_list[node] != 0:
            cycle_node = node
            break
    return cycle_node


# Helper function which builds adjacency list and indegree list
def build_adjacency_and_indegree_list(nodes, edges):
    adjaceny_list = {}
    indegree_list = {}
    for node in nodes:
        adjaceny_list[node] = []
        indegree_list[node] = 0

    for edge in edges:
        adjaceny_list[edge.source].append(edge.target)
        indegree_list[edge.target] += 1

    return adjaceny_list, indegree_list


