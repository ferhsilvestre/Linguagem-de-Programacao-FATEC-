# 2. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método para subtrair dois números, retornar o resultado e o apresentando.

def subtrair():
    n1 = int(input("Informe o primeiro valor: "))
    n2 = int(input("Informe o segundo valor: "))
    r = n1 - n2
    return r
    # ou return n1 - n2

def main():
    print("A diferença entre os dois números é",subtrair())

main()