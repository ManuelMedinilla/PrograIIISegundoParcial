class NodoArboles(object):  # Definición de la clase NodoArboles
    def __init__(self, x):  # Inicialización del método __init__
        self.val = x  # Asignación del valor x al atributo val
        self.izquierda = None  # Asignación de None al atributo izquierda
        self.derecha = None  # Asignación de None al atributo derecha

def ordenamiento_de_arrays_a_bst(nums):  # Definición de la función ordenamiento_de_arrays_a_bst
    # Devuelve la raíz de un árbol binario utilizando la recursividad dividiendo la matriz por la mitad en cada llamada
    # eligiendo el elemento en la mitad como nodo actual.
    if not nums:  # Comprobación si la lista de números está vacía
        return None  # Retorno None si la lista de números está vacía
    mid_val = len(nums) // 2  # Cálculo del índice medio de la lista de números
    node = NodoArboles(nums[mid_val])  # Creación del nodo con el valor medio de la lista de números
    node.izquierda = ordenamiento_de_arrays_a_bst(nums[:mid_val])  # Creación del subárbol izquierdo
    node.derecha = ordenamiento_de_arrays_a_bst(nums[mid_val + 1:])  # Creación del subárbol derecho
    return node  # Retorno del nodo

def preOrder(node):  # Definición de la función preOrder
    # El recorrido preorden sigue el orden de raíz, izquierda, derecha.
    if not node:  # Comprobación si el nodo es None
        return  # Retorno si el nodo es None
    print(node.val)  # Impresión del valor del nodo
    preOrder(node.izquierda)  # Recorrido preorden del subárbol izquierdo
    preOrder(node.derecha)  # Recorrido preorden del subárbol derecho

arrays_nums = [1, 2, 3, 4, 5, 6, 7]  # Lista de números original
print("Array original:")  
print(arrays_nums)  # Impresión de la lista de números original
result = ordenamiento_de_arrays_a_bst(arrays_nums)  # Llamada a la función para convertir la lista en un árbol balanceado
print("\nArray a árbol balanceado:")
preOrder(result)  # Impresión del árbol en preorden
