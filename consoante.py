def consoante_cont(l):
    cont = 0
    for name  in l:
        for j in name :
            if j and j not in "AEIOU":
                cont+=1
    return cont
def main():
    list_nome =[]
    nome = str(input("digite o nome: ")).upper().strip()
    while nome != "":
        list_nome.append(nome)
        nome = str(input("digite o nome: ")).upper().strip()
    for i in range(len(list_nome)):
        consoante = consoante_cont(list_nome[i])
        print(f"{list_nome[i]}:{consoante}")
main()