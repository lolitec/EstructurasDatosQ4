def main():
    n = consNumero()
    print(f"La secuencia hasta esa posición es: {fibonacci(n)}")

def consNumero():
    while True:
        try:
            n = int(input("Ingrese la posicion que desea consultar: "))
            if n < 0:
                continue
            else:
                break
        except ValueError:
            continue
    return n

def fibonacci(n):
    numbers = [0,1]
    i = 2
    if n == 0:
        return numbers[:1]
    while i < n:
        newN = numbers[i-1] + numbers[i-2]
        numbers.append(newN)
        i += 1
    return numbers

if __name__ == "__main__":
    main()