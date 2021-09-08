# 7. (Função sem retorno sem parâmetro) Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a A, deverá calcular a média aritimética das notas dos alunos, se for P, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada ao final.
# N1, N2 e N3 são notas.

# P1, P2 e P3 são pesos.

# Média ponderada = (N1 * P1 + N2 * P2 + N3 * P3 ) / (P1 + P2 + P3)

def media():     
    n1 = float(input("Insira a primeira nota: "))
    n2 = float(input("Insira a segunda nota: "))
    n3 = float(input("Insira a terceira nota: "))
    letra = input("Insira A (média aritimética) ou P (média ponderada): ").strip().upper()[0]

    if letra == "A":
        media_a = (n1 + n2 + n3) / 3
        print(f'A média aritmética entre as notas é de {media_a:.2f}')
    
    elif letra == "P":
        media_p = (n1 * 5 + n2 * 3 + n3 * 2 ) / (5 + 3 + 2)
        print(f'A média ponderada entre as notas é de {media_p:.2f}')
    
    else:
        (print('Essa média não é válida!'))

def main():
    media()

main()