# Algoritmo: Cocke-Younger-Kasami (CYK)

## Enunciado
Algoritmo de análisis sintáctico para gramáticas independientes del contexto. Permite determinar si una cadena pertenece al lenguaje generado por una gramática en Forma Normal de Chomsky mediante programación dinámica.

## Solucion

### Paso 0:Prerequisitos
#### Condiciones necesarias de la gramática inicial
* G = (Σ_N, Σ_T, S, P), debe ser una GIC sin producciones compresoras
* G debe estar en Forma Normal de Chomsky (FNC):
  - Producciones de la forma A → BC donde A, B, C ∈ Σ_N
  - Producciones de la forma A → a donde A ∈ Σ_N, a ∈ Σ_T
#### Cadena
- w ∈ Σ_T* es la cadena de entrada a analizar

### Definiciones fundamentales

#### Definición de subcadenas
- w_ij ∈ Σ_T* es una subcadena de w ∈ Σ_T*:
  - Comienza con el símbolo de la posición i
  - Tiene longitud j
  - w_ij = w_i w_{i+1}...w_{i+j-1}
- Observación: w_1n = w si |w| = n

#### Definición de conjuntos de no terminales
- N_ij = { A ∈ Σ_N | A -->* w_ij }
  - Es el conjunto de no terminales que pueden derivar la subcadena w_ij

### Paso 1: Inicialización de subcadenas unitarias
Para i = 1 hasta n
   1. N_i1 = { A | A → a y el símbolo i-ésimo de w es a }

### Paso 2: Construcción de la tabla
Para j = 2 hasta n
   1. Para i = 1 hasta n-j+1
      1. N_ij = ∅
      2. Para k = 1 hasta j-1
         1. N_ij = N_ij ∪ { A | A → BC, B ∈ N_ik, C ∈ N_{i+k,j-k} }

### Paso 3: Verificación
Si S ∈ N_1n → w ∈ L(G)

#### Explicación
- Este algoritmo calcula para todo i,j (i ∈ {1,...,n}, j ≤ n-i+1), el conjunto de variables que generan w_ij, donde w_ij es la subcadena de w que comienza en el símbolo que ocupa la posición i y que contiene j símbolos.
- La palabra w será generada por la gramática si la variable inicial S pertenece al conjunto N_1n.
- Los cálculos se organizan en una tabla triangular donde cada celda N_ij contiene los no terminales que pueden derivar la subcadena correspondiente.