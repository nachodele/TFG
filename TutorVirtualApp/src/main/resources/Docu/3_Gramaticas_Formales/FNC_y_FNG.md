# Forma Normal de Chomsky (FNC) y Forma Normal de Greibach (FNG)

La **Forma Normal de Chomsky (FNC)** y la **Forma Normal de Greibach (FNG)** son dos formas estandarizadas de representar gramáticas libres de contexto (GIC). Estas normalizaciones son fundamentales en la teoría de lenguajes formales, ya que simplifican el análisis y procesamiento de las gramáticas, permitiendo su uso en algoritmos como el análisis sintáctico y la construcción de autómatas.

---

## Forma Normal de Chomsky (FNC)

### Definición
Una gramática libre de contexto \( G = (N, T, P, S) \) está en **Forma Normal de Chomsky** si todas sus producciones tienen una de las siguientes formas:
1. \( A → BC \), donde \( A, B, C \in N \) y \( B, C \neq S \).
2. \( A → a \), donde \( A \in N \) y \( a \in T \).

**Restricciones**:
- No se permiten producciones con más de dos símbolos no terminales en el lado derecho.
- No se permiten producciones con cadenas vacías (\( ε \)), excepto si el lenguaje incluye explícitamente \( ε \).

### Propiedades
- Toda gramática libre de contexto puede transformarse en una gramática equivalente en FNC.
- Los árboles de derivación asociados a gramáticas en FNC son **binarios**, lo que simplifica el análisis sintáctico.

### Algoritmo para Convertir a FNC
1. **Eliminar producciones nulas (\( ε \))**:
   - Identificar los símbolos anulables y modificar las reglas afectadas.
2. **Eliminar producciones unitarias (\( A → B \))**:
   - Sustituir cada regla unitaria por las producciones del símbolo al que deriva.
3. **Eliminar símbolos inútiles**:
   - Eliminar símbolos inaccesibles e improductivos.
4. **Transformar las producciones restantes**:
   - Dividir reglas con más de dos símbolos no terminales en varias reglas binarias.

#### Ejemplo
Dada la gramática:
\[
G = (N, T, P, S)
\]
Con:
- \( N = \{S, A\} \),
- \( T = \{a, b\} \),
- \( P = \{S → AB,\; A → aA,\; A → a,\; B → bB,\; B → b\} \).

Pasos para convertir a FNC:
1. Eliminar producciones nulas: No hay reglas con \( ε \).
2. Eliminar producciones unitarias: No hay reglas unitarias.
3. Transformar reglas largas: Todas las reglas ya cumplen con la FNC.

Gramática resultante en FNC:
\[
P' = \{S → AB,\; A → aA,\; A → a,\; B → bB,\; B → b\}.
\]

---

## Forma Normal de Greibach (FNG)

### Definición
Una gramática libre de contexto \( G = (N, T, P, S) \) está en **Forma Normal de Greibach** si todas sus producciones tienen la forma:
\[
A → aα
\]
Donde:
- \( A \in N \),
- \( a \in T \),
- \( α \in N^* \) (cero o más no terminales).

**Restricciones**:
- Cada producción comienza con un símbolo terminal seguido por una cadena opcional de no terminales.
- No se permiten producciones con cadenas vacías (\( ε \)), excepto si el lenguaje incluye explícitamente \( ε \).

### Propiedades
- Toda gramática libre de contexto puede transformarse en una gramática equivalente en FNG.
- Las derivaciones generadas por una gramática en FNG tienen una estructura directa que facilita la construcción de autómatas.

### Algoritmo para Convertir a FNG
1. Partir de una gramática en Forma Normal de Chomsky (FNC).
2. Eliminar recursividad por la izquierda.
3. Reorganizar las reglas para cumplir con la estructura requerida (\( A → aα \)).

#### Ejemplo
Dada la gramática:
\[
G = (N, T, P, S)
\]
Con:
- \( N = \{S, A\} \),
- \( T = \{a, b\} \),
- \( P = \{S → Aa,\; A → Ab,\; A → a\} \).

Pasos para convertir a FNG:
1. Eliminar recursividad por la izquierda:
   - Introducir un nuevo símbolo no terminal (\( Z \)) para manejar la recursividad.
   - Resulta: \( P' = \{S → Aa,\; A → aZ,\; Z → bZ | ε\} \).
2. Reorganizar las producciones:
   - Todas las reglas ahora comienzan con un terminal.

Gramática resultante en FNG:
\[
P'' = \{S → Aa,\; A → abZ,\; Z → bZ | b\}.
\]

---

## Comparación entre FNC y FNG

| **Característica**         | **FNC**                                  | **FNG**                                  |
|----------------------------|------------------------------------------|------------------------------------------|
| Restricción principal      | Producción binaria o terminal única      | Producción inicia con un terminal        |
| Uso principal              | Análisis sintáctico y algoritmos CYK     | Construcción de autómatas y parsers LL(1) |
| Eliminación del vacío (\( ε \)) | Obligatoria                            | Obligatoria                              |

---

## Importancia

### Forma Normal de Chomsky
1. Facilita el diseño del algoritmo CYK para determinar si una cadena pertenece al lenguaje generado por una gramática.
2. Simplifica el análisis sintáctico al reducir las producciones a formas estándar.

### Forma Normal de Greibach
1. Es útil para construir autómatas deterministas y analizadores sintácticos predictivos como los parsers LL(1).
2. Proporciona una estructura directa para derivaciones.

---

## Conclusión

Tanto la Forma Normal de Chomsky como la Forma Normal de Greibach son herramientas fundamentales para trabajar con gramáticas libres de contexto. Mientras que la FNC es ideal para el análisis sintáctico mediante algoritmos como CYK, la FNG es más adecuada para construir autómatas y analizadores predictivos. Ambas formas son equivalentes en términos del lenguaje generado y permiten simplificar el trabajo con lenguajes formales.
