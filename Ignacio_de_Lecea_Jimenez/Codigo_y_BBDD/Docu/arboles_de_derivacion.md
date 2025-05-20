# Árboles de Derivación

Los árboles de derivación son representaciones gráficas que muestran cómo se deriva una cadena de un lenguaje a partir del símbolo inicial de una gramática. Son herramientas fundamentales en la teoría de lenguajes formales, especialmente en gramáticas libres de contexto, ya que permiten visualizar el proceso de derivación y analizar la estructura jerárquica de las cadenas generadas.

---

## Definición

Un árbol de derivación es un grafo en forma de árbol que satisface las siguientes propiedades:
1. Raíz: El nodo raíz del árbol corresponde al símbolo inicial ( S ) de la gramática.
2. Hojas: Las hojas del árbol corresponden a símbolos terminales o a la cadena vacía ( λ ).
3. Nodos interiores: Los nodos interiores corresponden a símbolos no terminales.
4. Producciones: Si un nodo está etiquetado con un símbolo no terminal  A , sus hijos (leídos de izquierda a derecha) deben corresponder a los símbolos en el lado derecho de alguna producción  A → X_1 X_2 ... X_k  de la gramática.

El conjunto de hojas, leído de izquierda a derecha, forma la cadena generada por el árbol, conocida como la producción del árbol.

---

## Construcción del Árbol

Para construir un árbol de derivación a partir de una gramática  G = (N, T, S, P) :
1. Comenzar con un nodo raíz etiquetado con el símbolo inicial  S .
2. Aplicar las reglas de producción sucesivamente:
   - Reemplazar un nodo no terminal con sus hijos según el lado derecho de una producción.
3. Continuar hasta que todas las hojas sean símbolos terminales o la cadena vacía ( λ ).

### Ejemplo
Sea la gramática:
 
G = (N, T, S, P)
  Donde:
-  N = S ,
-  T = a, b ,
-  P = S → aSb ; S → ab .

Para derivar la cadena  aaabbb :
1. Aplicamos  S → aSb :  S ⇒ aSb ⇒ aaSbb ⇒ aaaSbbb ⇒ aaabbb .
2. El árbol correspondiente es:

   S
   / | \
a   S   b
   / | \
   a   S   b
      / | \
      a   ε   b


---

## Propiedades del Árbol de Derivación

1. Unicidad para una Derivación:
   - Cada derivación tiene un único árbol asociado.
   - Sin embargo, una misma cadena puede tener varias derivaciones diferentes (más a la izquierda o más a la derecha).

2. Ambigüedad:
   - Una gramática es ambigua si existe al menos una cadena que puede ser representada por más de un árbol de derivación diferente.
   - Ejemplo: Para una gramática que genera expresiones aritméticas simples, la cadena "id + id * id" puede tener dos árboles diferentes dependiendo del orden en que se evalúan las operaciones.

3. Relación con Derivaciones:
   - Si leemos las etiquetas de las hojas del árbol (de izquierda a derecha), obtenemos la cadena generada por el árbol.
   - Las derivaciones más a la izquierda o más a la derecha corresponden a diferentes formas posibles del árbol.

---

## Subárboles

Un subárbol es cualquier parte del árbol cuya raíz es un nodo cualquiera y cuyos nodos son los descendientes directos e indirectos de dicho nodo.

### Propiedad
Los nodos terminales de un subárbol, leídos de izquierda a derecha, forman una frase respecto al nodo raíz del subárbol.

Ejemplo:
En el árbol anterior para  aaabbb , el subárbol cuya raíz es el segundo  S  genera la frase  ab .

---

## Relación entre Árboles y Lenguajes

1. Producción del Árbol:
   - La cadena generada por un árbol corresponde al conjunto de etiquetas en las hojas leídas secuencialmente.

2. Teorema Fundamental:
   - Sea  G = (N, T, S, P)  una gramática libre de contexto y sea  w ∈ T^* . Entonces:
     -  w ∈ L(G)  si y solo si existe un árbol de derivación en  G  cuya producción es  w .

---

## Ambigüedad en Gramáticas

Una gramática es ambigua si existe al menos una cadena que puede ser generada por más de un árbol de derivación diferente.

### Ejemplo
Sea la gramática:
 
G = (N, T, S, P)
  Con producciones:
-  S → SS | id .

Para la cadena "ididid", los árboles posibles son:

Árbol 1:

   S
/   \
S     S
/       \
id       SS
      /  \
   id    id

Árbol 2:

   S
   /   \
SS    id
/  \
id    id

Ambos árboles generan la misma cadena pero tienen estructuras diferentes; por lo tanto, esta gramática es ambigua.

---

## Aplicaciones

1. Análisis Sintáctico:
   - Los árboles se utilizan en compiladores para representar la estructura jerárquica del código fuente.

2. Procesamiento del Lenguaje Natural (PLN):
   - Representan estructuras gramaticales en oraciones humanas.

3. Visualización y Depuración:
   - Ayudan a entender y depurar reglas gramaticales complejas.

4. Validación Estructural:
   - Verifican si una cadena pertenece al lenguaje generado por una gramática dada.

---

En resumen, los árboles de derivación son herramientas gráficas esenciales para representar y analizar cómo las cadenas se generan mediante reglas gramaticales. Permiten estudiar propiedades como ambigüedad y estructura jerárquica en lenguajes formales.
