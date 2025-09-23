from ejercicio2_1724110249 import consNumero
from unittest.mock import patch

def testPositivos():
    with patch('builtins.input', side_effect=["-1","-4","-11","4"]):
        resultado = consNumero()
        assert resultado == (4)

def testNumeros():
    with patch('builtins.input', side_effect=["cat","dog","turtle","ñ{+/}}","4"]):
        resultado = consNumero()
        assert resultado == (4)

