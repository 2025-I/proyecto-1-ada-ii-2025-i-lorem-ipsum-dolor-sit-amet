# tests/test_problema1.py
import time
import pytest
from pathlib import Path
import os
import sys
import re
import string
import random
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path

# Configuración de paths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.problema1.fuerza_bruta import resolver_fuerza_bruta
from src.problema1.programacion_dinamica import resolver_programacion_dinamica
from src.problema1.voraz import resolver_voraz

# ====================
# Funciones auxiliares
# ====================

def normalizar_test(cadena):
    """Función de normalización para tests (debe ser idéntica a la usada en los algoritmos)"""
    s = cadena.lower()
    replacements = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'ü':'u', 'ñ':'n'}
    for old, new in replacements.items():
        s = s.replace(old, new)
    return re.sub(r'[^a-z0-9]', '', s)

def generar_cadena_aleatoria(longitud):
    """Genera cadena aleatoria para pruebas de rendimiento"""
    chars = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(chars) for _ in range(longitud))

def medir_tiempo(funcion, entrada, repeticiones=5):
    """Mide tiempo promedio de ejecución"""
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion(entrada)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return sum(tiempos) / repeticiones

def leer_datos_prueba(ruta_input, ruta_expected):
    """Lee archivos de prueba"""
    with open(ruta_input, 'r', encoding='utf-8') as f:
        n = int(f.readline())
        entradas = [line.strip() for line in f.readlines()[:n]]
    
    with open(ruta_expected, 'r', encoding='utf-8') as f:
        esperados = [line.strip() for line in f.readlines()]
    
    return entradas, esperados

# ====================
# Pruebas unitarias
# ====================

@pytest.mark.parametrize("entrada,esperado", [
    ("Anita lava la tina", "anitalavalatina"),
    ("a", "a"),
    ("", ""),
    ("12321", "12321"),
    ("A man, a plan, a canal: Panama", "amanaplanacanalpanama")
])
def test_resultados_exactos(entrada, esperado):
    """Verifica que los algoritmos devuelvan resultados exactos para casos conocidos"""
    resultado_pd = resolver_programacion_dinamica(entrada)
    resultado_vz = resolver_voraz(entrada)
    
    # Verificación estricta para programación dinámica
    assert resultado_pd == esperado, \
        f"PD falló: Esperado '{esperado}' ({len(esperado)}), Obtenido '{resultado_pd}' ({len(resultado_pd)})"
    
    # Verificación laxa para voraz (puede ser subóptimo pero debe ser palíndromo)
    assert resultado_vz == resultado_vz[::-1], "El resultado voraz no es palíndromo"
    assert len(resultado_vz) <= len(esperado), \
        f"Voraz devolvió cadena más larga que el óptimo: {len(resultado_vz)} > {len(esperado)}"

# ====================
# Pruebas con archivos
# ====================

@pytest.mark.parametrize("tamaño", ['juguete', 'small'])
def test_archivos(tamaño):
    """Prueba los algoritmos con archivos de entrada/salida"""
    base_path = Path(__file__).parent / "data" / tamaño
    input_path = base_path / "input_p1.txt"
    expected_path = base_path / "expected_p1.txt"
    
    entradas, esperados = leer_datos_prueba(input_path, expected_path)
    
    for entrada, esperado in zip(entradas, esperados):
        # Programación dinámica debe coincidir exactamente
        resultado_pd = resolver_programacion_dinamica(entrada)
        assert resultado_pd == esperado, \
            f"PD falló en {tamaño}: Esperado '{esperado}', Obtenido '{resultado_pd}'"
        
        # Voraz debe devolver un palíndromo válido (puede ser subóptimo)
        resultado_vz = resolver_voraz(entrada)
        assert resultado_vz == resultado_vz[::-1], "Voraz no devolvió palíndromo"
        assert len(resultado_vz) <= len(esperado), \
            f"Voraz devolvió cadena más larga que el óptimo en {tamaño}"

# ====================
# Pruebas de rendimiento
# ====================

@pytest.mark.parametrize("algoritmo,tamaño", [
    (resolver_programacion_dinamica, 100),
    (resolver_programacion_dinamica, 1000),
    (resolver_programacion_dinamica, 5000),
    (resolver_voraz, 100),
    (resolver_voraz, 10000),
    (resolver_voraz, 50000),
    (resolver_fuerza_bruta, 10),
    (resolver_fuerza_bruta, 12)
], ids=[
    "PD-100", "PD-1000", "PD-5000",
    "VORAZ-100", "VORAZ-10000", "VORAZ-50000",
    "FB-10", "FB-12"
])
def test_rendimiento(algoritmo, tamaño):
    """Pruebas de rendimiento para diferentes tamaños de entrada"""
    if algoritmo == resolver_fuerza_bruta and tamaño > 15:
        pytest.skip("Fuerza bruta es muy lento para tamaños grandes")
    
    cadena = generar_cadena_aleatoria(tamaño)
    tiempo = medir_tiempo(algoritmo, cadena)
    
    print(f"\n{algoritmo.__name__} ({tamaño} elementos): {tiempo:.4f} segundos")
    
    # Umbrales de tiempo (ajustar según hardware)
    if algoritmo == resolver_fuerza_bruta:
        assert tiempo < 2.0
    elif algoritmo == resolver_programacion_dinamica:
        assert tiempo < 5.0
    else:
        assert tiempo < 0.5

