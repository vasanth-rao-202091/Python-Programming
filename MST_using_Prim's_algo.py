from heapq import heapify, heappush, heappop

class Graph:
       def __init__(self):                         #use of constructor
        self.adjacency_list = {}

       def add_edge(self, v1, v2, w=1):            # method to add edges
        if v1 in self.adjacency_list:
            self.adjacency_list[v1].append((v2, w))
        else:
            self.adjacency_list[v1] = [(v2, w)]

        if v2 in self.adjacency_list:
            self.adjacency_list[v2].append((v1, w))
        else:
            self.adjacency_list[v2] = [(v1, w)]
       def display(self):                          # method to display the adjacency list
        for vertex in self.adjacency_list.keys():
            print(f"{vertex} -> {self.adjacency_list[vertex]}")


if __name__ == "__main__":

    v = int(input("Enter the Number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    
    print("\nStart entering edges (s,d,w): ")
    edges = [list(map(int, input().split(" "))) for i in range(num_edges)]
    s = int(input("\nEnter starting node of the graph: "))
  
    g = Graph()                                  # Graph Object
    
    for edge in edges:
        v1, v2, w = edge
        g.add_edge(v1, v2, w)

    minheap = []
    
    result = []
    n = len(g.adjacency_list.keys())
    
    visited = {s}
    
    for nxt in g.adjacency_list[s]:
        heappush(minheap,(nxt[1],s,nxt[0]))      #(w,s,d)
    
    while (len(minheap) != 0 and len(result) < n-1):
        cur_node = heappop(minheap)
        s = cur_node[2]
        if s in visited:
            continue
        result.append(cur_node)
        for nxt in g.adjacency_list[s]:
            d = nxt[0]
            w = nxt[1]
            if d not in visited:
                heappush(minheap,(w,s,d))
        visited.add(s)
    print("The Edges present in MST: ")
    print(result)
