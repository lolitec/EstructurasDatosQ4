from ejercicio5_1724110249 import cons_num_materias
from unittest.mock import patch

def testNormal():
    with patch('builtins.input', side_effect=["5"]):
        resultado = cons_num_materias()
        assert resultado == (5)

def testStrings():
    with patch('builtins.input', side_effect=["cat","dog","turtle","5"]):
        resultado = cons_num_materias()
        assert resultado == (5)

def testCero():
    with patch('builtins.input', side_effect=["0","5"]):
        resultado = cons_num_materias()
        assert resultado == (5)

def testNone():
    with patch('builtins.input', side_effect=[None,"5"]):
        resultado = cons_num_materias()
        assert resultado == (5)