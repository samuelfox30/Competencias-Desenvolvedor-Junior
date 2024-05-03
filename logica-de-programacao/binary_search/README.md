# Busca Binária

Este programa implementa o algoritmo de busca binária em Python. A busca binária é um algoritmo poderoso e eficiente utilizado para encontrar um determinado valor em uma lista ordenada de elementos. Sua eficiência está principalmente na redução do número de comparações necessárias para encontrar o valor desejado, especialmente em listas grandes.

### Como funciona?
A ideia fundamental por trás da busca binária é dividir repetidamente a lista pela metade e comparar o valor desejado com o elemento no meio da lista. Se o valor desejado for igual ao elemento no meio da lista, a busca é bem-sucedida. Caso contrário, a metade da lista em que o valor desejado não pode estar é eliminada e a busca continua na outra metade até que o valor seja encontrado ou a lista seja esgotada.

### Requisitos para utilizar o programa:
- Ter o python instalado em seu sistema
- Abrir o programa search.py em seu ambiente python

## Explicação do código:

Primeiramente temos uma função chamada binary_search, responsável por realizar todo o processo de encontrar a posição do número e retorna-lo. Para isso, ela precisa de dois requisitos: a lista em que você deseja procurar o número que quer, e o número que quer encontrar.

Em seguida, dentro da função, temos um 'try/except' responsáveis por tratar os possíveis erros do código da função, erros como a entrada de Strings na função ou no caso do número que deseja encontrar não estiver na lista informada, retornando 'None' para ambas ocasiões.

Continuando a leitura para dentro do 'try', definimos duas variaveis que serão essenciais para todo o código, são elas: center_position e center_number, uma contém a posição central da lista no atual loop, e a outra contém o número contido nessa posição central, respectivamente. 

Seguindo a diente, temos algumas condições que definem o caminho em que o processo deve seguir. O primeiro 'if' diz que se a primeira e a última posição ter o índice 0, significa que essa é a primeira vez em que a função está lidando com a lista informada, o que indica que o índice da ultima posição não é o verdadeiro, e que por isso, caso a condição seja verdadeira, é adicionada uma nova última posição, que é referente ao tamanho da lista. Mas caso a primeira ou a última posição já não tenham mais o índice 0, isso significa que ela não deve mudar o valor da última posição, pois ele já foi alterado.

A segunda condição é a condição final, referente a quando o número objetivo é encontrado. Este verifica se o valor central é igual ao número que informou, se sim, ele retorna a posição de tal, se não, ele apenas iguinora as linhas de código referente a condição.

A terceira e a quarta verificam quase a mesma coisa, mas leval o código a caminhos opostos. A terceira condição diz que, caso o número central seja menor que o meu objetivo, ele irá repetir a função com um novo valor para a primeira posição, o qual será a antiga posição central da lista. Já a quarta condição diz que, caso a posição central seja, agora, maior que o objetivo, será dado um novo valor à última posição, e em seguida repetir a função com o novo valor.

##

No final do código, temos uma lista teste que contém apenas números ímpares em ordem crescente. Em seguida recebemos do usuário o número em que ele deseja procurar, amazenamos esse valor na variavel objective, que depois passaremos na chamada da função binary_search, juntamente da lista que criamos.

### Observações

Para a execução do código, é necessário que se utilize uma lista de números já em ordem crescente, pois um código que ordena valores seguindo os mesmos princícios da busca binária já é outro programa. Este é focado na realização da busca binária, apenas.

### Agradecimetos

Obrigado por ler até aqui! Se você tiver qualquer feedback, sugestão de melhoria ou identificar qualquer erro, não hesite em entrar em contato. Seu feedback é muito valioso para mim e me ajuda a melhorar continuamente. Obrigado mais uma vez por visitar este repositório!