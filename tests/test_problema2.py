import unittest
import time
import random
import os
import sys
# Configuración de paths
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.problema2.voraz import resolver_problema as voraz
from src.problema2.fuerza_bruta import resolver_fuerza_bruta
from src.problema2.programacion_dinamica import resolver_programacion_dinamica

def generar_arbol_aleatorio(n, calif_min=1, calif_max=100, seed=None):
    """
    Genera una estructura jerárquica aleatoria válida (sin ciclos, máximo un padre por nodo).
    Retorna una matriz de relaciones (adyacencia) y la lista de calificaciones.
    """
    if seed is not None:
        random.seed(seed)

    relaciones = [[0] * n for _ in range(n)]
    nodos_disponibles = list(range(n))
    random.shuffle(nodos_disponibles)

    # Creamos relaciones tipo árbol
    for i in range(1, n):
        hijo = nodos_disponibles[i]
        padre = random.choice(nodos_disponibles[:i])
        relaciones[padre][hijo] = 1  # padre → hijo

    calificaciones = [random.randint(calif_min, calif_max) for _ in range(n)]
    return relaciones, calificaciones


def verificar_restricciones(relaciones, salida):
    invitados = [i for i, x in enumerate(salida[:-1]) if x == 1]
    for emp in invitados:
        for supervisor in range(len(relaciones)):
            if relaciones[supervisor][emp] == 1 and supervisor in invitados:
                return False
        for subordinado in range(len(relaciones)):
            if relaciones[emp][subordinado] == 1 and subordinado in invitados:
                return False
    return True

def normalizar_salida_vector(vector, total):
    return vector + [total]

