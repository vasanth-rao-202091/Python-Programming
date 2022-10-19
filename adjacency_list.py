#edges to adjacency list of weighted undirected graph
v = int(input("Please enter the no.of vertices: "))

adj_list = {}
edges = int(input("Please enter the no.of edges: ")) #taking input

print("\nStart Entering edges(s,d,w): ")
for i in range(edges):
    v1,v2,w = list(map(int,input().split(" ")))
    #adding edges to the list
    if v1 in adj_list:
        adj_list[v1].append((v2,w))
    else:
        adj_list[v1] = [(v2,w)]
    if v2 in adj_list:
        adj_list[v2].append((v1,w))
    else:
        adj_list[v2] = [(v1,w)]
print("\nThe Adjacency List is:  ")
for vertex in adj_list.keys():
    print(f"{vertex} -> {adj_list[vertex]}")
