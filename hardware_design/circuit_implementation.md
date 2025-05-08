# 2-Bit ALU Hardware Implementation Guide

This document outlines the process for building a 2-bit ALU using 7400 series logic ICs.

## Required Components

- **Logic Gate ICs:**
  - 7408: Quad 2-input AND gates
  - 7432: Quad 2-input OR gates
  - 7486: Quad 2-input XOR gates
  - 7404: Hex inverter (NOT gates)
  - 7483: 4-bit binary full adder (optional, can be built from gates)

- **Other Components:**
  - Breadboard
  - 4× DIP switches (for input A, B, and operation select)
  - 3× LEDs (for 2-bit output and carry/borrow)
  - 220Ω resistors for LEDs
  - Jumper wires
  - 5V power supply

## Circuit Design

### Input Section

1. **Input Configuration:**
   - Use DIP switches to set the 2-bit inputs A and B
   - Use a 3-bit DIP switch to select the operation (see operation codes below)

### Operation Selector

The operation selector uses 3 bits to determine which operation to perform:
- `000`: AND
- `001`: OR
- `010`: XOR
- `011`: ADD
- `100`: SUB
- `101`: NOT

We'll implement this using a multiplexer structure.

### Operation Implementations

#### 1. Bitwise AND (Op Code: 000)

![AND Gate Implementation](images/and_implementation.jpg)

```
For each bit position i:
Result[i] = A[i] AND B[i]
```

Components:
- 1× 7408 (AND gates)

#### 2. Bitwise OR (Op Code: 001)

```
For each bit position i:
Result[i] = A[i] OR B[i]
```

Components:
- 1× 7432 (OR gates)

#### 3. Bitwise XOR (Op Code: 010)

```
For each bit position i:
Result[i] = A[i] XOR B[i]
```

Components:
- 1× 7486 (XOR gates)

#### 4. Addition (Op Code: 011)

The 2-bit addition requires:
1. Half adder for bit 0
2. Full adder for bit 1 (to handle carry)

```
// For bit 0:
Sum[0] = A[0] XOR B[0]
Carry = A[0] AND B[0]

// For bit 1:
Sum[1] = A[1] XOR B[1] XOR Carry
Carry_out = (A[1] AND B[1]) OR (A[1] AND Carry) OR (B[1] AND Carry)
```

Components:
- 1× 7486 (XOR gates)
- 1× 7408 (AND gates)
- 1× 7432 (OR gates)

Alternative: Use a 7483 4-bit binary full adder (easier implementation).

#### 5. Subtraction (Op Code: 100)

For 2's complement subtraction:
1. Invert all bits of B
2. Add 1 to the inverted B
3. Add A to the 2's complement of B

```
// Convert B to 2's complement
B_complement[0] = NOT B[0]
B_complement[1] = NOT B[1]

// Add 1 (for 2's complement)
// This can be incorporated into the addition logic

// Perform addition
Result = A + B_complement
```

Components:
- 1× 7404 (NOT gates)
- Addition components as listed above

#### 6. NOT (Op Code: 101)

```
For each bit position i:
Result[i] = NOT A[i]
```

Components:
- 1× 7404 (NOT gates)

### Multiplexer for Operation Selection

We need a multiplexer to select the appropriate operation based on the 3-bit operation selector. This can be implemented using AND gates and OR gates, or using a dedicated multiplexer IC like 74151.

### Output Display

- Connect 2 LEDs to display the 2-bit result
- Connect 1 LED to display the carry/borrow signal
- Use 220Ω resistors in series with each LED

## Full Circuit Diagram

Below is a simplified block diagram of the complete ALU:

```
                  ┌─────────┐
       A[1:0] ───►│         │
                  │  ALU    │
       B[1:0] ───►│         │───► Result[1:0]
                  │         │
Op_Select[2:0] ──►│         │───► Carry/Borrow
                  └─────────┘

```

## Wiring Instructions

1. **Power and Ground:**
   - Connect 5V to the power rails on the breadboard
   - Connect ground to the ground rails

2. **Input Switches:**
   - Wire the DIP switches to provide inputs A[1:0], B[1:0], and Op_Select[2:0]
   - Connect one side of each switch to ground
   - Connect the other side to the appropriate input with a pull-up resistor to 5V

3. **Operation Circuit:**
   - Wire the logic gates according to the operation implementations above
   - Use the multiplexer to select the appropriate operation output

4. **Output LEDs:**
   - Connect the output signals through 220Ω resistors to the LEDs
   - Connect the other end of the LEDs to ground

## Testing the Circuit

1. Set operation select to `000` (AND)
   - Try different combinations of A and B and verify outputs

2. Repeat for each operation:
   - `001`: OR
   - `010`: XOR
   - `011`: ADD
   - `100`: SUB
   - `101`: NOT

## Troubleshooting Tips

1. **No Output:**
   - Check power and ground connections
   - Verify all ICs are properly seated in breadboard
   - Check for loose wires

2. **Incorrect Output:**
   - Verify input switches are working properly
   - Check operation selector connections
   - Trace signal flow through each gate

3. **Inconsistent Output:**
   - Check for floating inputs (all inputs should be connected to either 5V or ground)
   - Verify power supply is stable

## Enhancement Ideas

1. **Seven-Segment Display:**
   - Add a decoder and 7-segment display to show the output in decimal

2. **Additional Operations:**
   - Implement NAND, NOR operations with the unused op codes

3. **Status Flags:**
   - Add zero flag detection
   - Add overflow detection

## IC Pin Configurations

### 7408 (AND Gates)
```
    Vcc  4B  4A  4Y  3B  3A  3Y
     |    |   |   |   |   |   |
    ┌┴────┴───┴───┴───┴───┴───┴┐
    │                          │
    │         7408             │
    │                          │
    └┬────┬───┬───┬───┬───┬───┬┘
     |    |   |   |   |   |   |
    GND  1A  1B  1Y  2A  2B  2Y
```

### 7432 (OR Gates)
```
    Vcc  4B  4A  4Y  3B  3A  3Y
     |    |   |   |   |   |   |
    ┌┴────┴───┴───┴───┴───┴───┴┐
    │                          │
    │         7432             │
    │                          │
    └┬────┬───┬───┬───┬───┬───┬┘
     |    |   |   |   |   |   |
    GND  1A  1B  1Y  2A  2B  2Y
```

### 7486 (XOR Gates)
```
    Vcc  4B  4A  4Y  3B  3A  3Y
     |    |   |   |   |   |   |
    ┌┴────┴───┴───┴───┴───┴───┴┐
    │                          │
    │         7486             │
    │                          │
    └┬────┬───┬───┬───┬───┬───┬┘
     |    |   |   |   |   |   |
    GND  1A  1B  1Y  2A  2B  2Y
```

### 7404 (NOT Gates)
```
    Vcc  6A  6Y  5A  5Y  4A  4Y
     |    |   |   |   |   |   |
    ┌┴────┴───┴───┴───┴───┴───┴┐
    │                          │
    │         7404             │
    │                          │
    └┬────┬───┬───┬───┬───┬───┬┘
     |    |   |   |   |   |   |
    GND  1A  1Y  2A  2Y  3A  3Y
```
