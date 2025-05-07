import re

def normalize_string(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())  #Se usa re para eliminar caracteres no alfanuméricos y convertir a minúsculas

def resolver_voraz(s):
    s = normalize_string(s)
    n = len(s)
    left = 0
    right = n - 1
    izquierda = []
    derecha = []

    while left <= right:
        if s[left] == s[right]:
            izquierda.append(s[left])
            if left != right:
                derecha.append(s[right])
            left += 1
            right -= 1
        elif s[left + 1:right + 1].count(s[right]) > s[left:right].count(s[left]):
            left += 1
        else:
            right -= 1

    return ''.join(izquierda + derecha[::-1])