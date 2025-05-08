# 2-Bit ALU Design and Implementation

This project involves the design and hardware implementation of a simplified 2-bit Arithmetic Logic Unit (ALU) using basic logic gates. The project includes both software simulation and physical hardware implementation components.

## Project Overview

An Arithmetic Logic Unit (ALU) is a fundamental component of any CPU, responsible for performing various arithmetic and logical operations. This project implements a simplified 2-bit ALU that can perform the following operations:

- Bitwise AND, OR, XOR
- Addition and Subtraction using 2's complement
- NOT (1's complement)

## Project Contents

### Software Simulation

- `src/alu_simulator.py`: Command-line simulation of the 2-bit ALU operations
- `src/alu_visualizer.py`: GUI-based visualization showing ALU operations and circuit diagrams

### Hardware Implementation

- `hardware_design/circuit_implementation.md`: Detailed guide for hardware implementation
- Images and circuit diagrams for physical construction

## Getting Started

### Software Requirements

- Python 3.6 or higher
- Tkinter (for GUI visualization)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/hassan220022/2-bit-alu.git
   cd 2-bit-alu
   ```

2. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Simulator

1. Run the command-line simulator:
   ```
   python src/alu_simulator.py
   ```

2. Run the GUI visualizer:
   ```
   python src/alu_visualizer.py
   ```

### Building the Hardware

See the detailed instructions in `hardware_design/circuit_implementation.md`.

## Hardware Components

For the physical implementation, you will need:

- Breadboard
- Logic Gate ICs (7408, 7432, 7486, 7404)
- LEDs (for output display)
- DIP Switches or Tactile Switches (for inputs)
- Power supply (5V)
- Wires and jumpers

## Operation Codes

The ALU uses a 3-bit operation selector:

| Operation | Op Code | Description |
|-----------|---------|-------------|
| AND       | 000     | Bitwise AND |
| OR        | 001     | Bitwise OR  |
| XOR       | 010     | Bitwise XOR |
| ADD       | 011     | Addition with carry |
| SUB       | 100     | Subtraction with borrow |
| NOT       | 101     | Bitwise NOT (1's complement) |

## Project Report

A detailed project report is available in `docs/project_report.md` covering:
- Theoretical background
- Design methodology
- Implementation details
- Testing procedures
- Results analysis

## Acknowledgments

- Course instructor and teaching assistants
- References and learning resources


you can also use for the [simulator](https://claude.ai/public/artifacts/ea8579f5-8a7f-4332-8920-95c36823ea32)