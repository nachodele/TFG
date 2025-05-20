# Algoritmo: Factorización a Izquierdas para GIC

## Enunciado
La factorización a izquierdas resuelve ambigüedades en gramáticas donde un mismo no terminal tiene producciones con prefijos comunes. Esto es crítico para analizadores predictivos que requieren decisiones únicas en cada paso.

## Solución

### Paso 1: Identificar prefijos comunes
Para cada A ∈ Σ_N (no terminales):
1. Analizar todas sus producciones:  
   `A → γ₁ | γ₂ | ... | γₙ`
2. Agrupar producciones con el mismo prefijo β:  
   `A → β·α₁ | β·α₂ | ... | β·αₚ`  
   Donde:  
   - β ∈ (Σ_T ∪ Σ_N)* (prefijo común)  
   - αᵢ ∈ (Σ_T ∪ Σ_N)* (sufijos diferenciadores)

### Paso 2: Crear nuevo símbolo no terminal
1. Añadir un nuevo no terminal A' al conjunto:  
   `Σ_N' = Σ_N ∪ {A'}`

### Paso 3: Reescribir producciones
Reemplazar el grupo de producciones identificadas por:
A → β·A'
A' → α₁ | α₂ | ... | αₚ

- Propósito: Separar el prefijo común β y delegar las variaciones al nuevo no terminal A'

### Paso 4: Mantener otras producciones
Si A tiene producciones sin prefijo común:  
`A → δ₁ | δ₂ | ... | δₘ` (donde δⱼ no comienzan con β)  
Conservarlas intactas:  
A → β·A' | δ₁ | δ₂ | ... | δₘ

### Paso 5: Verificación

#### Criterios de validación
1. Eliminación de prefijos comunes:  
   - Ningún no terminal debe tener producciones con prefijos idénticos

2. Equivalencia de lenguajes:  
   - Demostrar que L(G) = L(G') mediante derivaciones paralelas

3. Consistencia estructural:  
   - Todas las αᵢ deben ser accesibles desde A'  
   - El prefijo β debe aparecer solo en la producción `A → β·A'`

4. No introducción de ambigüedades:  
   - Cada conjunto de producciones factorizadas debe permitir solo una derivación válida por cadena

#### Métodos de comprobación
- Derivación guiada: Para cadenas que usaban el prefijo común, verificar que solo hay un árbol de derivación en G'  
- Análisis FIRST/FOLLOW: Confirmar que los conjuntos FIRST de las producciones factorizadas son disjuntos  
- Simulación de parser: Ejecutar un analizador predictivo con la gramática modificada para detectar conflictos  
