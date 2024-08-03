import importlib # Essa porra recarrega o modulo
import aula78_m # O modulo é como se fosse uma arma de uma bala, ai o importlib recarrega essa arma

print(aula78_m.variavel)

for i in range(10):
    importlib.reload(aula78_m)
    print(i)

print('Fim')