from collections import deque
from tree import Node, Tree

def get_length(root: Node):
    # verificar si la raiz es nula
    if root == None: return

    # longitud
    length = -1
    # cola usada para contar los hijso
    dq = deque([root])

    while dq:
        # obtener longitud de la cola
        q_size = len(dq)
        # incrementar la variabled de longitud por cada iteracion
        length += 1
        for i in range(q_size):
            # obtener el nodo actual
            current_node = dq.popleft()
            #recorrer los ojos del nodo actual
            for c in current_node.children:
                dq.append(c)
    return length

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
t = Tree(root=n1)

# Insertar Nodos
t.insert_at(n1, n2)
t.insert_at(n2, n3)
t.insert_at(n1, n4)
t.insert_at(n4, n5)

print(f"La longitud del arbol es de: {get_length(t.root)}")
