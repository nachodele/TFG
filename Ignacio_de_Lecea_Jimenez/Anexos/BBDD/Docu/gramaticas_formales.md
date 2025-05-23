# Gramáticas Formales

Las gramáticas formales son estructuras matemáticas utilizadas para describir lenguajes formales mediante un conjunto de reglas que determinan cómo se generan las cadenas válidas de un lenguaje. Estas gramáticas son fundamentales en la teoría de lenguajes formales, autómatas y la computación, y tienen aplicaciones tanto en la lingüística como en las ciencias de la computación.

## Definición Formal

Una gramática formal se define como una cuádrupla:

 
G = (N, T, S, P)
  
Donde:
-  N : Conjunto finito de símbolos no terminales (variables). Representan categorías sintácticas intermedias.
-  T : Conjunto finito de símbolos terminales. Son los elementos finales del lenguaje.
-  S ∈ N : Símbolo inicial o axioma. Es el punto de partida para generar cadenas.
-  P : Conjunto finito de reglas de producción. Cada regla tiene la forma  u  → v , donde  u  y  v  son cadenas sobre  N ∪ T , y  u ≠ ε  (no vacío).

El lenguaje generado por una gramática  G , denotado como  L(G) , es el conjunto de todas las cadenas formadas únicamente por símbolos terminales que pueden derivarse a partir del símbolo inicial  S  mediante las reglas de producción.

## Jerarquía de Chomsky

Noam Chomsky clasificó las gramáticas formales en cuatro tipos según las restricciones en sus reglas de producción y los lenguajes que generan. Esta clasificación se conoce como la Jerarquía de Chomsky:

| Tipo | Nombre                     | Restricciones en las Producciones                | Lenguaje Generado            | Máquina Reconocedora        |
|------|----------------------------|--------------------------------------------------|------------------------------|-----------------------------|
| 0    | Sin restricciones          |  u  → v , donde  u, v ∈ (N ∪ T)^*  y  u ≠ ε  | Lenguajes recursivamente enumerables | Máquina de Turing          |
| 1    | Sensibles al contexto      |  xAy  → xvy , donde  A ∈ N, v ≠ ε                | Lenguajes sensibles al contexto | Autómata linealmente acotado |
| 2    | Libres de contexto         |  A  → v , donde  A ∈ N, v ∈ (N ∪ T)^*                 | Lenguajes libres de contexto  | Autómata de pila            |
| 3    | Regulares                  |  A  → aB, A  → a, A  → ε, con restricciones específicas | Lenguajes regulares          | Autómata finito            |

### Gramáticas Tipo 3: Regulares
- Las reglas tienen una estructura muy restringida:
  - Lineales por la derecha:  A → aB o  A → a.
  - Lineales por la izquierda:  A → Ba o  A → a.
- Generan lenguajes simples que pueden representarse mediante expresiones regulares.

### Gramáticas Tipo 2: Libres de Contexto
- Cada regla tiene un único no terminal en el lado izquierdo:  A → v.
- Se utilizan ampliamente para modelar lenguajes naturales y lenguajes de programación.
- Ejemplo: Una gramática que genera cadenas del tipo  a^n b^n : n ≥ 1:
  - Reglas: 
    -  S → aSb
    -  S → ab.

### Gramáticas Tipo 1: Sensibles al Contexto
- Las producciones permiten que el contexto determine la forma en que se aplica una regla.
- Ejemplo: Una gramática que genera cadenas del tipo  a^n b^n c^n : n ≥ 1.

### Gramáticas Tipo 0: Sin Restricciones
- No tienen limitaciones en sus producciones.
- Son las más generales y pueden describir cualquier lenguaje recursivamente enumerable.

## Conceptos Relacionados

### Formas Sentenciales y Sentencias
- Una forma sentencial es cualquier cadena derivada desde el símbolo inicial usando las reglas de producción.
- Una sentencia es una forma sentencial compuesta únicamente por símbolos terminales.

### Derivaciones
- Derivación más a la izquierda: Se aplica siempre la regla al símbolo no terminal más a la izquierda.
- Derivación más a la derecha: Se aplica siempre la regla al símbolo no terminal más a la derecha.

### Ambigüedad
Una gramática es ambigua si existe al menos una cadena que puede derivarse mediante dos o más árboles sintácticos diferentes. Esto puede evitarse rediseñando la gramática.

### Árboles de Derivación
Un árbol de derivación representa gráficamente cómo se genera una cadena desde el símbolo inicial siguiendo las reglas de producción. Los nodos internos corresponden a símbolos no terminales, mientras que las hojas representan símbolos terminales.

## Formas Normales

Para simplificar el análisis y procesamiento, las gramáticas libres de contexto pueden transformarse en formas normales:

1. Forma Normal de Chomsky (FNC):
   - Todas las producciones tienen una de estas formas:
     -  A → BC, donde  B, C ∈ N.
     -  A → a, donde  a ∈ T.
   - No contiene producciones vacías ( ε) ni unitarias ( A → B).

2. Forma Normal de Greibach (FNG):
   - Todas las producciones tienen la forma:
     -  A → aα, donde  a ∈ T, α ∈ N^*.

## Ejemplos

### Ejemplo 1: Gramática Regular
Gramática que genera cadenas del tipo "ab", "aabb", "aaabbb", etc.:

 
G = (S, A, a, b, S, P)
  Reglas:
-  S → aA
-  A → bS
-  S → ε

Lenguaje generado:  L(G) = a^n b^n : n ≥ 0.

### Ejemplo 2: Gramática Libre de Contexto
Gramática para el lenguaje palíndromo sobre el alfabeto {a, b}:

 
G = (S, a, b, S, P)
  Reglas:
-  S → aSa
-  S → bSb
-  S → ε

Lenguaje generado: Palíndromos sobre {a, b}.

---

Las gramáticas formales son herramientas esenciales para describir lenguajes y analizar su estructura. Su clasificación jerárquica permite abordar problemas computacionales con diferentes niveles de complejidad y diseñar autómatas o algoritmos específicos para su reconocimiento.
