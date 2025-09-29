from ejercicio6_1724110249 import nueva_edad
from unittest.mock import patch

def testNuevaEdad():
    edades = [20, 30, 40]
    with patch('builtins.input', side_effect=["50"]):
        nueva_edad(edades)
        assert edades == [20, 30, 40, 50]

def testStrings():
    edades = [20, 30, 40]
    with patch('builtins.input', side_effect=["cat","dog","50"]):
        nueva_edad(edades)
        assert edades == [20, 30, 40, 50]

def testCero():
    edades = [20, 30, 40]
    with patch('builtins.input', side_effect=["0","50"]):
        nueva_edad(edades)
        assert edades == [20, 30, 40, 50]

def testNone():
    edades = [20, 30, 40]
    with patch('builtins.input', side_effect=[None,"50"]):
        nueva_edad(edades)
        assert edades == [20, 30, 40, 50]
