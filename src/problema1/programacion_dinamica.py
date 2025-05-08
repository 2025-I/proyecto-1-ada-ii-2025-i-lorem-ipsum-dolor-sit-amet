import re

def normalizar(cadena):
    """Normalización mejorada que maneja acentos"""
    s = cadena.lower()
    replacements = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'ü':'u', 'ñ':'n'}
    for old, new in replacements.items():
        s = s.replace(old, new)
    return re.sub(r'[^a-z0-9]', '', s)

def resolver_programacion_dinamica(cadena):
    s = normalizar(cadena)
    n = len(s)
    if n == 0:
        return ''
    
    # Tabla DP donde dp[i][j] indica si s[i..j] es palíndromo
    dp = [[False] * n for _ in range(n)]
    resultado = ""
    
    # Todos los substrings de longitud 1 son palíndromos
    for i in range(n):
        dp[i][i] = True
        resultado = s[i]
    
    # Verificar substrings de longitud 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            if len(resultado) < 2:
                resultado = s[i:i+2]
    
    # Verificar substrings de longitud > 2
    for longitud in range(3, n+1):
        for i in range(n-longitud+1):
            j = i + longitud - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if longitud > len(resultado):
                    resultado = s[i:j+1]
    
    return resultado