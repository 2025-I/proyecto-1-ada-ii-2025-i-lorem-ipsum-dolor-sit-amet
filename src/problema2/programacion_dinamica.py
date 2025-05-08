#Impletar algoritmo de programación dinámica para resolver el problema de planificación de fiesta
# problema2/programacion_dinamica.py
from collections import defaultdict

def resolver_programacion_dinamica(empleados, relaciones, calificaciones):
    """
    Función principal de DP para el problema 2
    Parámetros actualizados:
    - empleados: int (número de empleados)
    - relaciones: matriz de supervisión (lista de listas)
    - calificaciones: lista de calificaciones (lista de enteros)
    """
    m = empleados
    
    # En lugar de usar la estructura de árbol con padres e hijos,
    # simplemente rastreamos las relaciones directas de supervisión
    supervisiones = [[] for _ in range(m)]
    
    # Construir estructura de supervisión
    for i in range(m):
        for j in range(m):
            if relaciones[i][j] == 1:
                supervisiones[i].append(j)  # i supervisa a j
    
    # Utilizamos programación dinámica para resolver el problema
    # dp[i][0] = máxima calificación posible para el subárbol con raíz en i, sin incluir i
    # dp[i][1] = máxima calificación posible para el subárbol con raíz en i, incluyendo i
    dp = [[-1, -1] for _ in range(m)]
    visitado = [False] * m
    
    def calcular_dp(nodo):
        if dp[nodo][0] != -1 and dp[nodo][1] != -1:
            return  # Ya calculado
            
        # Inicializar valores
        dp[nodo][0] = 0  # No incluir este nodo
        dp[nodo][1] = calificaciones[nodo]  # Incluir este nodo
        
        # Marcar como visitado para evitar ciclos
        visitado[nodo] = True
        
        for subordinado in supervisiones[nodo]:
            if not visitado[subordinado]:
                calcular_dp(subordinado)
            
            # Si incluimos el nodo actual, no podemos incluir a sus subordinados directos
            dp[nodo][1] += dp[subordinado][0]
            
            # Si no incluimos el nodo actual, podemos elegir lo mejor para cada subordinado
            dp[nodo][0] += max(dp[subordinado][0], dp[subordinado][1])
        
        # Desmarcar para permitir otros caminos
        visitado[nodo] = False
    
    # Calcular para cada nodo no visitado
    for nodo in range(m):
        if not visitado[nodo]:
            calcular_dp(nodo)
    
    # Determinar qué empleados invitar
    seleccionado = [False] * m
    
    def seleccionar(nodo, puede_incluir):
        visitado[nodo] = True
        
        if puede_incluir and dp[nodo][1] > dp[nodo][0]:
            seleccionado[nodo] = True
            # Si seleccionamos este nodo, no podemos seleccionar a sus subordinados
            for subordinado in supervisiones[nodo]:
                if not visitado[subordinado]:
                    seleccionar(subordinado, False)
        else:
            seleccionado[nodo] = False
            # Si no seleccionamos este nodo, podemos seleccionar a sus subordinados
            for subordinado in supervisiones[nodo]:
                if not visitado[subordinado]:
                    seleccionar(subordinado, True)
    
    # Reiniciar visitado para la selección
    visitado = [False] * m
    
    for nodo in range(m):
        if not visitado[nodo]:
            seleccionar(nodo, True)
    
    suma_total = sum(calificaciones[i] for i in range(m) if seleccionado[i])
    return seleccionado, suma_total

def procesar_problema2(lineas):
    """
    Función para procesar múltiples casos de entrada
    """
    idx = 0
    n_problemas = int(lineas[idx])
    idx += 1
    resultados = []
    
    for _ in range(n_problemas):
        m = int(lineas[idx])
        idx += 1
        
        # Leer matriz de relaciones
        relaciones = []
        for _ in range(m):
            relaciones.append(list(map(int, lineas[idx].split())))
            idx += 1
        
        calificaciones = list(map(int, lineas[idx].split()))
        idx += 1

        # Llamar a la función con los 3 parámetros requeridos
        invitados, suma = resolver_programacion_dinamica(
            empleados=m,
            relaciones=relaciones,
            calificaciones=calificaciones
        )
        
        # Formatear salida según especificaciones
        salida = ' '.join(['1' if x else '0' for x in invitados]) + ' ' + str(suma)
        resultados.append(salida)
    
    return resultados

if __name__ == "__main__":
    import sys
    lineas = sys.stdin.read().splitlines()
    for resultado in procesar_problema2(lineas):
        print(resultado)
        # print(' '.join(map(str, invitados)) + ' ' + str(puntaje)) 