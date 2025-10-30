## crear un programa que permita al usuario ingresar una linea de texto y que cuente cuantas letras dependiendo la eleccion
# existen en esa linea de texto, el usuario podra elegir cualquier letra del alfabeto ya seab nayusculas o minusculas y el sistema
# entregara el numero de veces que esa letra aparece en la linea, utiliza una pila
def main():
    cadena = cons_cadena()
    letra = cons_letra()
    print(cuenta_letra(cadena,letra))

def cons_cadena():
    cadena = []
    for letra in input("Ingrese la cadena de texto: "):
        cadena.append(letra)
    return cadena


def cons_letra():
    abc = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
  'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
    while True:
        letra = input("Ingrese su letra a buscar: ").lower()
        if letra and letra in abc:
            break
    return letra

def cuenta_letra(cadena,letra):
    cuenta = 0
    orig = cadena.copy()
    while cadena:
        if letra == cadena.pop():
            cuenta += 1
    if cuenta == 0:
        return f"La letra {letra} no se encuentra en la cadena"
    else:
        return f"La letra {letra} se encuentra {cuenta} veces en {"".join(orig)}"

if __name__ == "__main__":
    main()