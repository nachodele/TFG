# Algoritmo: Conversión de un Automata finito no determinista (AFND) a un Automata finito determinista (AFD). (Método de Subconjuntos)

## Enunciado
El objetivo es diseñar un procedimiento sistemático que, a partir del conjunto de estados y transiciones del AFND, genere un AFD que reconozca exactamente el mismo lenguaje, asegurando que cada estado del AFD represente un subconjunto de estados del AFND original.

## Solución

- Definiciones clave
### Cierre-λ (ε-clausura)
Para un conjunto de estados S en un AFN:
- Cierre-λ(S) = Conjunto de todos los estados alcanzables desde S usando 0 o más transiciones λ.
- Cálculo:
  1. Inicializar `cierre_λ(S) = S`
  2. Usar una pila/cola para procesar estados:
     - Para cada estado `s` en `cierre_λ(S)`:
       - Añadir todos los estados `t` alcanzables desde `s` mediante λ-transiciones
       - Repetir hasta que no se añadan nuevos estados

### Función mueve(T, a)
- mueve(T, a) = Conjunto de estados alcanzables desde T usando exactamente una transición con el símbolo `a` (sin considerar λ-transiciones).

### Paso 1: Inicialización
1. Calcular el estado inicial del AFD:
   - `U = cierre_λ({q₀})` donde `q₀` es el estado inicial del AFN
2. Añadir `U` a `estados_AFD` como no marcado

### Paso 2: Procesar estados del AFD
Mientras existan estados no marcados en `estados_AFD`:
1. Seleccionar un estado T no marcado
2. Marcar T
3. Para cada símbolo `a` ∈ Σ:
   - Calcular `U = cierre_λ(mueve(T, a))`
   - Si `U ∉ estados_AFD`:
     - Añadir `U` a `estados_AFD` como no marcado
   - Definir transición: `tran_AFD[T, a] = U`

### Paso 3: Definir estados finales del AFD
Un estado `T` del AFD es final si contiene al menos un estado final del AFN original.

#### Estructuras de datos
- estados_AFD: Lista de conjuntos de estados del AFN (representan estados del AFD)
- tran_AFD: Tabla de transiciones del AFD (clave: estado AFD + símbolo, valor: estado AFD)
- Pila/Cola: Para gestionar estados no marcados (implementación eficiente)

### Paso 4: Verificación

#### Criterios de validación
1. Determinismo:
   - Para cada estado `T` y símbolo `a`, `tran_AFD[T, a]` debe estar exactamente definido
2. Equivalencia de lenguajes:
   - Comprobar que `L(AFD) = L(AFN)` mediante pruebas con cadenas críticas
3. Completitud:
   - Todos los estados accesibles desde el inicial deben estar en `estados_AFD`

#### Métodos de comprobación
- Simulación paralela: Para una cadena `w`, comparar el recorrido en el AFD con todos los posibles recorridos en el AFN
- Minimización: Aplicar el algoritmo de minimización de AFD para verificar si el resultado es óptimo