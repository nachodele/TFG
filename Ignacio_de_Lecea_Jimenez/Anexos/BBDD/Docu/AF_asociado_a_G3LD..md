# Autómata Finito Asociado a una Gramática Lineal por la Derecha (G3LD)

Una gramática lineal por la derecha (G3LD) es un tipo de gramática regular cuyas producciones tienen la forma:
-  A  → aB   
-  A  → a   
donde  A, B  son no terminales y  a  es un símbolo terminal. Estas gramáticas generan exactamente los lenguajes regulares, por lo que existe un autómata finito capaz de reconocer el mismo lenguaje producido por la gramática.

---

## Construcción de un Autómata Finito a partir de una G3LD

Para asociar un autómata finito (puede ser determinista o no determinista) a una gramática lineal por la derecha, se sigue un procedimiento estándar:

1. Crear un estado para cada no terminal  
   - Cada símbolo no terminal de la gramática se representa como un estado en el autómata.
   - El *símbolo inicial*  S  de la gramática será el *estado inicial* en el autómata.

2. Añadir transiciones para cada producción  
   - Para cada regla de la forma  A  → aB :  
     Se inserta una transición desde el estado correspondiente a  A  hacia el estado correspondiente a  B  con la etiqueta  a .  
   - Para cada regla de la forma  A  → a :  
     Se inserta una transición desde el estado correspondiente a  A  hacia un estado *final* con la etiqueta  a .

3. Definir los estados finales  
   - Cualquier no terminal cuya producción derive directamente en un símbolo terminal puede asociarse a una transición a un *estado final* único.  
   - Alternativamente, se crea un estado final de “salida” al que llegan las transiciones que consumen el último símbolo terminal.

4. Gestionar producciones con cadena vacía (ε)  
   - Si la gramática permite la derivación de la cadena vacía (ε) y el no terminal que la genera es  S , se marcará el estado inicial como final.  
   - Si se generan vacíos desde no terminales distintos de  S , suele ser necesario un ajuste adicional (como crear transiciones ε o eliminar esas reglas según la equivalencia que se desee).

---

## Ejemplo

Sea la gramática de tipo 3 lineal por la derecha:
 
G = (S, A, 0, 1, P, S)
  con las producciones:
1.  S  → 0S 
2.  S  → 1A 
3.  S  → 1 
4.  A  → 0A 
5.  A  → 1 

Paso 1: Estados

- Estados: S, A  
- Estado inicial: S.  

Paso 2: Transiciones

- De la regla S  → 0S:  
  Transición etiquetada con “0” desde S hacia S.
- De la regla S  → 1A:  
  Transición etiquetada con “1” desde S hacia A.
- De la regla S  → 1:  
  Transición etiquetada con “1” desde S hacia un estado final, llámese F.
- De la regla A  → 0A:  
  Transición etiquetada con “0” desde A hacia A.
- De la regla A  → 1:  
  Transición etiquetada con “1” desde A hacia el estado final F.

Paso 3: Estado Final

- Creamos un estado F y lo marcamos como final.
- Agregamos las transiciones de tipo  A  → a  o  S  → a  apuntando hacia F.

El autómata resultante (en una versión no determinista para simplificar) puede representarse así:

| Estado | 0         | 1         |
|------------|---------------|---------------|
| →S         | S             | A, F (dos transiciones posibles: una a A y otra a F si se quisiera ver en modo no determinista, pero regularmente se partiría en una sola producción) |
| A          | A             | F             |
| *F         | -             | -             |

Donde:
- →S indica que S es el estado inicial.
- *F indica que F es el estado final.

> Nótese que, en una implementación determinista, la regla S  → 1 suele manejarse con un estado adicional si se desea evitar la no determinación. El enfoque exacto depende de si se prefiere un AFND o un AFD.

---

## Observaciones

1. Equivalencia: El autómata finito obtenido reconoce exactamente el mismo lenguaje que la gramática lineal por la derecha.  
2. Determinismo: En general, el método produce un *autómata finito no determinista* (AFND), que posteriormente se puede convertir en un AFD mediante el algoritmo del subconjunto (conjunto potencia).  
3. Gramáticas con ε: Si la gramática puede generar la cadena vacía (ε), se debe marcar el estado inicial como final o manipular las reglas para reflejar este caso, según la construcción deseada.  

---

## Conclusión

Dada una gramática lineal por la derecha (G3LD), se puede construir un autómata finito que genere el mismo lenguaje a través de un proceso de asociación de estados a los no terminales y la creación de transiciones basadas en las producciones. Esta construcción muestra la equivalencia fundamental entre las gramáticas regulares y los autómatas finitos.  
