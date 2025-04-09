def produto_fem(sex, resposta):
    respondeu_sim=0
    cont_fi=0
    cont_f=0
    for resposta in "sim":
        respondeu_sim +=1        
        if sex in "f":
            cont_fi +=1
    porcentagem_f = ((cont_fi)/respondeu_sim) 
    return respondeu_sim,porcentagem_f
def produto_mas(sex,resposta):
    respondeu_nao=0
    cont_mi=0
    cont_m = 0 
    for resposta in "nao":
        respondeu_nao += 1
        if sex in "m":
            cont_mi +=1           
    porcentagem_m = ((cont_mi)/respondeu_nao)
    return respondeu_nao,porcentagem_m
def main():
    for i in range(6):
        sexo = str(input("qual a sua sexualidade: "))
        resposta = str(input("resposta sim/nao: "))
    contadores_f =produto_fem(sexo,resposta)
    contadores_m = produto_mas(sexo,resposta)
    print(contadores_m)
    print(contadores_f)
main()