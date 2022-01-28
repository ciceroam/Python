import random
c = random.randint(1, 5)
u = int(input('Pensei em um número de 1 a 5, qual é? '))
if u == c:
    print('Você acertou! :)')
else:
    print('Errrroouuu! Era {}'.format(c))

c = random.randint(1, 5)
u = int(input('Pensei em outro, \33[1;32mqual\33[m é? '))
print('Você acertou! :)' if u == c else 'Errrroouuu! Era {}'.format(c))
