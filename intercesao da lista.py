def intercesao(a,b):
    intercesao = []
    for i in range(len(a)):
        if a[i] in b and a[i]:
            intercesao.append(a[i])
    return intercesao
def main():
    a = [2,4,6,8,10,12]
    b = [2,3,5,10,7,11]
    c = intercesao(a,b)
    print("a:",a)
    print("b:",b)
    print(f"intercesão das lista{c}")
if __name__ == "__main__":
    main()