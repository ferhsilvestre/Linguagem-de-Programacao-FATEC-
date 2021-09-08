# 4. (Função sem retorno sem parâmetro) Faça uma função/método que leia um único valor representado em segundos, converta-o e apresente o resultado em horas, minutos e segundos.

def conversao():
    segundos = int(input('Informe a quantidade de segundos para conversão: '))

    h = segundos / 3600
    r = segundos % 3600
    m = r / 60
    s = r % 60

    print(f'A conversão de {segundos} segundos é igual a {int(h)}h {int(m)}min {int(s)}s')

def main():
    conversao()

main()