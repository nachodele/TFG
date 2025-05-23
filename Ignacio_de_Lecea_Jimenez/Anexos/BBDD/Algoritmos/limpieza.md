# Algoritmo: Simplificación de una gramática independiente de contexto (GIC)

## Enunciado
Simplificación (=limpieza) de una gramática.
Este proceso transforma una gramática independiente del contexto (GIC) en una forma normal o estándar, eliminando elementos innecesarios mientras preserva el lenguaje generado.

## Solución

### Algoritmo 1: Eliminar No Terminales que no deriven cadenas terminales  
Objetivo: Eliminar símbolos no terminales que no puedan generar cadenas compuestas únicamente por terminales.  

#### 1. Inicialización:  
   - `Σ_N'`: Contiene SOLO los no terminales con al menos una producción directa a cadenas de SOLO terminales.
   - `P'`: Solo incluye producciones donde el lado derecho sean exclusivamente terminales.
   - ATENCIÓN: Un no terminal como `A → BC` NO se incluye en esta fase inicial.
   - ATENCIÓN: Un no terminal como `A → aB` NO se incluye en esta fase inicial.

#### 2. Iteración (proceso hasta punto fijo):  
   - En cada iteración, se añaden a `Σ_N'` SOLO los no terminales que puedan derivar cadenas usando ÚNICAMENTE:
     * Símbolos terminales, o
     * No terminales ya presentes en `Σ_N'`
   - EJEMPLO CORRECTO: Si tenemos `B → CD` y ya sabemos que `C, D ∈ Σ_N'`, entonces añadimos `B` a `Σ_N'`.
   - EJEMPLO CORRECTO: Si tenemos `E → aF` y ya sabemos que `F ∈ Σ_N'`, entonces añadimos `E` a `Σ_N'`.
   - EJEMPLO INCORRECTO: Si tenemos `G → aH` pero `H ∉ Σ_N'`, entonces NO podemos añadir `G` a `Σ_N'`.

#### 3. Detección de no generativos:
   - CRÍTICO: Cualquier no terminal que no esté en `Σ_N'` al finalizar el algoritmo es NO GENERATIVO.
   - Casos particulares a detectar:
     * Recursión sin salida: Un no terminal como `B → aB` (sin reglas alternativas) NUNCA puede generar una cadena terminal.
     * Dependencias circulares: Si `X → Y` y `Y → Z` y `Z → X` (sin otras alternativas), ninguno puede generar terminales.
     * Recursiones indirectas: Si `A → BC`, `C → AD`, entonces hay una dependencia circular que impide generar.

#### 4. Eliminación obligatoria:
   - Se DEBEN eliminar TODAS las producciones que contengan al menos un símbolo no generativo.
   - EJEMPLO: Si `B` no es generativo, entonces se eliminan todas las producciones de la forma `A → αBβ` y `B → γ`.
   - REGLA ESTRICTA: Si todos los no terminales en la parte derecha de una producción no son generativos, esa producción DEBE ser eliminada.

### Algoritmo 2: Eliminar Reglas y Producciones que no deriven del axioma  
Objetivo: Eliminar símbolos y producciones inaccesibles desde el símbolo inicial `S`.  

#### 1. Inicialización:  
   - Inicialmente, SOLO `S` está en `Σ_N'`. Tanto `P'` como `Σ_T'` comienzan vacíos.

#### 2. Expansión (proceso iterativo):  
   - Para cada no terminal `A` en `Σ_N'`, se añaden TODAS sus producciones a `P'`.
   - Todos los símbolos que aparecen en el lado derecho de estas producciones:
     * Si es un terminal, se añade a `Σ_T'`
     * Si es un no terminal, se añade a `Σ_N'`

#### 3. Verificación de accesibilidad:
   - Al finalizar, cualquier símbolo (terminal o no terminal) que no esté en `Σ_T'` o `Σ_N'` es INACCESIBLE.
   - Todas las producciones que contengan símbolos inaccesibles DEBEN ser eliminadas.

### Algoritmo 3: Eliminar las λ-producciones  
Objetivo: Eliminar producciones vacías (`A → λ`), excepto posiblemente `S → λ` si λ pertenece al lenguaje.  

