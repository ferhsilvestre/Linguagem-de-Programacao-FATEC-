# 4. Baixe o arquivo futebol.txt que esta na pasta Material do aula do Teams. Leia este arquivo e o apresente. Com os dados lidos, armazene na estrutura Futebol (posicao_jogo, altura, peso, imc), calcule o IMC (Índice de Massa Corporal), armazene na estrutura e também em outro arquivo, mas agora chamado futebol_imc.txt. Apresente este novo arquivo.
# Observação: esse exercício deve ser testado fora do Colab, no Idle ou qualquer outra IDE, porque usará um arquivo que estará na pasta material de aula do Teams.

class Futebol_Imc:
    posicao = " "
    altura = float
    peso = float
    imc = float

def ler():
    arq_futebol = open('futebol.txt', 'r')
    vet_futebol = []
    for lin in arq_futebol.readlines():
        dados = lin.split(",")
        vet_futebol.append(dados)
    arq_futebol.close()
    return vet_futebol

def imc(tabela):
    arq_imc = open('futebol_imc.txt', 'w')
    for i in range(len(tabela)):
        f = Futebol_Imc()
        f.posicao = tabela[i][0]
        f.altura = float(tabela[i][1])
        f.peso = float(tabela[i][2])
        f.imc = (f.peso / (f.altura**2))
        tabela.append(f)
        arq_imc.write(f'{f.posicao},{f.altura},{f.peso},{f.imc:.1f}\n')
    arq_imc.close()

def apresentar():
    arq_imc = open('futebol_imc.txt','r')
    print('Posição \t\t Altura \tPeso \t\t IMC\n')
    for x in arq_imc.readlines():
        j, a, p, i = x.strip().split(',')
        print(j,'\t\t',a,'\t\t',p, '\t\t', i)
    arq_imc.close()

def main():
    tabela = ler()
    imc(tabela)
    apresentar()

main()