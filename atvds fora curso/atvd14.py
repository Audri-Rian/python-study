import math

# Solicita o tamanho da área a ser pintada
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calcula a quantidade total de tinta necessária, considerando 10% de folga
litros_necessarios = (area / 6) * 1.1

# Calcula a quantidade de latas de 18 litros necessárias
latas_18L = math.ceil(litros_necessarios / 18)
custo_latas_18L = latas_18L * 80

# Calcula a quantidade de galões de 3,6 litros necessários
galoes_3_6L = math.ceil(litros_necessarios / 3.6)
custo_galoes_3_6L = galoes_3_6L * 25

# Calcula a mistura de latas e galões para minimizar o desperdício
latas_mistura = int(litros_necessarios // 18)
restante = litros_necessarios % 18
galoes_mistura = math.ceil(restante / 3.6)
custo_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

# Exibe os resultados
print("\nOpções de compra:")
print(f"1. Apenas latas de 18 litros: {latas_18L} lata(s), Custo: R$ {custo_latas_18L:.2f}")
print(f"2. Apenas galões de 3,6 litros: {galoes_3_6L} galão(ões), Custo: R$ {custo_galoes_3_6L:.2f}")
print(f"3. Mistura de latas e galões: {latas_mistura} lata(s) e {galoes_mistura} galão(ões), Custo: R$ {custo_mistura:.2f}")
