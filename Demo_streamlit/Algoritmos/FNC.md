# Algoritmo: Conversión de una Gramática independiente de contexto (GIC) a Forma Normal de Chomsky (FNC)

## Enunciado
Transformar una gramática independiente del contexto G a su Forma Normal de Chomsky, donde toda producción tiene uno de estos formatos:
- A → BC (donde B y C son no terminales)
- A → a (donde a es un terminal)
- S → λ (solo si λ ∈ L(G))

## Solución
### Paso 0: Precondiciones
- Sea G = (Σ_T, Σ_N, S, P) / λ∉L(G) una gramática independiente del contexto sin la cadena vacía.
- Las reglas de una gramática solo pueden tener como parte derecha:
 * Un solo símbolo terminal: A → a
 * Exactamente dos símbolos no terminales: Y → SB

### Paso 1: Limpiar gramática

#### 1.1 Aplicar algoritmos de limpieza (apoyarse en el algoritmo de limpieza)
Obtener G' = (Σ_T', Σ_N', S, P') limpia / L(G) = L(G')

#### 1.2 Verificar formato de producciones resultantes
Resultado P': A → w donde:
- si |w|=1 → w∈Σ_T
- si |w|>1 → w∈(Σ_T∪Σ_N)*

### Paso 2: Quitar terminales a la derecha cuando |w|>1

#### 2.1 Identificar producciones con terminales en cadenas largas
∀ A → w / |w|>1, donde A → X₁X₂...Xₙ

#### 2.2 Sustituir terminales por nuevos no terminales
∀ X_i=a∈Σ_T, hacer:
- Crear símbolo C_a ∈Σ_N'
- Transformar a∈Σ_T por C_a∈Σ_N
- Crear producción: C_a → a ∈P'

#### 2.3 Verificar resultado
Resultado: P': A → B₁B₂... Bₙ ∨ A → a
- Donde todos los B_i son no terminales

### Paso 3: Eliminar cadenas a la derecha con |w|>2

#### 3.1 Identificar producciones largas
Si A --> B₁B₂...Bₙ donde n>2

#### 3.2 Binarizar producción
Entonces transformar producción en:
- A-->B₁D₁
- D₁-->B₂D₂
- ...
- D_{n-2}-->B_{n-1}B_n

#### 3.3 Actualizar conjunto de no terminales
Añadir nuevos no terminales D₁, D₂, ..., D_{n-2} ∈Σ_N

### Paso 4: Verificación

#### 1. Estructura de las reglas
- Regla estricta: Toda producción debe cumplir:

* Forma A → BC: exactamente dos no terminales.
* Forma A → a: exactamente un terminal.

#### 2. Manejo correcto de λ
Si λ ∉ L(G):
- Eliminar todas las producciones que generen λ.
- Asegurar que ninguna regla derive en λ indirectamente.
- Si λ ∈ L(G):
Permitir S' → λ solo si S' es el símbolo inicial.
No permitir λ en otras producciones.

- Ejemplo de error:
Si la gramática original tiene S → aSb | λ, en FNC debe:
Introducir S' → S | λ (nuevo símbolo inicial).
Eliminar S → λ y ajustar las reglas restantes para preservar palíndromos pares/impares.

#### 3. Equivalencia de lenguajes
Verificación obligatoria:
- Asegurar que L(G) = L(G'), donde:
G = gramática original.
G' = gramática en FNC.

- Métodos para comprobarlo:
Generar cadenas de ejemplo en ambas gramáticas y comparar.
Usar derivaciones formales o herramientas de parsing para validar equivalencia estructural.

- Caso crítico:
Si la gramática original no genera λ, la FNC tampoco debe incluir S → λ (excepto si es el símbolo inicial).