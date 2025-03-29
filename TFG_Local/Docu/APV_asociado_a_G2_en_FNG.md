# APV Asociado a una Gramática Independiente del Contexto (G2) en Forma Normal de Greibach (FNG)

Un **autómata a pila por vaciado (APV)** es un modelo que acepta un lenguaje si, al finalizar el procesamiento de una cadena, la pila queda completamente vacía. Cuando se trabaja con una **gramática independiente del contexto (G2)** en **Forma Normal de Greibach (FNG)**, es posible construir un APV que reconozca el mismo lenguaje generado por la gramática. Este proceso se basa en la equivalencia entre autómatas a pila y gramáticas independientes del contexto.

---

## Forma Normal de Greibach (FNG)

Una gramática  G = (N, T, P, S)  está en **Forma Normal de Greibach** si todas sus producciones tienen la forma:
 
A → aα,
  donde:
-  A ∈ N : Es un símbolo no terminal.
-  a ∈ T : Es un símbolo terminal.
-  α ∈ N^* : Es una cadena (posiblemente vacía) de símbolos no terminales.

La FNG tiene las siguientes propiedades:
1. Cada producción comienza con un símbolo terminal.
2. Es adecuada para construir autómatas a pila porque permite procesar los símbolos terminales en el mismo orden en que aparecen en la entrada.

---

## Construcción del APV Asociado

### Idea General
El APV asociado a una gramática en FNG utiliza la pila para simular las derivaciones de la gramática. Los símbolos no terminales se apilan y se desapilan según las reglas de producción, mientras que los símbolos terminales se comparan directamente con la entrada.

### Componentes del APV
Dada una gramática  G = (N, T, P, S)  en FNG, el APV asociado  M = (Q, Σ, Γ, δ, q_0, Z_0)  se define como:
-  Q = q_0, q_1 : Conjunto de estados.
  -  q_0 : Estado inicial.
  -  q_1 : Estado final.
-  Σ = T : Alfabeto de entrada (símbolos terminales).
-  Γ = N ∪ T ∪ Z_0 : Alfabeto de la pila.
  - Incluye los no terminales ( N ), los terminales ( T ) y un símbolo inicial especial ( Z_0 ).
-  Z_0 ∈ Γ : Símbolo inicial de la pila.
-  F = ∅ : No hay estados finales porque la aceptación es por vaciado de pila.

### Transiciones
La función de transición  δ(q, a, X) = (p, w)  se define como:
1. **Inicialización**:
   - Desde el estado inicial ( q_0 ), apilar el símbolo inicial de la gramática ( S ) junto con  Z_0 :
     -  δ(q_0, ε, Z_0) = (q_0, SZ_0). 

2. **Procesamiento de Producciones**:
   - Para cada producción  A → aα :
     - Si el símbolo en la cima de la pila es  A , desapilarlo y apilar  αa^R  (los símbolos terminales y no terminales en orden inverso):
       -  δ(q_0, ε, A) = (q_0, αa). 

3. **Consumo de Terminales**:
   - Si el símbolo en la cima de la pila coincide con el símbolo leído en la entrada ( a = b):
     - Desapilarlo y avanzar en la entrada:
       -  δ(q_0, a, a) = (q_0, ε). 

4. **Aceptación**:
   - Cuando se alcanza una configuración con la pila vacía ( Z_0), el autómata acepta:
     -  δ(q_0, ε, Z_0) = (q_1, ε). 

---

## Ejemplo: Lenguaje Balanceado

Sea el lenguaje:
 
L = a^n b^n : n ≥ 1.
  
### Gramática en FNG
La gramática asociada es:
 
G = (S, a, b, P, S),
  con las producciones:
1.  S → aSb ,
2.  S → ab. 

### Construcción del APV
El APV asociado tiene:
- Estados:  Q = {q_0} ,
- Alfabeto de entrada:  Σ = {a, b} ,
- Alfabeto de pila:  Γ = {S, a, b, Z_0} ,
- Estado inicial:  q_0,
- Símbolo inicial de la pila:  Z_0.

#### Transiciones
1. Inicialización:
   - Apilar el símbolo inicial ( SZ_0):
     -  δ(q_0, ε, Z_0) = (q_0, SZ_0). 

2. Procesamiento de Producciones:
   - Para  S → aSb :
     - Desapilar  S , apilar  bSa^R = bSa:
       -  δ(q_0, ε, S) = (q_0, bSa). 
   - Para  S → ab :
     - Desapilar  S , apilar  ba^R = ba:
       -  δ(q_0, ε, S) = (q_0, ba). 

3. Consumo de Terminales:
   - Leer 'a' y desapilar 'a':
     -  δ(q_0, a, a) = (q_0, ε). 
   - Leer 'b' y desapilar 'b':
     -  δ(q_0, b, b) = (q_0, ε). 

4. Aceptación:
   - Cuando se alcanza una configuración con la pila vacía ( Z_0):
     -  δ(q_0, ε, Z_0) = (q_f, ε). 

---
### Secuencia de Procesamiento (continuación)

Para procesar la cadena "aabb" utilizando el APV asociado a la gramática en FNG:

1. **Inicialización**:  
   Configuración inicial:  
    
q_0, aabb, Z_0 → q_0, aabb, SZ_0
     
   Se apila el símbolo inicial  S  junto con  Z_0 .

2. **Primera Producción ( S → aSb )**:  
   Usamos la producción  S → aSb , desapilamos  S  y apilamos  bSa :  
    
q_0, aabb, SZ_0 → q_0, aabb, bSaZ_0
     
3. **Consumo del Primer 'a'**:  
   Leemos el primer 'a' de la entrada y desapilamos  a :  
    
q_0, aabb, bSaZ_0 → q_0, abb, bSZ_0
     
4. **Segunda Producción ( S → ab )**:  
   Usamos la producción  S → ab , desapilamos  S  y apilamos  ba :  
    
q_0, abb, bSZ_0 → q_0, abb, bbaZ_0
     
5. **Consumo del Segundo 'a'**:  
   Leemos el segundo 'a' de la entrada y desapilamos  a :  
    
q_0, abb, bbaZ_0 → q_0, bb, bbZ_0
     
6. **Consumo del Primer 'b'**:  
   Leemos el primer 'b' de la entrada y desapilamos  b :  
    
q_0, bb, bbZ_0 → q_0, b, bZ_0
     
7. **Consumo del Segundo 'b'**:  
   Leemos el segundo 'b' de la entrada y desapilamos  b :  
    
q_0, b, bZ_0 → q_0, ε, Z_0
     
8. **Aceptación por Vaciado de Pila**:  
   La pila queda vacía al alcanzar  Z_0, lo que indica que la cadena es aceptada:  
    
q_0, ε, Z_0 → q_f, ε, ε
     
---

## Observaciones

1. **Equivalencia Garantizada**:
   - El APV simula directamente las derivaciones de la gramática en FNG.
   - Cada producción de la gramática corresponde a una transición en el APV.

2. **Procesamiento Jerárquico**:
   - La pila permite manejar estructuras jerárquicas como las generadas por gramáticas independientes del contexto.

3. **Aceptación por Vaciado**:
   - El APV acepta únicamente si la pila queda completamente vacía al finalizar el procesamiento.

---

## Conclusión

El APV asociado a una gramática independiente del contexto en forma normal de Greibach procesa las cadenas siguiendo las reglas de derivación de la gramática. Este modelo demuestra cómo los autómatas a pila son equivalentes a las gramáticas independientes del contexto y pueden reconocer los mismos lenguajes mediante operaciones sobre su pila.
