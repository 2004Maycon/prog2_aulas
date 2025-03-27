def main():
    cont_m = 0
    cont_f = 0
    alt =0
    maior_altura= -9999
    menor_altura = 9999
    for i in range(5):
        altura = float(input())
        sexo = str(input()).upper()
       
        if altura > maior_altura:
            maior_altura = altura
        if altura < menor_altura:
            menor_altura = altura 
        if sexo == "M":
            cont_m+=1
        if sexo == "F":
            alt += altura
            cont_f += 1
    media_f = alt/cont_f
    print("maior altura",maior_altura)
    print("menor altura",menor_altura)
    print(f"media,{media_f :.2f}")
    print("numeros de homens",cont_m)
    return 0
if __name__ == "__main__":
    main()

    
