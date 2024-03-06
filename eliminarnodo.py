class NodoArboles(object):  # Definición de la clase NodoArboles
    def __init__(self, x):  # Inicialización del método __init__
        self.val = x  # Asignación del valor x al atributo val
        self.izquierda = None  # Asignación de None al atributo izquierda
        self.derecha = None  # Asignación de None al atributo derecha

def borrar_nodo(root, key):  # Definición de la función borrar_nodo
    if not root:  # Comprobación si el nodo es None
        return root  # Retorno del nodo si es None

    if root.val > key:  # Comprobación si el valor del nodo es mayor que la clave
        root.izquierda = borrar_nodo(root.izquierda, key)  # Recursión en el subárbol izquierdo
    
    elif root.val < key:  # Comprobación si el valor del nodo es menor que la clave
        root.derecha = borrar_nodo(root.derecha, key)  # Recursión en el subárbol derecho
    
    else:  # Si el valor del nodo es igual a la clave
        if not root.derecha:  # Comprobación si el hijo derecho es None
            return root.izquierda  # Retorno del hijo izquierdo como nueva raíz
        elif not root.izquierda:  # Comprobación si el hijo izquierdo es None
            return root.derecha  # Retorno del hijo derecho como nueva raíz
        else:  # Si hay hijos izquierdo y derecho en el nodo
            temp_val = encontrar_minimo(root.derecha)  # Encuentra el valor mínimo en el subárbol derecho
            root.val = temp_val.val  # Reemplaza el valor del nodo con el valor mínimo encontrado
            root.derecha = borrar_nodo(root.derecha, temp_val.val)  # Elimina el nodo mínimo en el subárbol derecho

    return root  # Retorno del nodo

def encontrar_minimo(node):  # Definición de la función encontrar_minimo
    while node.izquierda:  # Bucle para encontrar el nodo mínimo
        node = node.izquierda  # Avance al nodo izquierdo
    return node  # Retorno del nodo mínimo

def preOrder(node):  # Definición de la función preOrder
    if not node:  # Comprobación si el nodo es None
        return  # Retorno si el nodo es None
    print(node.val)  # Impresión del valor del nodo
    preOrder(node.izquierda)  # Recorrido preorden del subárbol izquierdo
    preOrder(node.derecha)  # Recorrido preorden del subárbol derecho

root = NodoArboles(5)  # Creación del nodo raíz con valor 5
root.izquierda = NodoArboles(3)  # Creación del hijo izquierdo con valor 3
root.derecha = NodoArboles(6)  # Creación del hijo derecho con valor 6
root.izquierda.izquierda = NodoArboles(2)  # Creación del nieto izquierdo con valor 2
root.izquierda.derecha = NodoArboles(4)  # Creación del nieto derecho con valor 4
root.izquierda.derecha.izquierda= NodoArboles(7)  # Creación del bisnieto izquierdo con valor 7

print("Nodo original:")
preOrder(root)  # Impresión del árbol original en preorden
result = borrar_nodo(root, 4)  # Llamada a la función para eliminar el nodo con valor 4
print("Después de borrar el nodo con valor 4:")
preOrder(result)  # Impresión del árbol después de eliminar el nodo con valor 4 en preorden
