# Listas
num = [4, 1, 6, 8, 4]
print(num)
num[0] = 3
print(num)
num.append(9)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(len(num))
num.insert(2, 0)
print(num)
num.pop(1)
print(num)
if 11 in num:
    num.remove(4)
else:
    print('Não encontrado o valor')
print(num)

num2 = list()

#linka
num2 = num
num2[0] = 99
print(num)
print(num2)

#copia
num2 = num[:]
num2[0] = 88
print(num)
print(num2)