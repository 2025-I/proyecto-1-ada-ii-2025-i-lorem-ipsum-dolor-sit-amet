# Informe de Tests Automatizados - Problema 2: Planificación de Fiesta

```
tests/test_problema2.py
```

El objetivo es verificar la funcionalidad de los algoritmos para el: **Planificación de fiesta corporativa en árbol jerárquico**.

---

## Objetivos de prueba

* Verificar que todas las implementaciones sean correctas.
* Confirmar que la solución entregada tiene el puntaje esperado.
* Medir el rendimiento para distintas escalas de entrada.
* Validar la consistencia del formato de salida.

---

## Herramientas utilizadas

* `unittest` de Python
* `time.perf_counter()` para mediciones de rendimiento
* Generación de instancias aleatorias válidas mediante `random` y verificación de estructuras jerárquicas tipo árbol

---

## Cobertura de pruebas

### 1. Prueba con casos del enunciado

```python
def test_casos_enunciado(self):
```

* Ejecuta los tres algoritmos sobre ejemplos extraídos del enunciado original.
* Verifica que:

  * La salida tenga el formato correcto (empleados invitados + puntaje).
  * Se respete la restricción de no invitar a empleados con relación directa.
  * El puntaje total sea el máximo posible.

### 2. Pruebas escalables con instancias aleatorias

Se usa la función auxiliar:

```python
def probar_instancia(self, n, estrategia_fn, nombre, repeticiones=5):
```

* Genera instancias jerárquicas aleatorias sin ciclos ni supervisiones cruzadas.
* Ejecuta la estrategia deseada (`Voraz`, `PD`, `FB`) varias veces.
* Mide tiempos promedio, máximo y mínimo.
* Verifica que:

  * El vector tenga longitud `n+1`.
  * Contenga solo `0` y `1`.
  * Se respeten todas las restricciones de jerarquía.

#### Pruebas incluidas:

| Nombre             | Tamaño (n) | Estrategias evaluadas           |
| ------------------ | ---------- | ------------------------------- |
| `test_juguete`     | 10         | Voraz, Fuerza Bruta, Dinámica   |
| `test_pequeno`     | 100        | Voraz, Dinámica                 |
| `test_mediano`     | 1000       | Voraz, Dinámica                 |
| `test_grande`      | 10000      | Voraz, Dinámica                 |
| `test_extragrande` | 50000      | Voraz (**omitido por defecto**) |

---

## Validaciones aplicadas

* **Formato de salida**:

  * Longitud del vector debe ser `n + 1`
  * Los primeros `n` valores deben ser `0` o `1`

* **Restricción de jerarquía**:

  * Ningún par supervisor-subordinado puede estar invitado simultáneamente

* **Puntaje esperado**:

  * En pruebas conocidas, el último elemento del vector debe coincidir con el puntaje esperado.

---

## Ejecución

```bash
python tests/test_problema2.py
```

---
## Notas adicionales

* La fuerza bruta solo se ejecuta en `n <= 10` por su alto costo computacional.
* `test_extragrande` está marcado con `@unittest.skip` y debe habilitarse manualmente si se desea ejecutar.
---
