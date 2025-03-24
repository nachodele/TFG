# Complejidad Computacional

La **complejidad computacional** es una rama fundamental de la informática teórica que estudia los recursos necesarios para resolver problemas computacionales. Estos recursos, principalmente **tiempo** y **espacio**, se miden en función del tamaño de la entrada del problema. La teoría de la complejidad computacional clasifica los problemas según su dificultad inherente y establece límites sobre qué problemas son resolubles en un tiempo razonable.

## Conceptos Fundamentales

### **Complejidad de Tiempo**
La complejidad de tiempo mide el número de pasos que un algoritmo necesita para completar su tarea. Se expresa mediante notaciones como O(f(n)), donde f(n) describe cómo crece el tiempo de ejecución en función del tamaño n de la entrada.

- **O(1)**: Tiempo constante, no depende del tamaño de la entrada.
- **O(n)**: Tiempo lineal, el tiempo crece proporcionalmente al tamaño de la entrada.
- **O(n^2)**: Tiempo cuadrático, el tiempo crece exponencialmente con el tamaño de la entrada.
- **O(\log n)**: Tiempo logarítmico, el tiempo crece lentamente al aumentar la entrada.

Ejemplo: En una búsqueda lineal, la complejidad es O(n), ya que se revisa cada elemento. En cambio, una búsqueda binaria en una lista ordenada tiene una complejidad O(\log n), siendo mucho más eficiente.

### **Complejidad de Espacio**
La complejidad de espacio mide cuánta memoria necesita un algoritmo durante su ejecución. También se expresa mediante notaciones como O(f(n)).

- **O(1)**: Uso constante de memoria.
- **O(n)**: Uso lineal de memoria respecto al tamaño de la entrada.

Ejemplo: Un algoritmo que almacena temporalmente todos los elementos procesados tendrá una complejidad espacial O(n).

## Clases de Complejidad

### **Clase P**
- Contiene problemas que pueden resolverse en tiempo polinómico (O(n^k)) por una máquina determinista.
- Representa los problemas "fáciles" o tratables computacionalmente.

### **Clase NP**
- Incluye problemas cuya solución puede verificarse en tiempo polinómico por una máquina determinista.
- Ejemplo: Resolver un sudoku (verificar si una solución es válida es rápido, pero encontrarla puede ser costoso).

### **Problemas NP-Completos**
- Son problemas en NP para los cuales cualquier otro problema en NP puede reducirse a ellos en tiempo polinómico.
- Ejemplo: El problema del viajante (TSP) o el problema de satisfacibilidad booleana (SAT).

### **Clase EXP**
- Problemas que requieren tiempo exponencial (O(2^n)) para resolverse.
- Representa problemas intratables debido al crecimiento exponencial del tiempo requerido.

## Relación entre Clases

Las clases P y NP tienen una relación jerárquica:

 
P ⊆ NP
  
Sin embargo, no está probado si P = NP. Este es uno de los problemas más importantes en la teoría de la complejidad computacional y forma parte de los "Problemas del Milenio".

## Notación O Grande

La notación O grande (O(f(n))) se utiliza para describir el peor caso del rendimiento de un algoritmo. Algunas otras notaciones relacionadas son:

- Ω(f(n)): Representa el mejor caso.
- Θ(f(n)): Representa el caso promedio.

Ejemplo:
Un algoritmo de ordenamiento por burbuja tiene:
- Complejidad temporal O(n^2) en el peor caso.
- Complejidad espacial O(1), ya que no requiere memoria adicional significativa.

## Problemas Indecidibles

Existen problemas que no pueden resolverse algorítmicamente, independientemente del tiempo o espacio disponible. Ejemplo clásico:
- **El problema de parada**: Determinar si un programa dado terminará o entrará en un bucle infinito.

Estos problemas destacan los límites inherentes a lo que puede lograrse con algoritmos computacionales.

## Aplicaciones Prácticas

La complejidad computacional tiene aplicaciones clave en:
1. **Optimización de algoritmos**: Elegir algoritmos eficientes para grandes volúmenes de datos.
2. **Criptografía**: Basada en problemas difíciles como factorización (NP).
3. **Inteligencia artificial**: Resolver problemas complejos como planificación o aprendizaje automático.
4. **Compiladores**: Analizar cadenas y optimizar código fuente.

## Conclusión

La teoría de la complejidad computacional no solo clasifica problemas según su dificultad, sino que también define los límites prácticos e inherentes a lo que puede calcularse. Es crucial para diseñar algoritmos eficientes y comprender las capacidades y limitaciones fundamentales de las computadoras.
