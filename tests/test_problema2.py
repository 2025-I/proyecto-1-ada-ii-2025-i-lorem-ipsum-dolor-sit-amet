import unittest
import time
import random
from src.problema2.voraz import resolver_problema

def generar_instancia_aleatoria(n, prob_arista=0.1, seed=None):
    """Genera una instancia aleatoria del problema"""
    if seed is not None:
        random.seed(seed)
    relaciones = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < prob_arista and i < j:
                relaciones[i][j] = 1  # i supervisa a j
    calificaciones = [random.randint(1, 100) for _ in range(n)]
    return relaciones, calificaciones

def verificar_restricciones(relaciones, salida):
    """Verifica que se cumplan las restricciones del problema"""
    invitados = [i for i, x in enumerate(salida[:-1]) if x == 1]
    for emp in invitados:
        for supervisor in range(len(relaciones)):
            if relaciones[supervisor][emp] == 1 and supervisor in invitados:
                return False
        for subordinado in range(len(relaciones)):
            if relaciones[emp][subordinado] == 1 and subordinado in invitados:
                return False
    return True

class TestFiestaVoraz(unittest.TestCase):

    def test_casos_enunciado(self):
        """Prueba los casos específicos del enunciado"""
        # Caso 1
        relacion1 = [
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,0],
            [0,0,0,0,1],
            [0,0,0,0,0]
        ]
        calif1 = [10,30,15,5,8]
        resultado1 = resolver_problema(relacion1, calif1)
        self.assertEqual(resultado1[-1], 38)
        self.assertTrue(verificar_restricciones(relacion1, resultado1))
        
        # Caso 2
        relacion2 = [
            [0,1,0,0,0,0],
            [0,0,1,1,0,0],
            [0,0,0,0,0,1],
            [0,0,0,0,1,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]
        ]
        calif2 = [12,18,5,10,8,7]
        resultado2 = resolver_problema(relacion2, calif2)
        self.assertEqual(resultado2[-1], 33)
        self.assertTrue(verificar_restricciones(relacion2, resultado2))

    def probar_instancia(self, n, prob_arista=0.01, repeticiones=5):
        """Función auxiliar para probar diferentes tamaños"""
        tiempos = []
        for _ in range(repeticiones):
            relaciones, calificaciones = generar_instancia_aleatoria(n, prob_arista)
            inicio = time.perf_counter()
            salida = resolver_problema(relaciones, calificaciones)
            fin = time.perf_counter()
            
            tiempos.append(fin - inicio)
            
            # Validaciones
            self.assertEqual(len(salida), n + 1)
            self.assertTrue(all(x in (0, 1) for x in salida[:-1]))
            self.assertTrue(verificar_restricciones(relaciones, salida))
        
        print(f"\nTamaño {n}:")
        print(f"  Tiempo promedio: {sum(tiempos)/len(tiempos):.4f} s")
        print(f"  Mejor tiempo: {min(tiempos):.4f} s")
        print(f"  Peor tiempo: {max(tiempos):.4f} s")

    def test_juguete(self):
        """10 elementos (caso juguete)"""
        self.probar_instancia(10)

    def test_pequeno(self):
        """100 elementos (caso pequeño)"""
        self.probar_instancia(100)

    def test_mediano(self):
        """1000 elementos (caso mediano)"""
        self.probar_instancia(1000)

    def test_grande(self):
        """10000 elementos (caso grande)"""
        self.probar_instancia(10000)

    @unittest.skip("Demasiado grande para ejecutar regularmente")
    def test_extragrande(self):
        """50000 elementos (caso extra grande)"""
        self.probar_instancia(50000)

if __name__ == '__main__':
    unittest.main(verbosity=2)