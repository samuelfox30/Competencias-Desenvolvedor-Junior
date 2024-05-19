# Bubble Sort

Este projeto implementa o algoritmo Bubble Sort em Python. O Bubble Sort é um método simples e intuitivo para ordenar listas. Embora não seja o mais rápido, é ótimo para entender os conceitos básicos de ordenação.

### Como funciona?
A ideia do Bubble Sort é bem simples: percorremos a lista várias vezes, comparando elementos adjacentes e trocando-os de lugar se estiverem na ordem errada. Esse processo continua até que toda a lista esteja ordenada. A cada passagem, o maior elemento "burbulha" para a sua posição correta.

### Requisitos para utilizar o programa:
- Ter o python instalado em seu sistema
- Abrir o arquivo bubble_sort.py no seu ambiente Python preferido

## Explicação do código:

Criamos uma função chamada bubble_sort que recebe uma lista e a ordena. Primeiro, calculamos o tamanho da lista. Depois, usamos dois laços for para garantir que todos os elementos sejam comparados e ordenados. O laço externo controla quantas vezes percorremos a lista, enquanto o laço interno cuida das comparações e trocas de elementos adjacentes.

Se um elemento for maior que o próximo, eles são trocados de lugar. Esse processo se repete até que a lista esteja completamente ordenada. No final, a função retorna a lista ordenada.

No fim do código, temos uma lista de exemplo chamada lista com números desordenados. O programa imprime a lista antes e depois de ser ordenada pela função bubble_sort.

### Observações

O Bubble Sort funciona bem para listas pequenas ou para fins de aprendizado, mas não é a melhor escolha para listas grandes. Algoritmos como Quick Sort ou Merge Sort são mais eficientes para grandes volumes de dados.

### Agradecimetos

Obrigado por ler até aqui! Se você tiver qualquer feedback, sugestão de melhoria ou identificar qualquer erro, não hesite em entrar em contato. Seu feedback é muito valioso para mim e me ajuda a melhorar continuamente. Obrigado mais uma vez por visitar este repositório!