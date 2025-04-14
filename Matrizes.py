import tkinter as tk
import random

def soma(a,b):
    somar = tk.Tk()
    somar.title("Matriz gerada")
    somar.geometry("300x200")
    label_somar = tk.Label(somar, text="Resultado da Soma:", font=("Arial", 12, "bold"))
    label_somar.grid(row=0, column=0, padx=10, pady=10)
    frame_a = tk.Frame(somar)
    frame_a.grid(row=1, column=0, padx=10)
    matriz_resultado = []
    for i in range(len(a)):
        linha = []
        for j in range(len(a[0])):
            numero= a[i][j] + b[i][j]
            linha.append(numero)
        matriz_resultado.append(linha)
    exibir_matriz(matriz_resultado, frame_a)
    somar.mainloop()

def sub(a,b):
    sub = tk.Tk()
    sub.title("Matriz gerada")
    sub.geometry("300x200")
    label_somar = tk.Label(sub, text="Resultado da Subtração:", font=("Arial", 12, "bold"))
    label_somar.grid(row=0, column=0, padx=10, pady=10)
    frame_a = tk.Frame(sub)
    frame_a.grid(row=1, column=0, padx=10)
    matriz_resultado = []
    for i in range(len(a)):
        linha = []
        for j in range(len(a[0])):
            numero= a[i][j] - b[i][j]
            linha.append(numero)
        matriz_resultado.append(linha)
    exibir_matriz(matriz_resultado, frame_a)
    sub.mainloop()

def mult(a,b):
    mult = tk.Tk()
    mult.title("Matriz geradas")
    mult.geometry("300x200")
    label_somar = tk.Label(mult, text="Resultado da Multiplicação:", font=("Arial", 12, "bold"))
    label_somar.grid(row=0, column=0, padx=10, pady=10)
    frame_a = tk.Frame(mult)
    frame_a.grid(row=1, column=0, padx=10)
    matriz_resultado = []
    for i in range(len(a)):
        linha = []
        for j in range(len(a[0])):
            numero= a[i][j] * b[j][i]
            linha.append(numero)
        matriz_resultado.append(linha)
    exibir_matriz(matriz_resultado, frame_a)
    mult.mainloop()

def tamanhoMatriz():
    valor_digitado = entradaTam.get()
    try:
        tamanhoM = int(valor_digitado)  # converte para inteiro
        gerandoMatriz(tamanhoM)
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

def exibir_matriz(matriz, frame):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            celula = tk.Label(frame, text=str(matriz[i][j]), width=5, height=2, relief="ridge", borderwidth=1)
            celula.grid(row=i, column=j, padx=2, pady=2)

def gerandoMatriz(num):
    matriz1= []
    matriz2 =[]
    for linha in range(num):
        linha = []
        for coluna in range(num):
            numero= random.randint(-100, 100)
            linha.append(numero)
        matriz1.append(linha)
    for linha in range(num):
        linha = []
        for coluna in range(num):
            numero= random.randint(-100, 100)
            linha.append(numero)
        matriz2.append(linha)
    mostrar_matrizes(matriz1, matriz2)
    
def mostrar_matrizes(a,b):
    aba.destroy()
    nova = tk.Tk()
    nova.title("Matrizes geradas")
    nova.geometry("250x250")
    label_a = tk.Label(nova, text="Matriz A", font=("Arial", 12, "bold"))
    label_a.grid(row=0, column=0, padx=10, pady=10)
    label_b = tk.Label(nova, text="Matriz B", font=("Arial", 12, "bold"))
    label_b.grid(row=0, column=1, padx=10, pady=10)
    frame_a = tk.Frame(nova)
    frame_a.grid(row=1, column=0, padx=10)
    frame_b = tk.Frame(nova)
    frame_b.grid(row=1, column=1, padx=10)
    exibir_matriz(a, frame_a)
    exibir_matriz(b, frame_b)
    botaoSoma = tk.Button(nova, text="Somar", command= lambda: soma(a,b))
    botaoSoma.grid(row= 2, column= 0, padx=10)
    botaoSub = tk.Button(nova, text="Subtrair", command= lambda: sub(a,b))
    botaoSub.grid(row= 3, column= 0, padx=10)
    botaoMult = tk.Button(nova, text="Multiplicar", command= lambda: mult(a,b))
    botaoMult.grid(row= 4, column= 0, padx=10)
    nova.mainloop()

aba = tk.Tk()
aba.title("Matrizes")
aba.geometry("600x100")
label = tk.Label(aba,text= "Escolha o tamanho da matriz quadrada a ser gerada:")
label.pack()
entradaTam = tk.Entry(aba)
entradaTam.pack()
botao = tk.Button(aba, text="Confirmar", command= tamanhoMatriz)
botao.pack()
aba.mainloop()