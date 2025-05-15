# Autómata Finito Asociado a una Gramática Lineal por la Izquierda (G3LI)

Una gramática lineal por la izquierda (G3LI) es un tipo de gramática regular en la que las producciones tienen la forma:
-  A  → Ba , donde  A, B ∈ N  y  a ∈ T ,
-  A  → a , donde  A ∈ N  y  a ∈ T .

El autómata finito asociado a una G3LI es un modelo matemático que reconoce el mismo lenguaje generado por dicha gramática. Este proceso de asociación se basa en la equivalencia entre gramáticas regulares y autómatas finitos.

---

## Construcción del Autómata Finito Asociado a una G3LI

Para construir un autómata finito determinista (AFD) asociado a una gramática lineal por la izquierda, se sigue un procedimiento que incluye invertir tanto las producciones de la gramática como las transiciones del autómata asociado.

### Pasos para la Construcción

1. Invertir la Gramática:
   - Dada una G3LI  G = (N, T, P, S) , invertir las producciones para obtener una gramática lineal por la derecha (G3LD):
     - Si  A  → Ba , se convierte en  A'  → aB' .
     - Si  A  → a , se convierte en  A'  → a .

2. Construir el Autómata Finito No Determinista ( ε-AFND ):
   - Asociar un estado del autómata a cada símbolo no terminal de la gramática.
   - Para cada producción invertida:
     - Si  A'  → aB' , añadir una transición del estado correspondiente a  A'  hacia el estado correspondiente a  B'  con el símbolo  a .
     - Si  A'  → a , añadir una transición del estado correspondiente a  A'  hacia un estado final con el símbolo  a .

3. Invertir el Autómata:
   - Cambiar el sentido de las transiciones.
   - Intercambiar los estados inicial y final.

4. Convertir el  ε-AFND  en un AFD:
   - Aplicar el algoritmo del subconjunto para eliminar transiciones no deterministas y vacías ( ε-transiciones).

---

## Ejemplo

### Gramática Lineal por la Izquierda
Sea la gramática:
 
G = (N, T, P, S)
  Donde:
-  N = S, A, B ,
-  T = 0, 1 ,
- Producciones ( P ):
  -  S → 0A; S → 1B; A → 0S; B → 1S; A → 0; B → 1. 

### Paso 1: Invertir la Gramática
Invertimos las producciones para obtener una G3LD:
 
P' = 
\begin{cases}
S → A0; S → B1,
A → S0; B → S1,
A → 0; B → 1.
\end{cases}
  
### Paso 2: Construcción del  ε-AFND 
Asociamos un estado a cada no terminal ( S, A, B) y construimos las transiciones:
- Desde  S → A0: Transición de  S  a  A  con entrada '0'.
- Desde  S → B1: Transición de  S  a  B  con entrada '1'.
- Desde  A → S0: Transición de  A  a  S  con entrada '0'.
- Desde  B → S1: Transición de  B  a  S  con entrada '1'.
- Desde  A → 0: Transición de  A  al estado final con entrada '0'.
- Desde  B → 1: Transición de  B  al estado final con entrada '1'.

### Paso 3: Invertir el Autómata
Cambiamos el sentido de las transiciones y los estados iniciales y finales.

### Paso 4: Convertir en un AFD
Aplicamos el algoritmo del subconjunto para obtener un autómata determinista equivalente.

---

## Propiedades del Autómata Asociado

1. Equivalencia:
   - El lenguaje reconocido por el autómata es exactamente el mismo que el generado por la gramática original.

2. Determinismo:
   - El autómata resultante es determinista después de aplicar el algoritmo del subconjunto.

3. Eficiencia:
   - La representación mediante un autómata permite procesar cadenas en tiempo lineal respecto al tamaño de la entrada.

---

## Teorema Fundamental

Para toda gramática regular (lineal por la izquierda o por la derecha), existe un autómata finito determinista que reconoce el lenguaje generado por dicha gramática. Inversamente, para todo autómata finito determinista existe una gramática regular equivalente que genera el mismo lenguaje.

---

## Aplicaciones

1. Análisis Léxico:
   - Los compiladores utilizan autómatas asociados a gramáticas regulares para reconocer tokens.

2. Procesamiento de Texto:
   - Permiten buscar patrones definidos por expresiones regulares.

3. Diseño Teórico:
   - Facilitan la demostración de propiedades formales de lenguajes regulares.

---

## Conclusión

El proceso de asociar un autómata finito a una gramática lineal por la izquierda demuestra la equivalencia entre las gramáticas regulares y los autómatas finitos. Esto refuerza su importancia tanto en teoría como en aplicaciones prácticas relacionadas con lenguajes formales y su reconocimiento.
