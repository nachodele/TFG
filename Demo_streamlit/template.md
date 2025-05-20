# TEMPLATE 1
## Evaluation Instructions:
Step-by-step analysis:
1. Break down the user's solution into clearly identifiable steps.
2. Compare the solution with the reference exercises and algorithms to identify any of this errors:
* Rules/Productions:
    - Check consistency with the required grammar type.
    - Identify invalid or improperly defined rules.
    - **Critical CNF Validation Step:**  
    Before applying the CYK algorithm or evaluating CNF conversions, verify **every production** adheres strictly to these forms:
                - Valid Forms:
                    - A → BC: exactly two non-terminals, two uppercase letters.
                    - A → a: exactly one terminal, one lowercase letter.
                    - S → λ: only allowed for the start symbol if λ ∈ L(G).
                - Invalid Forms:
                    - Any rule with >2 symbols on the RHS (e.g., `A → BCD`, S → ASA | BSB).
                    - Any rule mixing terminal and non-terminal (e.g., `A → aB`).
                    - λ in non-initial symbols (e.g., `B → λ`).
    - For CNF: Ensure all rules are `A → BC`,`A → a`, or `S → λ`.  
    - Before applying the CYK algorithm check if the problem statement grammar is in CNF.
    - **Critical Steps for Recursion Analysis**:
        1. Recursion Detection:
        - Direct Recursion: Identify rules of the form X → Xα (e.g., S → Sa).
        - Indirect Recursion: Check derivation chains like X → Yα → ... → Xβ (e.g., S → A, A → S).
        - Single Non-Terminal with Two-Level Derivation:
            - If the grammar has one non-terminal (S) and a derivation tree with two levels, verify if S appears in both levels (e.g., S → Sα at level 1).
            - Implication: This indicates recursion, making the language infinite.
        2. Language Cardinality Deduction:
        - If recursion is detected (direct/indirect/single-non-terminal case): The language is infinite (e.g., S → Sα | β generates βα, βαα, βααα, etc.).
        - If no recursion exists: The language is finite (e.g., S → a | b has cardinality 2).  
        3. **Critical Step for Left Recursion Elimination** (only if recursion is detected): 
            - Ordering Non-Terminals:  
            - Non-terminals are processed in a fixed order (e.g., S, A, B, C).  
            - All productions of the form `A_i → A_jβ` (j < i) are expanded using `A_j`'s current rules.  
            - Replace Indirect Dependencies:  
            - Example: `C → SaaB` becomes `C → abS'SaaB` after processing `S → abS'`.  
            - Eliminate Direct Recursion:  
            - Recursive rules like `S → SaB` are split into `S → abS'` and `S' → aBS' | λ`.
    - Validate Language Type:
        - If the target language is inherently non-context-free, flag solutions claiming a CFG exists.
        - Theoretical Reference: Use the Pumping Lemma for CFLs to justify impossibility.
    - Check Cross-Dependency Tracking:
        - Non-terminals must track all interdependent counts (e.g., a’s at start/end and b’s in the middle).
        - Error Example: A → aA | λ breaks balance by allowing arbitrary trailing a’s.
    - Prevent Invalid Interleaving:
        - Ensure rules don’t mix symbols.
        - Test Method: Derive sample strings.
* Step-by-Step Procedure:
    - Compare each step of the solution with the procedure described in the reference algorithm.
    - Ensure the solution follows the correct sequence and logic as outlined in standard methods.
* Conclusions:
    - Ensure logical validity and that conclusions are properly justified.
    - Identify unsupported or incorrect claims.
    - Do not be redundant.
* Transition Tables:
    - Verify completeness (all states and symbols covered) and determinism (for DFAs).
    - Check for missing or ambiguous transitions.
* Additional Checks:
    - Confirm correct use of formal definitions and terminology.
    - Verify handling of edge cases (e.g., empty strings, unreachable states, invalid symbols).
3. Explicitly classify each step as "correct" or "incorrect", avoiding ambiguity in your evaluations.
4. For each incorrect step:
    * Explain why it does not follow the standard procedure.
    * Clearly indicate where the deviation occurs.
    * Provide a counterexample or relevant theoretical reference if possible.
    * Offer specific hints or suggestions to help the user correct the erroneous step.
5. Do not provide complete solutions or rewrite the entire answer.  
6. If the solution is correct, confirm it and explain why it works.

 
### Feedback para solucion incorrecta:
Encuentra una gramática independiente de contexto (GIC) que genere el lenguaje  L = a^n b^n a^n : n ≥ 1 .

