# Algoritmo: Eliminar la Recursividad por la Izquierda en un paso

## Enunciado
Cuando un símbolo no terminal A tiene producciones de la forma A → Aα, lo que impide el análisis predictivo. El objetivo es transformar la gramática original en una equivalente sin recursividad izquierda.

## Solución

### Paso 1: Identificar símbolos no terminales con recursividad
Para cada A ∈ Σ_N (conjunto de no terminales):
1. Analizar todas sus producciones:  
   `A → γ₁ | γ₂ | ... | γₙ`
2. Clasificar las producciones en dos grupos:  
   - Recursivas por la izquierda: `A → Aα₁ | Aα₂ | ... | Aαₚ`  
   - No recursivas: `A → β₁ | β₂ | ... | βₘ`  
   Donde:  
   - αᵢ ∈ (Σ_T ∪ Σ_N)*  
   - βⱼ ∈ (Σ_T ∪ Σ_N)* y βⱼ no comienza con A

### Paso 2: Crear nuevo símbolo no terminal
Para cada A con recursividad identificada:
1. Añadir un nuevo no terminal A' al conjunto:  
   `Σ_N' = Σ_N ∪ {A'}`

### Paso 3: Reescribir producciones del no terminal original
Reemplazar las producciones de A por:  
A → β₁A' | β₂A' | ... | βₘA'
A → β₁ | β₂ | ... | βₘ

- Propósito: Romper la recursión directa usando el nuevo no terminal A'
- Restricción: Ningún βⱼ puede comenzar con A

### Paso 4: Definir producciones del nuevo no terminal
Para el nuevo A', crear producciones que capturan la recursión residual:  
A' → α₁A' | α₂A' | ... | αₚA'
A' → α₁ | α₂ | ... | αₚ

- Nota: Cada αᵢ corresponde a la parte derecha de las producciones recursivas originales (sin el A inicial)

### Paso 5: Eliminar producciones recursivas originales
Remover del conjunto P todas las producciones de la forma:  
`A → Aαᵢ`

### Paso 6: Verificación

#### Criterios de validación
1. Ausencia de recursividad izquierda:  
   - Ninguna producción debe tener la forma `B → Bγ` para cualquier B ∈ Σ_N

2. Equivalencia de lenguajes:  
   - Comprobar que L(G) = L(G') mediante derivaciones de cadenas representativas

3. Consistencia en las producciones:  
   - Todas las βⱼ deben ser accesibles desde A  
   - Todas las αᵢ deben ser alcanzables desde A'

4. Terminación garantizada:  
   - Cada derivación en G' debe tener un camino finito hacia símbolos terminales

#### Métodos de comprobación
- Derivación inversa: Generar cadenas con la gramática original y verificar que son aceptadas por la nueva  
- Autómatas equivalentes: Construir AFNs a partir de ambas gramáticas y demostrar equivalencia  
- Análisis de cadenas críticas: Probar cadenas que exploten la recursividad original (ej: `A → Aa | b` → probar `baaaa`)  

