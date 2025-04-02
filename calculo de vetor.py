def vetorial(a,b):
    for i in range(len(a) or len(b)):
        x = a[1] * b[2] - a[2] * b[1]
        y = a[2] * b[0] - a[0]*b[2]
        z = a[0]*b[1] - a[1]*b[0]
        return [x,y,z]
def main():
    e=[]
    f = []
    for i in range (3):
        c = int(input("digite  seu vetor A: "))
        d = int(input("digite seu vetor B:"))
        e.append(c)
        f.append(d)
    resultado = vetorial(e,f)
    print(f"o resultado do produto vetorial de {e} e {f} é {resultado}")
main()