# Implementación algoritmo voraz para problema de subsecuencias palindrómicas
import re

def normalize_string(s):
    """Normaliza la cadena según las especificaciones del proyecto"""
    return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

def palindroma_voraz(s):
    """Solución voraz para encontrar la subsecuencia palindrómica más larga"""
    normalized = normalize_string(s)
    n = len(normalized)
    if n == 0:
        return ""
    
    left = 0
    right = n - 1
    result = []
    
    while left <= right:
        if normalized[left] == normalized[right]:
            result.append(normalized[left])
            left += 1
            right -= 1
        else:
            # Decisión voraz
            if (left + 1 <= right and normalized[left + 1] == normalized[right]):
                left += 1
            elif (right - 1 >= left and normalized[left] == normalized[right - 1]):
                right -= 1
            else:
                left += 1
                right -= 1
    
    return ''.join(result + result[:-1][::-1])