def fatorial(num, exibirCalculo=False):
    """
    -> Calcula o fatorial de um número
    :param num: Número a ser calculado.
    :param exibirCalculo: (Opcional) Exibir o cálculo na tela.
    """
    res = 1
    for c in range(num, 0, -1):
        if exibirCalculo:
            print(f"{c}", end='')
            if c > 1:
                print(f" * ", end='')
            else:
                print(f" = ", end='')
        res *= c
    print(f"{res}")


help(fatorial)
numero = int(input("Digite um número para calcular o fatorial: "))
calculo = str(input("Mostrar o cálculo? (S) ou (N) ")).upper()
fatorial(numero, True if calculo == "S" else False)
