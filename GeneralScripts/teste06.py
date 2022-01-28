# tupla
carros = ('Gol', '2008', 'Fiesta', 'Jeep', 'Ka')

#carros[5] = 'Ranger'

print(carros)

print(sorted(carros))

print(len(carros))

print(carros.index('2008'))

for pos, carro in enumerate(carros):
    print(f'O carro {carro} está na posição {pos}.')
