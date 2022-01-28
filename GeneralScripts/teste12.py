def leiaInt(frase):
    valor = input(frase)
    while not valor.isnumeric():
        print("\033[0;31mValor digitado não é inteiro, digite novamente!\033[m")
        valor = input(frase)
    return valor


n = leiaInt("Digite um número inteiro: ")
print(f"Número digitado {n} é um inteiro.")
