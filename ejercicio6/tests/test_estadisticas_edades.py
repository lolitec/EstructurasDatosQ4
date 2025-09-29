from ejercicio6_1724110249 import edad_minima, edad_maxima, promedio_edades, mediana_edades

def test_edad_minima():
    assert edad_minima([20, 30, 40]) == 20
    assert edad_minima([40, 30, 20]) == 20
    assert edad_minima([25]) == 25

def test_edad_maxima():
    assert edad_maxima([20, 30, 40]) == 40
    assert edad_maxima([40, 30, 20]) == 40
    assert edad_maxima([25]) == 25

def test_promedio_edades():
    assert promedio_edades([20, 30, 40]) == 30
    assert promedio_edades([10, 20, 30, 40]) == 25
    assert promedio_edades([25]) == 25

def test_mediana_edades():
    assert mediana_edades([20, 30, 40]) == 30
    assert mediana_edades([10, 20, 30, 40]) == 25
    assert mediana_edades([25]) == 25
