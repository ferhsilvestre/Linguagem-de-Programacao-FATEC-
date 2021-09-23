# 1. Para fazer o cadastro em uma rede social, o usuário deve preencher vários dados, inclusive um e-mail válido, ou seja, um e-mail deve conter UM caracter arroba '@' e UM ou MAIS caracteres ponto '.'
# Crie uma função que retorne como resposta, se um e-mail é 'válido' ou 'inválido'. Não use nenhum método/função pronto ou o operador in no if, da linguagem Python. Avalie caracter por caracter. Deve ser criada a função main para chamar a da verificação.

def email_check(email):
    total_arroba = total_ponto = 0
    for i in range(len(email)):
        if email[i] == "@":
            total_arroba += 1
        if email[i] == ".":
            total_ponto += 1 
    if total_arroba == 1 and total_ponto >= 1:
        return 'válido'
    else:
        return 'inválido'

def main():
    e_mail = input("Insira seu e-mail: ")
    print("O e-mail digitado é", email_check(e_mail))

main()


