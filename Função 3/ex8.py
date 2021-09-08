# 8. (Função com retorno sem parâmetro) Faça uma função/método retorne um vetor com os três primeiros números perfeitos. Sabe-se que um número é perfeito quando é igual a soma de seus divisores (exceto ele mesmo).
# Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito. Não use função pronta.
# 1º número perfeito: 6
# 2º número perfeito: 28
# 3º número perfeito: 496

def num_perfeito():
    perfeito = []

    for n in range(1,497):
        soma = 0

        for p in range(1,n):

            if n % p == 0:
                soma = soma + p
            
        if n == soma:
            perfeito.append(soma)
            
    return perfeito

def main():
    print(num_perfeito())

main()