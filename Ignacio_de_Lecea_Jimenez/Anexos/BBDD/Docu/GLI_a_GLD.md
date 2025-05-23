# Algoritmo: Conversión de una Gramática Lineal por la Izquierda (GLI) a Gramática Lineal por la Derecha (GLD)

## Enunciado
Algoritmo para transformar una Gramática Lineal por la Izquierda (GLI) en una Gramática Lineal por la Derecha (GLD), centrándose en el proceso de eliminación del "axioma inducido".

## Paso 1: Invertir producciones lineales
- Regla general:  
  Para cada producción de la forma `A → Ba` (típica de GLI), invierta el orden:  
  `A → aB`.  
  - Ejemplo:  
    - GLI: `B → Ab` → GLD: `B → bA`.  
- Producciones terminales:  
  Las reglas `A → a` se mantienen igual.  

---

## Paso 2: Manejar el axioma inducido
Si el símbolo inicial `S` aparece en el lado derecho de alguna producción:  
1. Cree un nuevo no terminal `S'`.  
2. Duplique todas las producciones de `S` en `S'`.  
3. Reemplace `S` por `S'` en las producciones donde aparezca en el lado derecho.  

---

## Paso 3: Construir un autómata intermedio
1. Convertir GLI a AFND:  
   - Cada no terminal `A` es un estado.  
   - Para `A → Ba`, agregue una transición `δ(B, a) = A`.  
   - Para `A → a`, agregue `δ(A, a) = q_f` (estado final).  
2. Invertir el autómata:  
   - Intercambie el estado inicial y los finales.  
   - Invierta todas las transiciones.  

---

## Paso 4: Convertir el autómata invertido a GLD
- Traducción de transiciones:  
  - `δ(A, a) = B` → `A → aB`.  
  - `δ(A, a) = q_f` → `A → a`.  

---

## Paso 5: Ajustar producciones terminales
- Asegurar que:  
  - Las reglas `A → a` sean válidas.  
  - Si la GLI original tenía `S → λ`, mantenerla en la GLD.  

---

## Ejemplo de conversión
GLI original:  
1. `S → Sa | b | λ`  
2. `A → Sa | b`  
3. `B → Ab | a`  

GLD equivalente:  
1. `S → aS | b | λ`  
2. `A → aS | b`  
3. `B → bA | a`  

---

## Verificación de equivalencia
1. Construir AFD para la GLI original.  
2. Invertir el AFD y convertirlo en GLD.  
3. Comparar lenguajes mediante derivaciones de cadenas clave (ej: `aab`, `bab`).  

Conclusión:  
La GLD resultante genera el mismo lenguaje regular que la GLI original.  
