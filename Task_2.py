import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()


# Додавання ребер (зв'язків між людьми)
G.add_edges_from([("Порту", "Ліссабон"),("Ліссабон", "Мадрид"), ("Мадрид", "Барселона"), ("Барселона", "Валенсія"),
                  ("Мадрид", "Валенсія"), ("Мадрид", "Париж"), ("Париж", "Марсель"), ("Париж", "Брюсель"), 
                  ("Брюсель", "Амстердам"), ("Амстердам", "Берлін"), ("Берлін", "Париж"),("Париж","Відень"),("Відень", "Берлін")])




# DFC через рекурсію (можна зробити й через stack)
def dfs(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(f"\n DFC: visited {vertex}", end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex])) 
graph = {
    "Порту": ['Ліссабон'],
    'Ліссабон': ['Порту','Мадрид'],
    'Мадрид': ['Валенсія', 'Барселона', 'Париж'],
    'Барселона': ['Мадрид', 'Валенсія'],
    'Валенсія': ['Барселона', 'Мадрид'],
    'Париж': ['Мадрид', 'Відень','Брюссель','Берлін', 'Марсель'],
    'Марсель':['Париж'],
    'Брюссель':['Париж', 'Амстердам'],
    'Амстердам':['Брюссель', 'Берлін'],
    'Берлін':['Париж', 'Амстердам', 'Відень'],
    'Відень':['Берлін', 'Париж']
}

# BFS через queue
def bfs(graph, start):
    visited, queue = {start}, [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        print(f"\nBFC: visited {vertex}")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append((vertex, neighbour))
    # Помилка в тому що повертаємо можливо?
    return visited

nx.draw(G, with_labels=True)
plt.show()

# Виконання DFS та BFS
dfs_path = dfs(graph,"Порту")
bfs_path = bfs(G, "Порту")

# print(f"DFS path: {dfs_path}")

# print(f"BFS path: {bfs_path}")

# Візуалізація графа
# nx.draw(G, with_labels=True)
# plt.show()

# dfs_path = list(nx.dfs_edges(G, source="Марсель"))
# bfs_path = list(nx.bfs_edges(G, source="Відень"))

# print(f"DFS path: {dfs_path}")
# print(f"BFS path: {bfs_path}")
