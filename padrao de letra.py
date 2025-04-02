def padrao(m):
    lista =[]
    if m[0] not in"AEIOU" and m[1] == "A": 
        for i in range(len(m)):
            if m[i] =="O":
                texto = m[i]
                if m not in "AEIOU" and m[i]== "O":
                    lista.append(texto)
    return lista
def main():
    k =  str(input()).upper().strip(".,;:!")
    l = padrao(k)
    print(k)
    print(l)
if __name__ == "__main__":
    main()


