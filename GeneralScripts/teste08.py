galera = list()
pessoa = list()
totalMaior = totalMenor = 0

for c in range(0, 3):
    pessoa.append(str(input("Nome: ")))
    pessoa.append(int(input("Idade: ")))
    galera.append(pessoa[:])
    pessoa.clear()

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totalMaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalMenor += 1

print(f'Temos {totalMenor} menor(es) de idade e {totalMaior} maior(es) de idade.')
