def main():
    cola = []
    while True:
        menu()
        seleccion = eleccion()
        if seleccion == "4":
            print("Saliendo del programa...")
            break
        proceso(seleccion, cola)


def menu():
    print("\n---- Menú ----")
    print("1. Agregar un cliente")
    print("2. Atender un cliente")
    print("3. Mostrar la cola")
    print("4. Salir")


def eleccion():
    valid = ["1", "2", "3", "4"]
    while True:
        elec = input("Elija: ").strip()
        if elec in valid:
            return elec


def proceso(n, cola):
    match n:
        case "1":
            while True:
                entrada = input("Ingrese el cliente y su clasificación (cliente.pdf urgente): ").split()
                if len(entrada) == 2:
                    cliente, clase = entrada
                    cola.append((cliente, clase.lower()))
                    break
                else:
                    continue

        case "2":
            if cola:
                preferentes = []
                normales = []
                for i, (cliente, clase) in enumerate(cola):
                    if clase == "preferente":
                        preferentes.append(i)
                    elif clase == "normal":
                        normales.append(i)
                    else:
                        break
                if len(preferentes) == 0 and len(normales) == 0:
                    cola.pop(0)
                elif preferentes:
                    for i in preferentes:
                        cola.pop(i)
                        break
                else:
                    for i in normales:
                        cola.pop(i)
                        break
            else:
                print("La cola está vacía intente agregando clientes antes")

        case _:
            if cola:
                print("\nCola actual:")
                for i, (cliente, clase) in enumerate(cola, start=1):
                    print(f"{i}. {cliente} ({clase})")
            else:
                print("La cola está vacía.")


if __name__ == "__main__":
    main()
