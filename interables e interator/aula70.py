# dir, hasattr e getattr em Python

string = 'Luiz'
metodo = 'upper1'


if hasattr (string, 'upper'):
    print('Existe upper')
    print(string.upper())
    print(getattr(string,metodo)())