class TestFiestaCompleta(unittest.TestCase):

    def test_casos_enunciado(self):
        casos = [
            (
                [[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]],
                [10,30,15,5,8],
                38
            ),
            (
                [[0,1,0,0,0,0],[0,0,1,1,0,0],[0,0,0,0,0,1],[0,0,0,0,1,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
                [12,18,5,10,8,7],
                33
            )
        ]
        for relaciones, calificaciones, esperado in casos:
            for estrategia, nombre in [
                (voraz, "Voraz"),
                (lambda r, c: normalizar_salida_vector(*resolver_fuerza_bruta(len(c), r, c)), "Fuerza Bruta"),
                (lambda r, c: normalizar_salida_vector(*resolver_programacion_dinamica(len(c), r, c)), "Programación Dinámica")
            ]:
                with self.subTest(metodo=nombre):
                    salida = estrategia(relaciones, calificaciones)
                    self.assertEqual(len(salida), len(calificaciones) + 1)
                    self.assertTrue(verificar_restricciones(relaciones, salida))
                    self.assertEqual(salida[-1], esperado)

    def probar_instancia(self, n, estrategia_fn, nombre, repeticiones=5):
        tiempos = []
        for i in range(repeticiones):
            relaciones, calificaciones = generar_arbol_aleatorio(n, seed=i)
            inicio = time.perf_counter()
            salida = estrategia_fn(relaciones, calificaciones)
            fin = time.perf_counter()

            tiempos.append(fin - inicio)
            self.assertEqual(len(salida), n + 1)
            self.assertTrue(all(x in (0, 1) for x in salida[:-1]))
            self.assertTrue(verificar_restricciones(relaciones, salida))

        print(f"\n[{nombre}] Tamaño {n}: Promedio: {sum(tiempos)/len(tiempos):.4f}s, Mejor: {min(tiempos):.4f}s, Peor: {max(tiempos):.4f}s")


    def test_juguete(self):
        self.probar_instancia(10, voraz, "Voraz")
        self.probar_instancia(10, lambda r, c: normalizar_salida_vector(*resolver_fuerza_bruta(len(c), r, c)), "Fuerza Bruta")
        self.probar_instancia(10, lambda r, c: normalizar_salida_vector(*resolver_programacion_dinamica(len(c), r, c)), "Programación Dinámica")

    def test_pequeno(self):
        self.probar_instancia(100, voraz, "Voraz")
        self.probar_instancia(100, lambda r, c: normalizar_salida_vector(*resolver_programacion_dinamica(len(c), r, c)), "Programación Dinámica")

    def test_mediano(self):
        self.probar_instancia(1000, voraz, "Voraz")
        self.probar_instancia(1000, lambda r, c: normalizar_salida_vector(*resolver_programacion_dinamica(len(c), r, c)), "Programación Dinámica")

    def test_grande(self):
        self.probar_instancia(10000, voraz, "Voraz")
        self.probar_instancia(10000, lambda r, c: normalizar_salida_vector(*resolver_programacion_dinamica(len(c), r, c)), "Programación Dinámica")

    @unittest.skip("Prueba muy costosa para ejecución normal")
    def test_extragrande(self):
        self.probar_instancia(50000, voraz, "Voraz")

# Agregar al final del archivo, justo antes de "if __name__ == '__main__':"
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def generar_grafica_complejidad():
    """
    Genera gráficas de complejidad para los algoritmos y las guarda en docs/images
    """
    # Crear directorio para imágenes si no existe
    docs_dir = Path(__file__).parent.parent / "docs"
    img_dir = docs_dir / "images2"
    os.makedirs(img_dir, exist_ok=True)
    
    # Definir tamaños de prueba para cada algoritmo
    sizes_fb = [5, 8, 10, 12, 15]  # Tamaños pequeños para fuerza bruta
    sizes_pd = [10, 50, 100, 500, 1000, 5000]  # Tamaños medianos para PD
    sizes_voraz = [10, 50, 100, 500, 1000, 5000, 10000]  # Incluye tamaños grandes
    
    # Recopilar tiempos de ejecución
    times_fb = []
    for n in sizes_fb:
        tiempo_total = 0
        repeticiones = 3
        for i in range(repeticiones):
            relaciones, calificaciones = generar_arbol_aleatorio(n, seed=i)
            inicio = time.perf_counter()
            normalizar_salida_vector(*resolver_fuerza_bruta(n, relaciones, calificaciones))
            fin = time.perf_counter()
            tiempo_total += fin - inicio
        times_fb.append(tiempo_total / repeticiones)
        print(f"Fuerza bruta con {n} elementos: {tiempo_total / repeticiones:.4f} segundos")
    
    times_pd = []
    for n in sizes_pd:
        tiempo_total = 0
        repeticiones = 3
        for i in range(repeticiones):
            relaciones, calificaciones = generar_arbol_aleatorio(n, seed=i)
            inicio = time.perf_counter()
            normalizar_salida_vector(*resolver_programacion_dinamica(n, relaciones, calificaciones))
            fin = time.perf_counter()
            tiempo_total += fin - inicio
        times_pd.append(tiempo_total / repeticiones)
        print(f"Programación dinámica con {n} elementos: {tiempo_total / repeticiones:.4f} segundos")
    
    times_voraz = []
    for n in sizes_voraz:
        tiempo_total = 0
        repeticiones = 3
        for i in range(repeticiones):
            relaciones, calificaciones = generar_arbol_aleatorio(n, seed=i)
            inicio = time.perf_counter()
            voraz(relaciones, calificaciones)
            fin = time.perf_counter()
            tiempo_total += fin - inicio
        times_voraz.append(tiempo_total / repeticiones)
        print(f"Algoritmo voraz con {n} elementos: {tiempo_total / repeticiones:.4f} segundos")
    
    # Crear gráfica individual para cada algoritmo
    plt.figure(figsize=(10, 6))
    plt.plot(sizes_fb, times_fb, 'o-', label='Fuerza Bruta')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Complejidad temporal: Fuerza Bruta')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(img_dir / 'fuerza_bruta_complexity_p2.png')
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes_pd, times_pd, 'o-', label='Programación Dinámica')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Complejidad temporal: Programación Dinámica')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(img_dir / 'programacion_dinamica_complexity_p2.png')
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes_voraz, times_voraz, 'o-', label='Algoritmo Voraz')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Complejidad temporal: Algoritmo Voraz')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(img_dir / 'voraz_complexity_p2.png')
    
    # Gráfica comparativa con escala logarítmica
    plt.figure(figsize=(12, 7))
    
    # Para la gráfica comparativa, seleccionamos tamaños comunes para todos
    common_sizes = [10]
    plt.plot(sizes_fb, times_fb, 'o-', label='Fuerza Bruta', color='red')
    plt.plot(sizes_pd, times_pd, 's-', label='Programación Dinámica', color='blue')
    plt.plot(sizes_voraz, times_voraz, '^-', label='Algoritmo Voraz', color='green')
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparativa de complejidad temporal entre algoritmos')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(img_dir / 'comparativa_algoritmos_p2.png')
    
    # Gráfica adicional: comparativa PD vs Voraz en tamaños medianos
    common_pd_voraz = [x for x in sizes_pd if x in sizes_voraz]
    pd_times = [times_pd[sizes_pd.index(n)] for n in common_pd_voraz]
    voraz_times = [times_voraz[sizes_voraz.index(n)] for n in common_pd_voraz]    
    print(f"\nLas gráficas de complejidad se han guardado en {img_dir}")

if __name__ == '__main__':
    # Descomentar para generar gráficas
    generar_grafica_complejidad()
    unittest.main(verbosity=2)
