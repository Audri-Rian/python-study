def criar_mutiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicador

duplicar = criar_mutiplicador(2)
triplicar = criar_mutiplicador(3)
quadruplicar = criar_mutiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
