# Problemas Irresolubles: Problema de Parada y Problema de Correspondencia de Post

En la teoría de la computación, los problemas irresolubles representan límites fundamentales del cálculo algorítmico. Estos problemas no pueden ser resueltos por ningún algoritmo o máquina de Turing, independientemente de los recursos disponibles. Dos ejemplos clásicos son el Problema de Parada y el Problema de Correspondencia de Post, ambos cruciales para entender la indecidibilidad y los límites de la computación.

---

## 1. Problema de Parada

### Definición
El Problema de Parada consiste en determinar si una Máquina de Turing  M , dada una entrada  w , se detendrá después de un número finito de pasos o continuará ejecutándose indefinidamente.

Formalmente, el problema puede expresarse como:
 
 {Dado } M  { (una Máquina de Turing) y } w  { (una entrada), decidir si } M(w)  { termina.}
  
### Indecidibilidad
Alan Turing demostró en 1936 que el Problema de Parada es indecidible, es decir, no existe una Máquina de Turing que pueda resolver este problema para todas las posibles combinaciones de  M  y  w .

#### Demostración por contradicción
1. Supongamos que existe una Máquina de Turing  H  que resuelve el Problema de Parada. Esta máquina toma como entrada  (M, w)  y:
   - Devuelve "sí" si  M(w)  se detiene.
   - Devuelve "no" si  M(w)  no se detiene.

2. Construyamos una nueva Máquina de Turing  D  que utiliza  H  como subrutina:
   - Si  H(M, M) =  {"sí"} , entonces  D(M)  entra en un bucle infinito.
   - Si  H(M, M) =  {"no"} , entonces  D(M)  se detiene.

3. Ahora evaluemos el comportamiento de  D(D) :
   - Si  H(D, D) =  {"sí"} , entonces  D(D)  entra en un bucle infinito, lo cual es contradictorio.
   - Si  H(D, D) =  {"no"} , entonces  D(D)  se detiene, lo cual también es contradictorio.

Por lo tanto, la existencia de  H  lleva a una contradicción lógica, demostrando que el Problema de Parada es indecidible.

### Implicaciones
- El Problema de Parada establece límites fundamentales para la computación: no es posible predecir con certeza si un programa terminará o no.
- Este resultado tiene aplicaciones prácticas, como en la detección automática de bucles infinitos en programas.

---

## 2. Problema de Correspondencia de Post

### Definición
El Problema de Correspondencia de Post (PCP) fue propuesto por Emil Post y se define como sigue:

Dado un alfabeto finito y dos conjuntos finitos de cadenas sobre dicho alfabeto:
 
A = u_1, u_2, ..., u_k,      B = v_1, v_2, ..., v_k,
  ¿existe una secuencia finita de índices  i_1, i_2, ..., i_n , con  1 ≤ i_j ≤ k , tal que las cadenas concatenadas sean iguales?
 
u_{i_1} u_{i_2} ... u_{i_n} = v_{i_1} v_{i_2} ... v_{i_n}.
  
### Indecidibilidad
El PCP es un problema indecidible; no existe un algoritmo general que pueda determinar si existe o no una solución para cualquier instancia arbitraria del problema.

#### Relación con el Problema de Parada
La indecidibilidad del PCP puede demostrarse mediante *reducción* desde el Problema de Parada:
- Si existiera un algoritmo para resolver el PCP, también podría usarse para resolver el Problema de Parada.
- Sin embargo, dado que el Problema de Parada es indecidible, esto implica que el PCP también lo es.

### Ejemplo
Supongamos:
 
A = u_1 = "a", u_2 = "ab",      B = v_1 = "aa", v_2 = "b".
  Buscamos una secuencia tal que las cadenas concatenadas sean iguales:
 
u_{i_1} u_{i_2} ... u_{i_n} = v_{i_1} v_{i_2} ... v_{i_n}.
  En este caso:
- Si elegimos la secuencia  i_1 = 1, i_2 = 2, i_3 = 2 :
  - Concatenando:  u_1 u_2 u_2 = "aababb" .
  - Concatenando:  v_1 v_2 v_2 = "aababb" .
  - Ambas cadenas son iguales; por lo tanto, esta es una solución.

Sin embargo, no existe un algoritmo general para determinar si tal secuencia existe en todos los casos posibles.

---

## Comparación entre los Problemas

| Aspecto                        | Problema de Parada                          | Problema de Correspondencia de Post         |
|--------------------------------|---------------------------------------------|---------------------------------------------|
| Naturaleza                     | Determinar si una máquina se detiene.       | Encontrar correspondencias entre cadenas.   |
| Propuesto por                  | Alan Turing (1936).                         | Emil Post (1946).                           |
| Método común para demostrar    | Contradicción lógica mediante reducción.    | Reducción desde problemas indecidibles.     |
| Resultado                      | Indecidible.                                | Indecidible.                                |
| Relación                       | Base para demostrar otros problemas.        | Reducible al Problema de Parada.            |

---

## Conclusión
Tanto el Problema de Parada como el Problema de Correspondencia de Post son ejemplos fundamentales en la teoría computacional que ilustran los límites del cálculo algorítmico. Estos problemas nos enseñan que hay preguntas dentro del ámbito computacional que ninguna máquina o algoritmo puede responder completamente. La comprensión y estudio de estos problemas son esenciales para delimitar lo que es posible y lo que está fuera del alcance del cómputo.
