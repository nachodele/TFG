# Algoritmo: Limpieza o Simplificación de Gramáticas

## Enunciado
Este proceso transforma una gramática independiente del contexto (GIC) en una forma normal o estándar, eliminando elementos innecesarios mientras preserva el lenguaje generado.

## Solución

## Algoritmo 1: Eliminar No Terminales que no deriven cadenas terminales

### Definición del problema
Sea G = (Σ_T, Σ_N, S, P) una GIC. Transformar G en G' = (Σ_T, Σ_N', S, P'), tal que L(G) = L(G')

### Pasos
1. Inicializar Σ_N' = {A ∈ Σ_N | (A → w) ∈ P y w ∈ Σ_T*}
2. Inicializar P' = {(A → w) ∈ P | A ∈ Σ_N' y w ∈ Σ_T*}
3. Repetir:
   - Añadir No Terminales a Σ_N':
     Σ_N' = Σ_N' ∪ {A ∈ Σ_N | (A → w) ∈ P y w ∈ (Σ_T ∪ Σ_N')*}
   - Hasta que no se puedan añadir más elementos No Terminales a Σ_N'

## Algoritmo 2: Eliminar Reglas y Producciones que no deriven del axioma

### Definición del problema
Sea G = (Σ_T, Σ_N, S, P) una GIC. Transformar G en G' = (Σ_T', Σ_N', S, P'), tal que L(G) = L(G')

### Pasos
1. Inicializar Σ_N' = {S}, P' = ∅, Σ_T' = ∅
2. Repetir:
   - ∀A ∈ Σ_N' | (A → w) ∈ P:
     2.1. Añadir (A → w) ∈ P'
     2.2. ∀B ∈ Σ_N | B ∈ w: Añadir B ∈ Σ_N'
     2.3. ∀a ∈ Σ_T | a ∈ w: Añadir a ∈ Σ_T'
     Σ_N' = Σ_N' ∪ {A ∈ Σ_N | (A → w) ∈ P y w ∈ (Σ_T ∪ Σ_N')*}
   - Hasta que no se puedan añadir nuevas producciones a P'

## Algoritmo 3: Eliminar las λ-producciones

### Identificar No Terminales Anulables
a) Sea G = (Σ_T, Σ_N, S, P). Extraer conjunto de anulables:
   a.1) Inicializar η = {A ∈ Σ_N | (A → λ)}
   a.2) Repetir:
        - Si B → w | w ∈ (Σ_N)* y todos los símbolos w_i ∈ η
          Añadir B ∈ η
        - Hasta que no se puedan añadir Σ_N a η

### Eliminar λ-producciones
b) Sustituir producciones B → X_1X_2...X_n, eliminando subconjuntos X_i anulables:
   b.1) Crear P' = ∅
   b.2) Si B → X_1X_2...X_n ∈ P:
        Entonces Añadir a P': B → Y_1Y_2...Y_n donde:
        - Y_i = X_i, si X_i no es anulable
        - Y_i = X_i ó λ, si X_i es anulable (combinaciones)
        - No introducir B → λ
   NOTA: Pueden aparecer nuevas producciones al combinar todas las soluciones Y_i = X_i ó λ

c) Si S ∈ η → Añadir S → λ a P

## Algoritmo 4: Eliminar las producciones unitarias

### Definición del problema
Sea G = (Σ_T, Σ_N, S, P) una GIC sin λ-transiciones. Transformar G en G' = (Σ_T, Σ_N', S, P'), tal que L(G) = L(G')

### Pasos
a) Construir conjuntos unitarios:
   - Para cada A ∈ Σ_N, construir:
     Unitario(A) = {B ∈ Σ_N | A →* B}
   - Donde →* representa la clausura reflexiva y transitiva de →

b) Eliminar Unitarios:
   1. Inicializar P' = P
   2. Para cada A ∈ Σ_N | Unitario(A) ≠ {A}:
      - Para cada B ∈ Unitario(A):
        - Para cada producción no unitaria (B → w) ∈ P:
          - Añadir (A → w) ∈ P'
   3. Eliminar todas las producciones unitarias de P'

## Nota sobre el orden de aplicación
Los algoritmos se pueden aplicar en distinto orden siempre que:
- Algoritmo 1 preceda al Algoritmo 2
- Algoritmo 3 preceda al Algoritmo 4

## Verificación
1. Comprobar que L(G) = L(G') verificando:
   - No hay no terminales inútiles
   - No hay producciones inaccesibles desde el axioma
   - No hay λ-producciones (excepto posiblemente S → λ)
   - No hay producciones unitarias
2. Verificar que todas las producciones tienen la forma correcta en la gramática resultante
