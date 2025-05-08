# Informe de Pruebas Unitarias - Problema 1: Subsecuencias Palindrómicas

```
tests/test_problema1.py
```

El objetivo es verificar la funcionalidad de los algoritmos para el **Problema 1: encontrar la subsecuencia palindrómica más larga**.

---

## Objetivos de prueba

* Validar que las implementaciones sean correctas.
* Asegurar que los algoritmos encuentra la subsecuencia palindrómica.
* Evaluar el rendimiento según el tipo de algoritmo.
* Confirmar que la normalización de cadenas sean correctas.

---

## Herramientas utilizadas

* **pytest**: framework de pruebas en Python.
* **time.perf\_counter()**: para medir tiempo de ejecución.
* **itertools / random / re**: para generación de casos y utilidades.
* **pathlib / os / sys**: para manejo de rutas multiplataforma.

---

## Estructura del archivo

### 1. Pruebas unitarias exactas

```python
@pytest.mark.parametrize("entrada,esperado", [...])
def test_resultados_exactos(...)
```
* **Programación Dinámica** debe coincidir exactamente.
* **Voraz** puede ser subóptimo, pero debe:

  * Ser palíndromo.
  * Tener longitud ≤ a la óptima.

#### Ejemplo:

```python
("Anita lava la tina", "anitalavalatina")
```

---

### 2. Pruebas con archivos externos

```python
@pytest.mark.parametrize("tamaño", ['juguete', 'small'])
def test_archivos(...)
```

* Carga datos de `tests/data/<tamaño>/input_p1.txt` y `expected_p1.txt`.
* Verifica que:

  * Dinámica coincida con la salida esperada.
  * Voraz produzca un palíndromo de longitud razonable.

---

### 3. Pruebas de rendimiento

```python
@pytest.mark.parametrize("algoritmo, tamanio", [...])
def test_rendimiento(...)
```

* Evalúa el tiempo promedio de ejecución para entradas generadas aleatoriamente.

* Umbrales definidos:

  * **Fuerza bruta**: < 5.0 s
  * **Programación Dinámica**: < 5.0 s
  * **Voraz**: < 0.5 s

* Omite fuerza bruta en tamaños grandes automáticamente.

#### Ejemplo de entrada:

```python
generar_cadena_aleatoria(10000)
```

---

### 4. Pruebas de propiedades

```python
def test_propiedades_palindromo():
```

* Verifica que todas las salidas:

  * Sean palíndromos.
  * Que PD sea al menos tan buena como FB o Voraz.

#### Frases utilizadas:

* "Race car"
* "No 'x' in Nixon"
* "Able was I ere I saw Elba"

---

### 5. Pruebas de normalización

```python
@pytest.mark.parametrize("entrada, esperado", [...])
def test_normalizacion(...)
```

* Evalúa la función `normalizar_test`, que debe comportarse como la usada en los algoritmos.
* Comprueba reemplazo de caracteres acentuados y eliminación de símbolos.

#### Ejemplo:

```python
("Dábale", "dabale")
("Año 2023", "ano2023")
```

---

## Consideraciones generales

* **Fuerza bruta** solo se prueba en tamaños ≤ 12.
* **Voraz** puede fallar en optimalidad pero debe ser válido.
* Todas las salidas esperadas deben ser palíndromos según normalización.

---

## Ejecución

```bash
pytest tests/test_problema1.py
```

---

