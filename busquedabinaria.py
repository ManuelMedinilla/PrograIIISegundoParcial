#escriba un programa de python para crear un arbol de busqueda binaria utilizando elementos de una matriz (dados)
# donde los elementos de una matriz se orden en orden acendene

class nodosarbol(object):  # Definición de la clase nodosarbol
    def __init__(self, x):  # Inicialización del método __init__
        self.val = x  # Asignación del valor x al atributo val
        self.izquierda = None  # Asignación de None al atributo izquierda
        self.derecha = None  # Asignación de None al atributo derecha

def ordenamiento_de_arrays_a_bst(nums):  # Definición de la función ordenamiento_de_arrays_a_bst
    if not nums:  # Comprobación si nums está vacío
        return None  # Retorno None si nums está vacío
    mid_val = len(nums) // 2  # Cálculo del índice medio de nums
    node = nodosarbol(nums[mid_val])  # Creación de un nodo con el valor medio de nums
    node.izquierda = ordenamiento_de_arrays_a_bst(nums[:mid_val])  # Creación del subárbol izquierdo
    node.derecha = ordenamiento_de_arrays_a_bst(nums[mid_val + 1:])  # Creación del subárbol derecho
    return node  # Retorno del nodo

def preOrder(node):  # Definición de la función preOrder
    if not node:  # Comprobación si el nodo es None
        return  # Retorno si el nodo es None
    print(node.val)  # Impresión del valor del nodo
    preOrder(node.izquierda)  # Recorrido preorden del subárbol izquierdo
    preOrder(node.derecha)  # Recorrido preorden del subárbol derecho

result = ordenamiento_de_arrays_a_bst([1, 2, 3, 4, 5, 6, 7])  # Llamada a la función para generar el árbol
preOrder(result)  # Llamada a la función para recorrer el árbol en preorden
