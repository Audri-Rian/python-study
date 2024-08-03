# Entendendo os sues próprios módulos Python
# O primeiro modúlo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

import aula77_m
from aula77_m import soma, variavel_modulo
print('Este módulo se chama',__name__)
print(variavel_modulo)
print(soma(2,3))
print(aula77_m.soma(2,3))