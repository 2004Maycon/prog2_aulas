def uniao(a,b):
    uniao = []
    uniao = a
    for elem in  b:
        if elem not in uniao:
            uniao.append(elem)
    return uniao
def main():
    a = [2,4,6,8,10,12]
    b = [2,3,5,10,7,11]
    c = uniao(a,b)
    print("a:",a)
    print("b:",b)
    print(f"uniao das lista{c}")
if __name__ == "__main__":
    main()