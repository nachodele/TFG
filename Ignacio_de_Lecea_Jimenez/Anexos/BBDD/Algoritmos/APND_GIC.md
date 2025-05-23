# Algoritmo: Conversión de un Autómata de Pila No Determinista (APND) en una Gramática Independiente del Contexto (GIC)

## Enunciado
Sea M un APND que utiliza su pila únicamente de una de estas dos formas:
- Elimina la cima (desapila). El tamaño de la pila decrece en una unidad.
- Consume su pila y añade dos símbolos nuevos a la pila. El tamaño de la pila crece en una unidad.

## Solucion

### Teorema fundamental
Dado M APND, existe un M' APND equivalente que utiliza la pila únicamente de una de estas dos formas:
- Elimina la cima (desapila). El tamaño de la pila decrece en una unidad.
- Consume su pila y añade dos símbolos nuevos a la pila. El tamaño de la pila crece en una unidad.

### Paso 1: Definición de símbolos no terminales
Crear símbolos de esta forma:
- [qAp] ∈ Σ_N

Donde:
- q, p son estados del APND
- A es un símbolo de pila
- [qAp] representa "desde el estado q, con A en la cima de la pila, se puede llegar al estado p vaciando la pila"

### Paso 2: Creación de producciones para transiciones que desapilan
Si (q_j, λ) ∈ Δ(q_i, a, A):
- Crear producción: [q_iAq_j] → a

Esta producción indica que desde el estado q_i, leyendo 'a' y con A en la cima de la pila, se puede transitar al estado q_j desapilando A.

### Paso 3: Creación de producciones para transiciones que apilan
Si (q_j, BC) ∈ Δ(q_i, a, A):
- Crear producción: [q_iAq_m] → a [q_jBq_n] [q_nCq_m] / q_n, q_m ∈ Q

Esta producción indica que desde el estado q_i, leyendo 'a' y con A en la cima, se puede transitar al estado q_j reemplazando A por BC, y eventualmente llegar a q_m.

### Paso 4: Definición del símbolo inicial
Establecer el símbolo inicial de la gramática:
- S = [q_0Zq_f]

Donde:
- q_0 es el estado inicial del APND
- Z es el símbolo inicial de la pila
- q_f es un estado final del APND

### Paso 5: Verificación

#### Propiedades a verificar
1. Comprobar que la gramática resultante es independiente del contexto
2. Verificar que L(APND) = L(GIC)
3. Confirmar que cada movimiento del APND tiene su equivalencia en la GIC

#### Métodos de comprobación
- Derivar cadenas en la GIC y comprobar su aceptación en el APND original
- Comprobar que las transiciones del autómata están correctamente reflejadas en las producciones
- Verificar que el símbolo inicial representa correctamente el comportamiento del APND desde el estado inicial hasta un estado final
