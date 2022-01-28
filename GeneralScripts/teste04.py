nome = input("Qual seu nome?")
idade = int(input("Qual a sua idade?"))

decadas = 0

for i in range(10, idade + 1, 10):
    print(i)
    decadas += 1

print("{}, você viveu {} décadas completas!".format(nome, decadas))

if idade < 18:
    print("Você é menor de idade!")
elif 18 <= idade < 60:
    print("Você é um adulto!")
else:
    print("Você é idoso!")

print("FIM")


