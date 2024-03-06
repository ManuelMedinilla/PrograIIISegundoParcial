class NodoArboles(object):  # Definición de la clase NodoArboles
    def __init__(self, x):  # Inicialización del método __init__
        self.val = x  # Asignación del valor x al atributo val
        self.izquierda = None  # Asignación de None al atributo izquierda
        self.derecha = None  # Asignación de None al atributo derecha

def valor_mas_cercano(root, target):  # Definición de la función valor_mas_cercano
    # root: es el nodo raíz del árbol, target: el valor para el cual se quiere encontrar el valor más cercano.
    if not root:  # Comprobación si el nodo raíz es None
        return float('inf')  # Retorno de infinito si el nodo raíz es None
    
    a = root.val  # Almacenamiento del valor del nodo raíz
    kid = root.izquierda if target < a else root.derecha  # Elección del hijo a explorar
    
    if not kid:  # Comprobación si el hijo es None
        return a  # Retorno del valor del nodo raíz
    
    b = valor_mas_cercano(kid, target)  # Llamada recursiva para obtener el valor más cercano en el subárbol
    return min((a, b), key=lambda x: abs(target - x))  # Retorno del valor más cercano entre el nodo actual y el valor obtenido del subárbol

root = NodoArboles(8)  # Creación del nodo raíz con valor 8
root.izquierda = NodoArboles(5)  # Creación del hijo izquierdo con valor 5
root.derecha = NodoArboles(14)  # Creación del hijo derecho con valor 14
root.izquierda.izquierda = NodoArboles(4)  # Creación del nieto izquierdo con valor 4
root.izquierda.derecha = NodoArboles(6)  # Creación del nieto derecho con valor 6
root.izquierda.derecha.izquierda = NodoArboles(7)  # Creación del bisnieto izquierdo con valor 7
root.derecha.derecha = NodoArboles(24)  # Creación del nieto derecho con valor 24
root.derecha.derecha.izquierda = NodoArboles(22)  # Creación del bisnieto izquierdo con valor 22

result = valor_mas_cercano(root, 19)  # Llamada a la función para encontrar el valor más cercano a 19
print(result)  # Impresión del resultado
