# 4. (Função com retorno com parâmetro) Faça um programa contendo uma função/método que receba duas notas (P1, P2) calcule a média, chame outra função na main que avalie se este aluno esta aprovado ou reprovado retornando a str/string 'Aprovado' ou 'Reprovado'.

def media(x,y):
    media_prova = (x + y) / 2
    return media_prova

def aprovacao(x):
    if x >= 6:
        return 'APROVADO'
    else:
        return 'Reprovado'

def main():
    p1 = float(input('Informe a nota da P1: '))
    p2 = float(input('Informe a nota da P2: '))
    m = media(p1, p2)
    print(f'O aluno ficou com a média de {m:.1f} e foi {aprovacao(m)}')

main()
