def f_crecimento(a,b):

    porc_a= 3
    porc_b = 1.5
    cont_ano = 0
    while b < a:
        a+= (a*porc_a)/100
        b+= (b*porc_b)/100
        cont_ano+=1
    return cont_ano
    

def main():
    a = 90000000
    b = 20000000
    print(f"falta {f_crecimento(a,b)} Anos para que a população do país A ultrapasse ou iguale a população do país B")
if __name__ == "__main__":
    main()