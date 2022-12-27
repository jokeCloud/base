"""
CONSTANTE = "Variáveis" que não vão mudar
muitas condições no mesmo if    (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 101

RADAR_1 = 60    # velocidade máxima do radar 1
LOCAL_1 = 100   # local onde o radar 1 está
RADAR_RANGE = 1  # a distância onde o radar pega

if local_carro and velocidade:
    if velocidade > RADAR_1:
        totalizador = LOCAL_1 + RADAR_RANGE
        if local_carro >= LOCAL_1 and local_carro <= totalizador:
            print(
                f'Passou do limite, veículo à {velocidade} km/h. '
                f'Velocidade permitida de {RADAR_1}km/h neste radar.'
            )
    else:
        print(
            f'Veículo à {velocidade} km/h. '
            f'Velocidade permitida de {RADAR_1}km/h neste radar.'
        )


vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('CArro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')
