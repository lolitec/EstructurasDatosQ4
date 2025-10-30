def main():
    expresion = cons_expresion()
    balanceado = balancear(expresion)
    if balanceado:
        print(f"La expresión {expresion} está balanceada")
    else:
        print(f"La expresión {expresion} no está balanceada")

def cons_expresion():
    expresion = input("Ingrese la expresión a verificar: ")
    return expresion

def balancear(n):
    pila = []
    for i in n:
        if i == "(":
            pila.append(i)
        elif i == ")":
            if not pila:
                return False
            pila.pop()
    if len(pila) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()