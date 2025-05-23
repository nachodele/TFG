# Algoritmo: Conversión de una Gramática independiente de contexto (GIC) a Forma Normal de Greibach (FNG)

## Enunciado
Una gramática G = (Σ_T, Σ_N, S, P), G.I.C. está en FNG si no contiene λ y todas las producciones son de la forma:
- A → aα donde A∈Σ_N, a∈Σ_T, α ∈(Σ_T∪Σ_N)*

FNG alternativa (preferida):
- A → aα donde A∈Σ_N, a∈Σ_T, α ∈Σ_N*

## Solucion

### Teoremas fundamentales

#### Teorema 1: Propagación de producciones
Si A → αβγ y β → β₁ | β₂ |...| βₙ
Entonces transformar A → αβγ en:
- A → αβ₁γ | αβ₂γ |...| αβₙγ

#### Teorema 2: Eliminación de recursividad por la izquierda
Sea A → Aα₁ | Aα₂ |...| Aαₙ | β₁ | β₂ |...| βₘ
Transformar en:
- A → β₁ | β₂ |...| βₘ | β₁Z | β₂Z |...| βₘZ
- Z → α₁ | α₂ |...| αₙ | α₁Z | α₂Z |...| αₙZ

Con Z como nuevo símbolo no terminal

### Paso 1: Preparación
Sea G = (Σ_T, Σ_N, S, P) una GIC limpia, donde:
- Σ_N = {A₁, A₂,..., Aₙ} con un orden establecido 
- A₁ = S (símbolo inicial)

#### Objetivo
Obtener producciones de la forma: Aᵣ → Aₛα / r < s

#### Proceso
1. Para cada Aⱼ ∈ Σ_N, repetir:
   1. Si Aₖ → Aⱼα, con k > j:
      - Aplicar Teorema 1 (propagación)
   2. Si Aₖ → Aⱼα, con k = j (recursiva):
      - Aplicar Teorema 2 (eliminación de recursividad)
   3. Continuar hasta que todas las producciones sean: Aᵣ → Aₛα donde r < s

### Paso 2: Eliminación de producciones Aᵢ → Aⱼα (i < j)
1. Sacar A → Bα de P
2. Para cada p∈P donde B → β:
   - Añadir A → βα

### Paso 3:Conversión final a FNG
1. Con este proceso, las reglas cuya parte izquierda es un antiguo símbolo no terminal ya están en FNG
2. Para convertir reglas con parte izquierda formada por un nuevo no terminal a FNG:
   - Aplicar el Teorema 1 sobre estas reglas

### Paso 4: Verificación
1. Comprobar que todas las producciones tienen la forma A → aα donde:
   - a es un símbolo terminal
   - α es una cadena (posiblemente vacía) de no terminales
2. Verificar que se conserva el lenguaje: L(G) = L(G')
