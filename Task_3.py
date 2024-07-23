import heapq

import networkx as nx
import matplotlib.pyplot as plt

# Створення вагового графа
G = nx.Graph()
G.add_edge("Порту", "Ліссабон", weight=332)
G.add_edge("Ліссабон", "Мадрид", weight=630)
G.add_edge("Мадрид", "Барселона", weight=627)
G.add_edge("Мадрид", "Валенсія", weight=360)
G.add_edge("Барселона", "Валенсія", weight=348)
G.add_edge("Мадрид", "Париж", weight=1276)
G.add_edge("Париж", "Марсель", weight=778)
G.add_edge("Париж", "Брюссель", weight=306)
G.add_edge("Брюссель", "Амстердам", weight=210)
G.add_edge("Амстердам", "Берлін", weight=665)
G.add_edge("Берлін", "Париж", weight=1049)
G.add_edge("Відень", "Париж", weight=1238)
G.add_edge("Відень", "Берлін", weight=685)






# Реалізація алгоритму Дейкстри (є в матеріалах з поясненнями)
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]
    while pq:
        print("pq: ", pq)
        print("sp:", shortest_paths)
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths


# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "Порту")
print(shortest_paths)
# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()