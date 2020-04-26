# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")

    def subtracao(self):
        subtracao = self.num1 - self.num2
        return print(f"{self.num1} - {self.num2} = {subtracao}")

    def multiplicacao(self):
        multiplicacao = self.num1 * self.num2
        return print(f"{self.num1} * {self.num2} = {multiplicacao}")

    def divisao(self):
        divisao = self.num1 / self.num2
        return print(f"{self.num1} / {self.num2} = {divisao}")

print("\n******************* Python Calculator *******************")
print("")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("")

opcao = input("Digite sua opção (1/2/3/4): ")
print("")
num1 = int(input("Primeiro numero: "))
print("")
num2 = int(input("Segundo numero: "))
print("")

if opcao == "1":
    soma = Calculadora(num1, num2)
    print(soma.soma())
elif opcao == "2":
    subtracao = Calculadora(num1, num2)
    print(subtracao.subtracao())
elif opcao == "3":
    multiplicacao = Calculadora(num1, num2)
    print(multiplicacao.multiplicacao())
elif opcao == "4":
    divisao = Calculadora(num1, num2)
    print(divisao.divisao())
else:
    print("Não é uma opção valida")
