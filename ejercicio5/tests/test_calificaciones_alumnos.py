from ejercicio5_1724110249 import calificaciones_alumnos
from unittest.mock import patch

def testNormal():
    with patch('builtins.input', side_effect=["5","4","6","7","9","2"]):
        resultado = calificaciones_alumnos(2,3,["Marquito","Leonardo"])
        assert resultado == [[5.0,4.0,6.0],[7.0,9.0,2.0]]

def testValores():
    with patch('builtins.input', side_effect=["cat","dog","tunk","5","4","6","7","9","2"]):
        resultado = calificaciones_alumnos(2,3,["Marquito","Leonardo"])
        assert resultado == [[5.0,4.0,6.0],[7.0,9.0,2.0]]

def testRango():
    with patch('builtins.input', side_effect=["506","-2","101","5","4","6","7","9","2"]):
        resultado = calificaciones_alumnos(2,3,["Marquito","Leonardo"])
        assert resultado == [[5.0,4.0,6.0],[7.0,9.0,2.0]]

def testNone():
    with patch('builtins.input', side_effect=[None,"5","4","6","7","9","2"]):
        resultado = calificaciones_alumnos(2,3,["Marquito","Leonardo"])
        assert resultado == [[5.0,4.0,6.0],[7.0,9.0,2.0]]