# 10. (Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro e positivo N e mostre o valor de S, obtido pelo seguinte cálculo:
# S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
# Observvação: Não pode usar vetor e função pronta da linguagem Python.

def fatorial():
    n = (int(input("Digite um número inteiro e positivo: ")))
    fat = 1
    s = 0

    for i in range (1, n + 1):
        fat *= i
        s += (1/fat)
        
    s += 1

    print(f"{s:.2f}")

def main():
    fatorial()

main()