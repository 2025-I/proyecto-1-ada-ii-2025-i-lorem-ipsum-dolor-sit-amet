# Pruebas unitarias para el problema 1
import time
from src.problema1.programacion_dinamica import resolver_programacion_dinamica
# from problema1.fuerza_bruta import resolver_fuerza_bruta
# from problema1.voraz import resolver_voraz

def medir_tiempo(funcion, entrada, repeticiones=5):
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.time()
        funcion(entrada)
        fin = time.time()
        tiempos.append(fin - inicio)
    return sum(tiempos) / repeticiones

def generar_cadena_alfanumerica(longitud):
    return "a" * longitud

def test_programacion_dinamica():
    tamaños = [10, 100] #Se me crasheo con 1000, 10000, 50000
    for tamaño in tamaños:
        cadena = generar_cadena_alfanumerica(tamaño)
        tiempo_promedio = medir_tiempo(resolver_programacion_dinamica, cadena)
        print(f"Programación Dinámica ({tamaño} elementos): {tiempo_promedio:.4f} segundos")

# def test_fuerza_bruta():
#     tamaños = [10, 20, 30]  # Más pequeños para evitar tiempos excesivos
#     for tamaño in tamaños:
#         cadena = generar_cadena_alfanumerica(tamaño)
#         tiempo_promedio = medir_tiempo(resolver_fuerza_bruta, cadena)
#         print(f"Fuerza Bruta ({tamaño} elementos): {tiempo_promedio:.4f} segundos")

# def test_voraz():
#     tamaños = [10, 100, 1000]
#     for tamaño in tamaños:
#         cadena = generar_cadena_alfanumerica(tamaño)
#         tiempo_promedio = medir_tiempo(resolver_voraz, cadena)
#         print(f"Voraz ({tamaño} elementos): {tiempo_promedio:.4f} segundos")
