# Algoritmo: Eliminar la Recursividad por la Izquierda en Múltiples Pasos

## Enunciado
La recursividad por la izquierda indirecta ocurre cuando dos o más símbolos no terminales participan en una cadena de derivaciones que finalmente recrean la recursividad izquierda. Este algoritmo resuelve tanto la recursividad directa como la indirecta.

## Solución

### Paso 1: Ordenar símbolos no terminales
1. Establecer un orden total en Σ_N:  
   `{A₁, A₂, ..., Aₙ | A₁ = S}`  
   - S es el axioma (símbolo inicial)  
   - El orden determina la secuencia de procesamiento  

### Paso 2: Iterar sobre cada no terminal A_i
Para cada `i = 1` hasta `n`:  
1. Eliminar recursividad indirecta:  
   - Para cada `j = 1` hasta `i-1`:  
     a. Identificar producciones de la forma:  
        `A_i → A_jβ` (donde β ∈ (Σ_T ∪ Σ_N)*)  
     b. Si `A_j` tiene producciones:  
        `A_j → α₁ | α₂ | ... | αₘ`  
     c. Reemplazar cada producción `A_i → A_jβ` por:  
        `A_i → α₁β | α₂β | ... | αₘβ`  
   - Propósito: Eliminar dependencias recursivas indirectas con símbolos ya procesados  

2. Eliminar recursividad directa de A_i:  
   - Aplicar el algoritmo de eliminación de recursividad izquierda en un paso:  
     a. Separar producciones de A_i en:  
        - Recursivas: `A_i → A_iγ₁ | ... | A_iγₚ`  
        - No recursivas: `A_i → δ₁ | ... | δₖ`  
     b. Crear nuevo no terminal `A_i'`  
     c. Reescribir producciones:  
        ```
        A_i → δ₁A_i' | ... | δₖA_i'  
        A_i' → γ₁A_i' | ... | γₚA_i' | γ₁ | ... | γₚ  
        ```  

### Paso 3: Verificación

#### Criterios de validación
1. Ausencia de recursividad izquierda:  
   - Ninguna producción debe tener formas:  
     - Directa: `B → Bα`  
     - Indirecta: `B → Cβ →* Bγ`  

2. Preservación del lenguaje:  
   - Todas las cadenas generadas por la gramática original deben ser generables en la nueva  
   - No se deben introducir cadenas nuevas  

3. Terminación de derivaciones:  
   - Cada aplicación de producción debe acercar a una cadena terminal  

#### Métodos de comprobación
- Derivación de cadenas críticas: Probar cadenas que explotaban la recursividad original  
- Análisis de árboles de derivación: Comparar estructuras en ambas gramáticas  
- Conversión a AF: Demostrar equivalencia mediante autómatas finitos  

