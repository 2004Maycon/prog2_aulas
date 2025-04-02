import random
def multiplicar_lista(lista):
    resultado = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            elemento2 =lista[j]
            elemento = lista[i] 
            resultando = elemento * elemento2
            if resultando in lista:
                resultado.append(resultando) 
                print(f"{elemento} X {elemento2}")
    return resultado
def main():
    l = [1,2,3,4,5,6,7,8,9,10]
    final = multiplicar_lista(l)
    print(l)
    print(f"{final}")
if __name__ == "__main__":
    main()
