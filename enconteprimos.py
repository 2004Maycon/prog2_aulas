import random
def F_primos(num):
    if num == 1:
        return False
    cont_exata = 0
    for d in range(1,num+1):
        if (num % d ) == 0:
            cont_exata +=1
    return cont_exata == 2
        
def inteiro(a):
    l_primos = []
    for elem in a:
        if F_primos(elem):
            l_primos.append(elem)
    return l_primos



def main():
    l=[1,2,3,4,20,40,80,100,5,7,9,10,8]
    primos= inteiro(l)
    print(l)
    print(primos)
 
if __name__ == "__main__":
    main()