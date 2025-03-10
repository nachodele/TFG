# Teoría de la Computabilidad

La **teoría de la computabilidad** es una rama de la informática teórica y la lógica matemática que estudia los límites y capacidades de los sistemas computacionales. Su objetivo principal es determinar qué problemas pueden resolverse mediante algoritmos y cuáles no, estableciendo así los fundamentos para entender la naturaleza de los problemas computacionales y sus restricciones.

---

## **1. Introducción a la Computabilidad**

### **1.1. Orígenes Históricos**
La computabilidad comenzó a desarrollarse en las décadas de 1930 y 1940, con contribuciones fundamentales de matemáticos y lógicos como:

- **Kurt Gödel (1931):** Con su teorema de incompletitud, demostró que existen proposiciones matemáticas indecidibles dentro de cualquier sistema axiomático consistente.
- **Alan Turing (1936):** Introdujo el concepto de Máquina de Turing como un modelo abstracto para formalizar el concepto de algoritmo. También demostró que existen problemas irresolubles, como el *Problema de Parada*.
- **Alonzo Church (1936):** Propuso el cálculo lambda como un formalismo equivalente a las Máquinas de Turing para definir funciones computables.

### **1.2. Conceptos Fundamentales**
- Un problema es **computable** si existe un algoritmo que lo resuelve en un número finito de pasos.
- Un problema es **indecidible** si no existe ningún algoritmo que pueda determinar una solución para todas las instancias posibles.

La computabilidad se basa en modelos matemáticos abstractos que formalizan el concepto de algoritmo, siendo la Máquina de Turing el modelo más influyente.

---

## **2. Modelos Matemáticos en Computabilidad**

### **2.1. Máquinas de Turing**
La Máquina de Turing (MT) es un modelo teórico que define una computadora idealizada capaz de realizar cálculos algorítmicos. Es universalmente aceptada como el estándar para medir la computabilidad.

#### **Definición Formal**
Una Máquina de Turing se define como una 7-tupla:
$$
M = (Q, \Sigma, \Gamma, q_0, \delta, F)
$$

Donde:
- $$Q$$: Conjunto finito de estados.
- $$\Sigma$$: Alfabeto de entrada.
- $$\Gamma$$: Alfabeto de cinta ($$\Sigma \subseteq \Gamma$$).
- $$q_0$$: Estado inicial ($$q_0 \in Q$$).
- $$\delta$$: Función de transición ($$Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$$).
- $$F$$: Conjunto de estados finales ($$F \subseteq Q$$).

#### **Funcionamiento**
1. La máquina lee un símbolo en la cinta.
2. Según su estado actual y el símbolo leído, realiza tres acciones:
   - Escribe un nuevo símbolo en la cinta.
   - Cambia su estado.
   - Mueve su cabeza lectora/escritora hacia la izquierda o derecha.

#### **Tipos Especiales**
- **Deterministas:** Cada configuración tiene una única transición definida.
- **No deterministas:** Pueden tener múltiples transiciones posibles desde una misma configuración.
- **Máquinas Universales:** Simulan cualquier otra Máquina de Turing; son base teórica para los computadores modernos.

### **2.2. Otros Modelos Computacionales**
Además de las Máquinas de Turing, existen otros formalismos equivalentes:
- **Funciones Recursivas:** Basadas en operaciones primitivas como composición y recursión.
- **Cálculo Lambda:** Formalismo desarrollado por Alonzo Church para representar funciones computables.
- **Autómatas Finitos y Autómatas con Pila:** Modelos más restringidos que reconocen lenguajes regulares y libres del contexto, respectivamente.

---

## **3. Lenguajes y Clasificación**

### **3.1. Jerarquía de Chomsky**
Los lenguajes formales se clasifican según su complejidad y los autómatas necesarios para reconocerlos:

| Tipo | Lenguaje                  | Máquina Asociada           |
|------|---------------------------|----------------------------|
| 0    | Recursivamente Enumerables | Máquina de Turing          |
| 1    | Sensibles al Contexto      | Autómata Linealmente Acotado |
| 2    | Libres del Contexto        | Autómata con Pila          |
| 3    | Regulares                  | Autómata Finito            |

### **3.2. Lenguajes Recursivos vs Recursivamente Enumerables**
1. **Lenguajes Recursivos (REC):**
   - Son aceptados por Máquinas de Turing que siempre terminan.
   - Cerrados bajo unión, intersección y complementación.
2. **Lenguajes Recursivamente Enumerables (RE):**
   - Son aceptados por Máquinas de Turing que pueden no detenerse para ciertas entradas.
   - Cerrados bajo unión e intersección, pero no bajo complementación.

---

## **4. Problemas Irresolubles**

### **4.1. Problema del Parada**
El problema más conocido en computabilidad:
- Enunciado: Dada una Máquina de Turing $$M$$ y una entrada $$w$$, ¿terminará $$M(w)$$?
- Resultado: Es indecidible; no existe un algoritmo general que lo resuelva.

### **4.2. Problema de Correspondencia de Post**
Consiste en determinar si existe una secuencia válida que iguale dos conjuntos dados mediante fichas o cadenas:
- Resultado: También es irresoluble.

---

## **5. La Tesis Church-Turing**

La tesis Church-Turing establece que cualquier función efectivamente calculable puede ser computada por una Máquina de Turing o equivalente (como funciones recursivas o cálculo lambda). Aunque no es demostrable formalmente debido a su naturaleza intuitiva, está ampliamente aceptada debido a su consistencia con todos los modelos conocidos.

#### Implicaciones:
1. La equivalencia entre diferentes modelos computacionales asegura que todos tienen el mismo poder expresivo.
2. Si un problema no puede resolverse por una Máquina de Turing, tampoco puede resolverse mediante ningún otro modelo razonable.

---

## **6. Extensiones y Modificaciones a las Máquinas de Turing**

Para abordar problemas específicos o explorar nuevas capacidades computacionales, se han desarrollado variantes del modelo básico:
1. Máquinas con múltiples cintas o pistas.
2. Máquinas con cintas infinitas hacia un solo lado (semi-infinitas).
3. Máquinas no deterministas (más útiles para análisis teóricos).

Aunque estas variantes pueden simplificar ciertas tareas, no aumentan el poder computacional general del modelo original.

---

## **7. Aplicaciones Prácticas**

La teoría de la computabilidad tiene aplicaciones fundamentales en diversas áreas:
1. Diseño Teórico del Software: Análisis formal del comportamiento del software mediante autómatas y lenguajes formales.
2. Compiladores: Traducción eficiente entre lenguajes mediante autómatas finitos y gramáticas formales.
3. Criptografía: Uso del concepto de indecibilidad para garantizar seguridad matemática.
4. Inteligencia Artificial: Modelado abstracto del razonamiento lógico mediante funciones recursivas.

---

## **8. Conclusión**

La teoría de la computabilidad define los límites teóricos del cálculo y establece las bases para disciplinas prácticas como la programación y el diseño algorítmico. Su relevancia trasciende lo académico al influir directamente en cómo entendemos las capacidades y limitaciones inherentes a las máquinas modernas.
