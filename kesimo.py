class NodoArboles(object):  # Definición de la clase NodoArboles
    def __init__(self, x):  # Inicialización del método __init__
        self.val = x  # Asignación del valor x al atributo val
        self.izquierda = None  # Asignación de None al atributo izquierda
        self.derecha = None  # Asignación de None al atributo derecha

def kth_smallest(root, k):  # Definición de la función kth_smallest
    stack = []  # Inicialización de una pila
    while root or stack:  # Bucle mientras el nodo raíz o la pila no estén vacíos
        while root:  # Bucle para recorrer todos los nodos izquierdos
            stack.append(root)  # Se añade el nodo actual a la pila
            root = root.izquierda  # Se avanza al nodo izquierdo
        root = stack.pop()  # Se obtiene el último nodo agregado a la pila
        k -= 1  # Se reduce en 1 el valor de k
        if k == 0:  # Comprobación si k es igual a 0
            return root.val  # Si k es igual a 0, se devuelve el valor del nodo actual
        root = root.derecha  # Se avanza al nodo derecho

root = NodoArboles(8)  # Creación del nodo raíz con valor 8
root.izquierda = NodoArboles(5)  # Creación del hijo izquierdo con valor 5
root.derecha = NodoArboles(14)  # Creación del hijo derecho con valor 14
root.izquierda.izquierda = NodoArboles(4)  # Creación del nieto izquierdo con valor 4
root.izquierda.derecha = NodoArboles(6)  # Creación del nieto derecho con valor 6
root.izquierda.derecha.izquierda = NodoArboles(8)  # Creación del bisnieto izquierdo con valor 8
root.izquierda.derecha.derecha = NodoArboles(7)  # Creación del bisnieto derecho con valor 7
root.derecha.derecha = NodoArboles(24)  # Creación del nieto derecho con valor 24
root.derecha.derecha.izquierda = NodoArboles(22)  # Creación del bisnieto izquierdo con valor 22

print(kth_smallest(root, 2))  # Impresión del segundo elemento más pequeño
print(kth_smallest(root, 3))  # Impresión del tercer elemento más pequeño
