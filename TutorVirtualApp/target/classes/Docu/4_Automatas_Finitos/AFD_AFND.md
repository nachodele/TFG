# Autómatas Finitos Deterministas (AFD) y No Deterministas (AFND)

Los **autómatas finitos deterministas (AFD)** y los **autómatas finitos no deterministas (AFND)** son modelos matemáticos utilizados para procesar cadenas de símbolos y reconocer lenguajes regulares. Ambos son fundamentales en la teoría de lenguajes formales, pero difieren en su estructura y funcionamiento.

---

## Autómata Finito Determinista (AFD)

### Definición
Un **autómata finito determinista** es un sistema en el que, para cada estado y símbolo de entrada, existe exactamente una transición definida. Formalmente, un AFD se describe como una quíntupla:
\[
M = (Q, \Sigma, \delta, q_0, F)
\]
Donde:
- \( Q \): Conjunto finito de estados.
- \( \Sigma \): Alfabeto finito de entrada.
- \( \delta: Q \times \Sigma \to Q \): Función de transición que asigna un único estado a cada par (estado actual, símbolo de entrada).
- \( q_0 \in Q \): Estado inicial.
- \( F \subseteq Q \): Conjunto de estados finales o de aceptación.

### Propiedades
1. **Determinismo**:
   - Para cada estado \( q \in Q \) y cada símbolo \( a \in \Sigma \), existe exactamente una transición definida (\( \delta(q, a) = p \)).
2. **No admite transiciones vacías (\( ε \))**:
   - Cada transición consume un símbolo del alfabeto.
3. **Lenguaje reconocido**:
   - El lenguaje aceptado por el AFD es el conjunto de cadenas que llevan al autómata desde el estado inicial a un estado final.

### Ejemplo
Sea el lenguaje \( L = \{w : w\; termina\; en\; 01\} \). Un AFD que lo reconoce tiene:
- \( Q = \{q_0, q_1, q_2\} \),
- \( \Sigma = \{0, 1\} \),
- Transiciones:
  - \( \delta(q_0, 0) = q_0,\, \delta(q_0, 1) = q_1 \),
  - \( \delta(q_1, 0) = q_2,\, \delta(q_1, 1) = q_1 \),
  - \( \delta(q_2, 0) = q_0,\, \delta(q_2, 1) = q_1 \),
- Estado inicial: \( q_0 \),
- Estado final: \( F = \{q_2\} \).

---

## Autómata Finito No Determinista (AFND)

### Definición
Un **autómata finito no determinista** permite múltiples transiciones para un mismo estado y símbolo de entrada. Formalmente, un AFND se describe como una quíntupla:
\[
M = (Q, \Sigma, \delta, q_0, F)
\]
Donde:
- \( Q,\, Σ,\, q_0,\, F \): Tienen el mismo significado que en un AFD.
- \( δ: Q × Σ → P(Q) \): Función de transición que asigna un conjunto de estados posibles a cada par (estado actual, símbolo de entrada).

### Propiedades
1. **No determinismo**:
   - Para un estado \( q \in Q \) y un símbolo \( a ∈ Σ\), pueden existir varias transiciones posibles (\( δ(q,a) ⊆ Q\)).
2. **Transiciones vacías (\( ε-transiciones\))**:
   - Puede cambiar de estado sin consumir ningún símbolo (\( δ(q, ε) ⊆ Q\)).
3. **Lenguaje reconocido**:
   - Una cadena es aceptada si existe al menos un camino desde el estado inicial hasta un estado final que consuma toda la cadena.

### Ejemplo
Sea el lenguaje \( L = \{w : w\; contiene\; la\; subcadena\; "01"\} \). Un AFND que lo reconoce tiene:
- \( Q = \{q_0, q_1, q_2\} \),
- \( Σ = {0, 1} \),
- Transiciones:
  - \( δ(q_0, 0) = {q_0},\, δ(q_0, 1) = {q_0,q_1} \),
  - \( δ(q_1, 0) = {q_2} ,\, δ(q_1, 1) = ∅,\; δ(q_2,a)=∅,\forall a∈Σ.\)

---

## Diferencias entre AFD y AFND

| **Característica**       | **AFD (Determinista)**                     | **AFND (No Determinista)**                |
|--------------------------|-------------------------------------------|------------------------------------------|
| **Número de transiciones** | Una única transición por símbolo y estado | Múltiples transiciones posibles por símbolo y estado |
| **Transiciones vacías (\( ε-transiciones\))** | No permitidas                             | Permitidas                               |
| **Simulación**           | Más simple                               | Más compleja                             |
| **Flexibilidad**         | Menos flexible                           | Más flexible                             |
| **Estados simultáneos**  | Solo puede estar en un estado a la vez    | Puede estar en varios estados simultáneamente |
| **Equivalencia**         | Todo AFD es también un AFND              | Todo AFND puede convertirse en un AFD    |

---

## Equivalencia entre AFD y AFND

Aunque los AFND parecen más poderosos debido a su no determinismo y flexibilidad adicional (como las transiciones vacías), ambos modelos son equivalentes en términos del conjunto de lenguajes que pueden reconocer: los lenguajes regulares.

### Conversión de AFND a AFD
Un AFND puede convertirse en un AFD equivalente mediante el algoritmo del subconjunto:
1. Cada conjunto de estados del AFND se convierte en un único estado del AFD.
2. La función de transición del AFD se construye considerando todas las posibles combinaciones de estados del AFND.

#### Ejemplo
Para el AFND descrito anteriormente con \( L = {w : w\; contiene\; "01"}\), el AFD equivalente tendría:
- Estados: Conjuntos potencia de los estados del AFND (\( P(Q) = {∅,\{q_0\},...}\)).
- Transiciones definidas para cada conjunto de estados.

---

## Aplicaciones

1. **Diseño de Compiladores**:
   - Los AFD se utilizan para construir analizadores léxicos debido a su simplicidad.
   - Los AFND son útiles para representar expresiones regulares durante las primeras etapas del diseño.

2. **Procesamiento de Texto**:
   - Los AFND permiten buscar patrones complejos gracias a su flexibilidad.

3. **Teoría Computacional**:
   - Ambos modelos son fundamentales para estudiar lenguajes regulares y sus propiedades.

---

## Conclusión

Los autómatas finitos deterministas (AFD) y no deterministas (AFND) son herramientas esenciales para modelar lenguajes regulares. Aunque los AFND ofrecen mayor flexibilidad debido a su no determinismo y transiciones vacías (\( ε-transiciones\)), los AFD son más simples de implementar y analizar. Sin embargo, ambos son equivalentes en términos del poder expresivo para reconocer lenguajes regulares.
