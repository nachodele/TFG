# Recursividad

La recursividad es un concepto fundamental en matemáticas, ciencias de la computación y teoría de lenguajes formales. Se refiere a la definición de un objeto, función o proceso en términos de sí mismo. En el contexto de gramáticas y lenguajes formales, la recursividad se utiliza para describir estructuras repetitivas y jerárquicas, como las cadenas generadas por una gramática o las funciones computables.

---

## Definición General

Un proceso o definición es recursivo si cumple con las siguientes características:
1. Caso Base: Especifica los objetos iniciales o condiciones que pertenecen al conjunto definido.
2. Regla Recursiva: Define cómo construir nuevos objetos a partir de los ya existentes.
3. Condición de Exhaustividad: Declara que ningún otro objeto fuera de los definidos por el caso base y las reglas recursivas pertenece al conjunto.

Ejemplo:
- Definición recursiva del conjunto de números pares (  {EVEN} ):
  1.  2 ∈  {EVEN}  (caso base).
  2. Si  x ∈  {EVEN} , entonces  x + 2 ∈  {EVEN}  (regla recursiva).
  3. Ningún otro número pertenece a   {EVEN}  (condición de exhaustividad).

---

## Recursividad en Gramáticas

En gramáticas formales, la recursividad ocurre cuando un símbolo no terminal aparece en el lado derecho de una producción que lo define. Esto permite generar estructuras repetitivas y cadenas infinitamente largas.

### Tipos de Recursividad

1. Recursividad por la Izquierda:
   - Ocurre cuando un símbolo no terminal aparece al inicio del lado derecho de una producción.
   - Ejemplo:
      
     A  → Aα;|; β
            Donde  A  es un símbolo no terminal,  α  es una cadena (posiblemente vacía) y  β  es una cadena que no comienza con  A .

   - Problema: La recursividad por la izquierda puede causar bucles infinitos en algoritmos como el análisis sintáctico por descenso recursivo.

2. Recursividad por la Derecha:
   - Ocurre cuando un símbolo no terminal aparece al final del lado derecho de una producción.
   - Ejemplo:
      
     A  → α A ;|; β
       
   - No presenta problemas para los analizadores sintácticos, pero puede ser menos eficiente en algunos casos.

---

## Eliminación de la Recursividad por la Izquierda

La recursividad por la izquierda puede eliminarse mediante transformaciones gramaticales que reestructuran las producciones sin alterar el lenguaje generado.

### Algoritmo General
Dada una producción con recursividad por la izquierda:
 
A  → Aα_1 | Aα_2 | ... | Aα_n | β_1 | β_2 | ... | β_m
  Donde  Aα_i  son producciones recursivas y  β_j  son producciones no recursivas:

1. Introducir un nuevo símbolo no terminal  A' .
2. Reemplazar las producciones originales por:
   -  A → β_1A' | β_2A' | ... | β_mA' 
   -  A' → α_1A' | α_2A' | ... | α_nA' | ε 

### Ejemplo
Gramática original:
 
E → E + T | T
  Eliminamos la recursividad por la izquierda:
1. Introducimos un nuevo símbolo  E' .
2. Reescribimos las producciones:
   -  E → T E' 
   -  E' → + T E' | ε 

---

## Recursividad en Funciones

En programación, una función es recursiva si se llama a sí misma directa o indirectamente durante su ejecución.

### Componentes de una Función Recursiva
1. Caso Base: Detiene la recursión cuando se cumple cierta condición.
2. Llamada Recursiva: La función se invoca a sí misma con parámetros modificados.

Ejemplo:
- Factorial ( n! = n × (n-1)! ):
def factorial(n):
if n == 0: # Caso base
return 1
else:
return n * factorial(n-1) # Llamada recursiva

---

## Recursión en Lenguajes Formales

En lenguajes formales, la recursión permite describir lenguajes infinitos mediante gramáticas finitas.

### Ejemplo: Lenguaje Palíndromo
El lenguaje de los palíndromos sobre el alfabeto  0, 1 :
 
L = ε, 0, 1, 00, 11, 010, 101, ...
  Puede definirse mediante una gramática recursiva:
- Caso base:  S → ε | 0 | 1 
- Regla recursiva:  S → 0S0 | 1S1 

---

## Importancia de la Recursividad

La recursividad es clave para modelar estructuras complejas y repetitivas en diversas áreas:
1. Gramáticas Formales:
 - Permite definir lenguajes infinitos con reglas finitas.
 - Es esencial para describir estructuras jerárquicas como expresiones matemáticas o sentencias en lenguajes de programación.
2. Programación:
 - Simplifica problemas complejos dividiéndolos en subproblemas más pequeños.
3. Teoría Computacional:
 - Relaciona funciones computables con máquinas abstractas como las máquinas de Turing.

---

## Conclusión

La recursividad es un concepto poderoso que se aplica tanto en gramáticas como en funciones computacionales para manejar estructuras repetitivas e infinitas. Aunque puede presentar desafíos como bucles infinitos o ineficiencia, su correcta utilización permite resolver problemas complejos con elegancia y claridad.
