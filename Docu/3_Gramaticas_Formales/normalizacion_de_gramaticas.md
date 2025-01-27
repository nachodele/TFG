# Normalización de Gramáticas

La **normalización de gramáticas** es el proceso mediante el cual se transforman las reglas de producción de una gramática en formas estándar, manteniendo el lenguaje generado intacto. Este proceso es fundamental en la teoría de lenguajes formales, ya que permite simplificar gramáticas, facilitar su análisis y hacerlas más adecuadas para aplicaciones prácticas como el diseño de compiladores o la construcción de autómatas.

---

## Objetivo de la Normalización

El objetivo principal de la normalización es transformar una gramática en una forma estándar que cumpla con ciertas restricciones específicas, sin alterar el lenguaje generado. Esto permite:
1. Simplificar el análisis sintáctico.
2. Eliminar ambigüedades y redundancias.
3. Facilitar la implementación en algoritmos y herramientas computacionales.

---

## Formas Normales

Existen dos formas principales de normalización para gramáticas libres de contexto (GIC): la **Forma Normal de Chomsky (FNC)** y la **Forma Normal de Greibach (FNG)**.

### 1. Forma Normal de Chomsky (FNC)

Una gramática \( G = (N, T, P, S) \) está en **Forma Normal de Chomsky** si todas sus producciones tienen una de las siguientes formas:
1. \( A → BC \), donde \( A, B, C \in N \) y \( B, C \neq S \).
2. \( A → a \), donde \( A \in N \) y \( a \in T \).

#### Propiedades
- No se permiten producciones con más de dos símbolos no terminales en el lado derecho.
- No se permiten producciones con cadenas vacías (\( ε \)), excepto si el lenguaje incluye explícitamente \( ε \).

#### Algoritmo para Convertir a FNC
1. **Eliminar producciones nulas (\( ε \))**:
   - Identificar los símbolos anulables (aquellos que pueden derivar \( ε \)).
   - Modificar las reglas afectadas para incluir todas las combinaciones posibles sin los símbolos anulables.
2. **Eliminar producciones unitarias (\( A → B \))**:
   - Sustituir cada regla unitaria por las producciones del símbolo al que deriva.
3. **Eliminar símbolos inútiles**:
   - Eliminar símbolos inaccesibles e improductivos.
4. **Transformar las producciones restantes**:
   - Dividir las reglas con más de dos símbolos no terminales en varias reglas binarias.

#### Ejemplo
Dada la gramática:
\[
G = (N, T, P, S)
\]
Con:
- \( N = \{S, A, B\} \),
- \( T = \{a, b\} \),
- \( P = \{S → AB,\; A → aA,\; A → a,\; B → bB,\; B → b\} \).

Pasos para convertir a FNC:
1. Eliminar producciones nulas: No hay reglas con \( ε \).
2. Eliminar producciones unitarias: No hay reglas unitarias.
3. Transformar reglas largas:
   - La regla \( S → AB \) ya está en FNC.
   - Las demás reglas también cumplen con las restricciones.

Gramática resultante en FNC:
\[
P' = \{S → AB,\; A → aA,\; A → a,\; B → bB,\; B → b\}.
\]

---

### 2. Forma Normal de Greibach (FNG)

Una gramática \( G = (N, T, P, S) \) está en **Forma Normal de Greibach** si todas sus producciones tienen la forma:
\[
A → aα
\]
Donde:
- \( A \in N \),
- \( a \in T \),
- \( α \in N^* \) (cero o más no terminales).

#### Propiedades
- Cada producción comienza con un símbolo terminal seguido por una cadena opcional de no terminales.
- No se permiten producciones con cadenas vacías (\( ε \)), excepto si el lenguaje incluye explícitamente \( ε \).

#### Algoritmo para Convertir a FNG
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

## Importancia de la Normalización

La normalización es crucial porque:
1. **Facilita el análisis sintáctico**: Las formas normales simplifican los algoritmos utilizados para procesar lenguajes formales.
2. **Optimiza compiladores**: Las gramáticas normalizadas son más eficientes para ser procesadas por herramientas computacionales.
3. **Garantiza consistencia**: Ayuda a evitar ambigüedades y errores estructurales en las gramáticas.

---

## Conclusión

La normalización de gramáticas es un proceso esencial para trabajar con lenguajes formales y sus aplicaciones prácticas. Tanto la Forma Normal de Chomsky como la Forma Normal de Greibach proporcionan estructuras estándar que facilitan el análisis y procesamiento eficiente de lenguajes libres de contexto.
