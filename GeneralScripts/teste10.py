from datetime import date


def voto(anoNasc):
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    if idade < 16:
        voto = "NEGADO"
    elif 18 <= idade < 70:
        voto = "OBRIGATÓRIO"
    else:
        voto = "OPCIONAL"
    return f"Para a idade {idade}: O voto é {voto}."


while True:
    anoInserido = int(input("Informe o ano de nascimento (0 para encerrar): "))
    if anoInserido == 0:
        break
    print(voto(anoInserido))

