'''
 ----- BUBBLE SORT -----

- O objetivo desse programa é ordenar de forma crescente os números de uma lista através da comparação contínua de dois números da lista, até que a comparação
tenha sido realizada com todos os numeros da lista.

'''

# Criando a função que receberá a lista que será ordenada
def bubble_sort(lst):
    # Armazenando o tamanho da lista em uma variavel
    list_size = len(lst)
    # Em resumo, os dois 'for' a seguir são responsáveis garantir que a comparação dos números tenha se repetido o suficiente para que todos os numeros estejam em ordem
    for i in range(list_size-1):
        for j in range(list_size-1-i):
            # Aqui é onde ocorre a comparação, quem se o segundo número for menor que o primeiro, isso significa que ele retrocederá um 'lugar' na lista
            if lst[j+1] < lst[j]:
                # Trocando os numeros de posição
                lst[j], lst[j+1] = lst[j+1], lst[j]
    # Por fim, retornando a lista
    return lst

# Lista exemplo
lista = [5, 4, 7, 5, 3, 9, 7, 0, 12, 24, 55, 34, 23, 21, 22]
print(f'Antes de ser ordenada: {lista}')
bubble_sort(lista)
print(f'Depois de ser ordenada: {lista}')