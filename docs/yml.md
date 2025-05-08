# Documentación del Workflow de GitHub Actions: `.github/workflows/build.yml`

## Descripción General

Este documento explica el archivo de configuración de GitHub Actions usado para automatizar la construcción y verificación del proyecto Python.

## Índice
1. Resumen del Workflow
2. Eventos de Activación
3. Configuración de Jobs
4. Pasos del Workflow
5. Estrategia de Matriz
6. Artefactos Generados
7. Recomendaciones y Mejoras

## Resumen del Workflow

El workflow `Build and Test Project` se encarga de construir el proyecto Python, verificar su estructura y generar artefactos para diferentes versiones de Python.

```yaml
name: Build and Test Project
```

## Eventos de Activación

El workflow se activa en las siguientes circunstancias:

- **Push**: Cuando se envían cambios a las ramas `main` o `dev`.
- **Pull Request**: Cuando se crea o actualiza un PR dirigido a las ramas `main` o `dev`.
- **Workflow Dispatch**: Permite ejecutar el workflow manualmente desde la interfaz de GitHub.

```yaml
on:
  push:
    branches: [ "main", "dev" ]
  pull_request:
    branches: [ "main", "dev" ]
  workflow_dispatch:
```

## Configuración de Jobs

El workflow define un único job denominado `build-and-test` que se ejecuta en el entorno Ubuntu más reciente.

```yaml
jobs:
  build-and-test:
    runs-on: ubuntu-latest
```

## Estrategia de Matriz

Se utiliza una estrategia de matriz para ejecutar el mismo conjunto de pasos con diferentes versiones de Python:

```yaml
strategy:
  matrix:
    python-version: ["3.9", "3.10", "3.11"]
```

Esta configuración crea 3 ejecuciones paralelas del job, cada una con una versión diferente de Python.

## Pasos del Workflow

El workflow ejecuta los siguientes pasos en secuencia:

1. **Checkout del Código**: Obtiene el código del repositorio.
   ```yaml
   - uses: actions/checkout@v2
   ```

2. **Configuración de Python**: Instala la versión de Python especificada en la matriz.
   ```yaml
   - name: Set up Python ${{ matrix.python-version }}
     uses: actions/setup-python@v4
     with:
       python-version: ${{ matrix.python-version }}
   ```

3. **Instalación de Dependencias**: Actualiza pip e instala las dependencias del proyecto.
   ```yaml
   - name: Install dependencies
     run: |
       python -m pip install --upgrade pip
       pip install setuptools wheel
       pip install -r requirements.txt
   ```

4. **Verificación de la Estructura**: Comprueba que el proyecto tenga los directorios y archivos esenciales.
   ```yaml
   - name: Verify project structure
     run: |
       # Comprueba la existencia de directorios y archivos críticos
   ```

5. **Creación de Artefactos**: Ejecuta los scripts de configuración y construye los artefactos del proyecto.
   ```yaml
   - name: Create build artifacts
     run: |
       python setup_project.py sdist bdist_wheel
       python setup.py sdist bdist_wheel
   ```

6. **Carga de Artefactos**: Guarda los artefactos generados para su descarga posterior.
   ```yaml
   - name: Upload artifacts
     uses: actions/upload-artifact@v3
     with:
       name: build-artifacts-${{ matrix.python-version }}
       path: artifacts/
   ```

## Artefactos Generados

El workflow genera paquetes Python (distribuciones fuente y wheels) que son almacenados como artefactos nombrados según la versión de Python utilizada:
- `build-artifacts-3.9`
- `build-artifacts-3.10` 
- `build-artifacts-3.11`

## Recomendaciones y Mejoras

Para mejorar este workflow, se podría considerar:

1. **Añadir Tests**: Incluir un paso que ejecute las pruebas unitarias con pytest.
2. **Cache de Dependencias**: Implementar caché para las dependencias Python para acelerar las ejecuciones.
3. **Envío a PyPI**: Configurar un job adicional para publicar automáticamente en PyPI cuando se crean tags.
4. **Notificaciones**: Configurar notificaciones en caso de fallo del workflow.
5. **Análisis de Código**: Integrar herramientas como flake8, black o mypy para asegurar la calidad del código.

---

*Este documento fue generado para documentar el archivo de configuración de GitHub Actions. Última actualización: Mayo 2025.*