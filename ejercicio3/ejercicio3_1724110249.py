def main():
    cadena = cons_cadena()
    print(f"Su cadena invertida es: {cadena_invertir(cadena)}")

def cadena_invertir(cadena):
    letras = []
    cadenaInvertida = ""
    for letra in cadena:
        letras.append(letra)
    for letra2 in range(len(letras)-1, -1, -1):
        cadenaInvertida += letras[letra2]
    return cadenaInvertida

def cons_cadena():
    while True:
        cadena = input("Ingrese el texto a invertir: ")
        if cadena == None:
            continue
        else:
            return cadena

if __name__ == "__main__":
    main()