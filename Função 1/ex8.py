# 8. (Função sem retorno sem parâmetro) Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.

def jogo():
    hora_inicio = int(input("Informe, com um número inteiro, apenas a HORA que você iniciou o jogo: "))
    minuto_inicio = int(input("Informe, com um número inteiro, apenas o MINUTO que você iniciou o jogo: "))
    hora_fim = int(input("Informe, com um número inteiro, apenas a HORA que você iniciou o jogo: "))
    minuto_fim = int(input("Informe, com um número inteiro, apenas o MINUTO que você iniciou o jogo: "))

    if minuto_fim < minuto_inicio:
        minuto_fim += 60
        hora_fim -= 1
    
    if hora_fim < hora_inicio:
        hora_fim += 24
    
    total_min = minuto_fim - minuto_inicio
    total_hora = hora_fim - hora_inicio
    total = total_hora * 60 + total_min

    print(f"Você jogou por {total} minutos!")

def main():
    jogo()

main()
