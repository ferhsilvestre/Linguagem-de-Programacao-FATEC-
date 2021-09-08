# 10. (Função sem retorno com parâmetro) Faça uma função/método para verificar e contar quantas letras a tem numa frase. Não use NENHUMA função pronta da linguagem Python.

def contar_letras(x):
    cont = 0
    for i in x:
        if i in "aáàã":
            cont += 1

    print(f"A sua frase contém {cont} letras 'a'!")

def main():
    frase = input('Digite uma frase: ')
    contar_letras(frase)

main()
