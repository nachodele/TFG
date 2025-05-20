# Algoritmo de Thompson: Conversión de expresiones regulares (ER) en autómatas finitos no deterministas (AFND).

## Enunciado
El algoritmo de Thompson es un método estándar para convertir expresiones regulares (ER) en autómatas finitos no deterministas (AFND), garantiza la construcción de un AFN que reconoce exactamente el mismo lenguaje que la expresión regular original.

## Solución

### Paso 1: Construcción de ERs básicas
Cada expresión regular básica se traduce directamente a un AFN simple:

#### Expresiones Regulares Básicas
- ER = a (símbolo único)
  - Un estado inicial q₀
  - Un estado final q₁
  - Una transición etiquetada con 'a' de q₀ a q₁

- ER = λ (cadena vacía)
  - Un estado inicial q₀
  - Un estado final q₁
  - Una transición λ (o ε) de q₀ a q₁

- ER = a* (cero o más repeticiones)
  - Un estado q₀ que es tanto inicial como final
  - Una transición que va de q₀ a sí mismo etiquetada con 'a'

- ER = a+ (una o más repeticiones)
  - Un estado inicial q₀
  - Un estado final q₁
  - Una transición de q₀ a q₁ etiquetada con 'a'
  - Una transición de q₁ a sí mismo etiquetada con 'a'

- ER = a? (cero o una instancia)
  - Un estado inicial q₀
  - Un estado intermedio q₁
  - Un estado final q₂
  - Una transición de q₀ a q₁ etiquetada con 'a'
  - Una transición λ de q₁ a q₂
  - Una transición λ directa de q₀ a q₂
  
- ER = a|b (Alternativa)
Alternativa entre los símbolos 'a' y 'b'. Su autómata finito equivalente tiene:

- Un estado inicial q₀
- Dos estados intermedios q₁ y q₂
- Un estado final q₃
- Una transición de q₀ a q₁ etiquetada con 'a'
- Una transición de q₀ a q₂ etiquetada con 'b'
- Transiciones λ de q₁ a q₃ y de q₂ a q₃

- ER = ab (Concatenación)
Concatenación de los símbolos 'a' y 'b'. Su autómata finito equivalente tiene:

- Un estado inicial q₀
- Un estado intermedio q₁
- Un estado final q₂
- Una transición de q₀ a q₁ etiquetada con 'a'
- Una transición de q₁ a q₂ etiquetada con 'b'

### Paso 2: Operaciones compuestas (Diagramas de Thomson)

#### Concatenación (r.s)
Para dos expresiones r y s con sus respectivos AFNs:
1. Identificar AFN(r) con estados q₀ a qₙ
2. Identificar AFN(s) con estados qₓ a qᵧ
3. Conectar el estado final de AFN(r) con el estado inicial de AFN(s) mediante una transición λ
4. El resultado tiene como estado inicial q₀ y como estado final qᵧ

#### Alternativa (r|s)
Para dos expresiones r y s con sus respectivos AFNs:
1. Crear un nuevo estado inicial qₐ
2. Crear un nuevo estado final qᵧ
3. Conectar qₐ con los estados iniciales de AFN(r) y AFN(s) mediante transiciones λ
4. Conectar los estados finales de AFN(r) y AFN(s) con qᵧ mediante transiciones λ

#### Cerradura de Kleene (r*)
Para una expresión r con su AFN:
1. Crear un nuevo estado inicial qₐ
2. Crear un nuevo estado final qᵧ
3. Conectar qₐ con el estado inicial del AFN(r) mediante una transición λ
4. Conectar el estado final del AFN(r) con qᵧ mediante una transición λ
5. Conectar el estado final del AFN(r) con su estado inicial mediante una transición λ
6. Conectar qₐ directamente con qᵧ mediante una transición λ

### Paso 3: Algoritmo completo

#### Procedimiento
1. Analizar la expresión regular usando un analizador sintáctico para obtener su representación en árbol
2. Recorrer el árbol de la expresión de forma recursiva:
   - Si se encuentra un símbolo básico (a, λ), crear el AFN correspondiente
   - Si se encuentra un operador (|, ., *), aplicar la construcción de Thompson adecuada a los subárboles
3. Al terminar el recorrido, el nodo raíz contendrá el AFN completo

#### Propiedades del AFN resultante
- El AFN siempre tendrá un único estado inicial y un único estado final
- Todas las transiciones estarán etiquetadas con un único símbolo del alfabeto o con λ
- El AFN puede contener estados y transiciones λ redundantes
- El número de estados en el AFN resultante es lineal respecto al tamaño de la expresión regular

### Paso 4: Verificación

#### Correctitud
- Comprobar que cada estado tiene transiciones válidas
- Verificar que el autómata acepta cadenas de prueba que pertenecen al lenguaje
- Confirmar que rechaza cadenas que no pertenecen al lenguaje

#### Optimización opcional
- Eliminar estados redundantes
- Combinar transiciones equivalentes
- Convertir el AFN resultante a un AFD mediante el algoritmo de construcción por subconjuntos
