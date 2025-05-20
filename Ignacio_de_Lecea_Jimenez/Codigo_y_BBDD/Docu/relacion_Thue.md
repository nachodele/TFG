# Relación de Thue

La relación de Thue es un concepto fundamental en la teoría de lenguajes formales y sistemas de reescritura. Introducida por el matemático noruego Axel Thue en 1914, esta relación se utiliza para modelar transformaciones de cadenas mediante reglas de reescritura. A continuación, se detalla su definición, propiedades y aplicaciones.

## Definición

Dada un conjunto finito  Σ  llamado alfabeto, un sistema de reescritura sobre  Σ  está definido por un conjunto finito de reglas de la forma:

 
(u, v) ∈ R
  
donde  u, v ∈ Σ^*  (el conjunto de todas las cadenas formadas con los símbolos del alfabeto). La relación de Thue, denotada como  *{↔} , es la clausura reflexiva, simétrica y transitiva de las reglas de reescritura  R . Esto significa que dos cadenas  x, y ∈ Σ^*  están relacionadas por  *{↔}  si y solo si una puede transformarse en la otra aplicando un número finito (incluido cero) de reglas en  R .

### Formalización

La relación de Thue se define como:

1. Reflexividad: Toda cadena está relacionada consigo misma:  x *{↔} x .
2. Simetría: Si  x *{↔} y , entonces  y *{↔} x .
3. Transitividad: Si  x *{↔} y  y  y *{↔} z , entonces  x *{↔} z .

En términos operativos, la relación permite transformar una cadena en otra mediante sustituciones definidas por las reglas del sistema.

## Propiedades

1. Equivalencia: La relación de Thue es una relación de equivalencia porque cumple las propiedades reflexiva, simétrica y transitiva.
2. Clausura bajo concatenación: Si  x_1 *{↔} y_1  y  x_2 *{↔} y_2 , entonces  x_1x_2 *{↔} y_1y_2 .
3. Compatibilidad con el contexto: Si  u_1 *{↔} u_2 , entonces para cualquier cadena  v, w ∈ Σ^* , se tiene que  v u_1 w *{↔} v u_2 w .

## Ejemplo

Supongamos un sistema de reescritura con las reglas:

-  aab  → bba 
-  bba  → abba 

Entonces:

1. Aplicando reflexividad:  aab *{↔} aab .
2. Aplicando una regla directamente:  aab *{↔} bba .
3. Aplicando transitividad: Si  aab *{↔} bba  y  bba *{↔} abba , entonces  aab *{↔} abba .

## Aplicaciones

La relación de Thue tiene numerosas aplicaciones en teoría de lenguajes formales y computación:

- Problema de la palabra en grupos: La relación se utiliza para determinar si dos palabras representan el mismo elemento en un grupo definido por presentaciones.
- Sistemas de reescritura: Modela transformaciones en cadenas para simplificación o normalización.
- Autómatas y gramáticas: Sirve como base para definir lenguajes generados por gramáticas formales.
- Compresión de datos: Se usa para identificar patrones repetitivos en cadenas.

## Importancia Histórica

El trabajo pionero de Axel Thue marcó el inicio del estudio sistemático de sistemas de reescritura y problemas relacionados con lenguajes formales. Aunque inicialmente su investigación no tuvo gran impacto, posteriormente fue reconocida como fundamental para el desarrollo de áreas como la teoría combinatoria sobre palabras, autómatas finitos y gramáticas.

---

La relación de Thue sigue siendo un área activa de investigación debido a su conexión con problemas computacionales complejos y su aplicabilidad en diversas disciplinas matemáticas e informáticas.
