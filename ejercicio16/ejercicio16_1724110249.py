def main():
    cola = []
    retro = []
    final = []
    while True:
        menu()
        seleccion = eleccion()
        if seleccion == "4":
            print("Saliendo del programa...")
            break
        proceso(seleccion, cola, retro, final)
    input()


def menu():
    print("\n---- Menú ----")
    print("1. Agregar un producto")
    print("2. Inspeccionar un producto")
    print("3. Inspeccionar los productos retrabajados")
    print("4. Salir")


def eleccion():
    valid = ["1", "2", "3", "4"]
    while True:
        elec = input("Elija: ").strip()
        if elec in valid:
            return elec


def proceso(n, cola, retro, final):
    match n:
        case "1":
            agregar(cola)

        case "2":
            inspeccionNormal(cola,retro,final)

        case _:
            if cola:
                print("\nCola actual:")
                for i, (cliente, clase) in enumerate(cola, start=1):
                    print(f"{i}. {cliente} ({clase})")
            else:
                print("La cola está vacía.")

def agregar(cola):
    entrada = input("\nIngrese el nuevo producto: ").strip()
    cola.append(entrada)

def inspeccionNormal(cola,retro,final):
    if cola:
        for producto in cola:
            while True:
                valid = input(f"\nIngrese 1 para aprobar {producto} y 2 para rechazarlo: ").strip()
                match valid:
                    case "1":
                        final.append(producto)
                        cola.pop(0)
                        break
                    case "2":
                        retro.append(producto)
                        cola.pop(0)
                        break
                    case _:
                        continue
    else:
        print("La cola está vacía intente agregando clientes antes")

if __name__ == "__main__":
    main()