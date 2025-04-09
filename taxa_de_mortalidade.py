def main():
    numero_crianças_nascidas= int(input("numero de crianças nascidos: "))
    criança_morta = 0
    mas_morta = 0
    viva_24oumenos = 0
    for i in range(numero_crianças_nascidas):
        sexo_criança = str(input("digite m ou f: "))
        while sexo_criança != "":
            messes_nascido = int(input("digite a quantidade de meses: "))
            if sexo_criança == "m":
                mas_morta += 1
            elif messes_nascido > 0 :
                criança_morta += 1
                if sexo_criança == "m":
                    mas_morta += 1
                if messes_nascido <= 24:
                    viva_24oumenos +=1
        sexo_criança = str(input("digite m ou f: "))
    porcentagem_morta = (criança_morta/numero_crianças_nascidas)*100
    porcentagem_mas = (mas_morta/criança_morta)*100
    porcentagem_vivo= (viva_24oumenos/criança_morta)*100
    print(f"total de crianças mortas: {porcentagem_morta}%")
    print(f"total de crianças mortas masculina : {porcentagem_mas}%")
    print(f"total de crianças vivas: {porcentagem_vivo}%")  
if __name__ == "__main__":
    main()