velocidade = 61 #velocidade atual do carro
local_carro = 102 #local aonde o carro está

radar_1 = 60 #velocidade maxima do radar
local_1 = 100 #local do radar
radar_area = 3 #area de reconhecimento do radar

carro_multado = velocidade>radar_1
carro_passou_no_radar =  local_carro >=(local_1-radar_area) and local_carro <= (local_1 +radar_area)

if carro_multado:
    print("A velocidade do carro passou do radar 1")

if carro_multado and carro_passou_no_radar:
    print("O carro foi multado")

'''
Ou seja, oque aconteceu o carro estava em uma velocidade mais alta do radar (60),
se caso o carro estivesse na posição do radar (local_radar - area_radar = 97 and local_radar +area_radar 103),
e estivesse acima da velocidade maxima do radar o carro será multado
'''
