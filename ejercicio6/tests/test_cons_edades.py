from ejercicio6_1724110249 import cons_edades
from unittest.mock import patch

def testNormal():
    with patch('builtins.input', side_effect=["20","30","40"]):
        resultado = cons_edades(3)
        assert resultado == [20,30,40]

def testStrings():
    with patch('builtins.input', side_effect=["cat","dog","20","30","40"]):
        resultado = cons_edades(3)
        assert resultado == [20,30,40]

def testCero():
    with patch('builtins.input', side_effect=["0","20","30","40"]):
        resultado = cons_edades(3)
        assert resultado == [0,20,30]

def testNone():
    with patch('builtins.input', side_effect=[None,"20","30","40"]):
        resultado = cons_edades(3)
        assert resultado == [20,30,40]
