import osmnx as ox
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from typing import List, Tuple, Dict
import math
import heapq
import networkx as nx
import time


def haversine(coord1: Tuple[float, float], coord2: Tuple[float, float]) -> float:
    """
    Вычисляет расстояние по хаверсинусу в км.
    """
    lon1, lat1 = coord1
    lon2, lat2 = coord2
    R = 6371
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlambda/2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def dijkstra(graph: nx.Graph,
              start: int,
              end: int) -> Tuple[List[int], float, List[str]]:
    """
    Поиск кратчайшего пути с помощью алгоритма Дейкстры с информацией о названиях ребер.
    """
    priority_queue = [(0, start, [start], [])]
    visited = set()

    while priority_queue:
        dist, current, path, streets = heapq.heappop(priority_queue)
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            return path, dist, streets

        for nx_next, attr in graph[current].items():
            if nx_next in visited:
                continue

            weight = attr[0].get("length", 1)
            new_dist = dist + weight
            new_path = path + [nx_next]
            new_streets = streets.copy()

            name = attr[0].get("name", "без названия")
            new_streets.append(name)

            heapq.heappush(priority_queue, (new_dist, nx_next, new_path, new_streets.copy()))


def visualize_path_with_network(G, path, streets=None, figsize=(20, 20)):
    """
    Визуализация графа с выделенной траекторией.
    """
    plt.figure(figsize=figsize)
    ax = plt.gca()

    edges = G.edges()
    lines = []
    for u, v in edges:
        lines.append(((G.nodes[u]['x'], G.nodes[u]['y']),
                       (G.nodes[v]['x'], G.nodes[v]['y'])))

    lc = LineCollection(lines, colors='grey', linewidths=0.5)
    ax.add_collection(lc)

    if path and len(path) > 1:
        path_lines = []
        for u, v in zip(path, path[1:]):
            path_lines.append(((G.nodes[u]['x'], G.nodes[u]['y']),
                                (G.nodes[v]['x'], G.nodes[v]['y'])))

        lc_path = LineCollection(path_lines, colors='red', linewidths=2)
        ax.add_collection(lc_path)

        if streets:
            for i in range(len(path) - 1):
                mid = (
                    (G.nodes[path[i]]['x'] + G.nodes[path[i+1]]['x'])/2,
                    (G.nodes[path[i]]['y'] + G.nodes[path[i+1]]['y'])/2,
                )
                if i < len(streets) and streets[i]:
                    plt.text(mid[0], mid[1], streets[i],
                             color='blue', ha='center', fontsize=8)

    ax.autoscale()
    plt.axis('equal')
    plt.title("Кратчайший маршрут")
    plt.xlabel("Долгота")
    plt.ylabel("Широта")
    plt.grid(False)
    plt.tight_layout()
    plt.show()


def main():
    print("Загрузка графа...")
    G = ox.load_graphml("Zagreb_road_network.graphml")

    print(f"Вершин графа: {len(G.nodes())}") 

    print(f"Pебер графа: {len(G.edges(data=True))}") 

    # Координаты старта и финиша
    start = ox.geocode("Илица улица, Загреб, Хорватия")
    end = ox.geocode("улица Савска, Загреб, Хорватия")

    start_node = ox.nearest_nodes(G, start[1], start[0])  
    end_node = ox.nearest_nodes(G, end[1], end[0])

    print(f"Начальная вершина: {start_node}")
    print(f"Конечная вершина: {end_node}")
    before = time.time()
    path, distance, streets = dijkstra(G, start_node, end_node)
    print("Время выполнения алгоритма:", time.time() - before, "секунд")
    if not path:
        print("Маршрут не найден")
    else:
        print(f"Найден путь длиной {distance/1000:.2f} км")
        print("Улицы на пути:")
        for s in streets:
            print(s)
        visualize_path_with_network(G, path, streets)


if __name__ == "__main__":
    main()