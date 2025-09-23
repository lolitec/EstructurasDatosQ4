from ejercicio2_1724110249 import fibonacci

def test_normal():
    resultado = fibonacci(4)
    assert resultado == [0,1,1,2]

def test_cero():
    resultado = fibonacci(0)
    assert resultado == [0]