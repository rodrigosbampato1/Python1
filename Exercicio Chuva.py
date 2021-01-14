dias=[]
vol=[]
media=0
quarta=0
i=0

for i in range (10):
    dias.append (input("Digite o dia da semana :" ))
    vol.append(float(input("Digite o volume de chuva :")))
    
soma=0
for vol in dias:
    soma == soma + vol

media = soma/len(dias)

while  i <10 :
    total += vol[i]
    if dias[i] == 'quarta-feira':
        quarta += vol[i]
    i += 1

    media = quarta / dias.count('quarta-feira')

    print("total  média ".format(total , media))