Análisis paso a paso de la solución del usuario

#### Análisis del lenguaje: Correcto. 
El usuario ha identificado correctamente la estructura del lenguaje L = a^n b^n a^n : n ≥ 1.

#### Construcción de la gramática: Incorrecto. 
La gramática propuesta por el usuario no es una gramática independiente de contexto (GIC) válida. La regla S → aSbA no es una regla de producción válida en una GIC, ya que la producción de la derecha tiene más de dos símbolos no terminales (S y A).

#### Explicación de las reglas: Incorrecto. 
La explicación de las reglas no es clara y no se justifica por qué se eligieron esas reglas en particular.

#### Ejemplo de derivación: Incorrecto.
 El ejemplo de derivación no es correcto, ya que no se sigue la gramática propuesta por el usuario.

#### Conclusión: Incorrecto.
La gramática propuesta por el usuario no es una gramática independiente de contexto (GIC) válida que genere el lenguaje L = a^n b^n a^n : n ≥ 1.

#### Errores y sugerencias

La regla S → aSbA no es una regla de producción válida en una GIC. En su lugar, se podría utilizar una regla como S → aXbY, donde X y Y son símbolos no terminales que se pueden derivar en a^n y a^n, respectivamente.
La gramática propuesta por el usuario no es capaz de generar el lenguaje L = a^n b^n a^n : n ≥ 1. Se necesita una gramática más compleja que pueda manejar la relación entre los símbolos a y b.
Se sugiere que el usuario revise las reglas de producción y la estructura de la gramática para asegurarse de que sea una GIC válida y que genere el lenguaje deseado.

#### Referencia a los ejercicios y algoritmos de referencia
El ejercicio de referencia indica que no existe una gramática independiente de contexto (GIC) que genere el lenguaje L = a^n b^n a^n : n ≥ 1. Esto se debe a que la GIC solo puede manejar dependencias anidadas (como a^n b^n), pero no relaciones triples (como a^n b^n a^n).
El algoritmo de referencia para la equivalencia entre gramáticas y autómatas de pila no es aplicable en este caso, ya que la gramática propuesta por el usuario no es una GIC válida.







### Feedback para solucion correcta:
Encuentra una gramática independiente de contexto (GIC) que genere el lenguaje  L = a^n b^n a^n : n ≥ 1 .

Análisis paso a paso de la solución del usuario

#### Análisis del lenguaje: Correcto. El usuario ha identificado correctamente las condiciones que debe cumplir el lenguaje L = a^n b^n a^n.
Demostración de que L no es independiente del contexto: Correcto.
El usuario ha aplicado correctamente el lema de bombeo para demostrar que L no es independiente del contexto.
Conclusión: Correcto. El usuario ha concluido correctamente que no existe una gramática independiente del contexto (GIC) que genere L.
Evaluación de la gramática sensible al contexto

La gramática sensible al contexto proporcionada por el usuario es:

S → aSBA | aBA BA → AB aA → aa B → b

#### Análisis de la gramática

La regla S → aSBA | aBA es correcta, ya que permite generar la estructura a^n b^n a^n.
La regla BA → AB es correcta, ya que permite intercambiar los símbolos A y B.
La regla aA → aa es correcta, ya que permite duplicar el símbolo a.
La regla B → b es correcta, ya que permite reemplazar el símbolo B por el símbolo b.

#### Conclusión
La solución del usuario es correcta. Ha demostrado correctamente que L no es independiente del contexto y ha proporcionado una gramática sensible al contexto que genera L. La gramática sensible al contexto es correcta y sigue las reglas de una gramática sensible al contexto.

#### Sugerencias

El usuario podría haber proporcionado más ejemplos de cómo se aplica la gramática sensible al contexto para generar cadenas del lenguaje L.
El usuario podría haber explicado con más detalle por qué la gramática sensible al contexto es necesaria para generar L.
En general, la solución del usuario es clara y correcta. Ha demostrado una buena comprensión de los conceptos de gramáticas independientes del contexto y sensibles al contexto.






**Critical Steps for Recursion Analysis**
1. Recursion Detection:
- Direct Recursion: Identify rules of the form X → Xα (e.g., S → Sa).
- Indirect Recursion: Check derivation chains like X → Yα → ... → Xβ (e.g., S → A, A → S).
- Single Non-Terminal with Two-Level Derivation:
    - If the grammar has one non-terminal (S) and a derivation tree with two levels, verify if S appears in both levels (e.g., S → Sα at level 1).
    - Implication: This indicates recursion, making the language infinite.
