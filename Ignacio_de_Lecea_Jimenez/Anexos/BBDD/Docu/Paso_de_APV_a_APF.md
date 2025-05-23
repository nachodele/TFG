# Paso de APV a APF

Un autómata a pila por vaciado (APV) acepta una cadena si, al finalizar su procesamiento, la pila queda completamente vacía, independientemente del estado en el que se encuentre el autómata. Por otro lado, un autómata a pila por estados finales (APF) acepta una cadena si, al finalizar su procesamiento, el autómata se encuentra en un estado final, sin importar el contenido de la pila. Ambos criterios son equivalentes en términos del conjunto de lenguajes que pueden reconocer, y es posible transformar un APV en un APF que acepte el mismo lenguaje.

---

## Estrategia para Convertir un APV en un APF

La idea principal para convertir un APV en un APF consiste en:
1. Añadir un nuevo estado final  q_f .
2. Crear transiciones- ε  desde las configuraciones donde la pila está vacía hacia este nuevo estado final.
3. Eliminar la dependencia del vaciado de la pila como criterio de aceptación.

### Pasos del Algoritmo

Dado un APV M = (Q, Σ, Γ, δ, q_0, Z_0), construimos un APF equivalente M' = (Q̄, Σ, Γ, δ̄, q_0, Z_0, F') siguiendo estos pasos:

1. Definir los nuevos componentes:
   - Q̄ = Q ∪ {q_f}, donde q_f es un nuevo estado final.
   - F' = {q_f}, el conjunto de estados finales contiene únicamente q_f.

2. Añadir transiciones-ε:
   - Para cada estado q ∈ Q, añadir una transición-ε hacia q_f si la pila está vacía:
     - δ̄(q, ε, Z_0) = (q_f, Z_0).

3. Mantener las transiciones originales:
   - Todas las transiciones originales del APV se mantienen sin cambios.

4. Eliminar la aceptación por vaciado de pila:
   - El nuevo autómata acepta únicamente si termina en el estado final  q_f.

---

## Ejemplo

### APV Original
Sea el lenguaje:
 
L = a^n b^n : n ≥ 1.
  
El APV correspondiente tiene:
- Estados:  Q = {q_0} ,
- Alfabeto de entrada:  Σ = {a, b} ,
- Alfabeto de la pila:  Γ = {A, Z_0} ,
- Estado inicial:  q_0,
- Símbolo inicial de la pila:  Z_0,
- Transiciones:
  1. Leer 'a' y apilar 'A':
     -  δ(q_0, a, Z_0) = (q_0, AZ_0), δ(q_0, a, A) = (q_0, AA). 
  2. Leer 'b' y desapilar 'A':
     -  δ(q_0, b, A) = (q_0, ε). 

Acepta si la pila queda vacía al finalizar el procesamiento.

---

### Conversión a APF
1. Añadir un nuevo estado final ( q_f):
   - Estados:  Q' = {q_0, q_f} .
   - Estados finales:  F' = {q_f} .

2. Añadir transiciones- ε:
   - Desde cualquier estado donde la pila esté vacía ( Z_0), añadir una transición- ε hacia el estado final:
     -  δ(q_0, ε, Z_0) = (q_f, Z_0). 

3. Mantener las transiciones originales:
   - Las transiciones para procesar 'a' y 'b' permanecen sin cambios.

#### Descripción del Nuevo APF
El nuevo autómata acepta únicamente si alcanza el estado final  q_f, independientemente del contenido de la pila.

---

## Observaciones

1. Equivalencia Garantizada:
   - El lenguaje aceptado por el APF resultante es exactamente el mismo que el aceptado por el APV original.

2. Eficiencia:
   - La conversión no altera significativamente la complejidad del autómata.

3. Aplicabilidad Recíproca:
   - De manera similar al paso de APF a APV descrito anteriormente, también es posible convertir un APV en un APF equivalente añadiendo nuevos estados finales y transiciones- ε.

---

## Conclusión

El paso de un autómata a pila por vaciado (APV) a uno por estados finales (APF) demuestra la equivalencia entre ambos criterios de aceptación para lenguajes independientes del contexto. Este proceso asegura que cualquier lenguaje reconocido por un APV puede ser reconocido por un APF equivalente y viceversa.
