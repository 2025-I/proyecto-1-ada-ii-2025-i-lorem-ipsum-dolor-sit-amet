import unittest
import time
import random
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

if __name__ == '__main__':
    unittest.main(verbosity=2)