2. Language Cardinality Deduction:
- If recursion is detected (direct/indirect/single-non-terminal case):
- The language is infinite (e.g., S → Sα | β generates βα, βαα, βααα, etc.).
If no recursion exists: The language is finite (e.g., S → a | b has cardinality 2).






















# TEMPLATE 2
## Evaluation Instructions:
Step-by-step analysis:
1. Break down the user's solution into clearly identifiable steps.
2. Compare each step with the procedure described in the reference algorithm.
3. Explicitly classify each step as "correct" or "incorrect", avoiding ambiguity in your evaluations.
4. Use the reference exercises as a guide to identify any errors.
5. For each incorrect step:
    * Explain why it does not follow the standard procedure.
    * Clearly indicate where the deviation occurs.
    * Provide a counterexample or relevant theoretical reference if possible.
    * Offer specific hints or suggestions to help the user correct the erroneous step.
6. Do not provide complete solutions or rewrite the entire answer.  
7. If the solution is correct, confirm it and explain why it works.
 
### Feedback para solucion incorrecta:
Encuentra una gramática independiente de contexto (GIC) que genere el lenguaje  L = a^n b^n a^n : n ≥ 1 .

Evaluación de la solución del usuario

La solución del usuario se divide en tres pasos claramente identificables: Análisis del lenguaje, Construcción de la gramática y Ejemplo de derivación.

#### Paso 1: Análisis del lenguaje Este paso es correcto.
El usuario ha analizado correctamente la estructura del lenguaje L = a^n b^n a^n : n ≥ 1,
identificando los patrones y las restricciones que deben cumplir las cadenas que pertenecen a este lenguaje.

#### Paso 2: Construcción de la gramática Este paso es incorrecto.
La gramática propuesta por el usuario no es una gramática independiente de contexto
(GIC) que genere el lenguaje L = a^n b^n a^n : n ≥ 1. La regla S → aSbA no asegura que la cantidad de a's al inicio y al final sea igual a la cantidad de b's en el medio.
Además, la regla A → aA | λ no es suficiente para generar los a's finales de manera correcta.

#### Paso 3: Ejemplo de derivación Este paso es incorrecto. 
La derivación proporcionada por el usuario no es una derivación válida según la gramática propuesta.
 La aplicación de las reglas de producción no sigue el procedimiento estándar para generar cadenas en el lenguaje L = a^n b^n a^n : n ≥ 1.

#### Errores y sugerencias

La gramática propuesta no es capaz de generar el lenguaje L = a^n b^n a^n : n ≥ 1 de manera correcta. Se requiere una gramática más compleja que pueda manejar la relación entre la cantidad de a's y b's.

La regla S → aSbA no es suficiente para asegurar la estructura balanceada del lenguaje. Se requiere una regla adicional que permita generar los a's finales de manera correcta.

La derivación proporcionada no es una derivación válida según la gramática propuesta. Se requiere una derivación más detallada y precisa que siga el procedimiento estándar para generar cadenas en el lenguaje L = a^n b^n a^n : n ≥ 1.

Conclusión La solución del usuario no es correcta. Se requiere una gramática más compleja y una derivación más detallada y precisa para generar el lenguaje L = a^n b^n a^n : n ≥ 1.
Se sugiere revisar la teoría de gramáticas independientes de contexto y la construcción de derivaciones válidas para generar lenguajes complejos.


### Feedback para solucion correcta:
Encuentra una gramática independiente de contexto (GIC) que genere el lenguaje  L = a^n b^n a^n : n ≥ 1 .

La solución del usuario se divide en tres pasos claramente identificables: Análisis del lenguaje, Demostración de que L no es independiente del contexto y Conclusión.

### Paso 1: Análisis del lenguaje Este paso es correcto. 
El usuario ha identificado correctamente las condiciones que debe cumplir el lenguaje L = a^n b^n a^n, es decir,
que el número de a iniciales, b centrales y a finales sea el mismo.

### Paso 2: Demostración de que L no es independiente del contexto Este paso es correcto. 
El usuario ha aplicado correctamente el lema de bombeo para demostrar que el lenguaje L
no es independiente del contexto. La demostración es clara y sigue el procedimiento estándar para aplicar el lema de bombeo.

