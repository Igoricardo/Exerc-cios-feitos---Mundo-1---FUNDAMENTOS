d = int(input('Informe por quantos dias você alugou o veículo:'))
km = float(input('Informe quantos KM rodados com o veículo:'))
print('O veículo foi alugado por {:.2f} dias e rodou cerca de {} km. Por tanto o valor do aluguel é R$ {:.2f} reais.'.format(d, km, d*60 + km*0.15))
