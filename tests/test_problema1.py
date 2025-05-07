import time
import pytest
from pathlib import Path
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.problema1.programacion_dinamica import resolver_programacion_dinamica
from src.problema1.fuerza_bruta import resolver_fuerza_bruta
from src.problema1.voraz import resolver_voraz

# Función para medir tiempos de ejecución
def medir_tiempo(funcion, entrada, repeticiones=5):
    """Mide el tiempo promedio de ejecución de una función"""
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()  # Más preciso que time.time()
        funcion(entrada)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return sum(tiempos) / repeticiones

# Función para leer archivos de prueba
def leer_datos_prueba(ruta_input, ruta_expected=None):
    """Lee archivos de prueba en formato del enunciado"""
    with open(ruta_input, 'r', encoding='utf-8') as f:
        n = int(f.readline())
        inputs = [f.readline().strip() for _ in range(n)]
    
    expected = None
    if ruta_expected:
        with open(ruta_expected, 'r', encoding='utf-8') as f:
            expected = [line.strip() for line in f.readlines()]
    
    return inputs, expected

# Fixture para cargar datos de prueba
@pytest.fixture(params=['small'])
def datos_prueba(request):
    base_path = Path(__file__).parent / 'data' / request.param
    inputs, expected = leer_datos_prueba(
        base_path / 'input_p1.txt',
        base_path / 'expected_p1.txt'
    )
    return {
        'tamaño': request.param,
        'inputs': inputs,
        'expected': expected
    }

# Pruebas unitarias básicas
@pytest.mark.parametrize("input, esperado", [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("abcde", "a"),  # Cualquier carácter es válido
    ("Dábale arroz", "dabalearroz")
])
def test_implementaciones(input, esperado):
    """Verifica que todas las implementaciones coincidan"""
    resultado_pd = resolver_programacion_dinamica(input)
    resultado_fb = resolver_fuerza_bruta(input)
    resultado_vz = resolver_voraz(input)
    
    assert len(resultado_pd) == len(esperado)
    assert len(resultado_fb) == len(esperado)
    assert len(resultado_vz) == len(esperado)
  # PD y Voraz deben coincidir exactamente

# Pruebas de rendimiento
@pytest.mark.parametrize("algoritmo, tamaño", [
    (resolver_programacion_dinamica, 100),
    (resolver_programacion_dinamica, 1000),
    (resolver_voraz, 100),
    (resolver_voraz, 10000),
    (resolver_fuerza_bruta, 10),
    (resolver_fuerza_bruta, 15)
], ids=[
    "PD-100", "PD-1000",
    "VORAZ-100", "VORAZ-10000",
    "FB-10", "FB-15"
])
def test_rendimiento(algoritmo, tamaño):
    """Prueba de rendimiento para diferentes tamaños de entrada"""
    cadena = "a" * tamaño  # Cadena simple para pruebas de tiempo
    tiempo = medir_tiempo(algoritmo, cadena)
    
    print(f"\n{algoritmo.__name__} ({tamaño} elementos): {tiempo:.6f} segundos")
    
    # Umbrales de tiempo (ajustar según necesidades)
    if algoritmo == resolver_fuerza_bruta:
        assert tiempo < 2.0
    elif algoritmo == resolver_programacion_dinamica:
        assert tiempo < 0.5
    else:
        assert tiempo < 0.1

# Prueba con datos desde archivos
def test_con_datos_externos(datos_prueba):
    """Prueba usando los archivos de datos"""
    for i, cadena in enumerate(datos_prueba['inputs']):
        resultado = resolver_programacion_dinamica(cadena)
        assert resultado == datos_prueba['expected'][i], \
            f"Error en {datos_prueba['tamaño']}, caso {i+1}"