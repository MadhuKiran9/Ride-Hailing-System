"""
Week 3 Deliverable — A* on a Real City Road Network
=====================================================
Implement A* using Haversine as the heuristic on an OSMnx road graph.
Then compare it against Dijkstra to measure how many fewer nodes it explores.

Rules:
  - Implement haversine() yourself (no geopy, no haversine library)
  - Implement astar() yourself (no nx.astar_path, no ox.shortest_path)
  - You MAY use: osmnx, heapq, math, matplotlib or folium for visualisation

Your implementation must:
  1. Download the road graph for your chosen city (from starter/points.py)
  2. Snap origin and destination lat/lng to the nearest graph nodes
  3. Run A* and return the path + total distance + nodes explored count
  4. Run your Week 2 Dijkstra on the same query (adapted for OSMnx graph)
  5. Print a comparison table
  6. Visualise the A* route on a map and save it
"""

import heapq
import math
import os
import sys

import osmnx as ox

sys.path.insert(0, "../starter")
from points import ORIGIN_LAT, ORIGIN_LNG, DEST_LAT, DEST_LNG, LABEL

os.makedirs("output", exist_ok=True)


# ── Haversine heuristic ───────────────────────────────────────────────────────

def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Return the great-circle distance in metres between two lat/lng points.
    Implement this from scratch using the formula in resources/haversine-explainer.md
    Do NOT use any library for this.
    """
    # --- your code here ---
    phi1, phi2 = math.radians(lat2), math.radians(lat1)
    del1 = phi1 - phi2
    del2 = math.radians(lon2 - lon1)
    R = 6_371_000 

    a = math.sin(del1 / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(del2 / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c
    pass


# ── A* implementation ─────────────────────────────────────────────────────────

def astar(G, origin_node: int, dest_node: int) -> tuple[list, float, int]:
    """
    Run A* on the OSMnx graph G from origin_node to dest_node.
    Use haversine() as the heuristic (straight-line distance to destination).

    Args:
        G:            OSMnx MultiDiGraph
        origin_node:  integer node ID (from ox.nearest_nodes)
        dest_node:    integer node ID

    Returns:
        path:          list of node IDs from origin to destination
        distance:      total path length in metres
        nodes_explored: how many nodes were popped from the heap

    Hints:
        - G.nodes[n]['y'] = latitude of node n
        - G.nodes[n]['x'] = longitude of node n
        - Edge weight: min(d['length'] for d in G[u][v].values())
        - Priority = g(n) + h(n)  where h = haversine(node, dest)
        - Track a `previous` dict to reconstruct the path
        - Track `nodes_explored` by incrementing each time you pop from the heap
          and process a node (i.e. not already visited)
    """
    dest_lat = G.nodes[dest_node]['y']
    dest_lon = G.nodes[dest_node]['x']
    INF = float('inf')
    # --- your code here ---
    g_distances = {}
    previous = {}
    visited = set()
    heap = []
    nodes_explored = 0

    for node in G.nodes:
        g_distances[node] = INF
    g_distances[origin_node] = 0

    h_origin = haversine(G.nodes[origin_node]['y'], G.nodes[origin_node]['x'], G.nodes[dest_node]['y'], G.nodes[dest_node]['x'])

    heapq.heappush(heap, (h_origin, origin_node))

    while heap:
        current_f, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue
        visited.add(current_node)
        nodes_explored += 1
        
        if current_node == dest_node:
            break
        
        for neighbour_node in G.neighbors(current_node):
            weight = min(d['length'] for d in G[current_node][neighbour_node].values())
            if g_distances[current_node] + weight < g_distances[neighbour_node]:
                h_neighbour = haversine(G.nodes[neighbour_node]['y'], G.nodes[neighbour_node]['x'], G.nodes[dest_node]['y'], G.nodes[dest_node]['x'])
                g_distances[neighbour_node] = g_distances[current_node] + weight
                heapq.heappush(heap, (h_neighbour + g_distances[neighbour_node], neighbour_node))
                previous[neighbour_node] = current_node
        
    distance = g_distances[dest_node]

    path = []

    if dest_node == origin_node:
        path = [origin_node]
    elif dest_node in visited:
        temp = dest_node
        while True:
            path.append(temp)

            if temp == origin_node:
                break
            
            temp = previous[temp]
        path.reverse()
    else:
        path = []


    return path, distance, nodes_explored


# ── Dijkstra (for comparison) ─────────────────────────────────────────────────

def dijkstra(G, origin_node: int, dest_node: int) -> tuple[list, float, int]:
    """
    Run Dijkstra on the same OSMnx graph.
    Same interface as astar() — returns (path, distance, nodes_explored).

    This is the same algorithm as Week 2 but adapted for:
      - OSMnx MultiDiGraph instead of a plain adjacency list
      - Stopping early when dest_node is reached (no need to explore the whole graph)
    """
    # --- your code here ---
    distances = {}
    previous = {}
    nodes_explored = 0

    # --- your code here ---
    INF = float("inf")

    for node in G.nodes:
        distances[node] = INF
    distances[origin_node] = 0
    
    heap = []
    heapq.heappush(heap, (0, origin_node))
    
    visited = set()

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue
        visited.add(current_node)
        nodes_explored += 1
        if current_node == dest_node:
            break
        
        for neighbour in G.neighbors(current_node):
            weight = min(d['length'] for d in G[current_node][neighbour].values())
            if current_dist + weight < distances[neighbour]:
                distances[neighbour] = current_dist + weight
                previous[neighbour] = current_node
                heapq.heappush(heap, (distances[neighbour], neighbour))
            
    distance = distances[dest_node]        

    path = []

    if dest_node == origin_node:
        path = [origin_node]
    elif dest_node in visited:
        temp = dest_node
        while True:
            path.append(temp)

            if temp == origin_node:
                break
            
            temp = previous[temp]
        path.reverse()
    else:
        path = []

    

    return path, distance, nodes_explored


# ── Visualisation ─────────────────────────────────────────────────────────────

def visualise_route(G, path: list, filename: str = "output/route_map.html"):
    """
    Plot the route on an interactive map using folium and save as HTML.
    If folium is not installed, fall back to a static matplotlib plot.

    Hint for folium:
        import folium
        m = folium.Map(location=[origin_lat, origin_lng], zoom_start=14)
        folium.PolyLine([(G.nodes[n]['y'], G.nodes[n]['x']) for n in path]).add_to(m)
        m.save(filename)
    """
    try:
        import folium
        m = folium.Map(
            location=[G.nodes[path[0]]['y'], G.nodes[path[0]]['x']],
            zoom_start=14
        )
        folium.PolyLine(
            [(G.nodes[n]['y'], G.nodes[n]['x']) for n in path]
        ).add_to(m)
        m.save(filename)
        print(f"Interactive map saved to: {filename}")
    except ImportError:
        # fallback: matplotlib static plot
        fig, ax = ox.plot_graph_route(G, path, route_linewidth=3, node_size=0, show=False)
        png_path = filename.replace(".html", ".png")
        fig.savefig(png_path, dpi=150, bbox_inches="tight")
        print(f"Static map saved to: {png_path}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print(f"Route: {LABEL}")
    print(f"  Origin:      ({ORIGIN_LAT}, {ORIGIN_LNG})")
    print(f"  Destination: ({DEST_LAT}, {DEST_LNG})\n")

    # 1. Download road network
    print("Loading road network (cached after first run)...")
    G = ox.graph_from_place("Ongole, Andhra Pradesh, India", network_type="drive")
    print(f"Graph: {G.number_of_nodes():,} nodes, {G.number_of_edges():,} edges\n")

    # 2. Snap coordinates to nearest graph nodes
    origin_node = ox.nearest_nodes(G, X=ORIGIN_LNG, Y=ORIGIN_LAT)
    dest_node   = ox.nearest_nodes(G, X=DEST_LNG,   Y=DEST_LAT)

    # 3. Run A*
    astar_path, astar_dist, astar_explored = astar(G, origin_node, dest_node)

    # 4. Run Dijkstra
    dijkstra_path, dijkstra_dist, dijkstra_explored = dijkstra(G, origin_node, dest_node)

    # 5. Print comparison
    print(f"{'Algorithm':<12} {'Nodes explored':>16} {'Distance':>12}")
    print("-" * 42)
    print(f"{'A*':<12} {astar_explored:>16,} {astar_dist/1000:>11.2f} km")
    print(f"{'Dijkstra':<12} {dijkstra_explored:>16,} {dijkstra_dist/1000:>11.2f} km")

    if dijkstra_explored > 0:
        saving = (1 - astar_explored / dijkstra_explored) * 100
        print(f"\nA* explored {saving:.0f}% fewer nodes for the same result.")

    # 6. Visualise
    if astar_path:
        visualise_route(G, astar_path)


if __name__ == "__main__":
    main()
