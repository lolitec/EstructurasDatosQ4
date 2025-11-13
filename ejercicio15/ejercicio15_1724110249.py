def main():
    cafe = {
    "Americano": 1,
    "Espresso": 2,
    "Macchiato": 3,
    "Capuchino": 4,
    "Latte": 5,
    "Mocha": 6
    }
    cola = []
    completados = []
    while True:
        menu()
        seleccion = eleccion()
        if seleccion == "5":
            print("Saliendo del programa...")
            break
        proceso(seleccion, cola, cafe, completados)


def menu():
    print("\n---- Menú ----")
    print("1. Agregar un pedido")
    print("2. Atender un pedido")
    print("3. Consultar pedidos pendientes")
    print("4. Consultar pedidos completados")
    print("5. Salir")


def eleccion():
    valid = ["1", "2", "3", "4", "5"]
    while True:
        elec = input("\nElija: ").strip()
        if elec in valid:
            return elec


def proceso(n, pendientes, cafes,completados):
    match n:
        case "1":
            while True:
                for cafe,prioridad in cafes.items():
                    print(f"{cafe} - Prioridad {prioridad}")
                entrada = input("\nIngrese el tipo de café que desea: ").strip()
                if entrada.title() in cafes:
                    pendientes.append(entrada.title())
                    break
                else:
                    continue

        case "2":
            if pendientes:
                prio = cafes[pendientes[0]]
                indice = 0

                for i in range(1, len(pendientes)):
                    if cafes[pendientes[i]] < prio:
                        prio = cafes[pendientes[i]]
                        indice = i
                completados.append(pendientes.pop(indice))
            else:
                print("\nLa cola está vacía, agregue pedidos antes.")
        
        case "3":
            if pendientes:
                print(f"\nLos pedidos pendientes son:")
                for i in pendientes:
                    print(i)
            else:
                print("\nNo hay pedidos pendientes")
        
        case _:
            if completados:
                print(f"\nLos pedidos completados son:")
                for i in completados:
                    print(i)
            else:
                print("\nNo hay pedidos completados")
                    


if __name__ == "__main__":
    main()
