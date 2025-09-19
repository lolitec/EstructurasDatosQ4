from ejercicio4_1724110249 import tamañoArreglo
from unittest.mock import patch

def testPositivo():
    with patch('builtins.input', side_effect=["3", "4"]):
        resultado = tamañoArreglo()
        assert resultado == (3,4)

def testNegativo():
    with patch('builtins.input', side_effect=["-3", "-4","-5","3","4"]):
        resultado = tamañoArreglo()
        assert resultado == (3,4)

def testCero():
    with patch('builtins.input', side_effect=["0","0","3","4"]):
        resultado = tamañoArreglo()
        assert resultado == (3,4)

def testValores():
    with patch('builtins.input', side_effect=["gato","perro","3","tortuga","4.3","elefante","4"]):
        resultado = tamañoArreglo()
        assert resultado == (3,4)
