# Transiciones con la Palabra Vacía

Las transiciones con la palabra vacía (también conocidas como transiciones- ε , movimientos- ε  o transiciones nulas) son un tipo especial de transición en los autómatas finitos no deterministas (AFND). Estas permiten que un autómata cambie de estado sin consumir ningún símbolo de la cadena de entrada. Este concepto es fundamental en la teoría de lenguajes formales y tiene aplicaciones en la construcción y simplificación de autómatas.

---

## Definición Formal

Un autómata finito no determinista con transiciones- ε  (AFN- ε ) es una extensión del modelo de autómatas finitos no deterministas (AFND). Se define como una quíntupla:
 
M = (Q, Σ, δ, q_0, F)
  Donde:
-  Q : Conjunto finito de estados.
-  Σ : Alfabeto finito de entrada.
-  δ: Q   x (Σ ∪ ε) → P(Q) : Función de transición que puede incluir transiciones etiquetadas con  ε .
-  q_0 ∈ Q : Estado inicial.
-  F ⊆ Q : Conjunto de estados finales.

En este modelo, las transiciones- ε  permiten al autómata moverse entre estados sin consumir ningún símbolo ( w = εw' ).

---

## Propiedades de las Transiciones- ε 

1. No Consumen Entrada:
   - Una transición- ε  permite cambiar de estado sin leer un símbolo del alfabeto.

2. No Expanden el Poder Expresivo:
   - Los lenguajes reconocidos por un AFN- ε  son los mismos que los reconocidos por un AFND o un AFD: los lenguajes regulares.

3. Conveniencia en Construcción:
   - Las transiciones- ε  simplifican la construcción de autómatas para ciertos lenguajes regulares y facilitan la combinación o unión de autómatas.

4. Clausura- ε :
   - La clausura- ε(q)  de un estado  q  es el conjunto de todos los estados que pueden alcanzarse desde  q  siguiendo únicamente transiciones- ε. Formalmente:
      
     clausura_ε(q) = p : p es alcanzable desde q usando 0 o más transiciones-ε.
       
---

## Ejemplo

### Lenguaje: Palabras que contienen "ab"
Sea el lenguaje  L = w : w; contiene "ab" .

#### Gramática Regular
Producciones:
1.  S → aA ; A → bB ; B → ε. 

#### AFN- ε 
El autómata asociado tiene:
- Estados:  Q = {q_0, q_1, q_2, q_3} ,
- Alfabeto:  Σ = {a, b} ,
- Transiciones:
  -  δ(q_0, a) = {q_1}.
  -  δ(q_1, b) = {q_2}.
  -  δ(q_2, ε) = {q_3}.

Diagrama:

q₀ --a--> q₁ --b--> q₂ --ε--> *q₃

---

## Eliminación de Transiciones- ε 

Aunque las transiciones- ε  son útiles para construir autómatas, pueden eliminarse para obtener un AFND equivalente (sin  ε) o incluso un AFD.

### Algoritmo para Eliminar Transiciones- ε 

1. Calcular Clausura- ε(q) :
   - Para cada estado  q ∈ Q, calcular el conjunto de estados alcanzables mediante transiciones- ε.

2. Actualizar Transiciones:
   - Para cada estado  q ∈ Q, y cada símbolo  a ∈ Σ:
     - Si existe una transición desde algún estado en  clausura_ε(q)  con el símbolo  a, añadir una transición desde  q hacia los estados alcanzables.

3. Actualizar Estados Finales:
   - Un estado será final si él mismo o algún estado en su clausura- ε(q) pertenece al conjunto de estados finales originales ( F' = F ∪ clausura_ε(F)).

#### Ejemplo
Para el AFN- ε del ejemplo anterior:
1. Clausuras:
   -  clausura_ε(q_0) = {q_0}.
   -  clausura_ε(q_1) = {q_1}.
   -  clausura_ε(q_2) = {q_2, q_3}.

2. Nuevas Transiciones:
   - Desde  q_0, a → q_1.
   - Desde  q_1, b → q_2.
   - Desde  q_2, b → q_3.

El AFND equivalente queda sin transiciones- ε.

---

## Ventajas y Limitaciones

### Ventajas
1. Simplicidad en Construcción:
   - Facilitan la unión y concatenación de lenguajes regulares.
2. Flexibilidad:
   - Permiten modelar comportamientos no deterministas complejos.

### Limitaciones
1. Conversión Necesaria:
   - Para aplicaciones prácticas (como análisis léxico), es necesario convertir el AFN- ε en un AFD.
2. Complejidad Computacional:
   - El cálculo de la clausura- ε puede ser costoso para autómatas grandes.

---

## Relación con Lenguajes Regulares

Las transiciones- ε:
- No amplían el conjunto de lenguajes reconocibles por los autómatas finitos.
- Son equivalentes a las operaciones básicas sobre lenguajes regulares (unión, concatenación y cierre).

---

## Conclusión

Las transiciones con la palabra vacía ( ε) son una extensión útil en los autómatas finitos no deterministas que simplifican su construcción y manipulación. Aunque no expanden el poder expresivo del modelo, son esenciales para comprender cómo se relacionan los autómatas con las gramáticas regulares y las expresiones regulares.
