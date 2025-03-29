# Generación de una Gramática Independiente del Contexto (G2) Asociada a un APV

Los **autómatas a pila por vaciado (APV)** y las **gramáticas independientes del contexto (GIC)** están estrechamente relacionados, ya que ambos reconocen los mismos lenguajes: los **lenguajes independientes del contexto (LIC)**. Dado un APV, es posible construir una GIC que genere exactamente el mismo lenguaje reconocido por el autómata. Este proceso se basa en la equivalencia entre los autómatas a pila y las gramáticas libres de contexto.

---

## Estrategia General para la Conversión

Dado un APV  M = (Q, Σ, Γ, δ, q_0, Z_0) , el objetivo es construir una gramática  G = (N, T, P, S)  tal que:
 
L(G) = L(M).
  
### Componentes de la Gramática
1. **Símbolos No Terminales ( N )**:
   - Cada no terminal tiene la forma  [q, A, p] , donde:
     -  q, p ∈ Q : Son estados del APV.
     -  A ∈ Γ : Es un símbolo de la pila.
   - El no terminal  [q, A, p]  representa todas las cadenas que llevan al autómata desde el estado  q , con  A  en la cima de la pila, hasta el estado  p , vaciando  A  en el proceso.

2. **Símbolos Terminales ( T )**:
   - Los símbolos terminales son los mismos que el alfabeto de entrada del APV ( T = Σ ).

3. **Producciones ( P )**:
   - Las producciones se derivan directamente de las transiciones del APV.

4. **Símbolo Inicial ( S )**:
   - El símbolo inicial es  [q_0, Z_0, q_f] , donde:
     -  q_0 : Estado inicial del APV.
     -  Z_0 : Símbolo inicial de la pila.
     -  q_f : Estado final ficticio que representa el vaciado completo de la pila.

---

## Construcción de las Producciones

### Tipos de Producciones
1. **Producciones para Transiciones con Entrada y Manipulación de Pila**:
   - Si  δ(q, a, A) = (p, γ) , donde  γ = B_1 B_2 ... B_k , entonces añadimos la producción:
      
     [q, A, r] → a [p, B_1, r_1] [r_1, B_2, r_2] ... [r_{k-1}, B_k, r].
          - Aquí  r_1, r_2, ..., r_{k-1}  son estados intermedios.

2. **Producciones para Transiciones- ε **:
   - Si  δ(q, ε, A) = (p, γ) , donde  γ = B_1 B_2 ... B_k , entonces añadimos la producción:
      
     [q, A, r] → [p, B_1, r_1] [r_1, B_2, r_2] ... [r_{k-1}, B_k, r].
       
3. **Producciones para Consumo Directo de Terminales**:
   - Si  δ(q, a, A) = (p, ε) , entonces añadimos la producción:
      
     [q, A, p] → a.
       
4. **Producciones para Vaciado Directo**:
   - Si  δ(q, ε, A) = (p, ε) , entonces añadimos la producción:
      
     [q, A, p] → ε.
       
---

## Ejemplo: Lenguaje Balanceado

Sea el lenguaje:
 
L = a^n b^n : n ≥ 1.
  
### APV Asociado
El APV correspondiente tiene:
- Estados:  Q = {q_0} ,
- Alfabeto de entrada:  Σ = {a, b} ,
- Alfabeto de la pila:  Γ = {A, Z_0} ,
- Transiciones:
  1. Leer 'a' y apilar 'A':
     -  δ(q_0, a, Z_0) = (q_0, AZ_0), δ(q_0, a, A) = (q_0, AA). 
  2. Leer 'b' y desapilar 'A':
     -  δ(q_0, b, A) = (q_0, ε). 

Acepta si la pila queda vacía al finalizar el procesamiento.

---

### Gramática Asociada
La gramática asociada tiene:

#### Símbolos No Terminales
 
N = {[q_0, Z_0, q_0], [q_0, A, q_0]}.
  
#### Símbolos Terminales
 
T = {a, b}.
  
#### Producciones
1. Desde el símbolo inicial ( S = [q_0,Z_0,q_0] ):
   - Apilar un 'A' por cada 'a' leído y desapilarlo por cada 'b':
     -  [q_0,Z_0,q_0] → a [q_0,A,q_0] b. 

2. Para manejar múltiples 'a' y 'b':
   - Recursión para apilar y desapilar múltiples 'A':
     -  [q_0,A,q_0] → a [q_0,A,q_0] b. 
   - Caso base para una sola 'a' y una sola 'b':
     -  [q_0,A,q_0] → ab. 

---

### Gramática Final
La gramática generada es:
 
G = ([q_0,Z_0,q_0], [q_0,A,q_0], {a,b}, P,[q_0,Z_0,q_0]),
  donde las producciones son:
1.  [q_0,Z_0,q_0] → a [q_0,A,q_0] b. 
2.  [q_0,A,q_0] → a [q_0,A,q_0] b. 
3.  [q_0,A,q_0] → ab. 

---

## Observaciones

1. **Equivalencia Garantizada**:
   - El lenguaje generado por la gramática es exactamente el mismo que el reconocido por el APV.

2. **Procesamiento Jerárquico**:
   - La gramática refleja directamente las operaciones de apilado y desapilado realizadas por el APV.

3. **Aplicaciones Prácticas**:
   - Este procedimiento es útil para convertir modelos basados en autómatas en representaciones gramaticales más manejables.

---

## Conclusión

La generación de una gramática independiente del contexto asociada a un APV demuestra cómo los lenguajes independientes del contexto pueden ser representados tanto mediante autómatas como mediante gramáticas equivalentes. Este proceso refuerza la conexión teórica entre ambas representaciones y su aplicabilidad práctica.
