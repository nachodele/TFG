# Jerarquía de Chomsky

La Jerarquía de Chomsky, propuesta por Noam Chomsky en 1956, es un sistema de clasificación que organiza los lenguajes formales y las gramáticas en función de su poder generativo. Este modelo jerárquico es fundamental en la teoría de lenguajes formales y autómatas, y clasifica las gramáticas en cuatro tipos principales: Tipo 0, Tipo 1, Tipo 2 y Tipo 3. Cada tipo representa una clase de lenguajes con un poder generativo creciente.

## Niveles de la Jerarquía

### Tipo 0: Gramáticas sin restricciones
- Lenguaje: Lenguajes recursivamente enumerables.
- Automatón: Máquina de Turing.
- Reglas de producción: No tienen restricciones específicas; pueden tener cualquier forma  α → β , donde  α  y  β  son cadenas de símbolos que incluyen terminales, no terminales o ambos.
- Características:
  - Son los lenguajes más generales.
  - Incluyen todos los lenguajes que pueden ser reconocidos por una Máquina de Turing.
  - No garantizan que el proceso de decisión termine (pueden ser no decidibles).

### Tipo 1: Gramáticas sensibles al contexto
- Lenguaje: Lenguajes sensibles al contexto.
- Automatón: Autómata linealmente acotado (LBA).
- Reglas de producción: De la forma  α A β → α Γ β , donde  A  es un símbolo no terminal,  α, β, Γ  son cadenas (posiblemente vacías), y  |Γ| ≥ |A| .
- Características:
  - Las reglas respetan el contexto en el que aparecen los símbolos no terminales.
  - Son más restrictivas que las gramáticas Tipo 0, pero aún muy expresivas.

### Tipo 2: Gramáticas libres de contexto
- Lenguaje: Lenguajes libres de contexto.
- Automatón: Autómata de pila (Pushdown Automaton).
- Reglas de producción: De la forma  A → Γ , donde  A  es un símbolo no terminal y  Γ  es una cadena formada por terminales y/o no terminales.
- Características:
  - Usadas ampliamente en lenguajes de programación para definir su sintaxis.
  - Generan estructuras jerárquicas como árboles de derivación.

### Tipo 3: Gramáticas regulares
- Lenguaje: Lenguajes regulares.
- Automatón: Autómata finito determinista o no determinista.
- Reglas de producción: De la forma:
  - Lineales por la derecha:  A → aB  o  A → a .
  - Lineales por la izquierda:  A → Ba  o  A → a .
- Características:
  - Son los lenguajes más simples dentro de la jerarquía.
  - Se pueden representar mediante expresiones regulares.
  - Adecuados para modelar sistemas con memoria limitada.

## Relación Jerárquica

La relación entre los niveles se puede visualizar como una inclusión jerárquica:

 
 {Lenguajes Regulares} ⊆ 
 {Lenguajes Libres de Contexto} ⊆ 
 {Lenguajes Sensibles al Contexto} ⊆ 
 {Lenguajes Recursivamente Enumerables}
  
Esto significa que cada nivel incluye a los lenguajes del nivel inferior, pero no necesariamente al revés. Por ejemplo, todos los lenguajes regulares son libres de contexto, pero no todos los lenguajes libres de contexto son regulares.

## Aplicaciones
La Jerarquía de Chomsky tiene aplicaciones fundamentales en:
1. Diseño e implementación de compiladores (análisis léxico y sintáctico).
2. Procesamiento del lenguaje natural (modelado lingüístico).
3. Teoría de autómatas y computabilidad (modelado matemático).

## Resumen en Tabla

| Tipo | Nombre                      | Lenguaje                   | Automátas                   | Reglas de Producción                |
|------|-----------------------------|----------------------------|-----------------------------|-------------------------------------|
| 0    | Sin restricciones           | Recursivamente enumerables | Máquina de Turing           | Ninguna restricción                |
| 1    | Sensibles al contexto       | Sensibles al contexto      | Autómata linealmente acotado|  |Γ| ≥ |α|         |
| 2    | Libres de contexto          | Libres de contexto         | Autómata con pila           |  A → Γ                  |
| 3    | Regulares                   | Regulares                  | Autómata finito             | Lineales por derecha o izquierda   |

La Jerarquía de Chomsky sigue siendo una herramienta esencial para comprender y clasificar los lenguajes formales, así como para analizar su complejidad computacional.
