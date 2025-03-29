# Autómatas Finitos

Los **autómatas finitos** son modelos matemáticos utilizados para representar y analizar sistemas que procesan cadenas de símbolos. Son fundamentales en la teoría de lenguajes formales y tienen aplicaciones prácticas en áreas como el diseño de compiladores, el análisis léxico y los sistemas de control.

---

## Definición General

Un **autómata finito** es una máquina abstracta que consta de:
1. Un conjunto finito de **estados**.
2. Un alfabeto finito de **símbolos de entrada**.
3. Una función de transición que define cómo se mueve entre estados en función de los símbolos de entrada.
4. Un estado inicial desde el cual comienza la ejecución.
5. Un conjunto de estados finales o de aceptación.

Se representa formalmente como una quíntupla:
 
M = (Q, Σ, δ, q_0, F)
  Donde:
-  Q : Conjunto finito de estados.
-  Σ : Alfabeto finito (símbolos de entrada).
-  δ: Q   x Σ → Q : Función de transición.
-  q_0 ∈ Q : Estado inicial.
-  F ⊆ Q : Conjunto de estados finales.

---

## Tipos de Autómatas Finitos

### 1. Autómatas Finitos Deterministas (DFA)
Un **DFA** es un autómata donde:
- Para cada estado  q ∈ Q  y cada símbolo  a ∈ Σ , existe exactamente una transición definida ( δ(q, a)  es único).

#### Propiedades:
- Es más fácil de implementar debido a su determinismo.
- Reconoce lenguajes regulares.

#### Ejemplo:
Sea el lenguaje  L = w : w; termina en 01 . Un DFA que lo reconoce tiene:
-  Q = q_0, q_1, q_2 ,
-  Σ = 0, 1 ,
- Transiciones:
  -  δ(q_0, 0) = q_0; δ(q_0, 1) = q_1 ,
  -  δ(q_1, 0) = q_2; δ(q_1, 1) = q_1 ,
  -  δ(q_2, 0) = q_0; δ(q_2, 1) = q_1 ,
- Estado inicial:  q_0 ,
- Estado final:  F = q_2 .

---

### 2. Autómatas Finitos No Deterministas (NFA)
Un **NFA** permite múltiples transiciones para un mismo estado y símbolo de entrada ( |δ(q, a)| > 1) o incluso ninguna transición.

#### Propiedades:
- Reconoce los mismos lenguajes que un DFA.
- Puede ser más compacto que un DFA.
- Es menos intuitivo para implementar directamente.

#### Ejemplo:
Para el mismo lenguaje  L = w : w; termina en 01 , un NFA podría tener:
- Transiciones adicionales que permiten múltiples caminos hacia estados finales.

---

### 3. Autómatas Finitos con Transiciones Vacías ( ε-NFA )
Un ** ε-NFA ** permite transiciones sin consumir ningún símbolo ( ε-transiciones).

#### Propiedades:
- Puede simplificar la construcción del autómata.
- Se puede convertir en un NFA equivalente eliminando las transiciones vacías mediante la clausura- ε .

---

## Lenguaje Reconocido por un Autómata

El lenguaje reconocido por un autómata finito  M = (Q, Σ, δ, q_0, F)  es el conjunto de todas las cadenas sobre el alfabeto  Σ  que llevan al autómata desde el estado inicial a uno de los estados finales:
 
L(M) = w : w ∈ Σ^* , δ^*(q_0, w) ∈ F
  Donde  δ^* : Q × Σ^* → Q  es la extensión de la función de transición para cadenas completas.

---

## Propiedades Fundamentales

1. **Equivalencia DFA-NFA**:
   - Todo lenguaje reconocido por un NFA también puede ser reconocido por un DFA equivalente.
   - La conversión se realiza mediante el algoritmo del subconjunto.

2. **Cierre bajo Operaciones**:
   Los lenguajes reconocidos por autómatas finitos son cerrados bajo las siguientes operaciones:
   - Unión,
   - Intersección,
   - Complemento,
   - Concatenación,
   - Clausura de Kleene ( L^* = L^0 ∪ L^1 ∪ L^2 ∪ ...).

3. **Relación con Expresiones Regulares**:
   - Todo lenguaje definido por una expresión regular puede ser reconocido por un autómata finito.
   - Inversamente, todo lenguaje reconocido por un autómata finito puede ser descrito mediante una expresión regular.

---

## Aplicaciones

1. **Análisis Léxico**:
   - Los autómatas finitos se utilizan en compiladores para reconocer tokens como palabras clave e identificadores.

2. **Procesamiento de Texto**:
   - Se emplean para buscar patrones en cadenas mediante expresiones regulares.

3. **Protocolos y Sistemas Secuenciales**:
   - Modelan sistemas con estados definidos y transiciones entre ellos (e.g., controladores lógicos programables).

4. **Validación y Verificación**:
   - Verifican si una cadena pertenece a un lenguaje formal o si cumple ciertas restricciones sintácticas.

---

## Ejemplo Práctico: Construcción del DFA desde una Gramática Regular

Dada una gramática regular lineal por la derecha:
 
G = (N, T, P, S)
  Con producciones:
-  S → aA | bB | ε ; A → aA | bS ; B → bB | aS.

El DFA asociado tiene los estados correspondientes a los no terminales ( S, A, B) y las transiciones definidas por las producciones.

---

## Minimización de Autómatas

La minimización busca reducir el número de estados en un DFA sin cambiar el lenguaje reconocido. El algoritmo típico consiste en:

1. Eliminar estados inaccesibles.
2. Agrupar estados equivalentes (aquellos que reconocen el mismo conjunto de cadenas).
3. Construir el DFA mínimo basado en estos grupos.

---

## Conclusión

Los autómatas finitos son herramientas fundamentales para modelar y analizar lenguajes regulares y sistemas secuenciales simples. Su simplicidad y versatilidad los hacen esenciales tanto en teoría como en aplicaciones prácticas.
