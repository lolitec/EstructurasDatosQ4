from ejercicio5_1724110249 import cons_nombre_alumno
from unittest.mock import patch

def testNormal():
    with patch('builtins.input', side_effect=["Marquito","Leonardo","Alan","Luis"]):
        resultado = cons_nombre_alumno(4)
        assert resultado == ["Marquito","Leonardo","Alan","Luis"]

def testNoChars():
    with patch('builtins.input', side_effect=["67","¨**@","0","Marquito","Leonardo","Alan","Luis"]):
        resultado = cons_nombre_alumno(4)
        assert resultado == ["Marquito","Leonardo","Alan","Luis"]

def testNone():
    with patch('builtins.input', side_effect=[None,"Marquito","Leonardo","Alan","Luis"]):
        resultado = cons_nombre_alumno(4)
        assert resultado == ["Marquito","Leonardo","Alan","Luis"]