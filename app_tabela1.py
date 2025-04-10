def main():
    tabela = []
    for i in range (5):
        lst_prod = []
        strprod = input("entre com o produto: ")
        lst_prod = strprod.split(",")
        lst_prod[3]= float(lst_prod[3])
        lst_prod[4] = int(lst_prod[4])
        tabela.append(lst_prod)
    print("*"*60)
    for produto in tabela:
        for atributo in produto:
            print(atributo,",",end=" ")
            print()
main()
     