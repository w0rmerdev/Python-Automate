#Automatizar o processo de criação de pastas e ficheiros para resolução de exercicíos 

import os

diretoria = str(input("diretoria: "))

nome_pasta = str(input("nome da pasta: "))

diretoria_nova_pasta = '/home/tomas/' + diretoria + '/' + nome_pasta

nome_ficheiro = str(input("nome do ficheiro, sem número ou terminação: "))

numero_exercicios = int(input("num total de exercícios: "))

terminacao = str(input("terminação da linguagem : "))

os.mkdir(diretoria_nova_pasta)
    
for i in range(1, numero_exercicios + 1):

    with open("/home/tomas/Desktop/uni/1ºAno/Semestre_Impar/P1/Exercicios/default.c") as f:
       
        lines = f.readlines()
        lines = [l for l in lines]
        
        with open(diretoria_nova_pasta + '/' + nome_ficheiro + str(i) + "." + terminacao, "x") as f1:
            
            f1.writelines(lines)

print("Done!!")
