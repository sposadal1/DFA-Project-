# Assignment 1: Lexical Pattern Recognition using DFA

**Course:** Formal Languages (2026)

**Institution:** EAFIT University - School of Applied Sciences and Engineering

**Professor:** Adolfo Andrés Castro Sánchez

**Author:** Samuel Posada

## 1. Project Description

This project implements a Deterministic Finite Automaton (DFA) designed to recognize three specific lexical patterns: "a", "abb", and "a*b+". The implementation is based on the theoretical model from Example 3.19 in the reference book Compilers: Principles, Techniques, & Tools by Aho et al.. The automaton identifies tokens by transitioning through a set of states based on the input alphabet Σ = {a, b}. This process is fundamental for the lexical analysis phase of a compiler.

## 2. Logistics

* **Operating System**: Windows 11.
* **Programming Language**: Python 3.13.12.
* **Development Tools**: Visual Studio Code (VS Code).

## 3. How to Run the Program

1. Ensure Python 3.13.12 is installed on your Windows 11 system.
2. Open PowerShell and navigate to the directory where the code is located.
3. Execute the command: python automata.py
4. Enter strings composed of the alphabet {a, b} when prompted by the program.
5. To exit the application, type 's' or 'S' and press Enter.

## 4. Algorithm Explanation

The program simulates the DFA logic by processing the input string character by character from left to right:

* **Transition Logic (funcion_transicion)**: This function acts as the state transition table. It receives the current state and a symbol ('a' or 'b') and returns the next state according to the defined graph: {0137, 247, 7, 58, 68, 8}.


* **Processing Engine (verificar_cadena)**: It manages the lifecycle of the automaton. It starts at the initial state 0137 and updates the state for every character in the input string. If at any point no transition is defined for a given symbol, the string is rejected immediately.
* **Acceptance Criteria**: Once the entire string is processed, the algorithm checks if the final state reached is part of the acceptance set (indicated by double circles in the diagram): {247, 58, 68, 8}.


* **Robustness (validar_cadena)**: A validation layer ensures that the program only processes strings containing valid symbols from the alphabet, handling potential user errors gracefully.

## 5. Video Presentation

The explanation of the development process, the theoretical background, and a functional demonstration can be found at the following link:

[INSERT VIDEO LINK HERE]
