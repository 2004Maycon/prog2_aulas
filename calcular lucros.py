def main():
    nome_mercadoria = str(input("digite o nome do seu produto"))
    cont_menor10= 0
    cont_entre10_20=0
    cont_maior20 = 0
    totaldevenda= 0
    totaldecompra=0
    while nome_mercadoria != "":
        preço_compra = int(input("preço de compra"))
        preço_venda = int(input("preço de venda"))
        lucro = ((preço_venda - preço_compra)/preço_compra)*100
        if  lucro <10:
            cont_menor10+=1
        elif lucro >=10 or lucro <= 20:
            cont_entre10_20+=1
        elif lucro <=20:
            cont_maior20+=1
        totaldecompra+=preço_compra
        totaldevenda+=preço_venda
        nome_mercadoria = str(input("digite o nome do seu produto"))
    totaldelucro=totaldevenda - totaldecompra
    print(f"lucros <10% {cont_menor10 :.2f}")
    print(f"lucros entre <10%  e >20% {cont_entre10_20:.2f}")
    print(f"lucros <20% {cont_maior20:.2f}")
    print(f"total de compras {totaldecompra:.2f}")
    print(f"total de vendas {totaldevenda:.2f}")
    print(f"total de lucros {totaldelucro:.2f}")        

    return 0 
if __name__ == "__main__":
    main()