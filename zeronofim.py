import random
def zero_no_final(lst):
    j = []
    n = []
    for i in range (len(lst)):
        if lst[i] != 0:
            n.append(lst[i])
        else:
            j.append(lst[i])
        
    zero_final = n+j
    return zero_final
def main():
    l =[random.randint(0,100) for _ in range(20)]
    print(l)
    print(zero_no_final(l))
if __name__ == "__main__":
    main()