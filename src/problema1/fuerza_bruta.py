# src/problema1/fuerza_bruta.py
import re
from itertools import combinations

def normalizar_cadena(s):
    """Normaliza la cadena incluyendo caracteres acentuados"""
    s = s.lower()
    # Reemplazar caracteres acentuados
    replacements = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ü': 'u', 'ñ': 'n'
    }
    for old, new in replacements.items():
        s = s.replace(old, new)
    # Eliminar todo lo que no sea alfanumérico
    return re.sub(r'[^a-z0-9]', '', s)

def es_palindromo(s):
    """Verifica si una cadena es palíndromo"""
    return s == s[::-1]

def resolver_fuerza_bruta(s):
    """Implementación fuerza bruta corregida"""
    s_normalizada = normalizar_cadena(s)
    n = len(s_normalizada)
    
    if n == 0:
        return ""
    
    max_palindromos = [s_normalizada[0]]  # Al menos el primer carácter es palíndromo
    max_len = 1
    
    # Probamos todas las posibles subsecuencias desde la más larga
    for length in range(n, 1, -1):
        found = False
        # Generamos todas las combinaciones posibles de índices para esta longitud
        for indices in combinations(range(n), length):
            subseq = ''.join([s_normalizada[i] for i in indices])
            if es_palindromo(subseq):
                if len(subseq) > max_len:
                    max_len = len(subseq)
                    max_palindromos = [subseq]
                    found = True
                elif len(subseq) == max_len:
                    if subseq not in max_palindromos:
                        max_palindromos.append(subseq)
        # Si encontramos palíndromos en esta longitud, no necesitamos ver longitudes menores
        if found:
            break
    
    # Devolvemos el primer palíndromo más largo encontrado
    return max_palindromos[0] if max_palindromos else ""