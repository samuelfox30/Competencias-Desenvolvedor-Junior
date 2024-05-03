'''
 ----- BUSCA BINÁRIA -----

- O objetivo desse programa é realizar uma busca binária estre números de uma lista, sendo capaz de achar a posição do número que você deseja encontrar, e retornar 
a posição do mesmo.

'''

# Função da busca_binária: ---> list = lista dos numeros, objective = numero que deseja encontrar, first_position = primeira posição da lista, last_position = última posição da lista
def binary_search(list, objective, first_position=0, last_position=0):

    # Resumidamente, este try e o except no final da função, são responsaveis por retornar None para qualquer tipo de erro, seja no caso de inserir Strings no lugar de números, ou caso o número que você quer achar (numero objetivo) não esteja na lista
    try:
        # Definindo posição central da lista
        center_position = (first_position+last_position)//2
        # Definindo número da posição central
        center_number = list[center_position]

        # Para definirmos qual é a primeira posição, primeiramente precisamos saber se já existe algum valor sendo indicado como primeira opção
        if first_position == 0 & last_position == 0:
            last_position = len(list)

        # Se o número central for igual ao que eu quero encontrar...
        if center_number == objective:
            # Retorne a posição central + possíveis posições anteriores = posição do número que quero encontrar
            return center_position
        
        # Se o numero central for menor do que o objetivo, isso significa que meu objetivo agora está a direita do número central
        if center_number < objective:
            # Redefine a primeira posição, que será a posição central
            first_position = center_position
            # Repete tudo com os novos valores
            return binary_search(list, objective, first_position, last_position)
        
        # Se o numero central for maior do que o objetivo, isso significa que meu objetivo agora está a esquerda do número central
        if center_number > objective:
            # Redefine a última posição, que será a posição central
            last_position = center_position
            # Repete tudo com os novos valores
            return binary_search(list, objective, first_position, last_position)
    except:
        return None




# ----- SIMULAÇÃO DO CÓDIGO -----

while True:

    # Lista de números impares, mas poderia ser qualquer lista com qualquer valor (a lista precisa estar em ordem crescente)
    odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15.5, 15.7, 17, 19, 21, 23, 25, 27, 27.3, 29.7, 29.9, 31, 33]
    # Recebe do usuário o valor que ele deseja procurar na lista
    objective = float(input(f'Qual número deseja procurar?'))
    # Armazena o resultado da busca na variavel objective
    result = binary_search(odd_numbers, objective)
    # Exibe o resultado
    print(f'The result is: {result}')

    # Esse código é apenas pra saber se você quer rodar o programa denovo ou não (não está relacionado com a busca binária)
    again = input('Rodar denovo?[S/N] ')
    if again.lower() != 's':
        break