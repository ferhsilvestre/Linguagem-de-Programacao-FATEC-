# 6. (Função com retorno sem parâmetro) Faça um programa contendo uma função/método que verifique se um número é par, retorne/mostre o valor bool True para par e False para ímpar.

def par_impar():
    n = int(input('Insira um número inteiro: '))
    if n % 2 == 0:
        return True
    else:
        return False

def main():    
    print(par_impar())

main()