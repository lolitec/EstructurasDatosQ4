# Revertir una cadena de palabras utilizando una pila
# Descripción: Cree un programa que permita al usuario ingresar una linea de texto y que utilizando una pila muestre la linea invertida
# La línea no tendra maximo de palabras

def main():
    texto = cons_texto()
    invertido = invertir(texto)
    for letra in invertido:
        print(letra,end="")
    print()

def cons_texto():
    texto = input("Ingrese su cadena: ")
    return texto

def invertir(texto):
    cadena = []
    invertir = []
    for letra in texto:
        cadena.append(letra)
    for _ in range(len(cadena)):
        invertir.append(cadena.pop())
    return invertir

if __name__ == "__main__":
    main()