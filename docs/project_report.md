# 2-Bit ALU Design and Implementation
## Project Report

**Course:** Computer Architecture  
**Due Date:** 12/5/2025  
**Team Members:** [List team members here]

## Table of Contents
1. [Introduction](#introduction)
2. [Theoretical Background](#theoretical-background)
3. [Design Methodology](#design-methodology)
4. [Implementation Details](#implementation-details)
5. [Testing and Validation](#testing-and-validation)
6. [Results Analysis](#results-analysis)
7. [Challenges and Solutions](#challenges-and-solutions)
8. [Conclusion](#conclusion)
9. [References](#references)
10. [Appendices](#appendices)

## Introduction

This report documents the design and implementation of a 2-bit Arithmetic Logic Unit (ALU) using basic logic gates. The ALU is a critical component of the CPU, responsible for executing arithmetic and logical operations. Our implementation focuses on a simplified 2-bit version that demonstrates the fundamental concepts of ALU design.

### Project Objectives

- To design a basic 2-bit ALU capable of performing simple arithmetic and logical operations
- To implement the ALU using discrete logic gate ICs
- To develop a software simulator that validates our hardware design
- To understand the internal hardware workings of an ALU

## Theoretical Background

### What is an ALU?

The Arithmetic Logic Unit (ALU) is a digital circuit that performs arithmetic and bitwise operations on binary numbers. It is a fundamental building block of the central processing unit (CPU) of a computer. Modern CPUs contain very complex ALUs capable of performing many operations. Our 2-bit ALU is a simplified version that demonstrates the basic principles.

### Operations Implemented

Our ALU implements six fundamental operations:

1. **Bitwise AND**: Performs a logical AND on each pair of corresponding bits
2. **Bitwise OR**: Performs a logical OR on each pair of corresponding bits
3. **Bitwise XOR**: Performs a logical XOR on each pair of corresponding bits
4. **Addition**: Adds two 2-bit numbers with carry
5. **Subtraction**: Subtracts using 2's complement method
6. **NOT**: Performs a logical NOT (1's complement) on the input

### Binary Representation and 2's Complement

For our 2-bit ALU, numbers are represented using only 2 bits, allowing values from 0 to 3:
- 00: 0
- 01: 1
- 10: 2
- 11: 3

For subtraction, we use the 2's complement method:
1. Invert all bits (1's complement)
2. Add 1 to the result

For a 2-bit number, the 2's complement is:
- 2's complement of 0 (00) is 0 (00)
- 2's complement of 1 (01) is 3 (11)
- 2's complement of 2 (10) is 2 (10)
- 2's complement of 3 (11) is 1 (01)

## Design Methodology

### System Architecture

Our ALU design follows a standard architecture with:
- Input registers for the two 2-bit operands (A and B)
- Operation selector (3-bit control signal)
- Logic for each operation
- Output register for the 2-bit result
- Carry/borrow flag

### Block Diagram

The high-level block diagram of our ALU is as follows:

```
                   ┌─────────────────┐
                   │                 │
       A[1:0] ────►│                 │
                   │                 │
       B[1:0] ────►│      ALU       │────► Result[1:0]
                   │                 │
Op_Select[2:0] ───►│                 │────► Carry/Borrow
                   │                 │
                   └─────────────────┘
```

### Logic Design

For each operation, we designed the appropriate logic circuits:

1. **AND Operation**: Direct implementation using AND gates
2. **OR Operation**: Direct implementation using OR gates
3. **XOR Operation**: Direct implementation using XOR gates
4. **Addition**: Implementation using half and full adders
5. **Subtraction**: Implementation using 2's complement and adders
6. **NOT Operation**: Direct implementation using NOT gates

### Component Selection

We selected the following 7400 series ICs for our implementation:
- 7408: Quad 2-input AND gates
- 7432: Quad 2-input OR gates
- 7486: Quad 2-input XOR gates
- 7404: Hex inverter (NOT gates)

## Implementation Details

### Hardware Implementation

#### Circuit Design

[Detailed circuit diagrams and explanations for each operation circuit]

#### Component List

- Breadboard
- Logic Gate ICs:
  - 1× 7408 (AND gates)
  - 1× 7432 (OR gates)
  - 1× 7486 (XOR gates)
  - 1× 7404 (NOT gates)
- 4× DIP switches (for inputs)
- 3× LEDs (for outputs)
- Resistors and wiring

#### Assembly Process

[Step-by-step description of the physical assembly process with photos]

### Software Simulation

To validate our hardware design and provide a learning tool, we developed two software components:

#### Command-Line Simulator

A Python-based simulator that demonstrates all ALU operations with various input combinations. The simulator provides a comprehensive test of all possible input combinations and verifies the expected outputs.

#### GUI Visualizer

A graphical interface that shows:
- Interactive inputs and outputs
- Visual representation of the circuit for each operation
- Real-time updates as inputs change

## Testing and Validation

### Test Methodology

We tested our ALU implementation using:
1. **Exhaustive testing**: Testing all possible input combinations (16 combinations for each operation)
2. **Edge cases**: Special focus on carry and borrow conditions
3. **Software validation**: Comparing hardware results with software simulation

### Test Results

[Detailed test results for each operation, including truth tables]

## Results Analysis

### Performance Evaluation

[Analysis of the ALU performance, including propagation delays and power consumption]

### Comparison with Expected Results

[Comparison between theoretical, simulated, and actual hardware results]

## Challenges and Solutions

### Technical Challenges

1. **Challenge 1**: [Description]
   **Solution**: [Description]

2. **Challenge 2**: [Description]
   **Solution**: [Description]

### Design Tradeoffs

[Discussion of design decisions and tradeoffs made during implementation]

## Conclusion

### Summary of Achievements

[Summary of what was accomplished and how it met the project objectives]

### Learning Outcomes

[Discussion of the educational value of the project]

### Future Improvements

Potential enhancements for future versions:
- Expanding to 4-bit or 8-bit operations
- Adding more complex operations (e.g., multiplication)
- Implementing a complete instruction set
- Creating a PCB version of the circuit

## References

1. [Reference 1]
2. [Reference 2]
3. [Reference 3]

## Appendices

### Appendix A: Complete Circuit Diagrams

[Detailed circuit diagrams]

### Appendix B: Source Code

[Links to the source code repositories or excerpts of key functions]

### Appendix C: Additional Photos

[Additional photos of the hardware implementation]
