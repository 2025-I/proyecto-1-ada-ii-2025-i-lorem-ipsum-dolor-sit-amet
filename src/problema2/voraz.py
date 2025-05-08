import heapq

class Empleado:
    def __init__(self, id, calificacion):
        self.id = id
        self.calificacion = calificacion
        self.hijos = []
        self.padre = None

def construir_arbol(matriz, calificaciones):

    n = len(matriz)
    empleados = [Empleado(i, calificaciones[i]) for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                empleados[i].hijos.append(empleados[j])
                empleados[j].padre = empleados[i]
    
    # Manejar múltiples raíces (por si es un bosque)
    raices = [emp for emp in empleados if emp.padre is None]
    return raices, empleados

def planificar_fiesta_voraz(raices):

    invitados = set()
    total = 0
    # Max-heap usando valores negativos
    heap = [(-emp.calificacion, emp) for emp in raices]
    heapq.heapify(heap)
    
    while heap:
        _, empleado = heapq.heappop(heap)
        
        # Verificar restricciones
        if (empleado.padre and empleado.padre.id in invitados) or \
           any(hijo.id in invitados for hijo in empleado.hijos):
            continue
        
        # Invitar empleado
        invitados.add(empleado.id)
        total += empleado.calificacion
        
        # Agregar hijos al heap
        for hijo in empleado.hijos:
            heapq.heappush(heap, (-hijo.calificacion, hijo))
    
    return invitados, total

def resolver_problema(matriz, calificaciones):

    raices, empleados = construir_arbol(matriz, calificaciones)
    
    # Caso especial: estructura vacía
    if not raices:
        return [0]*len(empleados) + [0]
    
    invitados, total = planificar_fiesta_voraz(raices)
    
    # Construir resultado en orden original
    resultado = [1 if i in invitados else 0 for i in range(len(empleados))]
    resultado.append(total)
    
    return resultado