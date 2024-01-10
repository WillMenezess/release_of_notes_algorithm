print("""Seja Bem Vindo Professor Alessandro Bertolani Oliveira!!
      Leitura de Notas do Curso EAD Da Universidade Vila Velha:
      Leitura de Pauta:\n""")

indice = 0
Alunos = 100
APROVADOS = 0
REPROVADOS = 0
MM = 0
PROVAREC = 0

while indice < Alunos:
    indice += 1
    AOP1 = float(input(f'Nota [0,1] da 1º AOP do Aluno {indice}:'))
    while AOP1 < 0 or AOP1 > 1:
        print('Erro na Digitação da nota da AOP1 [0,1]. Tente Novamente.')
        AOP1 = float(input(f'Nota [0,1] da 1º AOP do Aluno {indice}:'))
    AOP2 = float(input(f'Nota [0,2] da 2º AOP do Aluno {indice}:'))
    while AOP2 < 0 or AOP2 > 2:
        print('Erro na Digitação da nota da AOP2 [0,2]. Tente Novamente.')
        AOP2 = float(input(f'Nota [0,2] da 2º AOP do Aluno {indice}:'))
    AOP3 = float(input(f'Nota [0,1] da 3º AOP do Aluno {indice}:'))
    while AOP3 < 0 or AOP3 > 1:
        print('Erro na Digitação da nota da AOP3 [0,1]. Tente Novamente')
        AOP3 = float(input(f'Nota [0,1] da 3º AOP do Aluno {indice}:'))
    PROVA = float(input(f'Nota [0,6] da Prova Regular do Aluno {indice}:'))
    while PROVA < 0 or PROVA > 6:
        print('Erro na Digitação da nota da Prova Regular [0,6]. Tente Novamente')
        PROVA = float(input(f'Nota [0,6] da Prova de Recuperação do Aluno {indice}:'))
    MM = AOP1 + AOP2 + AOP3 + PROVA 
    if MM < 7:
        PROVAREC = float(input(f'Nota[0,10] da Prova de Recuperação do Aluno {indice}:'))
        while PROVAREC < 0 or PROVAREC > 10:
            print('Erro na Digitação da nota da Prova Regular [0,10]. Tente Novamente')
            PROVAREC = float(input(f'Nota[0,10] da Prova de Recuperação do Aluno {indice}:'))
    MG = (MM + PROVAREC) / 2
    if MM >= 7 or MG >= 5:
        print(f'O aluno {indice} foi [APROVADO]')
        APROVADOS += 1
    else:
        print(f'O aluno {indice} foi [REPROVADO]')
        REPROVADOS += 1
        
print(f"{(APROVADOS*100/Alunos):.2f}% dos alunos foram aprovados.")
print(f"{(REPROVADOS*100/Alunos):.2f}% dos alunos foram reprovados.")
print('Sua pauta foi concluída com sucesso! Tenha um bom dia!')



