# Implementación programación dinámica para problema de subsecuencias palindrómicas
import re

def normalizar(cadena):
    # Elimina todos los caracteres no alfanuméricos y convierte a minúsculas.

    return re.sub(r'[^a-z0-9]', '', cadena.lower())

def resolver_programacion_dinamica(cadena):

    # Dada una cadena de entrada, devuelve su subcadena palindrómica más larga,
    # ignorando mayúsculas/minúsculas y caracteres no alfanuméricos.

    s = normalizar(cadena)
    n = len(s)
    if n == 0:
        return ''

    # Inicializar la tabla dp
    # dp[i][j] = True si la subcadena s[i..j] es un palíndromo
    dp = [[False] * n for _ in range(n)]
    
    # Todas las subcadenas de longitud 1 son palíndromos
    for i in range(n):
        dp[i][i] = True
    
    inicio = 0  # Índice de inicio del palíndromo más largo
    max_longitud = 1  # Longitud del palíndromo más largo
    
    # Verificar palíndromos de longitud 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            inicio = i
            max_longitud = 2
    
    # Verificar palíndromos de longitud 3 o más
    for longitud in range(3, n+1):
        for i in range(n-longitud+1):
            j = i + longitud - 1  # Índice final
            
            # Verificar si s[i..j] es un palíndromo
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                
                if longitud > max_longitud:
                    inicio = i
                    max_longitud = longitud
    
    # Retornar la subcadena palindrómica más larga
    return s[inicio:inicio + max_longitud]
