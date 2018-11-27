class Node:
    def __init__(self, key):
        self.key = key
        self.children = set()

    def __repr__(self):
        return str(self.key)

    def add_child(self, node):
        self.children.add(node)


def dfs(node, visited):
    if node in visited:
        return False
    visited.add(node)

    for child in node.children:
        if not dfs(child, visited):
            return False

    visited.remove(node)
    return True


def is_possible(list_of_classes):
    nodes = dict()

    for course, req in list_of_classes:
        if course not in nodes:
            nodes[course] = Node(course)
        if req not in nodes:
            nodes[req] = Node(req)

        course = nodes[course]
        req = nodes[req]

        course.add_child(req)

    for node in nodes.values():
        if not dfs(node, set()):
            return False

    return True


if __name__ == "__main__":
    # is_possible should only return false if we have cyclic dependencies
    # Union Find is the best way to find cycles in a directed graph
    print(is_possible([[0,1],[0,2],[1,2]]))