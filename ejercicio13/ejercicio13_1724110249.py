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
    print("1. Agregar un documento")
    print("2. Imprimir un documento")
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
                entrada = input("Ingrese el documento y su etiqueta (doc.pdf urgente): ").split()
                if len(entrada) == 2:
                    doc, etiqueta = entrada
                    cola.append((doc, etiqueta.lower()))
                    break
                else:
                    continue

        case "2":
            if cola:
                urgentes = []
                normales = []
                for i, (doc, etiqueta) in enumerate(cola):
                    if etiqueta == "urgente":
                        urgentes.append(i)
                    elif etiqueta == "normal":
                        normales.append(i)
                    else:
                        continue
                if len(urgentes) == 0 and len(normales) == 0:
                    cola.pop(0)
                elif urgentes:
                    for i in urgentes:
                        cola.pop(i)
                        break
                else:
                    for i in normales:
                        cola.pop(i)
                        break
            else:
                print("La cola está vacía intente agregando documentos antes")

        case _:
            if cola:
                print("\nCola actual:")
                for i, (doc, etiqueta) in enumerate(cola, start=1):
                    print(f"{i}. {doc} ({etiqueta})")
            else:
                print("La cola está vacía.")


if __name__ == "__main__":
    main()
