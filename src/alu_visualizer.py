"""
2-Bit ALU Visualizer
This module provides a GUI to visualize the 2-bit ALU operations
and show the corresponding logic gate connections.
"""

import tkinter as tk
from tkinter import ttk
import math
from alu_simulator import ALU, format_binary

class LogicGate:
    """Represents a logic gate for drawing"""
    def __init__(self, canvas, x, y, gate_type, inputs=None, label=""):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.type = gate_type
        self.inputs = inputs or []
        self.label = label
        self.width = 60
        self.height = 40
        self.output_x = x + self.width
        self.output_y = y + self.height/2
        
    def draw(self):
        """Draw the logic gate on the canvas"""
        if self.type == "AND":
            # Draw AND gate
            self.canvas.create_rectangle(self.x, self.y, self.x + self.width*0.7, self.y + self.height)
            self.canvas.create_arc(
                self.x + self.width*0.2, self.y, 
                self.x + self.width*1.1, self.y + self.height,
                start=270, extent=180, style="chord"
            )
        elif self.type == "OR":
            # Draw OR gate
            self.canvas.create_arc(
                self.x - self.width*0.2, self.y, 
                self.x + self.width*0.7, self.y + self.height,
                start=270, extent=180, style="chord"
            )
            self.canvas.create_arc(
                self.x - self.width*0.1, self.y, 
                self.x + self.width*0.8, self.y + self.height,
                start=270, extent=180, style="chord"
            )
        elif self.type == "XOR":
            # Draw XOR gate (OR with extra curve)
            self.canvas.create_arc(
                self.x - self.width*0.2, self.y, 
                self.x + self.width*0.7, self.y + self.height,
                start=270, extent=180, style="chord"
            )
            self.canvas.create_arc(
                self.x - self.width*0.1, self.y, 
                self.x + self.width*0.8, self.y + self.height,
                start=270, extent=180, style="chord"
            )
            self.canvas.create_arc(
                self.x - self.width*0.3, self.y, 
                self.x + self.width*0.6, self.y + self.height,
                start=270, extent=180, style="arc"
            )
        elif self.type == "NOT":
            # Draw NOT gate
            self.canvas.create_polygon(
                self.x, self.y,
                self.x, self.y + self.height,
                self.x + self.width*0.7, self.y + self.height/2
            )
            self.canvas.create_oval(
                self.x + self.width*0.7, self.y + self.height/2 - 5,
                self.x + self.width*0.7 + 10, self.y + self.height/2 + 5
            )
            
        # Draw label
        self.canvas.create_text(self.x + self.width/2, self.y - 10, text=self.label)
        
        # Draw output line
        self.canvas.create_line(
            self.output_x, self.output_y, 
            self.output_x + 30, self.output_y
        )
        
        # Draw input lines
        input_spacing = self.height / (len(self.inputs) + 1)
        for i, input_label in enumerate(self.inputs):
            input_y = self.y + input_spacing * (i + 1)
            self.canvas.create_line(self.x - 30, input_y, self.x, input_y)
            self.canvas.create_text(self.x - 40, input_y, text=input_label)


