import casas.lannister, casas.stark, casas.targaryen
import utilidades.manejo_listas as manejo_listas

def mostrar_menu():
    print("╔═══════════════════════╗")
    print("     𝔊𝔞𝔪𝔢 𝔬𝔣 𝔗𝔥𝔯𝔬𝔫𝔢𝔰")
    print("╚═══════════════════════╝")

    while True: 
        manejo_listas.imprimir_separador()
        print("1. Mostrar información de una Casa:")
        print("2. Unir miembros de dos casas:")
        print("3. Salir")
        opcion = leer_opcion("Ingrese una opcion: ", 1, 3)
        if opcion == 1:
            menu_de_casas()
        elif opcion == 2:
            unir_miembros()
        elif opcion == 3:
            print("Saliendo...")
            exit()
            
def leer_opcion(prompt: str, minimo: int, maximo: int):
    while True:
        opcion = (input(prompt)) 
        if opcion.isdigit() :
            opcion = int(opcion)
            if minimo <= opcion <= maximo:
                return opcion
            else:
                print(f"La opcion debe ser un número entre {minimo} y {maximo}")
        else:
            print(f"La opcion debe ser un número entre {minimo} y {maximo}")


def menu_de_casas():
    print("1. Lannister")
    print("2. Stark")
    print("3. Targaryen")
    print("4. Volver")

    opcion = leer_opcion("Ingrese una opcion: ", 1, 4)
    if opcion == 1:
        casas.lannister.mostrar_informacion()
    elif opcion == 2:
        casas.stark.mostrar_informacion()
    elif opcion == 3:
        casas.targaryen.mostrar_informacion()
    elif opcion == 4:
        mostrar_menu()

def unir_miembros():
    print("¿Que casas desea unir?")
    print("1. Lannister y Stark")
    print("2. Stark y Targaryen")
    print("3. Lannister y Targaryen")
    print("4. Volver")

    opcion = leer_opcion("Ingrese una opcion: ", 1, 4)
    if opcion == 1:
        miembros_unidos = manejo_listas.concatenar_listas(casas.lannister.obtener_miembros(), casas.stark.obtener_miembros())
        print(miembros_unidos)
    elif opcion == 2:
        miembros_unidos =manejo_listas.concatenar_listas(casas.stark.obtener_miembros(), casas.targaryen.obtener_miembros())
        print(miembros_unidos)
    elif opcion == 3:
        miembros_unidos = manejo_listas.concatenar_listas(casas.lannister.obtener_miembros(), casas.targaryen.obtener_miembros())
        print(miembros_unidos)
    elif opcion == 4:
        mostrar_menu()