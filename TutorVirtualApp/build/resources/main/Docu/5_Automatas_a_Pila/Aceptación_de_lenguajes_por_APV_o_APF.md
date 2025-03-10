# Aceptación de Lenguajes por un Autómata a Pila (AP): Por Vaciado de Pila (APV) o por Estados Finales (APF)

Los **autómatas a pila (AP)** son máquinas abstractas que reconocen lenguajes independientes del contexto (LIC). Existen dos criterios principales mediante los cuales un AP puede aceptar un lenguaje: **por vaciado de pila** (APV) o **por estados finales** (APF). Ambos criterios son equivalentes en términos del conjunto de lenguajes que pueden reconocer, aunque su implementación y análisis pueden diferir.

---

## Criterios de Aceptación

### 1. Aceptación por Vaciado de Pila (APV)
Un AP acepta una cadena si, después de procesarla completamente, la pila queda vacía, independientemente del estado en el que se encuentre el autómata.

#### Definición Formal
Sea \( M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0) \) un AP. El lenguaje aceptado por vaciado de pila es:
\[
L(M) = \{ w \in \Sigma^* : (q_0, w, Z_0) \vdash^* (q, \epsilon, \epsilon),\; q \in Q \}.
\]
Donde:
- \( w \): Cadena de entrada.
- \( Z_0 \): Símbolo inicial de la pila.
- \( \vdash^* \): Secuencia de transiciones.

En este criterio:
- El estado final no es relevante.
- La pila debe estar completamente vacía al finalizar el procesamiento.

---

### 2. Aceptación por Estados Finales (APF)
Un AP acepta una cadena si, después de procesarla completamente, el autómata se encuentra en un estado final, independientemente del contenido de la pila.

#### Definición Formal
Sea \( M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F) \) un AP. El lenguaje aceptado por estados finales es:
\[
L(M) = \{ w \in \Sigma^* : (q_0, w, Z_0) \vdash^* (q_f, \epsilon, \gamma),\; q_f \in F,\; \gamma \in \Gamma^* \}.
\]
Donde:
- \( F \subseteq Q \): Conjunto de estados finales.
- \( w \): Cadena de entrada.
- \( Z_0 \): Símbolo inicial de la pila.
- \( q_f \): Estado final alcanzado.

En este criterio:
- La pila puede o no estar vacía al finalizar el procesamiento.
- Lo importante es que el autómata termine en un estado final.

---

## Equivalencia entre APV y APF

### Teorema
Todo lenguaje aceptado por un AP mediante vaciado de pila también puede ser aceptado por otro AP mediante estados finales y viceversa. Es decir:
\[
L_{\text{APV}} = L_{\text{APF}}.
\]

#### Demostración Intuitiva
1. **De APV a APF**:
   - Añadir un nuevo estado final \( q_f \).
   - Crear una transición-\( ε\) desde cualquier configuración donde la pila esté vacía hacia \( q_f \).

2. **De APF a APV**:
   - Añadir un nuevo símbolo inicial para la pila (\( X_0\)).
   - Crear transiciones para vaciar la pila al alcanzar un estado final.

Esta equivalencia asegura que ambos criterios reconocen exactamente los lenguajes independientes del contexto.

---

## Ejemplo: Lenguaje Balanceado

Sea el lenguaje:
\[
L = \{a^n b^n : n ≥ 1\}.
\]

### Autómata por Vaciado de Pila (APV)
1. Estados: \( Q = {q_0} \),
2. Transiciones:
   - Leer 'a' y apilar 'A':  
     \( δ(q_0, a, Z_0) = (q_0, AZ_0), δ(q_0, a, A) = (q_0, AA). \)
   - Leer 'b' y desapilar 'A':  
     \( δ(q_0, b, A) = (q_0, ε). \)

Acepta si la pila queda vacía al finalizar el procesamiento.

### Autómata por Estados Finales (APF)
1. Estados: \( Q = {q_0, q_f} \),
2. Transiciones:
   - Igual que en el APV.
   - Al vaciar la pila (\( ε\)), transición-\( ε\) hacia el estado final:  
     \( δ(q_0, ε, Z_0) = (q_f, ε). \)

Acepta si termina en \( q_f\).

---

## Ventajas y Desventajas

| **Criterio**           | **Ventajas**                                                                 | **Desventajas**                                                              |
|-------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------|
| **Por Vaciado de Pila** | No requiere definir estados finales.                                         | Puede ser menos intuitivo para modelar ciertos lenguajes.                    |
| **Por Estados Finales** | Extiende naturalmente la idea de aceptación en autómatas finitos.            | Requiere manejar explícitamente los estados finales y las transiciones asociadas. |

---

## Aplicaciones

1. **Análisis Sintáctico**:
   - Los analizadores sintácticos basados en gramáticas libres de contexto suelen utilizar autómatas a pila con aceptación por estados finales.

2. **Modelado Teórico**:
   - La aceptación por vaciado simplifica pruebas teóricas sobre lenguajes independientes del contexto.

3. **Conversión entre Representaciones**:
   - La equivalencia entre ambos criterios permite elegir el enfoque más conveniente según el problema.

---

## Conclusión

La aceptación por vaciado de pila y por estados finales son dos enfoques equivalentes para definir los lenguajes reconocidos por autómatas a pila. Aunque sus implementaciones pueden diferir ligeramente, ambos son fundamentales para modelar lenguajes independientes del contexto y tienen aplicaciones prácticas y teóricas significativas.
