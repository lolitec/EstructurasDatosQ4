def main():
    linea = cons_linea()
    especiales = num_especiales(linea)
    print(f"La linea {"".join(linea)} tiene {especiales} carácteres especiales")

def cons_linea():
    pila = []
    for letra in input("Ingrese su linea de texto: "):
        pila.append(letra)
    return pila

def num_especiales(linea):
    n = 0
    valid = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    while linea:
        letra = linea.pop()
        if letra.lower() not in valid:
            n += 1
    return n

if __name__ == "__main__":
    main()