import time
from random import *
import os


# Define as tensões de calibração para sensores de pH
tensaoAcido = 942.0
tensaoNeutra = 1650.0

# Variáveis de calibração
calibracao_saturacao = 1600
calibracao_temperatura = 25

# Constantes Calculo
tensao_volts = 3.3
resolucao_analogico_digital = 4096.0
offset_milivolts = 1500.0
ph_neutro = 7.0
ph_acido = 4.0
concentracao_maxima_ppm = 1200
leitura_sensor_maxima = 1023

QUALIDADE_ALTA = 3
QUALIDADE_MEDIA = 2
QUALIDADE_BAIXA = 1
QUALIDADE_PESSIMA = 0

QUALIDADES_DO_AR = [
    "Péssima",
    "Ruim",
    "Regular",
    "Boa",
]

QUALIDADES_AGUA = [
    "Perigo, água ácida",
    "Perigo, água alcalina",
    "PH Neutro",
    "Excelente!",
]


solucoes_melhorar_o_oceano = [
    "reduzindo o lixo plástico",
    "fazendo descarte correto de lixos quando estiver na praia",
    "participando de mutirões de limpeza",
    "evitando o uso de embalagem plásticas como sacolas e garrafas"
]

solucoes_melhorar_o_ar = [
    "utilizando transporte público",
    "plantando árvores na sua região",
    "reduzindo o uso de veículos a combustão",
    "utilizando energia limpa como solar e eólica"
]

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
WHITE = '\033[37m'
RESET = '\033[0m'

def exibir_com_cor(text, cor):
    print(cor + text + RESET)


def calcular_ph_agua(leituraPH):
    # Valores calculados para o cálculo do pH, de acordo com valores obtidos em sensores do arduino
    tensaoPH = leituraPH * (tensao_volts / resolucao_analogico_digital)
    declive = (ph_neutro - ph_acido) / ((tensaoNeutra - offset_milivolts) / 3.0 - (tensaoAcido - offset_milivolts) / 3.0)
    interceptacao = ph_neutro - declive * (tensaoNeutra - offset_milivolts) / 3.0
    pH = declive * (tensaoPH - offset_milivolts) / 3.0 + interceptacao
    return pH

def calcular_condutividade_eletrica(leitura_condutividade, temperatura):
    # Cálculo da condutividade elétrica (CE) da água a partir da leitura do sensor de condutividade elétrica
    tensao_cond_eletrica = leitura_condutividade * (tensao_volts / resolucao_analogico_digital)
    cond_eletrica = tensao_cond_eletrica / (1.0 + 0.0185 * (temperatura - 25.0))
    return cond_eletrica
    
def calcular_monoxido_de_carbono(leitura_mc):
    ppm_por_unidade = concentracao_maxima_ppm / leitura_sensor_maxima
    monoxido_carbono = ppm_por_unidade * leitura_mc
    return round(monoxido_carbono)

def obter_qualidade_da_agua(valor_ph):
    if 6.5 <= valor_ph <= 8.5:
        return QUALIDADE_ALTA
    elif valor_ph == 7:
        return QUALIDADE_MEDIA
    else:
        return QUALIDADE_PESSIMA

def obter_qualidade_do_ar(monoxido_de_carbono):
    if monoxido_de_carbono <= 350:
        return QUALIDADE_ALTA
    elif 350 < monoxido_de_carbono <= 800:
        return QUALIDADE_MEDIA
    elif 800 < monoxido_de_carbono <= 1200:
        return QUALIDADE_BAIXA
    else:
        return QUALIDADE_PESSIMA
    
def obter_qualidade_de_acordo_com_valor(valor, valores_qualidade):
    if valor == QUALIDADE_PESSIMA:
        return RED + valores_qualidade[QUALIDADE_PESSIMA] + RESET
    elif valor == QUALIDADE_BAIXA:
        return YELLOW + valores_qualidade[QUALIDADE_BAIXA] + RESET
    elif valor == QUALIDADE_MEDIA:
        return WHITE + valores_qualidade[QUALIDADE_MEDIA] + RESET
    else:
        return GREEN + valores_qualidade[QUALIDADE_ALTA] + RESET

def exibir_solucoes_se_necessario(mensagem, qualidade, solucoes):
    if qualidade < QUALIDADE_MEDIA:
        print(mensagem + solucoes[qualidade])


def obter_maximo(valor1, valor2):
    if valor1 > valor2:
        return valor1
    else:
        return valor2

def limpar_terminal():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Unix
        os.system('clear')

temperatura = randint(0, 40)
leituraPH = randint(0, 7000)
leitura_condutividade_eletrica = randint(0, 5000)
leitura_oxigenio = randint(0, 5000)
leitura_monoxido_carbono = randint(10, 1200)
while True:
    # Valores random para simular sensores de leitura
    # Utiliza a leitura anterior para não variar muito
    temperatura = obter_maximo(0, temperatura + randint(-3, 3))
    temperatura = min(temperatura, 45)  # garante que a temperatura não ultrapasse 45 graus
    leituraPH = randint(0, 7000) #obter_maximo(0, leituraPH + randint(-100, 100))
    leitura_condutividade_eletrica = obter_maximo(0, leitura_condutividade_eletrica + randint(-50, 50))
    leitura_oxigenio += obter_maximo(0, randint(-50, 50))
    leitura_monoxido_carbono += obter_maximo(0, randint(-50, 50))
    
    # Exibindo os valores
    valor_pH = calcular_ph_agua(leituraPH)
    condutividadeEletrica = calcular_condutividade_eletrica(leitura_condutividade_eletrica, temperatura)
    monoxido_de_carbono = calcular_monoxido_de_carbono(leitura_monoxido_carbono)
    
    qualidade_da_agua = obter_qualidade_da_agua(valor_pH)
    qualidade_do_ar = obter_qualidade_do_ar(monoxido_de_carbono)

    print("Temperatura:", temperatura, "°C")
    print(f"pH: {valor_pH:.2f}")
    print(f"Condutividade Elétrica: {condutividadeEletrica:.2f} mS/cm")
    print(f"Monóxido de Carbono: {monoxido_de_carbono:.2f} ppm")
    print(f"Qualidade da Água: {obter_qualidade_de_acordo_com_valor(qualidade_da_agua, QUALIDADES_AGUA)}") # Chama a função para medir a qualidade da água
    print(f"Qualidade do Ar: {obter_qualidade_de_acordo_com_valor(qualidade_do_ar, QUALIDADES_DO_AR)}")
    
    exibir_solucoes_se_necessario("Você pode melhorar a qualidade do ar ", qualidade_do_ar, solucoes_melhorar_o_ar)
    exibir_solucoes_se_necessario("Você pode melhorar a qualidade da água ", qualidade_da_agua, solucoes_melhorar_o_oceano)

    time.sleep(1)
    limpar_terminal()


