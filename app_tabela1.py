def letabela():
    tabela = []
    for i in range (5):
        lst_prod = []
        strprod = input("entre com o produto: ")
        lst_prod = strprod.split(",")
        lst_prod[3]= float(lst_prod[3])
        lst_prod[4] = int(lst_prod[4])
        tabela.append(lst_prod)
    return tabela
def print_tabela(tabela):
    for produto in tabela:
        for atributo in produto:
            print(atributo,",",end=" ")
        print()
def prodmaiorquant(tabela):
    prodmaior = []
    maior_quant = tabela[0][len(tabela[0]-1)]
    for i in range(1,len(tabela)):
        if tabela[i][-1] > maior_quant:
            maior_quant = tabela[i][-1]
            prodmaior = tabela[i]
    return prodmaior
def print_produto(prod):
    print("id",prod[0])
    print("nome",prod[1])
    print("fabricante",prod[2])
    print("preço",prod[3])
    print("quantidade",prod[4],"/n")

def main():
    tabela =letabela()
    print()
    print("*"*60)
    print_tabela(tabela) 
    prod_maior_quant = prodmaiorquant(tabela)
    print_produto(prod_maior_quant) 
main()
     