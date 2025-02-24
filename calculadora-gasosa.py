# Entrada de dados
preco_gasosa = float(input("Digite o preço da gasolina: R$ "))
quilometros_por_litro = float(input("Digite a quilometragem por litro: "))
distancia = float(input("Digite a distância a ser percorrida (apenas um sentido): "))
ida_volta = input("Ida e volta? (S/N): ").strip().upper()

if ida_volta == 'S':
    distancia_total = distancia * 2
else:
    distancia_total = distancia

manutencao = float(input("Digite as despesas de manutenção por mês: R$ "))
dias = int(input("Digite o número de dias que o trajeto será feito: "))

# Custo com combustível para o trajeto (considerando a distância total definida)
custo_combustivel = (distancia_total / quilometros_por_litro) * preco_gasosa

# Custo de manutenção diluído por dia (assumindo que a despesa mensal é para os dias informados)
custo_manutencao_por_viagem = manutencao / dias

# Custo total da viagem para um dia
custo_viagem = custo_combustivel + custo_manutencao_por_viagem

# Custo por quilômetro
custo_por_quilometro = custo_viagem / distancia_total

# Custo total considerando os dias informados
custo_total_dias = custo_viagem * dias

print("\n ========================================================= \n")

print(f"O custo total da viagem (por dia) será de R$ {custo_viagem:.2f}")
print(f"O custo por quilômetro será de R$ {custo_por_quilometro:.2f}")
print(f"O custo total da viagem em {dias} dias será de R$ {custo_total_dias:.2f}")
