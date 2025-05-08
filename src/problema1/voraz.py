import re

def normalize_string(s):
    s = s.lower()
    replacements = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'ü':'u', 'ñ':'n'}
    for old, new in replacements.items():
        s = s.replace(old, new)
    return re.sub(r'[^a-z0-9]', '', s)

def resolver_voraz(s):
    s = normalize_string(s)
    max_palindrome = ""
    
    for i in range(len(s)):
        # Caso impar (centro único)
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(max_palindrome):
                max_palindrome = s[l:r+1]
            l -= 1
            r += 1
        
        # Caso par (centro doble)
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > len(max_palindrome):
                max_palindrome = s[l:r+1]
            l -= 1
            r += 1
    
    return max_palindrome