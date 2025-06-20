# Clase del nodo
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent_pointer: Node # Piensa que esto apunta al padre
    
    def __str__(self) -> str:
        return f"({self.data})"

# Clase del arbol
class Tree:
    def __init__(self, root: Node):
        self.root = root

    def insert_at(self, child: Node, new_node):
        new_node.parent_pointer = child
        child.children.append(new_node)

# Imprime el propio nodo dado, el padre (si es que tiene) y los hijos
def print_parent_and_child(node: Node):
    cstr = ""
    for c in node.children:
        cstr += " " + str(c) + " "

    try:
        print(f"{str(node.parent_pointer)} -> {str(node)} -> [{str(cstr)}]")
        
    except AttributeError:
        print(f"{str(node)} -> [{str(cstr)}]")

# Itera desde la raiz de forma iterativa y retorna una lista con los nodos del arbol
def iterate_from_root(root: Node):
    if root == None:
        return

    stack = [root]
    output = []

    while stack:
        current_node = stack.pop()
        output.append(current_node.data)
        for c in reversed(current_node.children):
            stack.append(c)
    
    return output

# Campo de pruebas
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

tree = Tree(root=n1)

tree.insert_at(n1, n2)
tree.insert_at(n2, n3)

tree.insert_at(n1, n4)
tree.insert_at(n4, n5)

print_parent_and_child(n1)
print_parent_and_child(n2)
print_parent_and_child(n3)
print_parent_and_child(n4)
print_parent_and_child(n5)

print(iterate_from_root(tree.root))