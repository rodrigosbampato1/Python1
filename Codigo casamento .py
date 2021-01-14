from pprint import pprint
from datetime import datetime
arrDatasDisponiveis=[]
qtdCasamDiponiveis=[]
arrDatascasamentoAgendadas=[]
arrNomeNoivos=[]


# Função para vericar existencia data repetida
def isDateExists(nova_data , datas) :
    for data in datas:
        if nova_data == data :
            return True
    return False  

# Cadastro de Datas de Casamento 

while True:
    nova_data= input("Digite a nova data para cadastro ou digite sair (dd/mm/aaaa):")
    if nova_data =="sair":
        break
    if isDateExists(nova_data , arrDatasDisponiveis) == True:
        print("Data ja Cadastrada") 
        continue
    arrDatasDisponiveis.append (nova_data) 
    qtdCasamDiponiveis.append (int(input("Digite a Quantidade de casamentos possiveis para data : ")))
    print("Data Cadastrada")
# Cadastro dos Noivos
while True:
    nome_casal= input("Digite o nome do casal, ou digite sair:")
    if nome_casal =="sair":
        break

    dataCasamento = input("Digite a data de casamento:")
    if isDateExists(dataCasamento , arrDatasDisponiveis) == False:
        print("Data de casamento não Disponível!") 
        continue
    else:
        # vericar a quantidade de casamentos disponiveis
        # considerando 
        idx = arrDatasDisponiveis.index(dataCasamento)
        if qtdCasamDiponiveis[idx] > 0:
            arrDatascasamentoAgendadas.append(dataCasamento)
            arrNomeNoivos.append(nome_casal)
            qtdCasamDiponiveis[idx] = qtdCasamDiponiveis[idx] - 1
            print("Casamento Agendado com sucesso!")
        else:
            print("Quantidade de casamento Indisponivel") 
