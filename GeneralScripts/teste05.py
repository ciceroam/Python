n = s = 0
while True:
    n = input("Digite um número (E para encerrar): ")
    if n.upper() == "E":
        break
    elif n.isnumeric():
        s = s + int(n)

print(f"A soma dos números informados é {s}.")
