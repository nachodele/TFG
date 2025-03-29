# Gramáticas Tipo 2 (Independientes de Contexto)

Las **gramáticas tipo 2**, también conocidas como **gramáticas libres de contexto**, son un tipo de gramática formal dentro de la **Jerarquía de Chomsky**. Estas gramáticas generan los **lenguajes libres de contexto**, que son fundamentales en la teoría de lenguajes formales y tienen aplicaciones prácticas en el diseño de lenguajes de programación y análisis sintáctico.

---

## Definición Formal

Una gramática libre de contexto se define como una cuádrupla:
 
G = (N, T, P, S)
  Donde:
-  N : Conjunto finito de **símbolos no terminales** (variables).
-  T : Conjunto finito de **símbolos terminales**, con  N ∩ T = ∅ .
-  P : Conjunto finito de **producciones**. Cada producción tiene la forma:
   
  A  → w
      Donde:
  -  A ∈ N  es un único símbolo no terminal.
  -  w ∈ (N ∪ T)^*  es una cadena formada por símbolos terminales y/o no terminales.
-  S : **Símbolo inicial**, con  S ∈ N .

El lenguaje generado por una gramática libre de contexto  G , denotado como  L(G) , es el conjunto de todas las cadenas formadas únicamente por símbolos terminales que pueden derivarse desde el símbolo inicial  S :
 
L(G) =  w ∈ T^* : S *{ →} w 
  
---

## Características Clave

1. **Restricción en las Producciones**:
   - En cada regla, el lado izquierdo debe ser un único símbolo no terminal.
   - No hay restricciones en el lado derecho.

2. **Reconocimiento por Autómatas**:
   - Los lenguajes libres de contexto pueden ser reconocidos por un **autómata con pila**.

3. **Aplicaciones Prácticas**:
   - Se utilizan ampliamente para modelar la sintaxis de lenguajes de programación y estructuras lingüísticas.

---

## Ejemplo de Gramática Libre de Contexto

### Ejemplo 1: Lenguaje Balanceado
Consideremos el lenguaje:
 
L = a^n b^n : n ≥ 1
  Una gramática libre de contexto que genera este lenguaje es:
 
G = (N, T, P, S)
  Donde:
-  N = S ,
-  T = a, b ,
- Producciones ( P ):
  -  S → aSb ,
  -  S → ab .

### Derivación
Para generar la cadena  aabb :
1. Aplicamos  S → aSb :  S ⇒ aSb ⇒ aaSbb ⇒ aabb. 

El lenguaje generado por esta gramática es:
 
L(G) = L = a^n b^n : n ≥ 1.
  
---

## Relación con la Jerarquía de Chomsky

Las gramáticas tipo 2 ocupan el tercer nivel en la Jerarquía de Chomsky y están relacionadas con otros tipos según su potencia:

| **Tipo** | **Restricciones en las Producciones**       | **Lenguaje Generado**            | **Máquina Reconocedora**      |
|----------|--------------------------------------------|-----------------------------------|--------------------------------|
| Tipo 0   | Sin restricciones                          | Lenguajes recursivamente enumerables | Máquina de Turing             |
| Tipo 1   | Sensibles al contexto ( |α| ≤ |β| ) | Lenguajes sensibles al contexto   | Autómata linealmente acotado   |
| Tipo 2   | Libres de contexto ( A → w)            | Lenguajes libres de contexto      | Autómata con pila              |
| Tipo 3   | Regulares ( A → aB o  A → a)       | Lenguajes regulares               | Autómata finito                |

---

## Propiedades Fundamentales

### Ventajas
1. **Expresividad**:
   - Permiten describir estructuras jerárquicas y anidadas, como expresiones matemáticas o bloques en lenguajes de programación.
2. **Reconocimiento Computacional**:
   - Los lenguajes libres de contexto pueden ser reconocidos eficientemente por autómatas con pila.

### Limitaciones
1. **Incapacidad para Describir Dependencias Complejas**:
   - No pueden describir lenguajes donde se requiere una relación más compleja entre los símbolos, como  L = a^n b^n c^n : n ≥ 1 .
2. **Ambigüedad**:
   - Una gramática libre de contexto puede ser ambigua si existe más de un árbol sintáctico para una misma cadena.

---

## Ambigüedad en Gramáticas Libres de Contexto

Una gramática es ambigua si una cadena puede derivarse mediante dos o más árboles sintácticos diferentes.

### Ejemplo
Consideremos la gramática:
-  E → E + E | E * E | (E) | id .

La cadena "id + id * id" puede derivarse mediante los siguientes árboles sintácticos:

1. Interpretación como suma antes del producto:  (id + id) * id .
2. Interpretación como producto antes de la suma:  id + (id * id) .

Para resolver ambigüedades, se pueden rediseñar las gramáticas o imponer prioridades entre operaciones.

---

## Formas Normales

Para simplificar el análisis y procesamiento, las gramáticas libres de contexto pueden transformarse en formas estándar:

### Forma Normal de Chomsky (FNC)
Una gramática está en FNC si todas sus producciones tienen alguna de las siguientes formas:
1.  A → BC , donde  B, C ∈ N; B ≠ S; C ≠ S.
2.  A → a , donde  a ∈ T.

### Forma Normal de Greibach (FNG)
Una gramática está en FNG si todas sus producciones tienen la forma:
 
A → aα
  Donde  a ∈ T; α ∈ N^*.

---

## Aplicaciones

1. **Lenguajes de Programación**:
   - Las gramáticas libres de contexto se utilizan para definir la sintaxis formal en compiladores y analizadores sintácticos.
   
2. **Procesamiento del Lenguaje Natural (PLN)**:
   - Modelan estructuras gramaticales jerárquicas en lenguas humanas.

3. **Diseño Teórico**:
   - Son esenciales para estudiar propiedades formales y límites computacionales.

---

En resumen, las gramáticas tipo 2 son herramientas poderosas para modelar estructuras jerárquicas y anidadas que aparecen tanto en lenguajes formales como naturales. Su capacidad para generar lenguajes libres de contexto las convierte en un componente esencial en la teoría computacional y sus aplicaciones prácticas.
