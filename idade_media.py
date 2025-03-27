def media_idade(a):
    cont = 0
    idade = int(input())
    idade_t =  0
    while idade > 0 :
        cont +=1
        idade_t += idade
        idade = int(input())
    media_total= idade_t / cont

    return media_total
def main():
    media = media_idade("")
    print("A media de idades é ",media)
main()