import utilidades.manejo_listas as manejo_listas

def obtener_miembros():
    return [
            "Aerys II Targaryen (Padre, el Rey Loco – fallecido)",
            "Rhaegar Targaryen (Hijo mayor – fallecido)",
            "Viserys Targaryen (Hijo – exiliado)",
            "Daenerys Targaryen (Hija - exiliada)"]

def obtener_lema():
    return "🐲 Lema: Fire and Blood"

def mostrar_informacion():
    manejo_listas.imprimir_separador()
    print("Casa Targaryen 🐉🔥")
    manejo_listas.imprimir_separador()
    print(obtener_lema())
    manejo_listas.imprimir_separador()
    print("Miembros:")
    i = 0
    while i < manejo_listas.contar_elementos(obtener_miembros()): # while i < len(obtener_miembros()), es como decir while i < 4
        print(obtener_miembros()[i])  # Aca se obtiene el miembro en la posición i 
        i += 1  # Aca se incrementa i en 1 para que se siga recorriendo la lista

