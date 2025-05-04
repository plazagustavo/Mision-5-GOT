def contar_elementos(lista):
    return len(lista)

def obtener_elemento(lista, posicion):  # devuelve el elemento en la posición indicada (debe validar 0 <= pos < len(lista))
    return lista[posicion]  

def concatenar_listas(lista1, lista2):  # devuelve una nueva lista con los elementos de ambas
    print ("\nMiembros unidos:")
    return lista1 + lista2              # 

def append_manual(lista, elemento): # devuelve una nueva lista con el elemento agregado al final sin usar append
    return lista + [elemento]


def imprimir_separador():
    print("--------------------")
