# Exercicios-criaçao-e-operaçoes-com-Matrizes
Objetivo: Criar uma aplicação gráfica em Python com tkinter que gere duas matrizes quadradas com valores inteiros aleatórios, permita somar, subtrair ou multiplicar as matrizes e exiba os resultados em janelas organizadas.


Algoritmo: 

Recebe uma variável

Função tamanhoMatriz(n)

tamanhoMatriz(num):

    converte num em int
    se for inteiro:
        Função gerandoMatriz(num)
    se não for:
        Exibe mensagem de erro

gerandoMatriz(num):

    Cria duas listas vazias
    Para cada linha cria listas com números aleatórios entre -100 e 100:
        Adicionar linha à matriz
    Função mostrar_matrizes(matriz1, matriz2)

mostrar_matrizes(a,b):

    Função exibir matriz(a, frame_a)
    Função exibir matriz(b, frame_b)
    Criar botões com chamadas:
        Função soma(a,b)
        Função sub(a,b)
        Função mult(a,b)
    
soma(a,b):

    criar matriz resultado
    somar os elementos de todas as listas dentro das matrizes em seus respectivos indices 
    Função exibir_matriz(a,b)

sub(a,b):

    criar matriz resultado
    subtrair os elementos de todas as listas dentro das matrizes em seus respectivos indices 
    Função exibir_matriz(a,b)

mult(a,b):

    criar matriz resultado
    multiplicar os elementos de todas as listas dentro das matrizes em seus respectivos indices 
    Função exibir_matriz(a,b)
    
exibir matriz(matriz, frame):

    para cara linha na matriz:
        criar e posicionar o número na grade correspondente
