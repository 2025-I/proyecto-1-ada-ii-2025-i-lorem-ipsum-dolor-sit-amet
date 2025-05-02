import os
from pathlib import Path

def create_file_with_comment(path, comment):
    """Crea un archivo con un comentario descriptivo"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"# {comment}\n")

def setup_project():
    """Genera la estructura básica del proyecto con archivos vacíos"""
    # Crear estructura de directorios
    dirs = [
        "src",
        "src/problema1",
        "src/problema2",
        "tests",
        "tests/data",
        "tests/data/small",
        "tests/data/medium",
        "tests/data/large",
        "tests/data/xlarge"
    ]

    # Crear directorios
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Directorio creado: {d}")

    # Archivos principales
    files = {
        "requirements.txt": "Dependencias del proyecto",
        "src/main.py": "Punto de entrada principal del programa",
        "src/file_chooser.py": "Interfaz para selección de archivos usando Tkinter",
        
        # Problema 1
        "src/problema1/__init__.py": "Inicialización del módulo problema1",
        "src/problema1/fuerza_bruta.py": "Implementación fuerza bruta para problema de subsecuencias palindrómicas",
        "src/problema1/programacion_dinamica.py": "Implementación programación dinámica para problema de subsecuencias palindrómicas",
        "src/problema1/voraz.py": "Implementación algoritmo voraz para problema de subsecuencias palindrómicas",
        
        # Problema 2
        "src/problema2/__init__.py": "Inicialización del módulo problema2",
        "src/problema2/fuerza_bruta.py": "Implementación fuerza bruta para problema de planificación de fiesta",
        "src/problema2/programacion_dinamica.py": "Implementación programación dinámica para problema de planificación de fiesta",
        "src/problema2/voraz.py": "Implementación algoritmo voraz para problema de planificación de fiesta",
        
        # Tests
        "tests/test_problema1.py": "Pruebas unitarias para el problema 1",
        "tests/test_problema2.py": "Pruebas unitarias para el problema 2"
    }

    # Crear archivos
    for file, comment in files.items():
        create_file_with_comment(file, comment)
        print(f"Archivo creado: {file}")

    print("\nEstructura del proyecto creada exitosamente:")
    print("📁 proyecto/")
    print("├── 📁 src/")
    print("│   ├── 📁 problema1/ (algoritmos para subsecuencias palindrómicas)")
    print("│   ├── 📁 problema2/ (algoritmos para planificación de fiesta)")
    print("│   ├── 📄 file_chooser.py")
    print("│   └── 📄 main.py")
    print("├── 📁 tests/ (pruebas unitarias)")
    print("└── 📄 requirements.txt (dependencias)")

if __name__ == "__main__":
    print("Iniciando creación de estructura del proyecto...\n")
    setup_project()