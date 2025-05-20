# Algoritmo: Conversión de una Expresion Regular (ER) a Gramática Regular (GR) a Autómata Finito (AF)

## Enunciado
El método de las derivadas permite resolver el problema de síntesis de Kleene, generando el autómata que acepta el lenguaje descrito por cualquier expresión regular (ER→AF) en tres pasos:
1. Calcular derivadas de la ER
2. Calcular gramática de tipo 3 que genera el lenguaje representado por la ER (ER→GR)
3. Transformar la gramática al AF (GR→AF)

## Solución

### Paso 1: Cálculo de derivadas

#### Definición de derivada
Derivada de una ER α respecto de un símbolo a∈Σ:
- D_a(α) = {x | ax ∈ α}

#### Reglas de cálculo
- D_a(∅) = ∅
- D_a(λ) = ∅
- D_a(a) = λ
- D_a(b) = ∅, ∀ b∈Σ, b ≠ a
- D_a(α+β) = D_a(α) + D_a(β)
- D_a(α·β) = D_a(α)·β + δ(α)·D_a(β) donde δ(α)= { λ si λ∈α,
                                                   ∅ si λ∉α}
- D_a(α*) = D_a(α)·α*

#### Composición de derivadas
- D_ab(α) = D_b(D_a(α))

#### Derivadas sucesivas
Podemos extender la noción de derivada a palabras completas:
- D_λ(α) = α (derivada respecto a la palabra vacía)
- D_ω(α) = D_a(D_ω'(α)) donde ω = aω'

#### Conjunto de derivadas
El conjunto de todas las derivadas posibles de una expresión regular α se denota:
- Der(α) := {D_ω(α) : ω ∈ Σ*}

Este conjunto es siempre finito, lo que permite construir un autómata finito.

#### Proceso para calcular todas las derivadas
1. Calcular derivadas de la ER=α_0:
   a) ∀a ∈ Σ:
      Calcular α_i=D_a(α_0), empezando por i=1.
   b) Para cada α_i nuevo generado:
      Calcular ∀a ∈ Σ, α_j=D_a(α_i)
   c) Repetir hasta que no se generen nuevos α_i

### Paso 2: Creación de una gramática

#### Definición de la gramática
Construiremos una gramática G a partir de una ER (ER→G):
- G = (Σ, {α_0...α_i}, α_0, P)

#### Construcción del conjunto de producciones P
Donde P se construye así:
a) Si D_a(α) = β, β≠λ, β≠∅:
   - Crear regla: α → aβ
b) Si λ ∈ D_a(α):
   - Crear regla: α → a
c) Si λ ∈ α_0:
   - Crear regla: α_0 → λ
d) Si D_a(α) = ∅:
   - No generar ninguna regla
e) Restricción de formato:  
   Todas las producciones deben ser de la forma:  
   - `X → aY` (transición)  
   - `X → a` (terminal)  
   - `X → λ` (solo si `λ ∈ L(α)` y `X` es el símbolo inicial).

#### Algoritmo detallado para gramática
1. Hallar todos los elementos del conjunto Der(α)
2. Definir un conjunto V de variables biyectable con Der(α)
   - La variable inicial q_0 se relaciona con la expresión α
3. Inicializar P1 := ∅ y P2 := {q_0 → λ} si λ ∈ L(α), ∅ en caso contrario
4. Mientras P2 ≠ P1:
   - P1 := P2
   - Para cada β ∈ Der(α):
     - Para cada a ∈ Σ:
       - Calcular γ := D_a(β), p := E(γ) y q := E(β) en V
       - Si λ ∈ L(γ), hacer P2 := P2 ∪ {q → a}
       - Si γ ≠ ∅, λ, hacer P2 := P2 ∪ {q → ap}
            - Si γ = λ → Añadir β → a
            - Si γ ≠ λ:
               - Asignar a γ un único no terminal p (nuevo o existente)
               - Añadir β → ap (¡Nunca β → aγ₁γ₂...γₙ!)
5. La gramática resultante es G = (V, Σ, q_0, P2)

Manejo explícito de λ y ∅ en producciones
1. Reglas para λ:

