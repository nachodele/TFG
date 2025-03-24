# Autómatas a Pila (AP)

Los **autómatas a pila (AP)** son modelos matemáticos que extienden los autómatas finitos al incorporar una memoria auxiliar en forma de pila. Esta característica les permite reconocer lenguajes más complejos, específicamente los **lenguajes independientes de contexto**, que no pueden ser reconocidos por autómatas finitos.

---

## Definición Formal

Un **autómata a pila** se define como una séptupla:
 
M = (Q, Σ, Γ, δ, q_0, Z_0, F)
  Donde:
-  Q : Conjunto finito de estados.
-  Σ : Alfabeto de entrada.
-  Γ : Alfabeto de la pila (símbolos que pueden almacenarse en la pila).
-  δ: Q   x (Σ ∪ ε)   x Γ → P(Q   x Γ^*) : Función de transición.
-  q_0 ∈ Q : Estado inicial.
-  Z_0 ∈ Γ : Símbolo inicial de la pila.
-  F ⊆ Q : Conjunto de estados finales.

### Interpretación de la Función de Transición
La función  δ(q, a, X) = (p, w)  significa que:
1. Si el autómata está en el estado  q ,
2. Lee el símbolo  a  de la entrada (o no consume nada si  a = ε),
3. Extrae el símbolo  X  de la cima de la pila,
4. Entonces:
   - Cambia al estado  p ,
   - Sustituye  X  por la cadena  w  en la pila.

---

## Funcionamiento del Autómata a Pila

El autómata a pila procesa una cadena de entrada mientras realiza operaciones sobre su pila. Estas operaciones incluyen:
1. **Apilar**: Insertar símbolos en la pila.
2. **Desapilar**: Eliminar símbolos de la cima de la pila.
3. **Mantener**: No modificar la pila.

El autómata acepta una cadena si:
1. Al finalizar el procesamiento, alcanza un estado final (**aceptación por estado final**), o
2. La pila queda vacía (**aceptación por vaciado de pila**).

---

## Lenguajes Reconocidos

Los autómatas a pila reconocen exactamente los **lenguajes independientes de contexto**, según los siguientes teoremas fundamentales:

1. **Teorema 1**: Para cada gramática independiente del contexto  G , existe un autómata a pila  M  tal que:
    
   L(G) = L(M)
     
2. **Teorema 2**: Para cada autómata a pila  M , existe una gramática independiente del contexto  G  tal que:
    
   L(M) = L(G)
     
---

## Ejemplo 1: Lenguaje Balanceado

Sea el lenguaje:
 
L = a^n b^n : n ≥ 1
  Este lenguaje contiene cadenas con igual número de  a's  y  b's , con todos los  a's  antes que los  b's.

### Construcción del AP
Un autómata a pila que reconoce este lenguaje tiene:
- Estados:  Q = {q_0, q_1} ,
- Alfabeto de entrada:  Σ = {a, b} ,
- Alfabeto de la pila:  Γ = {A, Z_0} ,
- Estado inicial:  q_0,
- Símbolo inicial de la pila:  Z_0,
- Estados finales:  F = {q_1} .

#### Transiciones
1. Desde el estado inicial ( q_0):
   - Leer un  a, apilar un símbolo  A:
     -  δ(q_0, a, Z_0) = (q_0, AZ_0) ,
     -  δ(q_0, a, A) = (q_0, AA) .
   - Leer un  b, desapilar un símbolo  A:
     -  δ(q_0, b, A) = (q_1, ε) .
2. Desde el estado final ( q_1):
   - Si no hay más símbolos en la entrada y la pila está vacía:
     - Aceptar.

---

## Ejemplo 2: Lenguaje Palíndromo

Sea el lenguaje:
 
L = w : w = w^R ; w ∈ Σ^*
  Este lenguaje contiene todas las cadenas que son palíndromos.

### Construcción del AP
Un autómata a pila que reconoce este lenguaje tiene:
- Estados:  Q = {q_0, q_1} ,
- Alfabeto de entrada:  Σ = {a, b} ,
- Alfabeto de la pila:  Γ = {a, b, Z_0} ,
- Estado inicial:  q_0,
- Símbolo inicial de la pila:  Z_0,
- Estados finales:  F = {q_1} .

#### Transiciones
1. Desde el estado inicial ( q_0):
   - Leer un símbolo y apilarlo ( a/b → A/B).
2. Al llegar al punto medio (detectado por algún criterio), cambiar al estado final ( q_1) y comenzar a desapilar mientras se leen los símbolos correspondientes.

---

## Autómatas Deterministas vs No Deterministas

### Autómatas Deterministas (APD)
Un AP es determinista si para cada configuración solo existe una transición posible. Los lenguajes aceptados por APD son un subconjunto estricto de los lenguajes independientes del contexto.

### Autómatas No Deterministas (APND)
Un AP es no determinista si permite múltiples transiciones para una misma configuración. Los APND pueden reconocer todos los lenguajes independientes del contexto.

---

## Aplicaciones

1. **Análisis Sintáctico**:
   - Los analizadores sintácticos utilizados en compiladores son implementaciones prácticas de autómatas a pila.

2. **Procesamiento del Lenguaje Natural**:
   - Se utilizan para modelar estructuras gramaticales jerárquicas en lenguas humanas.

3. **Reconocimiento y Validación**:
   - Reconocen patrones complejos como expresiones aritméticas o estructuras anidadas.

---

## Conclusión

Los autómatas a pila son herramientas fundamentales para trabajar con lenguajes independientes del contexto y modelar estructuras jerárquicas y anidadas. Su capacidad para manejar memoria auxiliar mediante una pila los hace más potentes que los autómatas finitos y esenciales en teoría computacional y aplicaciones prácticas.
