'''
x ou X - hexadecimal
caractere
> - ESquerda
< - direita
^ - centro
sinal - + ou +

ex .: 0>-100, .1f
conversion flags - "!r !s !a
'''

variavel = "ABC"

print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10}.")

print(f"{variavel: ^10}.")

print(f"{51894894.4568846:-,.1f}")

print(f"O hexadecimal de 1500 é {1500:08X}")