## Nome e RM dos Alunos
*Jeniffer De Moraes RM: 555448*

*Maria Eduarda RM: 558457*

*Matheus Diniz RM: 555683*

## Link do vídeo explicativo
https://youtu.be/gjf1lLk9ph0?si=RUbqehrCoj55Bpou

## Detalhes do Projeto

Este projeto é um sistema de monitoramento de qualidade da água e do ar utilizando sensores simulados. Ele calcula parâmetros como pH da água, condutividade elétrica e monóxido de carbono no ar, exibindo a qualidade dos mesmos e sugerindo soluções para melhorar a qualidade com base nas leituras.

### Funcionalidades
- *Cálculo do pH da água:* Utiliza leitura de sensores e tensões de calibração para determinar o pH da água.
- *Cálculo da condutividade elétrica:* Calcula a condutividade elétrica da água ajustada para a temperatura ambiente.
- *Cálculo do monóxido de carbono:* Determina a concentração de monóxido de carbono no ar.
- *Qualidade da água e do ar:* Avalia a qualidade com base nos valores calculados e exibe mensagens de alerta se necessário.
- *Soluções para melhorias:* Sugere ações para melhorar a qualidade da água e do ar se os valores estiverem fora dos padrões aceitáveis.

## Instruções de Uso

1. *Clone o repositório:*  
   git clone https://github.com/Jenismoraes/gs-python.git

2. *Execute o script principal:*  
   python principal.py

O script irá simular leituras de sensores e exibir os valores calculados, a qualidade correspondente e sugestões de melhorias no terminal.

## Requisitos

- *Python 3*
- *import time*
- *from random import **
- *import os*

## Dependências

- time.sleep(1): Pausa a execução do programa por 1 segundo em cada iteração do loop, permitindo que a simulação atualize os valores de leitura periodicamente.
Biblioteca random:
- from random import *: Importa todas as funções da biblioteca random. No código, as funções randint e random são usadas para gerar valores aleatórios que simulam as leituras dos sensores.
- Biblioteca os: São usados na função limpar_terminal() para limpar o terminal.

## Informações Relevantes

O script simula leituras de sensores, gerando valores aleatórios dentro de faixas específicas para simular variações realistas. O código também inclui funções para calcular e exibir os valores, além de limpar o terminal a cada iteração para uma visualização clara e organizada.

## Explicação do Código

O código é organizado em várias funções que calculam diferentes parâmetros de qualidade da água e do ar a partir de leituras de sensores simulados. Abaixo está uma descrição detalhada de cada parte:

### Importações e Configurações Iniciais

python
import time
from random import randint
import os

### Constantes e Variáveis de Calibração

Define as tensões de calibração e outras variáveis necessárias para os cálculos.

### Funções de Utilidade

- *exibir_com_cor(text, cor):* Exibe texto colorido no terminal.
- *calcular_ph_agua(leituraPH):* Calcula o pH da água a partir da leitura do sensor.
- *calcular_condutividade_eletrica(leitura_condutividade, temperatura):* Calcula a condutividade elétrica da água ajustada para a temperatura.
- *calcular_monoxido_de_carbono(leitura_mc):* Calcula a concentração de monóxido de carbono no ar.
- *obter_qualidade_da_agua(valor_ph):* Determina a qualidade da água com base no valor de pH.
- *obter_qualidade_do_ar(monoxido_de_carbono):* Determina a qualidade do ar com base na concentração de monóxido de carbono.
- *obter_qualidade_de_acordo_com_valor(valor, valores_qualidade):* Retorna a qualidade correspondente ao valor fornecido, com a cor apropriada.
- *exibir_solucoes_se_necessario(mensagem, qualidade, solucoes):* Exibe sugestões de melhorias se a qualidade estiver abaixo do aceitável.
- *obter_maximo(valor1, valor2):* Retorna o maior valor entre dois fornecidos.
- *limpar_terminal():* Limpa o terminal para uma exibição organizada.
