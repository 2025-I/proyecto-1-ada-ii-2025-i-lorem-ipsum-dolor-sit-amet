import re

def normalizar(cadena):
    s = cadena.lower()
    reemplazos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u', 'ñ': 'n'}
    for antiguo, nuevo in reemplazos.items():
        s = s.replace(antiguo, nuevo)
    return re.sub(r'[^a-z0-9]', '', s)

def resolver_programacion_dinamica(cadena):
    s = normalizar(cadena)
    n = len(s)
    if n == 0:
        return ''

    rev = s[::-1]
    # dp[i][j] guarda la subsecuencia palindrómica más larga entre s[0..i-1] y rev[0..j-1]
    dp = [[""] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            if s[i] == rev[j]:
                dp[i + 1][j + 1] = dp[i][j] + s[i]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], key=len)

    return dp[n][n]
