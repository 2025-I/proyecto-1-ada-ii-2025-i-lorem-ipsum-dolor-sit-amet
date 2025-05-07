# Implementación fuerza bruta para problema de subsecuencias palindrómicas
import re
from itertools import combinations

def normalizar_cadena(s):
    """Normaliza la cadena según el enunciado"""
    return re.sub(r'[^a-z0-9]', '', s.lower())

def es_palindromo(s):
    """Verifica si una cadena es palíndromo"""
    return s == s[::-1]

def resolver_fuerza_bruta(s):  # <<- Este es el nombre que debe coincidir
    """Implementación principal que deben importar los tests"""
    s_normalizada = normalizar_cadena(s)
    n = len(s_normalizada)
    max_longitud = 0
    resultados = set()

    for longitud in range(n, 0, -1):
        for indices in combinations(range(n), longitud):
            subsecuencia = ''.join([s_normalizada[i] for i in indices])
            if es_palindromo(subsecuencia):
                if len(subsecuencia) > max_longitud:
                    max_longitud = len(subsecuencia)
                    resultados = {subsecuencia}
                elif len(subsecuencia) == max_longitud:
                    resultados.add(subsecuencia)
        if resultados:
            break
    return next(iter(resultados)) if resultados else ""

