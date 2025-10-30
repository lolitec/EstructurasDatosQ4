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
    print("----2 para vender un boleto----")
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
                print(f"El cliente {cola.pop(0)} ha comprado un boleto")
                print(f"La cola actual es: {", ".join(cola)}")
            else:
                print("La cola está vacía intente agregando un nuevo cliente")
        case _:
            print(f"La cola actual es: {", ".join(cola)}")

if __name__ == "__main__":
    main()