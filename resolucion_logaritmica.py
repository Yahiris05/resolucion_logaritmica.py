import math

def quicksort(arr):
    """Ordenamiento QuickSort optimizado"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def resolver_ecuacion_log(producto, suma, max_iter=1000):
    """Versión iterativa mejorada para mayor estabilidad"""
    if producto <= 0 or suma <= 0:
        return None
    
    base = producto ** (1/suma) if suma != 0 else 2.0
    
    for _ in range(max_iter):
        try:
            log_val = math.log(producto, base)
            error = log_val - suma
            
            if abs(error) < 1e-10:  
                return base
                
            base *= math.exp(-error/suma)
            
        except (ValueError, ZeroDivisionError):
            return None
            
    return base  

def procesar_cuartetos(datos):
    """Procesamiento robusto de todos los cuartetos"""
    resultados = []
    exitosos = 0
    
    for i in range(0, len(datos), 4):
        if i + 3 >= len(datos):
            continue
            
        cuarteto = datos[i:i+4]
        suma = cuarteto[0] + cuarteto[3]
        producto = cuarteto[1] * cuarteto[2]
        
        base = resolver_ecuacion_log(producto, suma)
        if base is not None:
            exitosos += 1
            estado = f"Base calculada: {base:.6f}"
        else:
            estado = "No se pudo calcular (producto ≤ 0 o no convergió)"
        
        resultados.append({
            "cuarteto": cuarteto,
            "suma": suma,
            "producto": producto,
            "base": base,
            "estado": estado
        })
    
    return resultados, exitosos

def main():
   
    datos_prueba = [2, 3, 4, 2, 1, 5, 5, 1, 8, 2, 2, 8]
    
    resultados, exitosos = procesar_cuartetos(datos_prueba)
    
    productos_validos = [r["producto"] for r in resultados if r["base"] is not None]
    productos_ordenados = quicksort(productos_validos)
    
    print("=== RESULTADOS ===")
    for i, res in enumerate(resultados, 1):
        print(f"\n- Cuarteto {i}: {res['cuarteto']}")
        print(f"  Suma: {res['suma']} | Producto: {res['producto']}")
        print(f"  {res['estado']}")
    
    print("\n=== ESTADÍSTICAS ===")
    print(f"Éxitos: {exitosos} | Fallos: {len(resultados) - exitosos}")
    print(f"Productos ordenados: {productos_ordenados}")

if __name__ == "__main__":
    main()

   
