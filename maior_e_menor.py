import random
def F_maior(lst):
    
    maior = -9999
    for i in range(len(lst)):
        if lst[i] > maior:
            maior = lst[i]
            i+=1
    return maior
def F_menor(lst):
    menor = 9999
    for i in range(len(lst)):
        if lst[i]< menor:
            menor = lst[i]
            i+=1
    return menor
def main():
    menor_lista = 0
    maior_lista=0
    l = [random.randint(1,50)  for _ in range(19)]
    maior_lista = F_maior(l)
    menor_lista = F_menor(l)
    print(l)
    print(maior_lista) 
    print(menor_lista)
if __name__ == "__main__":
    main()