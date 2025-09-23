from ejercicio3_1724110249 import cons_cadena
from unittest.mock import patch

def test_normal():
    with patch('builtins.input', side_effect=["Hola"]):
        resultado = cons_cadena()
        assert resultado == "Hola"
    
def test_none():
    with patch('builtins.input', side_effect=[None,"Hola"]):
        resultado = cons_cadena()
        assert resultado == "Hola"