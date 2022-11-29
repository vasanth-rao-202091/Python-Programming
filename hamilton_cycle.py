source = int(input("Enter Source Vertex: "))
num_vertices = int(input("Enter Number of vertices: "))
num_edges = int(input("Enter Number of edges: "))
# file = "./graph1.txt"

adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

def print_adjacency_matrix():
    for row in adjacency_matrix:
        print(row)
        
# graph = open(file)

# for line in graph:
#     s,d = (int(x) for x in line.split(" "))
    #  adjacency_matrix[s][d] = 1
    #  adjacency_matrix[d][s] = 1

for i in range(num_edges):
    s,d = (int(x) for x in input("Enter source, destination (s d): ").split(" "))
    adjacency_matrix[s][d] = 1
    adjacency_matrix[d][s] = 1

print_adjacency_matrix()

visited = [False for _ in range(num_vertices)]
visited[source] = True
def hamiltonion_cycle(matrix,source,vertices,visited,path=[]):
    path.append(source)
    
    if vertices == 1:
        s = path[0]
        if matrix[source][s]:
            print(f"{path+[s]=}")
        path.pop()
        return

    for nxt in range(num_vertices):
        if not visited[nxt] and matrix[source][nxt]:
            visited[nxt]=True
            hamiltonion_cycle(matrix,nxt,vertices-1,visited,path)
            visited[nxt] = False
    path.pop()

hamiltonion_cycle(adjacency_matrix,source,num_vertices,visited)
