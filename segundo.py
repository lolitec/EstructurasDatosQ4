import sys

def main():
    try:
        incorrecto = int(input())
    except ValueError:
        sys.exit()
    if 0 <= incorrecto and incorrecto < 60:
        correcto = int(input())
        if 0 <= correcto and correcto < 60:
            resultado = incorrecto - correcto
            if resultado < 0:
                if resultado == -1:
                    print(f"ADELANTAR {resultado * -1} SEGUNDO")
                else:
                    print(f"ADELANTAR {resultado * -1} SEGUNDOS")
            else:
                if resultado == 1:
                    print(f"ATRASAR {resultado} SEGUNDO")
                else:
                    print(f"ATRASAR {resultado} SEGUNDOS")
        else:
            sys.exit()
    else:
        sys.exit()

if __name__ == "__main__":
    main()