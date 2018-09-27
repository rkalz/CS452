import heapq
import sys


class GraphNode:
    def __init__(self, node_id):
        self.id = node_id
        self.children = dict()
        self.parent = None
        self.cost = None

    def __repr__(self):
        return str(self.id)

    # lt and eq needed for heapqueue
    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost


class Graph:
    def __init__(self):
        self.nodes = dict()

    def add(self, id):
        node = GraphNode(id)
        self.nodes[id] = node

    def connect(self, id_a, id_b, dist):
        if id_a in self.nodes and id_b in self.nodes:
            a = self.nodes[id_a]
            b = self.nodes[id_b]
            a.children[dist] = b

    def shortest_path(self, id_a, id_b):
        if id_a not in self.nodes or id_b not in self.nodes:
            return None

        if id_a == id_b:
            return [id_a]

        origin = self.nodes[id_a]
        origin.cost = 0

        queue = []

        for _, node in self.nodes.items():               # O(|V| log |V|)
            if node is not origin:
                node.parent = None
                node.cost = sys.maxsize
            heapq.heappush(queue, node)

        while len(queue) != 0:
            parent = heapq.heappop(queue)
            for dist, child in parent.children.items():  # O(|E|)
                new_dist = parent.cost + dist
                if new_dist < child.cost:
                    child.cost = new_dist
                    child.parent = parent.id

                    # Reorder heap based on new values
                    heapq.heapify(queue)                 # THIS IS O(|V|) UGH, USE FIBONACCI HEAP FOR O(1)

        path = []
        node_id = id_b
        if self.nodes[node_id].parent is None:
            # No path exists
            return None

        while node_id is not None:
            path.insert(0, node_id)
            node_id = self.nodes[node_id].parent

        return path


if __name__ == "__main__":
    graph = Graph()
    graph.add('A')
    graph.add('B')
    graph.add('C')
    graph.add('D')
    graph.add('E')

    graph.connect('A', 'B', 5)
    graph.connect('A', 'C', 7)
    graph.connect('B', 'C', 3)
    graph.connect('A', 'D', 12)
    graph.connect('B', 'D', 6)
    graph.connect('B', 'E', 13)
    graph.connect('C', 'D', 4)
    graph.connect('D', 'E', 10)
    graph.connect('C', 'E', 19)

    print(graph.shortest_path('A', 'E'))





