#Quantos atendiemtos foram realizados?
#Quantos foram do tipo consulta?
#O valor total arrecadado
#O valor mé dio dos atendimentos

import csv

numero_de_atendimentos = 0
numero_de_consutas = 0
valor_total_arrecadado = 0
valor_médio_atendimentos = 0

with open('exercicio.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        numero_de_atendimentos += 1
        if linha['tipo'].strip() == 'Consulta':
            numero_de_consutas += 1
        valor_total_arrecadado += int(linha['valor'])
        valor_médio_atendimentos = valor_total_arrecadado/numero_de_atendimentos



    print(f'o numero de antendimentos foi de {numero_de_atendimentos}')
    print(f'o numero de consultas foi de {numero_de_consutas}')
    print(f'o numero de consultas foi de {valor_total_arrecadado}')
    print(f'o valor medio de atendimentos foi de {round(valor_médio_atendimentos)}')
#teste
    

