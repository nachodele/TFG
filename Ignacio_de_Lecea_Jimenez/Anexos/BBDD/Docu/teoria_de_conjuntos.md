# Teoría de Conjuntos

La teoría de conjuntos es una rama fundamental de las matemáticas que estudia las propiedades, relaciones y operaciones entre conjuntos, los cuales son colecciones bien definidas de objetos llamados elementos. Fue introducida formalmente por Georg Cantor a finales del siglo XIX y constituye la base para muchas áreas de las matemáticas y la lógica.

---

## Conceptos Fundamentales

### Conjunto
Un conjunto es una colección de objetos considerados como una unidad. Cada objeto en un conjunto se denomina elemento. Si un elemento x pertenece a un conjunto A, se denota como x ∈ A. Si no pertenece, se escribe x ∉ A.

Ejemplo:
- A = 1, 2, 3, donde 1 ∈ A y 4 ∉ A.

### Conjunto Vacío
El conjunto vacío, denotado por  ∅  o   , es el conjunto que no contiene ningún elemento.

### Subconjunto
Un conjunto A es un subconjunto de otro conjunto B (denotado como A ⊆ B) si todos los elementos de A también están en B.

Ejemplo:
- Si B = 1, 2, 3, entonces A = 1, 2 es un subconjunto de B.

### Cardinalidad
La cardinalidad de un conjunto es el número de elementos que contiene. Se denota como |A|.

Ejemplo:
- Si A = 1, 2, 3, entonces |A| = 3.

### Conjunto Potencia
El conjunto potencia de un conjunto X, denotado como P(X), es el conjunto formado por todos los subconjuntos de X.

Ejemplo:
- Si X = a, b, entonces P(X) = ∅, a, b, a, b.

---

## Operaciones entre Conjuntos

### Unión
La unión de dos conjuntos A y B, denotada como A ∪ B, es el conjunto que contiene todos los elementos que están en A, en B, o en ambos.

Ejemplo:
- Si A = 1, 2 y B = 2, 3, entonces A ∪ B = 1, 2, 3.

### Intersección
La intersección de dos conjuntos A y B, denotada como A ∩ B, es el conjunto que contiene los elementos comunes a ambos conjuntos.

Ejemplo:
- Si A = 1, 2 y B = 2, 3, entonces A ∩ B = 2.

### Diferencia
La diferencia entre dos conjuntos (A - B) es el conjunto de elementos que están en A pero no en B.

Ejemplo:
- Si A = 1, 2, 3 y B = 2, 3, 4, entonces A - B = 1.

### Complemento
El complemento de un conjunto A respecto a un conjunto universal U, denotado como U - A o simplemente como A^c, es el conjunto de todos los elementos en el universo que no están en A.

Ejemplo:
- Si el universo es U = 1, 2, 3, 4, 5 y A = 1, 2, 3, entonces el complemento es: 
 A^c = U - A = 4, 5.

---

## Clasificación según Cardinalidad

### Finitos e Infinitos
Un conjunto es finito si tiene un número limitado de elementos; es infinito si su cardinalidad no puede contarse.

### Numerables y No Numerables

#### Conjuntos Numerables
Un conjunto es numerable si puede establecerse una biyección con los números naturales 
(|ℕ| = ℵ_0 ).

Ejemplos:
- Los números naturales ℕ.
- Los números enteros ℤ.
- Los números racionales ℚ.

#### Conjuntos No Numerables
Un conjunto es no numerable si su cardinalidad excede la de los números naturales ( |X| > |ℕ| = ℵ_0 ).

Ejemplos:
- Los números reales ℝ.
- El conjunto potencia de los números naturales P(ℕ).

---

## Relaciones entre Conjuntos

### Igualdad
Dos conjuntos son iguales ( A = B ) si tienen exactamente los mismos elementos.

### Inclusión Propia
Un conjunto está estrictamente incluido en otro ( A ⊂ B) si todos los elementos de  A \ están en B pero existen elementos adicionales fuera.

---

## Relaciones de Equivalencia

Una relación sobre un conjunto se llama relación de equivalencia si cumple las siguientes propiedades:

1. Reflexividad: Todo elemento está relacionado consigo mismo.
   - Formalmente: Para todo elemento a ∈ S ; aRa.

2. Simetría: Si un elemento está relacionado con otro, entonces ese otro también está relacionado con el primero.
   - Formalmente: Para todo par de elementos a,b∈S ; aRb implica bRa.

3. Transitividad: Si un elemento está relacionado con un segundo y este con un tercero, entonces el primero está relacionado con el tercero.
   - Formalmente: Para todo a,b,c∈S ; aRb∧bRc implica aRc.

---

## Clases de Equivalencia

Las relaciones de equivalencia dividen al conjunto original en subconjuntos disjuntos llamados clases de equivalencia, donde cada clase agrupa a todos los elementos que están relacionados entre sí. 

Si una relación de equivalencia está definida sobre un conjunto S ; [a] denota la clase de equivalencia del elemento a∈S.

Propiedades:
1. Las clases son disjuntas: Dos clases diferentes no comparten elementos.
2. La unión de todas las clases cubre completamente al conjunto original.

Ejemplo:
- La relación "ser congruente módulo m" sobre los enteros divide al conjunto ℤ\ en exactamente m\ clases equivalentes.

---

## Conjunto Cociente

El conjunto cociente, denotado como S/R, es el conjunto formado por todas las clases equivalentes definidas por la relación R.

Ejemplo:
Si la relación "ser congruente módulo 4" está definida sobre los enteros,
 ℤ/≡_4= 0],[1],[2],[3].

---