# ====================
# Pruebas de propiedades
# ====================

def test_propiedades_palindromo():
    """Verifica propiedades fundamentales de los algoritmos"""
    casos = [
        "Race car",
        "No 'x' in Nixon",
        "Able was I ere I saw Elba",
        "Madam, I'm Adam"
    ]
    
    for caso in casos:
        # Todos deben devolver palíndromos
        resultado_pd = resolver_programacion_dinamica(caso)
        resultado_vz = resolver_voraz(caso)
        resultado_fb = resolver_fuerza_bruta(caso)
        
        assert resultado_pd == resultado_pd[::-1]
        assert resultado_vz == resultado_vz[::-1]
        assert resultado_fb == resultado_fb[::-1]
        
        # PD debe devolver la solución óptima
        assert len(resultado_pd) >= len(resultado_vz)
        assert len(resultado_pd) >= len(resultado_fb)

# ====================
# Pruebas de normalización
# ====================

@pytest.mark.parametrize("entrada,esperado", [
    ("Dábale", "dabale"),
    ("México", "mexico"),
    ("Canción", "cancion"),
    ("Año 2023", "ano2023"),
    ("¡Hola!", "hola")
])
def test_normalizacion(entrada, esperado):
    """Verifica que la normalización funcione correctamente"""
    assert normalizar_test(entrada) == esperado
# ====================
# Generación de gráficas de complejidad
# ====================

def generar_grafica_complejidad():
    """Genera gráficas de complejidad para los algoritmos y las guarda en docs/images"""
    # Crear directorio para imágenes si no existe
    docs_dir = Path(__file__).parent.parent / "docs"
    img_dir = docs_dir / "images"
    os.makedirs(img_dir, exist_ok=True)
    
    # Tamaños de entrada para cada algoritmo
    sizes_fb = [2, 4, 6, 8, 10, 12]
    sizes_pd = [10, 50, 100, 500, 1000, 5000]
    sizes_voraz = [10, 50, 100, 1000, 10000, 50000]
    
    # Recopilar tiempos de ejecución
    times_fb = []
    for n in sizes_fb:
        cadena = generar_cadena_aleatoria(n)
        tiempo = medir_tiempo(resolver_fuerza_bruta, cadena)
        times_fb.append(tiempo)
        print(f"Fuerza bruta con {n} elementos: {tiempo:.4f} segundos")
    
    times_pd = []
    for n in sizes_pd:
        cadena = generar_cadena_aleatoria(n)
        tiempo = medir_tiempo(resolver_programacion_dinamica, cadena)
        times_pd.append(tiempo)
        print(f"Programación dinámica con {n} elementos: {tiempo:.4f} segundos")
    
    times_voraz = []
    for n in sizes_voraz:
        cadena = generar_cadena_aleatoria(n)
        tiempo = medir_tiempo(resolver_voraz, cadena)
        times_voraz.append(tiempo)
        print(f"Algoritmo voraz con {n} elementos: {tiempo:.4f} segundos")
    
    # Crear gráfica individual para cada algoritmo
    plt.figure(figsize=(10, 6))
    plt.plot(sizes_fb, times_fb, 'o-', label='Fuerza Bruta')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Complejidad temporal: Fuerza Bruta')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(img_dir / 'fuerza_bruta_complexity.png')
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes_pd, times_pd, 'o-', label='Programación Dinámica')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Complejidad temporal: Programación Dinámica')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(img_dir / 'programacion_dinamica_complexity.png')
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes_voraz, times_voraz, 'o-', label='Algoritmo Voraz')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Complejidad temporal: Algoritmo Voraz')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(img_dir / 'voraz_complexity.png')
    
    # Gráfica comparativa (ajustando escalas)
    plt.figure(figsize=(12, 7))
    
    # Para la gráfica comparativa, seleccionamos solo algunos puntos para equilibrar la visualización
    plt.plot(sizes_fb, times_fb, 'o-', label='Fuerza Bruta', color='red')
    
    # Usar un rango común de tamaños para comparar PD y Voraz
    common_sizes = [10, 50, 100]
    times_pd_common = []
    times_voraz_common = []
    
    for n in common_sizes:
        cadena = generar_cadena_aleatoria(n)
        tiempo_pd = medir_tiempo(resolver_programacion_dinamica, cadena)
        tiempo_voraz = medir_tiempo(resolver_voraz, cadena)
        times_pd_common.append(tiempo_pd)
        times_voraz_common.append(tiempo_voraz)
    
    plt.plot(common_sizes, times_pd_common, 's-', label='Programación Dinámica', color='blue')
    plt.plot(common_sizes, times_voraz_common, '^-', label='Algoritmo Voraz', color='green')
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparativa de complejidad temporal entre algoritmos')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(img_dir / 'comparativa_algoritmos.png')
    
    print(f"\nLas gráficas de complejidad se han guardado en {img_dir}")

if __name__ == "__main__":
    # Si se ejecuta el script directamente, generar las gráficas
    generar_grafica_complejidad()