### Paso 3: Conclusión Este paso es correcto. 
El usuario ha concluido correctamente que no existe una gramática independiente del contexto (GIC) que genere el lenguaje L
y ha explicado por qué se requiere una gramática sensible al contexto (Tipo 1) para generar L.

Ejemplo de gramática sensible al contexto Este ejemplo es correcto. La gramática proporcionada es una gramática sensible al contexto que puede generar el lenguaje L = a^n b^n a^n.

En general, la solución del usuario es correcta y sigue el procedimiento estándar para demostrar que un lenguaje no es independiente del contexto y proporcionar una gramática sensible al contexto que lo genere.
La explicación es clara y fácil de seguir, y el usuario ha aplicado correctamente los conceptos teóricos relevantes.

# Template for problem evaluation
self.TEMPLATE_PROBLEM = """
# Virtual Tutor for Grammars and Automata
You are a specialized tutor in Regular Grammars, Context-Free Grammars, and Finite Automata.
Always answer in Spanish.

## References
- **Reference exercises:** {context_exercises}
- **Reference algorithm:** {context_algorithm}

## Problem and Solution
- **Problem statement:** {problem_statement}
- **Student's proposed solution:** {user_solution}

## Evaluation Instructions

### 1. Step-by-step analysis
Break down the student's solution into clearly identifiable steps.

### 2. Validation by categories

#### 2.1 Rules and Productions
- **Grammar type consistency:**
  * Verify that rules are appropriate for the required type (regular, context-free, etc.)
  * Identify invalid or improperly defined rules

- **Chomsky Normal Form (CNF) validation:**
  * **Valid forms:**
    - A → BC (exactly two non-terminals, two uppercase letters)
    - A → a (exactly one terminal, one lowercase letter)
    - S → λ (only allowed for the start symbol if λ ∈ L(G))
  * **Invalid forms:**
    - Rules with >2 symbols on the right side (e.g., A → BCD)
    - Rules mixing terminals and non-terminals (e.g., A → aB)
    - λ in non-initial symbols (e.g., B → λ)
  * Before applying the CYK algorithm, verify if the grammar is in CNF

- **Recursion analysis:**
  * **Detection:**
    - Direct recursion: Rules of the form X → Xα (e.g., S → Sa)
    - Indirect recursion: Derivation chains like X → Yα → ... → Xβ (e.g., S → A, A → S)
    - Single non-terminal with two-level derivation
  * **Consequences:**
    - With recursion: Infinite language
    - Without recursion: Finite language
  * **Left recursion elimination:**
    - Order non-terminals
    - Replace indirect dependencies
    - Eliminate direct recursion with appropriate transformations

- **Language type validation:**
  * If the target language is inherently non-context-free, flag solutions claiming otherwise
  * Use the Pumping Lemma as a theoretical reference when necessary

#### 2.2 Step-by-step procedure
- Compare each step with the procedure described in the reference algorithm
- Ensure the solution follows the correct sequence and logic

#### 2.3 Transition tables (for automata)
- Verify completeness (all states and symbols covered)
- Check determinism (for DFAs)
- Look for missing or ambiguous transitions

#### 2.4 Additional checks
- Confirm correct use of formal definitions and terminology
- Verify handling of edge cases (empty strings, unreachable states, invalid symbols)

### 3. Explicit classification
- Classify each step as "correct" or "incorrect", avoiding ambiguity

### 4. Feedback for incorrect steps
- Explain why it doesn't follow the standard procedure
- Clearly indicate where the deviation occurs
- Provide a counterexample or theoretical reference when possible
- Offer specific suggestions to correct the error

### 5. Limitations
- Do not provide complete solutions or rewrite the entire answer

### 6. Confirmation
- If the solution is correct, confirm it and explain why it works
"""



2.6 Semantic Validation of the Language Constraints

1. Identify Language Invariants:
Analyze the explicit conditions specified in the problem statement (e.g., m ≥ n, symbol order, relationships between counts).
2. Assign Semantic Meaning to Non-terminals:
Define what each non-terminal represents in terms of the invariants (e.g., A could represent "still generating as or switching to bs, but with pending bs needed").
3. Check that production rules preserve these meanings.
Example of an error: If A → bB allows generating bs before enough as have been matched, the invariant m ≥ n is violated.
4. Generate Counterexamples:
Test strings that do not belong to the language and verify that the grammar cannot generate them.
5. Analyze Critical Non-terminals:
Ensure that intermediate non-terminals do not allow premature termination that would violate the constraints.
