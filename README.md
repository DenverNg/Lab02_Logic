# Repo structure
folder named `22127085`  with the following structure:

   - Folder `22127085`
        - File `22127085.ipynb` 
        - Folder `models`, `Input`, `Output`and file `logic.py`
        - Folder `PS4` that include your works on exercise 4:
            - `source_code.py`: Source code (file .py)
            - `report.pdf`: Report (file .pdf)


# Part 1-3

For questions 1-3, you will work directly in `22127085/22127085.ipynb`. The comment `# YOUR CODE HERE` will indicate the parts you need to complete (remember to comment out the line raise `NotImplementedError()` before submitting). Mathematical symbols must be presented in code according to the following symbol list:"

<center>

|                                                               |           Math symbols           | Code                                                                                                                 |
| :------------------------------------------------------------ | :------------------------------: | -------------------------------------------------------------------------------------------------------------------- |
| constant symbol                                               |              hcmus               | ```Constant('hcmus')``` (must be lowercase)                                                                          |
| variable symbol                                               |               $x$                | ```Variable('$x')``` ( must be lowercase)                                                                            |
| atomic formula                                                |   Rain, LocatedIn(hcmus, $x$)    | ```Atom('Rain')```, ```Atom('LocatedIn', 'hcmus', '$x')``` <br> (predicate must be uppercase, arguments are symbols) |
| negation                                                      |           $\neg$ Rain            | ```Not(Atom('Rain'))```                                                                                              |
| conjunction                                                   |        Rain $\land$ Snow         | ```And(Atom('Rain'), Atom('Snow'))```                                                                                |
| disjunction                                                   |         Rain $\lor$ Snow         | ```Or(Atom('Rain'), Atom('Snow'))```                                                                                 |
| implication                                                   |      Rain $\Rightarrow$ Wet      | ```Implies(Atom('Rain'), Atom('Wet'))```                                                                             |
| equivalence                                                   |    Rain $\Leftrightarrow$ Wet    | ```Equiv(Atom('Rain'), Atom('Wet'))```                                                                               |
| existential quantification                                    | $\exists x$ LocatedIn(hcmus,$x$) | ```Exists('$x', Atom('LocatedIn', 'hcmus', '$x'))```                                                                 |
| universal quantification                                      |   $\forall x$ MadeOfAtoms($x$)   | ```Forall('$x', Atom('MadeOfAtoms', '$x'))```                                                                        |
| conjunction with many argument <br>(similar with disjunction) |      A $\land$ B $\land$ C       | ```AndList([Atom('A'), Atom('B'), Atom('C')]) ```                                                                    |
  
</center>

# Part 4
Given a Knowledge Base **(KB)** and a statement $\alpha$, both represented by prepositional logic and change to CNF. Determine if KB entails $\alpha$ (KB ⊨ $\alpha$) by resolution.

- I have provided you with seven test cases, of which I have included examples of expected outputs for the first two test cases (input01.txt, input02.txt). Your task is to determine the outputs for all test cases and present them in two ways: 
    + Write the output explanation in your report. 
    + Design your own Python scripts to generate these outputs from given inputs.   

- Write short evaluations about the advantages and disadvantages of resolution method for prepositional logic, propose your own solution for specific problem.

**a. Desribe the experiment data.**
- **Input data**: **KB** and $\alpha$ with CNF stored in **input.txt**. This file have the following structure:
    - The first line contains $\alpha$ statement
    - The second line has N – the number of clauses in the KB.
    - N following lines are clauses in KB, one line for each clause.
    
Positive literal is represented by an uppercase character (A-Z). Negative literal is positive literal with minus (‘-‘) before the character.

Literals are linked by OR. Bettween literals and keywords there can be more than one space.

- **Output data**: The set of statements that are generated during the whole resolution process and the conclusion clause is stored in **output.txt**. This file must have the following structure:
    - The first line contains M1 – the number of generated clauses in first loop. M1 following lines describe those clauses (including empty clause), each line represents a clause. The empty clause is represented by “{}”
    - Next loops are also represented as ($M_2$, $M_3$,…, $M_n$ clauses) the first loop. 
    - The last line is the conclusion clause, which mean if “KB entails $\alpha$?”. Print YES if KB entails $\alpha$. NO for the opposite.
    - Remove redundant clause (same clauses in same loop, or the loops before).
    
    
- **Main function must**:
    - Read the input data and store it in a suitable data structure.
    - Call PL-Resolution function for execute resolution algorithm.
    - Export the output data with the required format.

- **Other important notes**:
    - Store the semantic information of true and false value in PL-RESOLUTION. Do not forget that we need to negate $\alpha$.
    - Literals in a clause is sorted by alphabetical ordering.
    - Infered condition is checked in each loop as when all the new clauses are generated from the current KB.
    - Clauses that have A V B V -B format and True value are similar to A V True can be removed.

**b. Evaluations**
- Read input data and store in suitable data structure, you will recieve 0.5
- Implementation of resolution method, you will recieve 0.75
- Each test case with a complete and correct explanation of the output will receive 0.5.
- If the report does not include a detailed explanation of how the output was obtained, that test case will not be scored.
- **If you only include the output explanation in the report without the code, you will receive 0.25 for each test case.**