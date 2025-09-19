from ejercicio1_1724110249 import consNum
from unittest.mock import patch

def testPositivo():
    with patch('builtins.input', side_effect=["-3","-7","gato","perro","5"]):
        resultado = consNum()
        assert resultado == (5)

def testCero():
    with patch('builtins.input', side_effect=["-3","gato","0"]):
        resultado = consNum()
        assert resultado == (1)
