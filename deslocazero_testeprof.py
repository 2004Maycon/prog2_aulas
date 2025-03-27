def deslocazero(l):
    for i in range(len(l)):
        if l[i] == 0:
           j = i
           for k in range(j+1,len(l)):
               l[j] = l[k]
               j+=1
           l[-1] = 0    
    return l            
def main():
    lst = [17,0,5,3,0,9,4,0,53,32]
    print("antes:",lst)
    deslocazero(lst)
    print("depois:",lst)
main()