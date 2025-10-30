# Programa que simule la atencion de clientes en una fila de un banco los clientes llegan y se agregan al final de la cola y el cajero los atiende en el mismo orden
# que llegaron
# 1. Crear cola vacia (lista)
# 2. El programa deberá mostrar un menú con:
#     a) agregar clientes a la cola
#     b) atender al cliente
#     c) mostrar la cola
#     d) salir
# 3. Cada vez que se agregue un cliente el programa deberá solicitar su nombre
# 4. Al atender un cliente, se debe eliminar al primer cliente de la cola y mostrar su nombre con una etiqueta de cliente atendido
# 5. Si se intenta atender cuando la cola está vacía el programa debe mostrar un mensaje apropiado
# 6. Mostrar la cola actual en cada interacción
def main():
    cola = []
    while True:
        menu()
        seleccion = eleccion()
        if seleccion == "4":
            break
        proceso(seleccion,cola)

def menu():
    print("----Ingrese el numero correspondiente a la accion que desea realizar----")
    print("----1 para agregar un cliente----")
    print("----2 para atender un cliente----")
    print("----3 para mostrar la cola----")
    print("----4 para salir----")

def eleccion():
    valid = ["1","2","3","4"]
    while True:
        elec = input("Elija: ")
        if elec not in valid:
            continue
        else:
            break
    return elec

def proceso(n,cola):
    match n:
        case "1":
            cola.append(input("Ingrese al nuevo cliente: "))
        case "2":
            if cola:
                print(f"{cola.pop(0)} ----Atendido----")
                print(f"La cola actual es: {", ".join(cola)}")
            else:
                print("La cola está vacía intente agregando un nuevo cliente")
        case _:
            print(f"La cola actual es: {", ".join(cola)}")

if __name__ == "__main__":
    main()