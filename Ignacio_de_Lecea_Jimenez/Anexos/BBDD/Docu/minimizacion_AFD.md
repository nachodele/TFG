# Algoritmo: Minimización de un Autómata Finito Determinista (AFD)

## Enunciado
Permite obtener un autómata equivalente con el mínimo número de estados posibles. Este proceso se basa en identificar y fusionar estados equivalentes (indistinguibles) mediante un algoritmo de particionamiento iterativo.

## Solucion

### Paso 1: Partición inicial  
Dividir el conjunto de estados Q en dos grupos:  
- Grupo 1: Estados de aceptación (F)  
- Grupo 2: Estados no aceptadores (Q - F)  

### Paso 2: Refinamiento iterativo  
Repetir hasta que no haya cambios en la partición:  
1. Para cada grupo G en la partición actual:  
   - Dividir G en subgrupos donde dos estados s y t pertenecen al mismo subgrupo si:  
     - ∀ símbolo a ∈ Σ, δ(s, a) y δ(t, a) están en el mismo grupo de la partición actual  
2. Reemplazar G por los nuevos subgrupos en la partición  

### Paso 3: Selección de estados representantes  
1. Para cada grupo en la partición final:  
   - Elegir un estado representante (ej: el de menor índice)  
2. Construir tabla de transiciones usando estos representantes  

### Paso 4: Construcción del AFD mínimo  
1. Estado inicial: Representante del grupo que contiene el estado inicial original  
2. Estados finales: Representantes de grupos que contienen al menos un estado final original  
3. Transiciones:  
   - δ_min(Gᵢ, a) = Gⱼ donde Gⱼ contiene δ(q, a) para todo q ∈ Gᵢ  

### Paso 5: Eliminación de redundancias  
1. Estados inactivos:  
   - Eliminar estados no finales con transiciones circulares ∀a ∈ Σ  
2. Estados inalcanzables:  
   - Eliminar estados no accesibles desde el estado inicial  
   - Eliminar transiciones hacia estos estados  

### Paso 6: Verificación  
1. Equivalencia:  
   - Comprobar que L(AFD original) = L(AFD mínimo) mediante pruebas con cadenas críticas  
2. Estabilidad:  
   - Confirmar que la partición final no cambia en iteraciones sucesivas  
3. Optimalidad:  
   - Asegurar que no existen estados equivalentes en el AFD resultante  

### Teorema fundamental de Myhill-Nerode  
El AFD mínimo obtenido es único (salvo renombramiento de estados) y reconoce el mismo lenguaje que el AFD original.  