class ALUVisualizer:
    """GUI for visualizing the 2-bit ALU operations"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("2-Bit ALU Visualizer")
        self.root.geometry("900x600")
        self.alu = ALU()
        
        self.create_widgets()
        
    def create_widgets(self):
        """Create all the GUI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input frame
        input_frame = ttk.LabelFrame(main_frame, text="Inputs", padding="10")
        input_frame.pack(fill=tk.X, pady=5)
        
        # Input A
        ttk.Label(input_frame, text="Input A (2-bit):").grid(row=0, column=0, padx=5, pady=5)
        self.input_a_var = tk.StringVar(value="00")
        self.a_bit1 = ttk.Checkbutton(input_frame, text="Bit 1", command=self.update_a)
        self.a_bit1.grid(row=0, column=1)
        self.a_bit0 = ttk.Checkbutton(input_frame, text="Bit 0", command=self.update_a)
        self.a_bit0.grid(row=0, column=2)
        ttk.Label(input_frame, textvariable=self.input_a_var).grid(row=0, column=3, padx=5)
        
        # Input B
        ttk.Label(input_frame, text="Input B (2-bit):").grid(row=1, column=0, padx=5, pady=5)
        self.input_b_var = tk.StringVar(value="00")
        self.b_bit1 = ttk.Checkbutton(input_frame, text="Bit 1", command=self.update_b)
        self.b_bit1.grid(row=1, column=1)
        self.b_bit0 = ttk.Checkbutton(input_frame, text="Bit 0", command=self.update_b)
        self.b_bit0.grid(row=1, column=2)
        ttk.Label(input_frame, textvariable=self.input_b_var).grid(row=1, column=3, padx=5)
        
        # Operation selector
        ttk.Label(input_frame, text="Operation:").grid(row=2, column=0, padx=5, pady=5)
        self.op_var = tk.StringVar(value="AND")
        op_combobox = ttk.Combobox(input_frame, textvariable=self.op_var, 
                                   values=["AND", "OR", "XOR", "ADD", "SUB", "NOT"])
        op_combobox.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
        op_combobox.bind("<<ComboboxSelected>>", self.update_display)
        
        # Result frame
        result_frame = ttk.LabelFrame(main_frame, text="Result", padding="10")
        result_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(result_frame, text="Result (2-bit):").grid(row=0, column=0, padx=5, pady=5)
        self.result_var = tk.StringVar(value="00")
        ttk.Label(result_frame, textvariable=self.result_var).grid(row=0, column=1, padx=5)
        
        ttk.Label(result_frame, text="Carry/Borrow:").grid(row=1, column=0, padx=5, pady=5)
        self.carry_var = tk.StringVar(value="0")
        ttk.Label(result_frame, textvariable=self.carry_var).grid(row=1, column=1, padx=5)
        
        # Canvas for visualization
        self.canvas_frame = ttk.LabelFrame(main_frame, text="Circuit Visualization", padding="10")
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.canvas = tk.Canvas(self.canvas_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Update the display initially
        self.update_display()
        
    def update_a(self):
        """Update input A based on checkbuttons"""
        a_val = (1 if self.a_bit1.instate(['selected']) else 0) * 2 + \
                (1 if self.a_bit0.instate(['selected']) else 0)
        self.input_a_var.set(format_binary(a_val))
        self.update_display()
        
    def update_b(self):
        """Update input B based on checkbuttons"""
        b_val = (1 if self.b_bit1.instate(['selected']) else 0) * 2 + \
                (1 if self.b_bit0.instate(['selected']) else 0)
        self.input_b_var.set(format_binary(b_val))
        self.update_display()
        
    def update_display(self, *args):
        """Update the result and visualization based on current inputs"""
        try:
            # Get inputs
            a_val = int(self.input_a_var.get(), 2)
            b_val = int(self.input_b_var.get(), 2)
            op_name = self.op_var.get()
            
            # Map operation name to code
            op_map = {
                "AND": ALU.AND,
                "OR": ALU.OR,
                "XOR": ALU.XOR,
                "ADD": ALU.ADD,
                "SUB": ALU.SUB,
                "NOT": ALU.NOT
            }
            
            # Execute operation
            op_code = op_map[op_name]
            result, carry = self.alu.execute(op_code, a_val, b_val)
            
            # Update result display
            self.result_var.set(format_binary(result))
            self.carry_var.set(str(carry))
            
            # Update visualization
            self.draw_circuit(op_name, a_val, b_val, result, carry)
            
        except Exception as e:
            print(f"Error updating display: {e}")
    
    def draw_circuit(self, op_name, a_val, b_val, result, carry):
        """Draw the circuit diagram for the selected operation"""
        # Clear canvas
        self.canvas.delete("all")
        
        # Draw title
        self.canvas.create_text(450, 30, text=f"2-Bit ALU: {op_name} Operation", font=("Arial", 16))
        
        # Draw input bits as switches
        self.draw_input_bits(a_val, b_val)
        
        # Draw operation-specific circuit
        if op_name == "AND":
            self.draw_and_circuit(a_val, b_val, result)
        elif op_name == "OR":
            self.draw_or_circuit(a_val, b_val, result)
        elif op_name == "XOR":
            self.draw_xor_circuit(a_val, b_val, result)
        elif op_name == "ADD":
            self.draw_add_circuit(a_val, b_val, result, carry)
        elif op_name == "SUB":
            self.draw_sub_circuit(a_val, b_val, result, carry)
        elif op_name == "NOT":
            self.draw_not_circuit(a_val, result)
            
        # Draw output LEDs
        self.draw_output_leds(result, carry)
    
    def draw_input_bits(self, a_val, b_val):
        """Draw the input bits as switches"""
        self.canvas.create_text(80, 80, text="Input A:", font=("Arial", 12))
        self.canvas.create_text(110, 110, text=f"A[1] = {a_val >> 1}")
        self.canvas.create_text(110, 140, text=f"A[0] = {a_val & 1}")
        
        self.canvas.create_text(80, 180, text="Input B:", font=("Arial", 12))
        self.canvas.create_text(110, 210, text=f"B[1] = {b_val >> 1}")
        self.canvas.create_text(110, 240, text=f"B[0] = {b_val & 1}")
    
    def draw_output_leds(self, result, carry):
        """Draw the output LEDs"""
        self.canvas.create_text(750, 100, text="Output:", font=("Arial", 12))
        
        # Result bit 1
        led_color = "red" if result & 2 else "white"
        self.canvas.create_oval(750, 130, 780, 160, fill=led_color, outline="black")
        self.canvas.create_text(790, 145, text=f"Result[1] = {result >> 1}")
        
        # Result bit 0
        led_color = "red" if result & 1 else "white"
        self.canvas.create_oval(750, 180, 780, 210, fill=led_color, outline="black")
        self.canvas.create_text(790, 195, text=f"Result[0] = {result & 1}")
        
        # Carry/Borrow
        if carry is not None:
            led_color = "red" if carry else "white"
            self.canvas.create_oval(750, 230, 780, 260, fill=led_color, outline="black")
            self.canvas.create_text(790, 245, text=f"Carry/Borrow = {carry}")
    
    def draw_and_circuit(self, a_val, b_val, result):
        """Draw the AND circuit"""
        # Draw bit 1 AND gate
        and1 = LogicGate(self.canvas, 350, 100, "AND", ["A[1]", "B[1]"], "AND1")
        and1.draw()
        
        # Draw bit 0 AND gate
        and0 = LogicGate(self.canvas, 350, 200, "AND", ["A[0]", "B[0]"], "AND0")
        and0.draw()
        
        # Connect to outputs
        self.canvas.create_line(and1.output_x + 30, and1.output_y, 750, 145)
        self.canvas.create_line(and0.output_x + 30, and0.output_y, 750, 195)
    
    def draw_or_circuit(self, a_val, b_val, result):
        """Draw the OR circuit"""
        # Draw bit 1 OR gate
        or1 = LogicGate(self.canvas, 350, 100, "OR", ["A[1]", "B[1]"], "OR1")
        or1.draw()
        
        # Draw bit 0 OR gate
        or0 = LogicGate(self.canvas, 350, 200, "OR", ["A[0]", "B[0]"], "OR0")
        or0.draw()
        
        # Connect to outputs
        self.canvas.create_line(or1.output_x + 30, or1.output_y, 750, 145)
        self.canvas.create_line(or0.output_x + 30, or0.output_y, 750, 195)
    
    def draw_xor_circuit(self, a_val, b_val, result):
        """Draw the XOR circuit"""
        # Draw bit 1 XOR gate
        xor1 = LogicGate(self.canvas, 350, 100, "XOR", ["A[1]", "B[1]"], "XOR1")
        xor1.draw()
        
        # Draw bit 0 XOR gate
        xor0 = LogicGate(self.canvas, 350, 200, "XOR", ["A[0]", "B[0]"], "XOR0")
        xor0.draw()
        
        # Connect to outputs
        self.canvas.create_line(xor1.output_x + 30, xor1.output_y, 750, 145)
        self.canvas.create_line(xor0.output_x + 30, xor0.output_y, 750, 195)
    
    def draw_add_circuit(self, a_val, b_val, result, carry):
        """Draw the ADD circuit (simplified)"""
        # Half adders and OR gate for simplified view
        ha1 = LogicGate(self.canvas, 250, 100, "XOR", ["A[0]", "B[0]"], "HA1-Sum")
        ha1.draw()
        
        ha2 = LogicGate(self.canvas, 250, 180, "AND", ["A[0]", "B[0]"], "HA1-Carry")
        ha2.draw()
        
        ha3 = LogicGate(self.canvas, 400, 100, "XOR", ["A[1]", "B[1]"], "HA2-Sum")
        ha3.draw()
        
        ha4 = LogicGate(self.canvas, 400, 180, "AND", ["A[1]", "B[1]"], "HA2-Carry")
        ha4.draw()
        
        ha5 = LogicGate(self.canvas, 550, 130, "XOR", ["HA2-Sum", "HA1-Carry"], "R[1]")
        ha5.draw()
        
        or1 = LogicGate(self.canvas, 550, 230, "OR", ["HA2-Carry", "Carry-Internal"], "Carry")
        or1.draw()
        
        # Connect the gates
        self.canvas.create_line(ha1.output_x + 30, ha1.output_y, 750, 195)  # R[0]
        self.canvas.create_line(ha2.output_x + 30, ha2.output_y, 450, 150)
        self.canvas.create_text(420, 140, text="Carry-Internal")
        
        self.canvas.create_line(ha5.output_x + 30, ha5.output_y, 750, 145)  # R[1]
        self.canvas.create_line(or1.output_x + 30, or1.output_y, 750, 245)  # Carry
    
    def draw_sub_circuit(self, a_val, b_val, result, borrow):
        """Draw the SUB circuit (simplified)"""
        # For subtraction, we'll show converter to 2's complement and then adder
        not1 = LogicGate(self.canvas, 200, 100, "NOT", ["B[1]"], "NOT-B[1]")
        not1.draw()
        
        not0 = LogicGate(self.canvas, 200, 180, "NOT", ["B[0]"], "NOT-B[0]")
        not0.draw()
        
        # Show simplified 2's complement logic
        self.canvas.create_text(350, 240, text="2's Complement Logic", font=("Arial", 10))
        self.canvas.create_text(350, 260, text="B' = NOT(B) + 1", font=("Arial", 8))
        
        # And then reuse add circuit visualization
        ha1 = LogicGate(self.canvas, 450, 100, "XOR", ["A[1]", "B'[1]"], "R[1]")
        ha1.draw()
        
        ha0 = LogicGate(self.canvas, 450, 180, "XOR", ["A[0]", "B'[0]"], "R[0]")
        ha0.draw()
        
        borrow_gate = LogicGate(self.canvas, 450, 260, "AND", ["Borrow Logic"], "Borrow")
        borrow_gate.draw()
        
        # Connect to outputs
        self.canvas.create_line(ha1.output_x + 30, ha1.output_y, 750, 145)
        self.canvas.create_line(ha0.output_x + 30, ha0.output_y, 750, 195)
        self.canvas.create_line(borrow_gate.output_x + 30, borrow_gate.output_y, 750, 245)
    
    def draw_not_circuit(self, a_val, result):
        """Draw the NOT circuit"""
        # Draw bit 1 NOT gate
        not1 = LogicGate(self.canvas, 350, 100, "NOT", ["A[1]"], "NOT1")
        not1.draw()
        
        # Draw bit 0 NOT gate
        not0 = LogicGate(self.canvas, 350, 200, "NOT", ["A[0]"], "NOT0")
        not0.draw()
        
        # Connect to outputs
        self.canvas.create_line(not1.output_x + 30, not1.output_y, 750, 145)
        self.canvas.create_line(not0.output_x + 30, not0.output_y, 750, 195)


if __name__ == "__main__":
    root = tk.Tk()
    app = ALUVisualizer(root)
    root.mainloop()
