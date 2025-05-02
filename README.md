[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/kKWtV-CB)
# Proyecto 1 - Programación dinámica y voraz 

## Integrantes

| Nombre completo                 | Código   |
|----------------------------------|----------|
| Joseph David Herrera Libreros    | 2266309  |
| Juan David Cuellar López         | 2266087  |
| Samuel Escobar Rivera            | 2266363  |

## Descripción del proyecto

Este proyecto resuelve dos problemas clásicos mediante programación dinámica y estructuras de datos eficientes:

### Problema 1: Subsecuencias más largas de un palíndromo

Dado un conjunto de cadenas, se encuentra la subsecuencia palindrómica más larga en cada una, ignorando mayúsculas, espacios y caracteres no alfanuméricos.

    Entrada: 

    Llego a tierra y le dijo: Dabale arroz a la zorra el abad, ella aceptó
    El ministro dijo Se es o no se es un ministro
    Maria dijo Yo dono rosas, oro no doy por ello el la dejo

    Salida: 

    dabalearrozalzorraelabad
    seesonoses
    yonodonorosasoronodoy


### Problema 2: Planeando una fiesta de la compañía

A partir de una jerarquía de empleados representada como un árbol, se selecciona el conjunto de invitados con la mayor suma de calificaciones de convivencia, cumpliendo que ningún supervisor directo esté invitado junto a su subordinado.

    Entrada: 
    
    2
    5
    0 1 0 0 0
    0 0 1 0 0
    0 0 0 1 0
    0 0 0 0 1
    1 0 0 0 0
    10 30 15 5 8
    6
    0 0 1 0 0 0
    1 0 0 0 0 0
    0 1 0 0 0 0
    0 0 0 1 0 0
    0 0 0 0 0 1
    1 0 0 0 0 0
    12 21 5 10 8 7


    Salida: 
    
    0 1 0 1 0 35
    1 0 0 0 0 1 19


Ambos problemas leen su entrada desde archivos seleccionados por el usuario mediante un file chooser y escriben la salida en la consola.
