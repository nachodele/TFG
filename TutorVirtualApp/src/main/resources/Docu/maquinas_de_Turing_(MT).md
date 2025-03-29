# Máquinas de Turing (MT)

Las **Máquinas de Turing (MT)** son dispositivos teóricos fundamentales en la teoría de la computación. Fueron introducidas por Alan Turing en 1936 como un modelo matemático para formalizar el concepto de algoritmo y computación. Las MT son más potentes que otros modelos de autómatas, ya que pueden simular cualquier proceso computacional que sea "algorítmicamente resoluble".

---

## Definición Formal

Una Máquina de Turing se define como una 7-úpla:
 
M = (Q, Σ, Γ, δ, q_0, B, F)
  Donde:
-  Q : Conjunto finito de estados.
-  Σ : Alfabeto de entrada (símbolos que pueden aparecer en la cadena de entrada).
-  Γ : Alfabeto de la cinta ( Σ ⊆ Γ ), incluye los símbolos de entrada y un símbolo especial  B  (blanco).
-  δ: Q   x Γ → Q   x Γ   x L, R : Función de transición.
  - Define cómo cambia el estado, qué escribe en la cinta y hacia dónde se mueve la cabeza lectora/escritora.
-  q_0 ∈ Q : Estado inicial.
-  B ∈ Γ : Símbolo blanco (espacio vacío en la cinta).
-  F ⊆ Q : Conjunto de estados finales.

---

## Funcionamiento

1. **Cinta**:
   - La cinta es infinita hacia la derecha y está dividida en celdas.
   - Cada celda puede contener un símbolo del alfabeto  Γ .

2. **Cabeza lectora/escritora**:
   - Lee el contenido de una celda.
   - Escribe un nuevo símbolo en la celda actual.
   - Se mueve a la izquierda ( L ) o a la derecha ( R ).

3. **Estados**:
   - La máquina comienza en el estado inicial ( q_0 ).
   - Según el estado actual y el símbolo leído, la función de transición  δ(q, X) = (q', Y, D)  determina:
     - El nuevo estado ( q' ).
     - El símbolo que se escribe ( Y ).
     - La dirección del movimiento ( D = L, R).

4. **Aceptación**:
   - Una cadena es aceptada si, después de una secuencia finita de transiciones, la máquina alcanza un estado final ( q_f ∈ F).

---

## Ejemplo: Lenguaje  L = a^n b^n : n ≥ 1

### Máquina de Turing
Sea una MT que acepta cadenas con igual número de  a's seguidos por  b's:
- Estados:  Q = q_0, q_1, q_2, q_f ,
- Alfabeto de entrada:  Σ = {a, b} ,
- Alfabeto de cinta:  Γ = {a, b, X, B} ,
- Estado inicial:  q_0,
- Estado final:  F = {q_f}.

#### Transiciones
1. Desde  q_0:
   - Leer 'a', escribir 'X', mover derecha:
     -  δ(q_0, a) = (q_1, X, R). 
   - Leer 'B', ir al estado final:
     -  δ(q_0, B) = (q_f, B, R). 

2. Desde  q_1:
   - Leer 'b', escribir 'X', mover izquierda:
     -  δ(q_1, b) = (q_2, X, L). 
   - Leer 'X', mover derecha:
     -  δ(q_1, X) = (q_1, X, R). 

3. Desde  q_2:
   - Leer 'X', mover izquierda:
     -  δ(q_2, X) = (q_2, X, L). 
   - Leer 'a', mover derecha:
     -  δ(q_2, a) = (q_0, X, R). 

---

## Clasificación y Extensiones

### Tipos de Máquinas de Turing
1. **Determinista**:
   - Para cada estado y símbolo leído hay una única transición definida.
2. **No determinista**:
   - Puede haber múltiples transiciones posibles para un mismo estado y símbolo.

### Extensiones
1. **MT Multicinta**:
   - Tiene varias cintas con cabezas independientes.
2. **MT Multidimensional**:
   - La cinta tiene más dimensiones (e.g., bidimensional).
3. **MT Universal**:
   - Puede simular cualquier otra máquina de Turing.

---

## Lenguajes Reconocidos por las Máquinas de Turing

### Lenguajes Recursivamente Enumerables
Un lenguaje es recursivamente enumerable si existe una MT que lo reconoce; es decir:
 
L(M) = w : M(w); acepta.
  
### Lenguajes Recursivos
Un lenguaje es recursivo si existe una MT que lo reconoce y siempre se detiene para cualquier entrada.

---

## Problemas Indecidibles

No todos los problemas son resolubles mediante una máquina de Turing. Ejemplo clásico:

### Problema del Paro
Dado un programa y una entrada específica:
- ¿El programa terminará o entrará en un bucle infinito?
Turing demostró que este problema es indecidible.

---

## Aplicaciones

1. **Modelado Teórico**:
   - Base para estudiar computabilidad y complejidad algorítmica.
2. **Simulación Computacional**:
   - Las MT son el fundamento teórico detrás del funcionamiento de las computadoras modernas.
3. **Resolución Algorítmica**:
   - Permiten analizar qué problemas pueden resolverse mediante algoritmos.

---

## Conclusión

Las Máquinas de Turing son un modelo teórico esencial para comprender los límites y las capacidades del cálculo algorítmico. Su versatilidad las convierte en una herramienta clave tanto en teoría como en aplicaciones prácticas relacionadas con lenguajes formales y computación.
