from ejercicio4_1724110249 import crearMatriz
from unittest.mock import patch

def testEnteros():
    with patch('builtins.input', side_effect=["2","3","4","5","6","7"]):
        resultado = crearMatriz(2,3)
        assert resultado == ([[2, 3, 4], [5, 6, 7]])

def testValores():
    with patch('builtins.input', side_effect=["2","3","gato","4","5","6.5","6","tortuga","7"]):
        resultado = crearMatriz(2,3)
        assert resultado == ([[2, 3, 4], [5, 6, 7]])