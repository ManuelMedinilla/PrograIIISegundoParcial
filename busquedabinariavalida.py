class NodoArboles(object):  # Definición de la clase NodoArboles
    def __init__(self, x):  # Inicialización del método __init__
        self.val = x  # Asignación del valor x al atributo val
        self.izquierda = None  # Asignación de None al atributo izquierda
        self.derecha = None  # Asignación de None al atributo derecha

def is_BST(root):  # Definición de la función is_BST
    # Utiliza un enfoque de recorrido inorden utilizando una pila.
    stack = []  # Creación de una pila vacía
    prev = None  # Inicialización del nodo previo como None

    while root or stack:  # Bucle principal mientras el nodo actual o la pila no estén vacíos
        while root:  # Bucle para recorrer todos los nodos izquierdos
            stack.append(root)  # Se añade el nodo actual a la pila
            root = root.izquierda  # Se avanza al nodo izquierdo
        root = stack.pop()  # Se obtiene el último nodo agregado a la pila
        if prev and root.val <= prev.val:  # Comprobación de si el árbol es un BST válido
            return False  # Si el árbol no es un BST válido, se devuelve False
        prev = root  # Actualización del nodo previo
        root = root.derecha  # Avance al nodo derecho

    return True  # Si el árbol es un BST válido, se devuelve True

root = NodoArboles(2)  # Creación del nodo raíz con valor 2
root.izquierda = NodoArboles(1)  # Creación del hijo izquierdo con valor 1
root.derecha = NodoArboles(3)  # Creación del hijo derecho con valor 3

result = is_BST(root)  # Llamada a la función para verificar si el árbol es un BST válido
print(result)  # Impresión del resultado

root = NodoArboles(1)  # Creación del nodo raíz con valor 1
root.izquierda = NodoArboles(2)  # Creación del hijo izquierdo con valor 2
root.derecha = NodoArboles(3)  # Creación del hijo derecho con valor 3

result = is_BST(root)  # Llamada a la función para verificar si el árbol es un BST válido
print(result)  # Impresión del resultado
