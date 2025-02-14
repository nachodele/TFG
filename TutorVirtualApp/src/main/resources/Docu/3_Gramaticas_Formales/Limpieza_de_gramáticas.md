# Limpieza de Gramáticas: Eliminación de Símbolos y Reglas No Generativas, y Eliminación de Reglas de Redenominación

La **limpieza de gramáticas** es un proceso esencial en la teoría de lenguajes formales para garantizar que una gramática sea eficiente, clara y no contenga elementos innecesarios o redundantes. Este proceso incluye la eliminación de símbolos inútiles, reglas no generativas y reglas de redenominación, manteniendo el lenguaje generado por la gramática intacto.

---

## Objetivo de la Limpieza

El objetivo principal de la limpieza es transformar una gramática en una versión equivalente que:
1. No contenga **símbolos superfluos** ni **reglas innecesarias**.
2. Sea más simple y fácil de analizar.
3. Genere el mismo lenguaje que la gramática original.

---

## Eliminación de Símbolos Inútiles

### Tipos de Símbolos Inútiles
1. **Símbolos inaccesibles**:
   - Son aquellos símbolos (terminales o no terminales) que no pueden ser alcanzados desde el símbolo inicial \( S \) mediante ninguna secuencia de derivaciones.
   - Ejemplo: Si \( G = (N, T, S, P) \) tiene \( A \in N \) pero no existe \( S \overset{*}{\Rightarrow} xAy \), entonces \( A \) es inaccesible.

2. **Símbolos improductivos**:
   - Son aquellos símbolos no terminales que no pueden derivar cadenas formadas únicamente por terminales.
   - Ejemplo: Si \( G = (N, T, S, P) \) tiene \( B \in N \) pero no existe \( B \overset{*}{\Rightarrow} w \), con \( w \in T^* \), entonces \( B \) es improductivo.

### Algoritmo para Eliminar Símbolos Inútiles
1. **Eliminar símbolos improductivos**:
   - Identificar los símbolos que pueden derivar cadenas terminales.
   - Eliminar los símbolos improductivos y las reglas asociadas.
2. **Eliminar símbolos inaccesibles**:
   - Identificar los símbolos que son alcanzables desde el símbolo inicial.
   - Eliminar los símbolos inaccesibles y las reglas asociadas.

#### Ejemplo
Dada la gramática:
\[
G = (N, T, S, P)
\]
Con:
- \( N = \{S, A, B, C\} \),
- \( T = \{a, b\} \),
- \( P = \{S → AB,\; A → aA,\; A → a,\; B → bB,\; C → cC\} \).

1. **Símbolos improductivos**:
   - \( C → cC \): Nunca deriva terminales. Eliminar \( C \).
2. **Símbolos inaccesibles**:
   - Desde \( S → AB \), solo se alcanzan \( A, B \). Eliminar \( C \).

Gramática limpia:
\[
G' = (N', T', S', P')
\]
Donde:
- \( N' = \{S, A, B\} \),
- \( T' = \{a, b\} \),
- \( P' = \{S → AB,\; A → aA,\; A → a,\; B → bB\} \).

---

## Eliminación de Reglas No Generativas

### Definición
Las **reglas no generativas** son aquellas que no contribuyen a generar cadenas terminales válidas en el lenguaje definido por la gramática.

### Algoritmo para Eliminar Reglas No Generativas
1. Identificar los **símbolos anulables**, es decir, aquellos que pueden derivar la cadena vacía (\( ε \)).
2. Modificar las producciones afectadas por los símbolos anulables para incluir todas las combinaciones posibles sin dichos símbolos.
3. Eliminar las producciones originales relacionadas con los símbolos anulables.

#### Ejemplo
Dada la gramática:
\[
G = (N, T, S, P)
\]
Con:
- \( N = \{S, A\} \),
- \( T = \{a, b\} \),
- \( P = \{S → Aa,\; A → ε,\; A → b\} \).

1. Identificar los símbolos anulables:
   - \( A → ε \): Entonces \( A \) es anulable.
2. Modificar las producciones afectadas:
   - De \( S → Aa \), se obtiene una nueva producción: \( S → a \).
3. Gramática limpia:
   - Producciones finales: \( P' = \{S → Aa,\; S → a,\; A → b\} \).

---

## Eliminación de Reglas de Redenominación

### Definición
Las **reglas de redenominación** son aquellas en las que un símbolo no terminal deriva directamente otro símbolo no terminal (\( A → B \)), sin aportar contenido adicional.

### Algoritmo para Eliminar Reglas de Redenominación
1. Construir un conjunto para cada símbolo no terminal con todos los símbolos a los que puede derivar directamente o indirectamente mediante reglas de redenominación.
2. Sustituir cada regla de redenominación por las producciones del símbolo al que deriva.
3. Eliminar las reglas redundantes.

#### Ejemplo
Dada la gramática:
\[
G = (N, T, S, P)
\]
Con:
- \( N = \{S, A, B\} \),
- \( T = \{a\} \),
- \( P = \{S → A,\; A → B,\; B → a\} \).

1. Construir conjuntos de redenominación:
   - Para \( S: S ⇒ A ⇒ B ⇒ a.\)
   - Para \( A: A ⇒ B ⇒ a.\)
   - Para \( B: B ⇒ a.\)
2. Sustituir reglas de redenominación:
   - Sustituir \( S → A,\; A → B:\) por sus producciones finales (\( S → a,\; A → a.\))
3. Gramática limpia:
   - Producciones finales: \( P' = \{S → a,\; A → a,\; B → a\}.\)

---

## Orden de Aplicación en la Limpieza

Para garantizar una limpieza efectiva y evitar inconsistencias en el proceso, se recomienda aplicar los algoritmos en el siguiente orden:

1. **Eliminar símbolos improductivos**.
2. **Eliminar símbolos inaccesibles**.
3. **Eliminar reglas no generativas**.
4. **Eliminar reglas de redenominación**.

---

## Conclusión

La limpieza de gramáticas es un paso crucial para garantizar su simplicidad y utilidad práctica sin alterar el lenguaje generado. Este proceso elimina elementos redundantes o inútiles y asegura que la gramática sea eficiente y fácil de interpretar en aplicaciones como compiladores o análisis sintáctico.
