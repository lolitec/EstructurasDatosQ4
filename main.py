def main():
  while True:
    try:
      line = input()
    except EOFError:
      break
    tokens = line.strip().split()
    enteros = []
    if tokens:
        for token in tokens:
            enteros.append(int(token))
    cantidad = len(enteros)
    if enteros:
        suma = sum(enteros)
    else:
        suma = 0
    print(cantidad, suma)
  

if __name__ == "__main__":
  main()