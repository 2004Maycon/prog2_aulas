import random
def matriz(linha,coluna,minimo,maximo):
    criar_matriz= []
    for i in range(linha):
        list_coluna = []
        for j in range(coluna):
            list_coluna.append(random.randint(minimo,maximo))
        criar_matriz.append(list_coluna)
    print(criar_matriz[i][j],end="")
    print()
    return criar_matriz
def trocar_coluna (criar_matriz):
    col_A= []
    col_b = []
    aux = []
    linha = len(criar_matriz)
    coluna = len(criar_matriz[0])
    if coluna > 2 :
        for i in range(linha):
            aux.append(criar_matriz[i][0])
            criar_matriz[i][0] = criar_matriz[i][3]
            criar_matriz[i][3] = aux[i]
        return criar_matriz
        print()
def print_matriz(criar_matriz):
    linha = len(criar_matriz)
    coluna = len(criar_matriz[0])
    for i in range(linha):
        for j in range(coluna):
           print(criar_matriz[i][j],end="  ")
        print()

def main():
    quantidade_de_linhas = int(input("digite quantas linhas voce quer "))
    quantidade_coluna = int(input("quantas colunas "))
    min = int(input("qual parametro de numeros "))
    max = int(input("qual parametro de numeros "))
    retornar  = matriz(quantidade_de_linhas,quantidade_coluna,min,max)
    coluna_trocada =trocar_coluna(retornar)
    print_matriz(coluna_trocada)
    print(f"coluna trocada{print_matriz}")
main()