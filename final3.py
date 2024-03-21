import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def dijkstra(self, start_vertex):
        distances = [float('inf')] * self.vertices
        distances[start_vertex] = 0
        pq = [(0, start_vertex)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 1, 4)
g.add_edge(2, 3, 8)
g.add_edge(2, 4, 2)
g.add_edge(3, 4, 7)
g.add_edge(4, 3, 9)
print(g.dijkstra(0))