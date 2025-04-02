def ausecia_aluno(turma):
    cont_falta=0
    cont_aluno = 0
    cont_faltab = 0
    cont_faltac = 0
    while turma != "":
        if turma == "a":
            cont_faltaa+=1
        elif turma == "b":
            cont_faltab+=1
        else:
            cont_faltac+=1
    turma_a = cont_faltaa/100
    turma_b = cont_faltab/100
    turma_c = cont_faltac/100
    return turma_a , turma_b , turma_c
def main():
    turma = str(input("digite turma A,B,C"))
    turma_A = ausencia_aluno(turma)
    turma_B = ausencia_aluno(turma)
    turma_C = ausencia_aluno(turma)
    print(f'{turma_A}%')
    print(f'{turma_B}%')
    print(f'{turma_C}%')
main()