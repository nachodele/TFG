# Gramáticas Tipo 1 (Sensibles al Contexto)

Las **gramáticas tipo 1**, también conocidas como **gramáticas sensibles al contexto**, son un tipo de gramática formal dentro de la **Jerarquía de Chomsky**. Estas gramáticas generan los **lenguajes sensibles al contexto**, que son más generales que los lenguajes libres de contexto pero más restringidos que los lenguajes recursivamente enumerables.

---

## Definición Formal

Una gramática tipo 1 se define como una cuádrupla:
 
G = (N, T, P, S)
  Donde:
-  N : Conjunto finito de **símbolos no terminales** (variables).
-  T : Conjunto finito de **símbolos terminales**, con  N ∩ T = ∅ .
-  S : **Símbolo inicial**, con  S ∈ N .
-  P : Conjunto finito de **reglas de producción** de la forma:
   
  Γ_1 A Γ_2  → Γ_1 ω Γ_2
      Donde:
  -  A ∈ N  es un símbolo no terminal.
  -  Γ_1, Γ_2, ω ∈ (N ∪ T)^*  son cadenas de símbolos terminales y/o no terminales.
  -  |Γ_1 A Γ_2| ≤ |Γ_1 ω Γ_2| , es decir, la longitud del lado derecho debe ser mayor o igual a la del lado izquierdo.

### Restricciones Específicas
- No se permite la **palabra vacía** ( ε ) en el lado derecho de las producciones, excepto en casos especiales como la regla inicial cuando el lenguaje incluye  ε .
- Las reglas dependen del contexto en el que aparece el símbolo no terminal ( A ).

---

## Lenguajes Generados

El conjunto de lenguajes generados por las gramáticas tipo 1 se denomina **lenguajes sensibles al contexto**. Estos lenguajes tienen las siguientes características:
1. **Reconocibles por Autómatas Linealmente Acotados (ALA)**:
   - Un ALA es una máquina de Turing con una cinta limitada en tamaño por la longitud de la entrada.
2. **Mayor Potencia que los Lenguajes Libres de Contexto**:
   - Incluyen lenguajes que no pueden ser generados por gramáticas libres de contexto.

Ejemplo: El lenguaje  L = a^n b^n c^n : n ≥ 1  es sensible al contexto pero no libre de contexto.

---

## Ejemplo de Gramática Tipo 1

Consideremos el lenguaje:
 
L = a^n b^n c^n : n ≥ 1
  
Una gramática tipo 1 que genera este lenguaje es:
 
G = (N, T, P, S)
  Donde:
-  N = S, A, B, C ,
-  T = a, b, c ,
-  S = S ,
- Reglas de producción ( P ):
  1.  S → aSBC 
  2.  S → ABC 
  3.  CB → BC 
  4.  aB → ab 
  5.  bC → bc 

### Derivación
Para generar la cadena  aabbcc :
1. Aplicamos  S → aSBC :  S ⇒ aSBC ⇒ aaSBCCB ⇒ aaABCCB ⇒ aabCCB ⇒ aabbCB ⇒ aabbBC ⇒ aabbcc. 

El lenguaje generado por esta gramática es:
 
L(G) = L = a^n b^n c^n : n ≥ 1.
  
---

## Relación con la Jerarquía de Chomsky

Las gramáticas tipo 1 ocupan el segundo nivel en la Jerarquía de Chomsky y están relacionadas con otros tipos de gramáticas según su potencia:

| **Tipo** | **Restricciones en las Producciones**       | **Lenguaje Generado**            | **Máquina Reconocedora**      |
|----------|--------------------------------------------|-----------------------------------|--------------------------------|
| Tipo 0   | Sin restricciones                          | Lenguajes recursivamente enumerables | Máquina de Turing             |
| Tipo 1   | Sensibles al contexto ( |α| ≤ |β| ) | Lenguajes sensibles al contexto   | Autómata linealmente acotado   |
| Tipo 2   | Libres de contexto ( A → w)            | Lenguajes libres de contexto      | Autómata de pila               |
| Tipo 3   | Regulares ( A → aB o  A → a)       | Lenguajes regulares               | Autómata finito                |

---

## Propiedades Fundamentales

### Ventajas
1. **Mayor Expresividad**:
   - Permiten describir lenguajes que dependen del contexto, como aquellos donde las relaciones entre símbolos están condicionadas por su entorno.
2. **Reconocimiento Computacional**:
   - Los lenguajes sensibles al contexto pueden ser reconocidos por autómatas linealmente acotados.

### Limitaciones
1. **Complejidad Computacional**:
   - Los lenguajes sensibles al contexto son más difíciles de analizar y procesar que los libres de contexto.
2. **Imposibilidad del Uso del Vacío**:
   - No permiten producciones con el símbolo vacío ( ε ), salvo para casos especiales.

---

## Importancia y Aplicaciones

Las gramáticas tipo 1 son útiles en áreas donde las relaciones contextuales entre símbolos son importantes:

1. **Lenguajes Naturales**:
   - Algunos aspectos del lenguaje humano requieren dependencias contextuales que pueden modelarse mediante gramáticas sensibles al contexto.
   
2. **Compiladores y Analizadores Sintácticos**:
   - Aunque los lenguajes de programación suelen modelarse con gramáticas libres de contexto, ciertas estructuras complejas pueden requerir sensibilidades contextuales.

3. **Teoría Computacional**:
   - Ayudan a entender los límites entre lo computable y lo decidible dentro del marco formal.

---

En resumen, las gramáticas tipo 1 proporcionan un modelo intermedio entre las gramáticas libres de contexto y las sin restricciones, permitiendo describir lenguajes más complejos mientras mantienen ciertas restricciones estructurales para facilitar su análisis.
