def F_material_radiativo(massa):
    tempo = 0
    while massa >= 0.5:
        massa = massa/2
        tempo+=50
    hora = tempo // 3600
    minutos= ( tempo%3600)//60
    segundos = (tempo%60)
    tempo =(f"tempo {hora}h{minutos}min{segundos}seg")
    return massa,tempo
def main():
    massa_inicial = float(input("digite sua massa inicial: "))
    massa_final,tempo_total= F_material_radiativo(massa_inicial)
    massa_final , tempo = F_material_radiativo(massa_inicial)
    print(f"a massa inicial: {massa_inicial}g")
    print(f"a massa final : {massa_final}g")
    print(f" o tempo {tempo_total}")
main()


