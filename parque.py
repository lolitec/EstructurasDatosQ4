import sys

def main():
    for line in sys.stdin:
        try:
            n = int(line.strip())
            if n == 0:
                break

            entrada = sys.stdin.readline().strip()
            numerosstr = entrada.split()
            numeros = []
            for numstr in numerosstr:
                numero = int(numstr)
                if not (0 <= numero <= 10**9):
                    sys.exit()
                numeros.append(numero)

            if len(numeros) != n:
                sys.exit()

            difanterior = numeros[1] - numeros[0]
            valido = True
            for i in range(len(numeros) - 1):
                diferencia = numeros[i+1] - numeros[i]
                if diferencia != difanterior:
                    valido = False
                    break

            if valido:
                print("1")
            else:
                diffinal = numeros[-1] - numeros[-2]
                index = len(numeros) - 1
                for i in range(len(numeros)-1, 0, -1):
                    diferencia = numeros[i] - numeros[i-1]
                    if diferencia == diffinal:
                        index = i
                    else:
                        break
                print(index)

        except (ValueError, IndexError):
            break

if __name__ == "__main__":
    main()
