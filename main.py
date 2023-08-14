import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree():
    x = TreeNode('X')
    y = TreeNode('Y')
    z = TreeNode('Z')
    a = TreeNode('A') 
    b = TreeNode('B')
    c = TreeNode('C')
    d = TreeNode('D')

    x.children = [y, z]
    y.children = [a, b]
    b.children = [c, d]

    return x

def bfs_shortest_path(root, start_value, target_value):
    queue = deque([(root, [])])

    while queue:
        node, path = queue.popleft()
        path = path + [node.value]

        if node.value == target_value:
            return path

        for child in node.children:
            queue.append((child, path))

    return None

def visualize_tree(root):
    G = nx.Graph()
    
    def add_edges(node):
        for child in node.children:
            G.add_edge(node.value, child.value)
            add_edges(child)
    
    add_edges(root)
    
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=2000, font_size=10, font_color='black', font_weight='bold')
    plt.show()

def main():
    root = build_tree()

    start_value = input("Enter start node value: ")
    target_value = input("Enter target node value: ")
    shortest_path = bfs_shortest_path(root, start_value, target_value)
  

    if shortest_path:
        print("Shortest path:", shortest_path)
        visualize_tree(root)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
