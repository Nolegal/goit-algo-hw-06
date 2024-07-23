import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (людей)
G.add_nodes_from(["Порту", "Мадрид", "Барселона", "Валенсія", "Париж", "Марсель", "Брюсель", "Амстердам", "Берлін","Відень"])

# Додавання ребер (зв'язків між людьми)
G.add_edges_from([("Порту", "Мадрид"), ("Мадрид", "Барселона"), ("Барселона", "Валенсія"),
                  ("Мадрид", "Валенсія"), ("Мадрид", "Париж"), ("Париж", "Марсель"), ("Париж", "Брюсель"), 
                  ("Брюсель", "Амстердам"), ("Амстердам", "Берлін"), ("Берлін", "Париж"),("Париж","Відень"),("Відень", "Берлін")])


# Візуалізація графа
nx.draw(G, with_labels=True)
plt.show()

# Кількість вершин
num_nodes = G.number_of_nodes()

# Кількість ребер
num_edges = G.number_of_edges()

degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
# Вивести ступені вершин

print(f"Ступінь центральності: {degree_centrality}")
print(f"Близькість вузла: {closeness_centrality}")
print(f"Посередництво вузла: {betweenness_centrality}")