def graus_farenheit(f):
    centigrados = (5/9)*(f-32)
    return centigrados
def main():
    for f in range(50,151):
        c = graus_farenheit(f) 
        print(f"{f},{c :.2f}")
if __name__ == "__main__":
    main()

