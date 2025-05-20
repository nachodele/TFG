# Tablas y Diagramas de Transición

Los tablas y diagramas de transición son representaciones fundamentales para describir el comportamiento de los autómatas finitos. Estas herramientas permiten visualizar y analizar cómo un autómata procesa cadenas de entrada para determinar si pertenecen al lenguaje que reconoce.

---

## Diagramas de Transición

Un diagrama de transición es una representación gráfica del funcionamiento de un autómata finito. Es un grafo dirigido donde:
- Cada nodo representa un estado del autómata.
- Cada arco entre nodos está etiquetado con un símbolo del alfabeto que indica la transición entre estados.
- El estado inicial se señala con una flecha que apunta hacia él.
- Los estados finales se indican con un doble círculo o un asterisco.

### Ejemplo
Consideremos un autómata finito determinista (AFD) que reconoce el lenguaje  L = w : w; termina en 01 . Este AFD tiene:
- Estados:  Q = q_0, q_1, q_2 ,
- Alfabeto:  Σ = 0, 1 ,
- Estado inicial:  q_0 ,
- Estado final:  F = q_2 ,
- Función de transición ( δ ):
  -  δ(q_0, 0) = q_0 , δ(q_0, 1) = q_1 ,
  -  δ(q_1, 0) = q_2 , δ(q_1, 1) = q_1 ,
  -  δ(q_2, 0) = q_0 , δ(q_2, 1) = q_1 .

El diagrama de transición es:

    →q₀ --0--> q₀
    |         |
    1         1
    ↓         ↓
    q₁ --0--> q₂*
    ↑         |
    |         1
    ---------->

---

## Tablas de Transición

Una tabla de transición es una representación tabular que describe la función de transición ( δ ) de un autómata. Cada fila corresponde a un estado y cada columna a un símbolo del alfabeto. Las celdas indican el estado al que se llega desde el estado actual al procesar el símbolo correspondiente.

### Ejemplo
Para el mismo AFD anterior, la tabla de transición sería:

| Estado | 0   | 1   |
|--------|------|------|
| →q₀    | q₀  | q₁  |
| q₁     | q₂  | q₁  |
| *q₂    | q₀  | q₁  |

#### Notación:
-  →q₀ : Estado inicial.
-  *q₂ : Estado final.

---

## Comparación entre Diagramas y Tablas

| Característica            | Diagrama de Transición                | Tabla de Transición                  |
|--------------------------------|------------------------------------------|------------------------------------------|
| Visualización              | Gráfica e intuitiva                      | Tabular y compacta                       |
| Facilidad para grandes autómatas | Difícil de manejar si hay muchos estados o transiciones. | Más adecuada para grandes autómatas.     |
| Uso en algoritmos          | Menos práctica para implementaciones     | Ideal para implementaciones computacionales. |

---

## Aplicaciones

1. Análisis Léxico en Compiladores:
   - Los diagramas y tablas se utilizan para modelar cómo se reconocen tokens en lenguajes de programación.

2. Procesamiento de Texto:
   - Permiten buscar patrones en cadenas mediante expresiones regulares.

3. Sistemas Secuenciales y Controladores Lógicos Programables (PLC):
   - Modelan sistemas con estados definidos y transiciones entre ellos.

4. Diseño Teórico y Simulación:
   - Facilitan la comprensión y simulación del comportamiento de los autómatas.

---

## Relación entre Diagramas y Tablas

Ambas representaciones son equivalentes en términos del lenguaje reconocido por el autómata:
- Un diagrama puede transformarse directamente en una tabla interpretando cada arco como una entrada en la función de transición.
- Una tabla puede convertirse en un diagrama trazando nodos y arcos según las transiciones definidas.

Por ejemplo, dado un AFND con transiciones vacías ( ε ), su tabla puede incluir columnas adicionales para representar las transiciones  ε , mientras que su diagrama incluiría arcos etiquetados como  ε .

---

## Ejemplo Completo: Conversión AFND a AFD

### AFND
Considere el siguiente AFND:

Diagrama:

     →q₀ --ε--> q₁
      |         |
      a         b
      ↓         ↓
      q₂       *q₃

Tabla de Transición:
| Estado | a   | b   | ε      |
|--------|-----|-----|--------|
| →q₀    | ∅   | ∅   | {q₁}  |
| q₁     | {q₂}| {q₃}| ∅      |
| q₂     | ∅   | ∅   | ∅      |
| *q₃    | ∅   | ∅   | ∅      |

### Conversión a AFD
Se construye una tabla para el AFD equivalente utilizando el algoritmo del subconjunto:

Tabla del AFD equivalente:
| Estado       | a       | b       |
|--------------|---------|---------|
| →{q₀}        | {q₂}    | {q₃}    |
| {q₂}         | ∅       | ∅       |
| *{q₃}        | ∅       | ∅       |

Diagrama del AFD equivalente:

     →{q₀} --a--> {q₂}
       |
       b
       ↓
       *{q₃}

---

## Conclusión

Las tablas y diagramas de transición son representaciones complementarias que permiten modelar y analizar el comportamiento de los autómatas finitos. Mientras que los diagramas son ideales para visualizar pequeños autómatas, las tablas son más prácticas para implementar algoritmos computacionales o manejar sistemas complejos.
