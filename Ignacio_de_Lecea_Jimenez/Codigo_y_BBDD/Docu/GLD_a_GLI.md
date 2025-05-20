# Algoritmo: Conversión de una Gramática Lineal por la Derecha (GLD) a Gramática Lineal por la Izquierda (GLI)

## Enunciado
Algoritmo para transformar una Gramática Lineal por la Derecha (GLD) en una Gramática Lineal por la Izquierda (GLI), centrándose en el proceso de eliminación del "axioma inducido".

## Solución

### Paso 1: Definición de la gramática

Sea G = (Σ_N, Σ_T, S, P) una gramática donde:
- Σ_N: conjunto de símbolos no terminales
- Σ_T: conjunto de símbolos terminales
- S: símbolo inicial (axioma)
- P: conjunto de producciones

### Paso 2: Eliminar "axioma inducido"

El "axioma inducido" es cualquier aparición del axioma S en la parte derecha de alguna producción. Para eliminarlo:

#### 2.1 Crear nuevo no terminal
- ∀p∈P que contenga el axioma inducido:
- Crear un nuevo no terminal S'
- Actualizar el conjunto de no terminales: Σ_N = Σ_N ∪ {S'}

#### 2.2 Duplicar producciones del axioma
- ∀p∈P: S → α
- Crear nueva producción p' = S' → α
- Actualizar el conjunto de producciones: P = P ∪ {p'}

#### 2.3 Reemplazar apariciones del axioma
- ∀p∈P: A → αSβ
- Transformar la producción a p': A → αS'β
- Actualizar el conjunto de producciones: P = P ∪ {p'} ∖ {p}

### Paso 3: Crear grafo dirigido G

#### 3.1 Crear nodos
- ∀A∈Σ_N: Crear un nodo A

#### 3.2 Crear arcos para producciones lineales
- ∀p∈P: A → aB : Crear un arco desde A hasta B etiquetado con a

#### 3.3 Crear arcos para producciones terminales
- ∀p∈P: A → a : Crear un arco desde A hasta λ etiquetado con a

#### 3.4 Tratar producciones vacías
- Si existe la regla: S → λ
  - Crear un arco sin etiqueta desde S hasta λ

### Paso 4: Crear grafo dirigido G' a partir de G

#### 4.1 Intercambiar nodos especiales
- Intercambiar nombres a los nodos S y λ

#### 4.2 Invertir arcos
- Invertir el sentido de todos los arcos

### Paso 5: Construir conjunto de reglas para GLI

#### 5.1 Definir símbolos no terminales
- ∀ nodo A (excepto λ): Crear A∈Σ_N

#### 5.2 Crear producciones lineales por la izquierda
- ∀ arco desde A hasta B etiquetado con a: Crear p: A → Ba

#### 5.3 Tratar producciones vacías
- Si existe arco desde S hasta λ: Crear p: S → λ

### Paso 6: Verificación

Comprobar que la nueva gramática G' = (Σ_N', Σ_T, S, P') es una GLI que genera el mismo lenguaje que la GLD original:

- Verificar que todas las producciones son de la forma A → Ba o A → a (forma lineal por la izquierda)
- Comprobar que cada cadena w derivable en G también es derivable en G'
- Asegurar que no se han introducido derivaciones nuevas no existentes en la gramática original
- Confirmar que se preserva la propiedad de generación de la cadena vacía, si existía en la GLD original
- Verificar la equivalencia mediante la construcción de autómatas finitos para ambas gramáticas

