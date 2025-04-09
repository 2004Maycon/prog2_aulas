import random
def matriz(linha,coluna,minimo,maximo):
    criar_matriz= []
    for i in range(linha):
        list_coluna = []
        for j in range(coluna):
            list_coluna.append(random.randint(minimo,maximo))
        criar_matriz.append(list_coluna)
    return criar_matriz
def print_matriz(criar_matriz):
    linha = len(criar_matriz)
    coluna = len(criar_matriz[0])
    for i in range(linha):
        for j in range(coluna):
            print(criar_matriz[i][j],end=" ")
        print()
def main():
    quantidade_de_linhas = int(input("digite quantas linhas voce quer "))
    quantidade_coluna = int(input("quantas colunas "))
    min = int(input("qual parametro de numeros "))
    max = int(input("qual parametro de numeros "))
    retornar_matriz  = matriz(quantidade_de_linhas,quantidade_coluna,min,max)
    print_matriz(retornar_matriz)
main()