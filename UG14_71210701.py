class Graph:
    def _init_(self):
        self.data = {}

    def addVertex(self, key):
        if key not in self.data:
            self.data[key] = set()

    def vertex(self):
        print("\nSeluruh Node = ", end="")
        for key in self.data:
            print(key, end=" ")
        print()

    def edge(self):
        print("Seluruh Edge = ", end="")
        v = set()
        for vex in self.data:
            for neighbor in self.data[vex]:
                if (neighbor, vex) not in v:
                    print(f"({v}, {neighbor})", end=" ")
                    v.add((v, neighbor))
        print()

    def addEdge(self, x, y):
        if x in self.data and y in self.data:
            self.data[x].add(y)
            self.data[y].add(x)

    def bfs(self, node):
        v = set()
        queue = [node]
        print("Hasil BFS Traversal:")
        while queue:
            vertex = queue.pop(0)
            if vertex not in v:
                print(vertex, end=" ")
                v.add(vertex)
                for n in self.data[vertex]:
                    if n not in v:
                        queue.append(n)
        print("\n")

# Membuat graf sesuai dengan gambar yang diberikan
graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')

graph.addEdge('c', 'e')
graph.addEdge('b', 'c')
graph.addEdge('d', 'e')
graph.addEdge('b', 'd')
graph.addEdge('c', 'g')
graph.addEdge('e', 'f')
graph.addEdge('a', 'b')

# Menampilkan vertex dan edge dari graf
graph.vertex()
graph.edge()

# Melakukan BFS traversal dari node 'a'
graph.bfs('a')