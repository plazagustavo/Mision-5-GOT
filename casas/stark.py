import utilidades.manejo_listas as manejo_listas

def obtener_miembros():
    return ["Eddard Stark (Padre)",
            "Catelyn Stark (Madre)",
            "Robb Stark (Hijo)",
            "Sansa Stark (Hija)", 
            "Arya Stark (Hija)", 
            "Bran Stark (Hijo)", 
            "Rickon Stark (Hijo menor)",
            "Jon Snow (Hijo bastardo)"]

def obtener_lema():
    return "❄️  Lema: Winter is coming"

def mostrar_informacion():
    """ Muestra información sobre la casa Stark 
    """
    manejo_listas.imprimir_separador()
    print("Casa Stark 🐺 ⚔️")
    manejo_listas.imprimir_separador()
    print(obtener_lema())
    manejo_listas.imprimir_separador()
    print("Miembros:")
    i = 0
    while i < manejo_listas.contar_elementos(obtener_miembros()): # while i < len(obtener_miembros()), es como decir while i < 8
        print(obtener_miembros()[i])  # Aca se obtiene el miembro en la posición i
        i += 1                        # Aca se incrementa i en 1 para que se siga recorriendo la lista