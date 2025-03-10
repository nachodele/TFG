# Relación de Thue

La **relación de Thue** es un concepto fundamental en la teoría de lenguajes formales y sistemas de reescritura. Introducida por el matemático noruego Axel Thue en 1914, esta relación se utiliza para modelar transformaciones de cadenas mediante reglas de reescritura. A continuación, se detalla su definición, propiedades y aplicaciones.

## Definición

Dada un conjunto finito \( \Sigma \) llamado alfabeto, un **sistema de reescritura** sobre \( \Sigma \) está definido por un conjunto finito de reglas de la forma:

\[
(u, v) \in R
\]

donde \( u, v \in \Sigma^* \) (el conjunto de todas las cadenas formadas con los símbolos del alfabeto). La relación de Thue, denotada como \( \overset{*}{\leftrightarrow} \), es la **clausura reflexiva, simétrica y transitiva** de las reglas de reescritura \( R \). Esto significa que dos cadenas \( x, y \in \Sigma^* \) están relacionadas por \( \overset{*}{\leftrightarrow} \) si y solo si una puede transformarse en la otra aplicando un número finito (incluido cero) de reglas en \( R \).

### Formalización

La relación de Thue se define como:

1. **Reflexividad**: Toda cadena está relacionada consigo misma: \( x \overset{*}{\leftrightarrow} x \).
2. **Simetría**: Si \( x \overset{*}{\leftrightarrow} y \), entonces \( y \overset{*}{\leftrightarrow} x \).
3. **Transitividad**: Si \( x \overset{*}{\leftrightarrow} y \) y \( y \overset{*}{\leftrightarrow} z \), entonces \( x \overset{*}{\leftrightarrow} z \).

En términos operativos, la relación permite transformar una cadena en otra mediante sustituciones definidas por las reglas del sistema.

## Propiedades

1. **Equivalencia**: La relación de Thue es una relación de equivalencia porque cumple las propiedades reflexiva, simétrica y transitiva.
2. **Clausura bajo concatenación**: Si \( x_1 \overset{*}{\leftrightarrow} y_1 \) y \( x_2 \overset{*}{\leftrightarrow} y_2 \), entonces \( x_1x_2 \overset{*}{\leftrightarrow} y_1y_2 \).
3. **Compatibilidad con el contexto**: Si \( u_1 \overset{*}{\leftrightarrow} u_2 \), entonces para cualquier cadena \( v, w \in \Sigma^* \), se tiene que \( v u_1 w \overset{*}{\leftrightarrow} v u_2 w \).

## Ejemplo

Supongamos un sistema de reescritura con las reglas:

- \( aab \rightarrow bba \)
- \( bba \rightarrow abba \)

Entonces:

1. Aplicando reflexividad: \( aab \overset{*}{\leftrightarrow} aab \).
2. Aplicando una regla directamente: \( aab \overset{*}{\leftrightarrow} bba \).
3. Aplicando transitividad: Si \( aab \overset{*}{\leftrightarrow} bba \) y \( bba \overset{*}{\leftrightarrow} abba \), entonces \( aab \overset{*}{\leftrightarrow} abba \).

## Aplicaciones

La relación de Thue tiene numerosas aplicaciones en teoría de lenguajes formales y computación:

- **Problema de la palabra en grupos**: La relación se utiliza para determinar si dos palabras representan el mismo elemento en un grupo definido por presentaciones.
- **Sistemas de reescritura**: Modela transformaciones en cadenas para simplificación o normalización.
- **Autómatas y gramáticas**: Sirve como base para definir lenguajes generados por gramáticas formales.
- **Compresión de datos**: Se usa para identificar patrones repetitivos en cadenas.

## Importancia Histórica

El trabajo pionero de Axel Thue marcó el inicio del estudio sistemático de sistemas de reescritura y problemas relacionados con lenguajes formales. Aunque inicialmente su investigación no tuvo gran impacto, posteriormente fue reconocida como fundamental para el desarrollo de áreas como la teoría combinatoria sobre palabras, autómatas finitos y gramáticas.

---

La relación de Thue sigue siendo un área activa de investigación debido a su conexión con problemas computacionales complejos y su aplicabilidad en diversas disciplinas matemáticas e informáticas.