#### 1. Identificación precisa de anulables:  
- Paso a: Se identifican todos los no terminales que puedan derivar en `λ`, directa o indirectamente:
  - Se inicia con aquellos con producciones directas hacia `λ`
  - Se añaden aquellos que pueden derivar a una cadena de solo anulables
  - EJEMPLO: Si `A → λ` y `B → A`, entonces `B` es anulable.
  - EJEMPLO: Si `C → DE` y tanto `D` como `E` son anulables, entonces `C` es anulable.
  - CRÍTICO: Si un no terminal sólo tiene producciones con al menos un no terminal no anulable, entonces NO es anulable.

#### 2. Eliminación precisa de λ-producciones:  
- Paso b: Para cada producción `B → X₁X₂...Xₙ` donde algún Xᵢ es anulable:
  - Se crean TODAS las combinaciones posibles omitiendo uno o más símbolos anulables.
  - EJEMPLO CORRECTO: Si `B → AC` y tanto `A` como `C` son anulables, se añaden `B → AC`, `B → A`, `B → C`, `B → λ`.
  - REGLA CRÍTICA: Sólo se generan nuevas producciones si el símbolo anulable aparece en la parte derecha de alguna regla.
  - RESTRICCIÓN IMPORTANTE: Si ninguna regla contiene un símbolo anulable en su parte derecha, NO se generan nuevas producciones.

#### 3. Tratamiento especial del axioma:
  - Si `S` es anulable y `λ` pertenece al lenguaje, se mantiene SOLO la producción `S → λ`.
  - Si `S` no aparece en ninguna parte derecha de otra producción, entonces ser anulable NO genera nuevas producciones.

### Algoritmo 4: Eliminar las producciones unitarias  
Objetivo: Eliminar reglas de la forma `A → B`, donde `B` es un no terminal.  

#### 1. Construcción precisa de conjuntos unitarios:  
   - Para cada no terminal `A`, se calcula `Unitario(A) = { B | A →* B usando SOLO producciones unitarias }`.
   - SIEMPRE incluir el propio `A` en su conjunto unitario.
   - EJEMPLO: Si `A → B` y `B → C`, entonces `Unitario(A) = {A, B, C}`.

#### 2. Sustitución completa:  
   - Para cada `A` y cada `B` en `Unitario(A)`, se añaden a `A` TODAS las producciones no unitarias de `B`.
   - EJEMPLO: Si `A →* C` y `C → a`, se añade `A → a`.
   - EJEMPLO: Si `A →* D` y `D → EF`, se añade `A → EF`.
   - REGLA ESTRICTA: Se eliminan TODAS las producciones unitarias originales.

### Orden de Aplicación y Verificación  
1. Los algoritmos DEBEN aplicarse en este orden preciso:
   - Algoritmo 1 (eliminar no generativos) → 
   - Algoritmo 2 (eliminar inaccesibles) → 
   - Algoritmo 3 (eliminar λ-producciones) → 
   - Algoritmo 4 (eliminar unitarias)

2. Razones del orden:
   - Si se aplica el Algoritmo 2 antes que el 1, podrían quedar símbolos no generativos.
   - El Algoritmo 3 puede generar producciones unitarias, que luego elimina el Algoritmo 4.

### Verificación final obligatoria:  
- Asegurar que:  
  - No queda ningún símbolo no generativo (especialmente verificar recursiones infinitas como `B → aB`)
  - No queda ningún símbolo inaccesible desde `S`
  - No quedan λ-producciones (excepto posiblemente `S → λ` si λ ∈ L(G))
  - No quedan producciones unitarias (`A → B` donde B es un no terminal)
- La gramática resultante DEBE generar exactamente el mismo lenguaje que la original.

### Errores críticos a evitar:
1. No detectar no terminales que solo pueden generar cadenas infinitas (como `B → aB` sin alternativas)
2. Aplicar incorrectamente el Algoritmo 1 omitiendo la eliminación de reglas con no terminales no generativos
3. Generar producciones falsas al eliminar λ-producciones cuando el símbolo anulable no aparece en partes derechas
4. Conservar producciones unitarias después de aplicar el Algoritmo 4