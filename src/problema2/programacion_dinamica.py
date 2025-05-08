# problema2/programacion_dinamica.py
def resolver_programacion_dinamica(empleados, relaciones, calificaciones):
    m = empleados
    supervisiones = [[] for _ in range(m)]

    # Construir estructura de supervisión (i supervisa a j)
    for i in range(m):
        for j in range(m):
            if relaciones[i][j] == 1:
                supervisiones[i].append(j)

    # Calcular padres para detectar raíces (los que no son supervisados)
    padres = [0] * m
    for i in range(m):
        for j in supervisiones[i]:
            padres[j] += 1
    raices = [i for i, p in enumerate(padres) if p == 0]

    dp = [[-1, -1] for _ in range(m)]
    visitado = [False] * m

    def calcular_dp(nodo):
        if dp[nodo][0] != -1 and dp[nodo][1] != -1:
            return
        dp[nodo][0] = 0
        dp[nodo][1] = calificaciones[nodo]
        visitado[nodo] = True
        for hijo in supervisiones[nodo]:
            if not visitado[hijo]:
                calcular_dp(hijo)
            dp[nodo][0] += max(dp[hijo][0], dp[hijo][1])
            dp[nodo][1] += dp[hijo][0]
        visitado[nodo] = False

    for raiz in raices:
        calcular_dp(raiz)

    seleccionado = [0] * m
    visitado = [False] * m

    def seleccionar(nodo, puede_incluir):
        visitado[nodo] = True
        if puede_incluir and dp[nodo][1] > dp[nodo][0]:
            seleccionado[nodo] = 1
            for hijo in supervisiones[nodo]:
                if not visitado[hijo]:
                    visitado[hijo] = True
                    seleccionar(hijo, False)
        else:
            for hijo in supervisiones[nodo]:
                if not visitado[hijo]:
                    visitado[hijo] = True
                    seleccionar(hijo, True)

    for raiz in raices:
        seleccionar(raiz, True)

    suma_total = sum(calificaciones[i] for i in range(m) if seleccionado[i] == 1)
    return seleccionado, suma_total


def procesar_problema2(lineas):
    idx = 0
    n_problemas = int(lineas[idx])
    idx += 1
    resultados = []

    for _ in range(n_problemas):
        m = int(lineas[idx])
        idx += 1

        relaciones = []
        for _ in range(m):
            relaciones.append(list(map(int, lineas[idx].split())))
            idx += 1

        calificaciones = list(map(int, lineas[idx].split()))
        idx += 1

        invitados, suma = resolver_programacion_dinamica(
            empleados=m,
            relaciones=relaciones,
            calificaciones=calificaciones
        )

        salida = ' '.join(['1' if x else '0' for x in invitados]) + ' ' + str(suma)
        resultados.append(salida)

    return resultados


if __name__ == "__main__":
    import sys
    lineas = sys.stdin.read().splitlines()
    for resultado in procesar_problema2(lineas):
        print(resultado)