- Si λ ∈ L(α) y α es el símbolo inicial: Añadir solo una producción: α → λ (nunca en símbolos no iniciales).
- Si λ ∈ D_a(β) para un no terminal β ≠ α_0: Generar β → a (no usar β → aλ).

2. Reglas para ∅:

- Si D_a(α) = ∅: No crear ninguna producción asociada.
- Si una derivada conduce a ∅: Excluirla del conjunto de variables gramaticales V.

3. Restricciones reforzadas:

- Eliminar producciones que contengan ∅ en la derecha.
- Prohibir λ como símbolo terminal (solo se usa como cadena vacía).

### Paso 3: Obtención del AF

Existen dos opciones para obtener el autómata finito:

#### Opción 1: Directamente desde las derivadas (ER→AF)
AF = (Σ, {α_i}∪{q_f}, δ, α_0, {q_f})
El autómata generado es un AFND-λ (autómata finito no determinista con transiciones-λ) porque:
- Permite transiciones-λ si λ ∈ α_0 (ej: δ(α_0, λ) = q_f).
- Puede tener múltiples transiciones para un mismo símbolo desde un estado.

Donde δ se construye así:
a) Si D_a(α) = β, β≠λ, β≠∅:
   - Crear transición: δ(α,a) = β
b) Si λ ∈ D_a(α):
   - q_f ∈ δ(α,a)
c) Si λ ∈ α_0:
   - q_f ∈ δ(α_0, λ)
d) Si D_a(α) = ∅:
   - δ(α,a) = ∅

#### Opción 2: Desde la gramática (GR→AF)
Sea G = (Σ_T, Σ_N, S, P) → AF = (Σ_T, Σ_N∪{q_f}, δ, S, {q_f})

Donde δ se construye así:
a) Para cada p ∈ P: α → aβ / α,β ∈ Σ_N, a ∈ Σ_T:
   - δ(α,a) = β
b) Para cada p ∈ P: α → a / α ∈ Σ_N, a ∈ Σ_T:
   - q_f ∈ δ(α,a)
c) Si {S → λ} ∈ P:
   - δ(S, λ) = q_f

El autómata generado es un AFN (autómata finito no determinista) debido a:
- Transiciones del tipo δ(X, a) = Y sin restricciones de unicidad.
- Si se requiere un AFD, aplicar el algoritmo de construcción de subconjuntos después.


#### Reglas ajustadas para linealidad:
- Para cada producción `X → aY`: 
Crear transición `δ(X, a) = Y`.  
- Para cada producción `X → a`: 
Crear transición `δ(X, a) = q_f`.  
- Prohibido: Transiciones del tipo `δ(X, a) = YZ`.

### Paso 4: Verificación

#### Verificación del cálculo de derivadas
1. Comprobar que el conjunto de derivadas calculado es finito
2. Verificar que cada derivada D_a(α) se ha calculado aplicando correctamente las reglas de cálculo
3. Confirmar que cada derivada representa el residuo del lenguaje tras leer el símbolo correspondiente
4. Asegurar que ∅ no aparezca en ninguna producción.
5. Validar que λ solo está en producciones del símbolo inicial (si aplica)

#### Verificación de la gramática resultante
1. Comprobar que toda producción en la gramática corresponde a una derivada calculada
2. Verificar que la gramática generada es de tipo 3 (regular)
3. Confirmar que no existen producciones redundantes o inalcanzables
4. Ninguna producción tiene >1 símbolo no terminal en la derecha.  
5. No hay producciones unitarias (`X → Y`).  
6. Todas las reglas son derecho-lineales.  


#### Verificación del autómata finito
1. Comprobar que cada estado del autómata corresponde a una derivada distinta
2. Verificar que las transiciones representan correctamente el cálculo de derivadas
3. Confirmar que el autómata reconoce exactamente el mismo lenguaje que la expresión regular original
4. No hay transiciones con cadenas (ej: `δ(q, ab)`). 
5. Confirmar que el autómata es AFN/AFN-λ según corresponda.
6. Si se requiere AFD, verificar que no haya transiciones-λ ni múltiples transiciones por símbolo.