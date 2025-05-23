# Algoritmo: Conversión de una gramática independiente del contexto (GIC) a un autómata de pila no determinista (APND)

## Enunciado
Dada una gramática independiente del contexto (GIC) G = (Σ_T, Σ_N, S, P), construir un autómata de pila no determinista (APND) M tal que L(G) = L(M).

## Solucion
### Paso 1: Construcción formal del APND

Definimos el autómata M como:
- Estados: Q = {q₁, q₂, q₃}
- Alfabeto de entrada: Σ_T
- Alfabeto de la pila: Γ = Σ_T ∪ Σ_N ∪ {z}, donde z es un símbolo especial de fondo de pila
- Función de transición: Δ
- Estado inicial: q₁
- Estados finales: {q₃}
- Símbolo inicial de la pila: z

### Paso 2: Reglas de construcción de Δ

1. Inicialización de la pila  
   - Δ(q₁, λ, z) = {(q₂, S z)}  
   (Desde q₁, con la pila en z y sin consumir entrada, apilar S sobre z y pasar a q₂)

2. Expansión de variables según las reglas de la GIC  
   - Para cada producción A → w en P:  
     Δ(q₂, λ, A) = {(q₂, w)}  
   (En q₂, si el tope de la pila es A, reemplazarlo por w sin consumir entrada)

3. Consumo de símbolos terminales  
   - Para cada a ∈ Σ_T:  
     Δ(q₂, a, a) = {(q₂, λ)}  
   (En q₂, si el símbolo de entrada es a y el tope de la pila es a, consumir a de la entrada y desapilar a)

4. Aceptación  
   - Δ(q₂, λ, z) = {(q₃, z)}  
   (En q₂, si el tope de la pila es z y no queda entrada, pasar a q₃ y dejar z en la pila)

### Paso 3: Descripción del funcionamiento

1. Inicio:  
   El autómata comienza en q₁ con la pila conteniendo solo z.

2. Carga de la variable inicial:  
   Sin consumir entrada, apila S sobre z y pasa a q₂.

3. Derivación:  
   En q₂, aplica producciones de la gramática:  
   - Si el tope de la pila es un no terminal A, lo reemplaza por el lado derecho de alguna producción A → w.

4. Consumo de entrada:  
   Si el tope de la pila es un terminal a y el siguiente símbolo de entrada es a, consume a de la entrada y lo desapila.

5. Aceptación:  
   Cuando la pila contiene solo z y toda la entrada ha sido consumida, el autómata pasa a q₃ y acepta la cadena.

### Paso 4: Verificación

- Equivalencia:  
  El lenguaje aceptado por el APND, L(M), es exactamente el lenguaje generado por la gramática original, L(G).
- Correctitud:  
  Cada derivación de la GIC se simula por una secuencia de movimientos del APND, y viceversa.
- Aceptación por estado final:  
  La aceptación ocurre si se llega al estado q₃ con la pila en z y sin entrada restante.