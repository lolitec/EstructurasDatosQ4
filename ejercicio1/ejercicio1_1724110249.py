def main():
    n = consNum()
    print(f"El factorial de {n} es : {factorial(n)}")

def consNum():
    while True:
        try:
            n = int(input("Ingrese su numero: "))
            if n < 0:
                continue
            elif n == 0:
                return 1
            else:
                return n
        except ValueError:
            continue

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
