# 2-Bit ALU Hardware Implementation Guide

This comprehensive guide will walk you through building a functional 2-bit ALU using standard 7400 series logic ICs. Each section includes detailed pin-by-pin wiring instructions, step-by-step instructions, and helpful diagrams.

## Required Components

### Logic ICs
- 1× **7408** ([Datasheet](https://www.ti.com/lit/ds/symlink/sn7408.pdf)): Quad 2-input AND gates
- 1× **7432** ([Datasheet](https://www.ti.com/lit/ds/symlink/sn7432.pdf)): Quad 2-input OR gates
- 1× **7486** ([Datasheet](https://www.ti.com/lit/ds/symlink/sn7486.pdf)): Quad 2-input XOR gates
- 1× **7404** ([Datasheet](https://www.ti.com/lit/ds/symlink/sn7404.pdf)): Hex inverter (NOT gates)

### Passive Components
- 1× Standard breadboard ([Amazon link](https://www.amazon.com/dp/B07DL13RZH))
- 6× SPDT switches for inputs ([Amazon link](https://www.amazon.com/dp/B07LCBMWGJ))
- 3× LEDs (different colors recommended) ([Amazon link](https://www.amazon.com/dp/B01AUI4VSI))
- 3× 330Ohm resistors for LEDs
- 6× 10kOhm pull-up resistors for switches
- Jumper wires kit ([Amazon link](https://www.amazon.com/dp/B07GD2BWPY))
- 4× 0.1uF ceramic capacitors (for decoupling)
- 5V power supply or 4× AA batteries with holder

### Tools
- Wire cutter/stripper
- Multimeter (for troubleshooting)
- Optional: Logic probe

## IC Pin Configurations

### 7408 (Quad AND Gates)
```
    VCC  4B  4A  4Y  3B  3A  3Y
     14  13  12  11  10   9   8
    ┌────┬───┬───┬───┬───┬───┬────┐
    │                             │
    │         SN7408              │
    │                             │
    └────┬───┬───┬───┬───┬───┬────┘
      1   2   3   4   5   6   7
     1A  1B  1Y  2A  2B  2Y  GND
```

### 7432 (Quad OR Gates)
```
    VCC  4B  4A  4Y  3B  3A  3Y
     14  13  12  11  10   9   8
    ┌────┬───┬───┬───┬───┬───┬────┐
    │                             │
    │         SN7432              │
    │                             │
    └────┬───┬───┬───┬───┬───┬────┘
      1   2   3   4   5   6   7
     1A  1B  1Y  2A  2B  2Y  GND
```

### 7486 (Quad XOR Gates)
```
    VCC  4B  4A  4Y  3B  3A  3Y
     14  13  12  11  10   9   8
    ┌────┬───┬───┬───┬───┬───┬────┐
    │                             │
    │         SN7486              │
    │                             │
    └────┬───┬───┬───┬───┬───┬────┘
      1   2   3   4   5   6   7
     1A  1B  1Y  2A  2B  2Y  GND
```

### 7404 (Hex Inverter)
```
    VCC  6A  6Y  5A  5Y  4A  4Y
     14  13  12  11  10   9   8
    ┌────┬───┬───┬───┬───┬───┬────┐
    │                             │
    │         SN7404              │
    │                             │
    └────┬───┬───┬───┬───┬───┬────┘
      1   2   3   4   5   6   7
     1A  1Y  2A  2Y  3A  3Y  GND
```

## Full Circuit Diagram

```mermaid
graph TD
    subgraph Inputs
        A1[A1]
        A0[A0]
        B1[B1]
        B0[B0]
        S1[S1]
        S0[S0]
    end
    
    subgraph "AND Operation"
        AND1[AND Gate]
        AND0[AND Gate]
        A1 --> AND1
        B1 --> AND1
        A0 --> AND0
        B0 --> AND0
    end
    
    subgraph "OR Operation"
        OR1[OR Gate]
        OR0[OR Gate]
        A1 --> OR1
        B1 --> OR1
        A0 --> OR0
        B0 --> OR0
    end
    
    subgraph "XOR/ADD Operation"
        XOR1[XOR Gate]
        XOR0[XOR Gate]
        CARRY[AND/OR for Carry]
        A1 --> XOR1
        B1 --> XOR1
        A0 --> XOR0
        B0 --> XOR0
        A0 --> CARRY
        B0 --> CARRY
        CARRY --> XOR1
    end
    
    subgraph "NOT/SUB Operation"
        NOT_B1[NOT Gate]
        NOT_B0[NOT Gate]
        B1 --> NOT_B1
        B0 --> NOT_B0
        NOT_B1 --> XOR1
        NOT_B0 --> XOR0
    end
    
    subgraph "Multiplexer"
        MUX1[MUX for Bit 1]
        MUX0[MUX for Bit 0]
        AND1 --> MUX1
        OR1 --> MUX1
        XOR1 --> MUX1
        AND0 --> MUX0
        OR0 --> MUX0
        XOR0 --> MUX0
        S1 --> MUX1
        S0 --> MUX1
        S1 --> MUX0
        S0 --> MUX0
    end
    
    subgraph Outputs
        R1[Result Bit 1]
        R0[Result Bit 0]
        C[Carry/Borrow]
        MUX1 --> R1
        MUX0 --> R0
        CARRY --> C
    end
```

## Step-by-Step Assembly Instructions

### 1. Power Setup (First Priority)

1. Place all ICs on the breadboard with the notch/dot facing the same direction
2. Connect pin 14 of all ICs to the power rail (+5V)
3. Connect pin 7 of all ICs to the ground rail
4. Place one 0.1uF decoupling capacitor between +5V and GND near each IC

```mermaid
graph LR
    subgraph "Power Connection"
        P5V[+5V Power Rail] --> IC1P[7408 Pin 14]
        P5V --> IC2P[7432 Pin 14]
        P5V --> IC3P[7486 Pin 14]
        P5V --> IC4P[7404 Pin 14]
        IC1G[7408 Pin 7] --> GND[Ground Rail]
        IC2G[7432 Pin 7] --> GND
        IC3G[7486 Pin 7] --> GND
        IC4G[7404 Pin 7] --> GND
    end
```

### 2. Input Switch Wiring

1. Set up 4 switches for inputs A1, A0, B1, B0:
   - Connect one terminal of each switch to GND
   - Connect the other terminal to a 10kOhm pull-up resistor to +5V
   - The junction of the switch and resistor is your input signal

2. Set up 2 switches for operation selection S1, S0:
   - Wire the same way as input switches
   - S1 and S0 determine the operation:
     - S1=0, S0=0: AND
     - S1=0, S0=1: OR
     - S1=1, S0=0: ADD
     - S1=1, S0=1: SUB

```mermaid
graph TD
    subgraph "Switch Wiring Example (for one input)"
        VCC[+5V] --> R[10kOhm Resistor] --> J[Junction Point] --> SW[SPDT Switch] --> GND[Ground]
        J -- "Signal Output" --> IC[To IC Input]
    end
```

### 3. Implement Basic Operations

#### AND Operation (7408)
- Connect A1 to pin 1 (1A) of 7408
- Connect B1 to pin 2 (1B) of 7408
- Output at pin 3 (1Y) is A1 AND B1
- Connect A0 to pin 4 (2A) of 7408
- Connect B0 to pin 5 (2B) of 7408
- Output at pin 6 (2Y) is A0 AND B0

#### OR Operation (7432)
- Connect A1 to pin 1 (1A) of 7432
- Connect B1 to pin 2 (1B) of 7432
- Output at pin 3 (1Y) is A1 OR B1
- Connect A0 to pin 4 (2A) of 7432
- Connect B0 to pin 5 (2B) of 7432
- Output at pin 6 (2Y) is A0 OR B0

#### XOR Operation (7486) / Addition
- Connect A1 to pin 1 (1A) of 7486
- Connect B1 to pin 2 (1B) of 7486
- Output at pin 3 (1Y) is A1 XOR B1
- Connect A0 to pin 4 (2A) of 7486
- Connect B0 to pin 5 (2B) of 7486
- Output at pin 6 (2Y) is A0 XOR B0

#### Carry Generation for Addition
1. Connect A0 to pin 10 (3A) of 7408
2. Connect B0 to pin 9 (3B) of 7408
3. Output at pin 8 (3Y) of 7408 is the carry from bit 0

4. To implement full adder for bit 1:
   - Connect A1 to pin 10 (3A) of 7486
   - Connect B1 to pin 9 (3B) of 7486
   - Connect the carry from bit 0 (pin 8 of 7408) to pin 13 (4A) of 7486
   - Connect +5V to pin 12 (4B) of 7486
   - Output at pin 11 (4Y) of 7486 is the full add result

#### NOT Operation (7404) / Subtraction
1. Connect B1 to pin 1 (1A) of 7404
2. Output at pin 2 (1Y) is NOT B1
3. Connect B0 to pin 3 (2A) of 7404
4. Output at pin 4 (2Y) is NOT B0

5. For subtraction with 2's complement:
   - Connect NOT B0 to pin 13 (4B) of 7486 instead of B0
   - Connect NOT B1 to pin 10 (3B) of 7486 instead of B1
   - Connect +5V to pin 12 (4B) of 7486 (as the carry-in '1' for 2's complement)

### 4. Implement Operation Selection with Multiplexer

We'll create a simple multiplexer using AND and OR gates:

For bit 0:
1. Connect S1 to pin 1 (1A) of 7404
2. Output at pin 2 (1Y) is NOT S1
3. Connect S0 to pin 3 (2A) of 7404
4. Output at pin 4 (2Y) is NOT S0

5. For AND result selection:
   - Connect NOT S1 to pin 12 (4A) of 7408
   - Connect NOT S0 to pin 13 (4B) of 7408
   - Connect output (pin 11) to one input of final OR gate
   - Connect AND result (A0 AND B0) to the other input of this AND gate

6. Repeat similar connections for OR and XOR/ADD operations with appropriate select signals
7. Combine all selected outputs with OR gates to get the final result

### 5. Output Display

1. Connect the result bit 1 through a 330Ohm resistor to an LED, then to ground
2. Connect the result bit 0 through a 330Ohm resistor to an LED, then to ground
3. Connect the carry/borrow output through a 330Ohm resistor to an LED, then to ground

```mermaid
graph LR
    R[Result Signal] --> RES[330Ohm Resistor] --> LED[LED] --> GND[Ground]
```

## Detailed Wiring Table

| Signal Source | Connected To | Purpose |
|---------------|--------------|---------|
| +5V | Pin 14 of all ICs | Power supply |
| GND | Pin 7 of all ICs | Ground |
| A1 switch | Pin 1 of 7408, Pin 1 of 7432, Pin 1 of 7486 | Input bit 1 to all operations |
| A0 switch | Pin 4 of 7408, Pin 4 of 7432, Pin 4 of 7486, Pin 10 of 7408 | Input bit 0 to all operations |
| B1 switch | Pin 2 of 7408, Pin 2 of 7432, Pin 2 of 7486, Pin 1 of 7404 | Input bit 1 to all operations |
| B0 switch | Pin 5 of 7408, Pin 5 of 7432, Pin 5 of 7486, Pin 9 of 7408, Pin 3 of 7404 | Input bit 0 to all operations |
| S1 switch | Pin 1 of 7404, Multiplexer logic | Operation select bit 1 |
| S0 switch | Pin 3 of 7404, Multiplexer logic | Operation select bit 0 |
| Pin 3 of 7408 | Multiplexer input | A1 AND B1 result |
| Pin 6 of 7408 | Multiplexer input | A0 AND B0 result |
| Pin 3 of 7432 | Multiplexer input | A1 OR B1 result |
| Pin 6 of 7432 | Multiplexer input | A0 OR B0 result |
| Pin 3 of 7486 | Multiplexer input | A1 XOR B1 result (for bit 1) |
| Pin 6 of 7486 | Multiplexer input | A0 XOR B0 result (for bit 0) |
| Pin 8 of 7408 | Pin 13 of 7486, Carry LED | Carry from bit 0 |
| Multiplexer output | Result bit 1 LED | Final result bit 1 |
| Multiplexer output | Result bit 0 LED | Final result bit 0 |

## Testing and Verification

### Basic Operation Testing

1. **AND Operation Test** (S1=0, S0=0):
   - A1=0, A0=0, B1=0, B0=0 → Result should be 00
   - A1=0, A0=1, B1=0, B0=1 → Result should be 01
   - A1=1, A0=1, B1=1, B0=1 → Result should be 11

2. **OR Operation Test** (S1=0, S0=1):
   - A1=0, A0=0, B1=0, B0=0 → Result should be 00
   - A1=0, A0=1, B1=1, B0=0 → Result should be 11
   - A1=1, A0=1, B1=0, B0=0 → Result should be 11

3. **Addition Test** (S1=1, S0=0):
   - A1=0, A0=1, B1=0, B0=1 → Result should be 10 (no carry)
   - A1=1, A0=1, B1=0, B0=1 → Result should be 10 (with carry)
   - A1=1, A0=1, B1=1, B0=1 → Result should be 11 (with carry)

4. **Subtraction Test** (S1=1, S0=1):
   - A1=1, A0=0, B1=0, B0=1 → Result should be 01 (no borrow)
   - A1=0, A0=1, B1=1, B0=0 → Result should be 01 (with borrow)

## Comprehensive Troubleshooting Guide

### No Power Issues
1. **Issue**: No LEDs light up at all
   - **Check**: Power connections to all ICs
   - **Fix**: Verify +5V at pin 14 and GND at pin 7 of all ICs

2. **Issue**: One IC not functioning
   - **Check**: Pin 14 (+5V) and pin 7 (GND) connections for that specific IC
   - **Fix**: Reconnect power or replace IC if damaged

### Incorrect Results

1. **Issue**: Wrong output for a specific operation
   - **Check**: Connections for that operation's circuit
   - **Fix**: Trace the signal path with a multimeter or logic probe

2. **Issue**: Inconsistent results
   - **Check**: Input switch connections and pull-up resistors
   - **Fix**: Ensure switches have proper pull-ups and make good contact

3. **Issue**: Operations work but selection doesn't
   - **Check**: S1, S0 switch connections and multiplexer logic
   - **Fix**: Verify selector signals reach the appropriate gates

### Signal Integrity Issues

1. **Issue**: Intermittent operation
   - **Check**: Loose connections on the breadboard
   - **Fix**: Press components firmly into breadboard or replace breadboard

2. **Issue**: Circuit works when probed but not otherwise
   - **Check**: Pull-up/pull-down resistors for floating inputs
   - **Fix**: Add 10kOhm pull-up/pull-down resistors to any floating inputs

3. **Issue**: Circuit works initially then stops
   - **Check**: Overheating components, power supply stability
   - **Fix**: Add decoupling capacitors, check for shorts, improve cooling

## Advanced Enhancements

1. **BCD to 7-Segment Display**:
   - Add a 7447 BCD to 7-segment decoder
   - Connect to common anode 7-segment display
   - Show decimal equivalent of binary output

2. **Multiple Operation Mode**:
   - Add toggle switch for "mode select"
   - Create additional circuitry for NAND, NOR, XNOR operations
   - Expand operation selector to 3 bits

3. **Status Flags Circuit**:
   - Zero flag: NOR all output bits
   - Negative flag: Connect to MSB (for signed operations)
   - Overflow detection circuit

## Real-World Applications and Context

This 2-bit ALU is a simplified version of circuits found in all modern processors. The principles demonstrated here are fundamentally the same as those used in commercial CPUs, just scaled up to handle more bits and more complex operations.

Understanding this circuit provides insight into:
- How arithmetic operations are performed in hardware
- The relationship between logical operations and arithmetic
- How operation selection works in a CPU
- The implementation of basic adder circuits

## Additional Resources

- [Digital Logic Design Tutorial](https://www.tutorialspoint.com/digital_circuits/index.htm)
- [Ben Eater's 8-bit Computer Series](https://www.youtube.com/watch?v=HyznrdDSSGM&list=PLowKtXNTBypGqImE405J2565dvjafglHU)
- [Interactive Logic Gate Simulator](https://logic.ly/)
- [Comprehensive TTL Databook](https://archive.org/details/ttldatabook)
- [Breadboard Circuit Tips and Tricks](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all)
