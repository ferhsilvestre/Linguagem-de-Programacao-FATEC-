# 7. (Função sem retorno com parâmetro) Faça uma função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, chame/crie OUTRA função que verifique se esta média aprova ou reprova o aluno.

def calcular_media(nota1, nota2):

    media = (nota1 + nota2) / 2

    print('Sua média é', media)

    verificar_aprovacao(media)



def verificar_aprovacao(m):

    if m >= 6:

        print('Aluno aprovado')

    else:

        print('Aluno reprovado')



def main():

    p1 = float(input('Digite a primeira nota: '))

    p2 = float(input('Digite a segunda nota: '))

    calcular_media(p1, p2)



main()