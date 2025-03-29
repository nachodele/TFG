# Paso de APF a APV

Un **autómata a pila por estados finales (APF)** es un modelo que acepta una cadena si, al finalizar su procesamiento, el autómata se encuentra en un estado final. Por otro lado, un **autómata a pila por vaciado (APV)** acepta una cadena si, al finalizar su procesamiento, la pila queda completamente vacía. Ambos criterios son equivalentes en términos del conjunto de lenguajes que pueden reconocer, y es posible transformar un APF en un APV que acepte el mismo lenguaje.

---

## Estrategia para Convertir un APF en un APV

Para transformar un APF en un APV:
1. **Añadir un nuevo símbolo inicial de la pila** ( Z' ):
   - Este símbolo servirá para marcar la base de la pila y garantizar que el autómata pueda vaciarla al final.
2. **Modificar las transiciones iniciales**:
   - Al iniciar el autómata, apilar  Z'  junto con el símbolo inicial original de la pila ( Z_0 ).
3. **Añadir transiciones para vaciar la pila**:
   - Crear transiciones- ε  desde los estados finales originales hacia un nuevo estado que se encargue de vaciar la pila.
4. **Eliminar la dependencia de los estados finales**:
   - El nuevo autómata aceptará únicamente cuando la pila quede vacía, independientemente del estado final.

---

## Algoritmo Formal

Dado un APF M = (Q, Σ, Γ, δ, q_0, Z_0, F), construimos un APV equivalente M' = (Q̄, Σ, Γ̄, δ̄, q̄_0, Z̄_0) siguiendo estos pasos:

1. **Definir los nuevos componentes**:
   - Q̄ = Q ∪ {q_v}, donde q_v es un nuevo estado encargado de vaciar la pila.
   - Γ̄ = Γ ∪ {Z'}, donde Z' es el nuevo símbolo inicial de la pila.
   - q̄_0 = q_0, el estado inicial permanece igual.
   - Z̄_0 = Z', el nuevo símbolo inicial de la pila.

2. **Modificar las transiciones**:
   - Al iniciar el autómata, apilar Z'Z_0:
     - δ̄(q_0, ε, Z') = (q_0, Z'Z_0).
   - Para cada estado final f ∈ F, añadir una transición-ε hacia q_v:
     - δ̄(f, ε, Z') = (q_v, ε).
   - En q_v, añadir transiciones-ε para vaciar la pila:
     - Para cada símbolo X ∈ Γ:
       - δ̄(q_v, ε, X) = (q_v, ε).

3. **Eliminar los estados finales**:
   - El conjunto de estados finales del nuevo autómata queda vacío (F' = ∅).

---

## Ejemplo

### APF Original
Sea el lenguaje:
 
L = a^n b^n : n ≥ 1.
  
El APF correspondiente tiene:
- Estados:  Q = {q_0, q_f} ,
- Alfabeto de entrada:  Σ = {a, b} ,
- Alfabeto de la pila:  Γ = {A, Z_0} ,
- Estado inicial:  q_0,
- Estado final:  F = {q_f},
- Transiciones:
  1. Leer 'a' y apilar 'A':
     -  δ(q_0, a, Z_0) = (q_0, AZ_0), δ(q_0, a, A) = (q_0, AA). 
  2. Leer 'b' y desapilar 'A':
     -  δ(q_0, b, A) = (q_f, ε). 

Acepta si termina en el estado final  q_f.

---

### Conversión a APV
1. Añadir el nuevo símbolo inicial ( Z'):
   - Al iniciar el autómata:
     - Apilar  Z'Z_0:  
        δ(q_0, ε, Z') = (q_0, Z'Z_0). 

2. Añadir transiciones- ε para vaciar la pila desde los estados finales originales ( q_f):
   - Desde  q_f:
     - Vaciar la pila:
       -  δ(q_f, ε, A) = (q_f, ε). 
       -  δ(q_f, ε, Z') = (q_f, ε). 

3. Eliminar los estados finales originales:
   - El conjunto de estados finales queda vacío ( F' = ∅).

#### Descripción del Nuevo APV
El nuevo autómata acepta únicamente si la pila queda completamente vacía al finalizar el procesamiento.

---

## Observaciones

1. **Equivalencia Garantizada**:
   - El lenguaje aceptado por el APV resultante es exactamente el mismo que el aceptado por el APF original.

2. **Eficiencia**:
   - Aunque se añaden nuevas transiciones y símbolos a la pila durante la conversión, no se altera significativamente la complejidad del autómata.

3. **Aplicabilidad Recíproca**:
   - De manera similar al paso de APF a APV descrito aquí, también es posible convertir un APV en un APF equivalente añadiendo nuevos estados finales y transiciones- ε.

---

## Conclusión

El paso de un autómata a pila por estados finales (APF) a uno por vaciado (APV) demuestra la equivalencia entre ambos criterios de aceptación para lenguajes independientes del contexto. Este proceso asegura que cualquier lenguaje reconocido por un APF puede ser reconocido por un APV equivalente y viceversa.
