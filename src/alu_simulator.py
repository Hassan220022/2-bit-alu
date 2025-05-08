"""
2-Bit ALU Simulator
This module simulates the functionality of a 2-bit ALU with operations:
- Bitwise AND, OR, XOR
- Addition and Subtraction (using 2's complement)
- NOT (1's complement)
"""

class ALU:
    """A 2-bit Arithmetic Logic Unit implementation"""
    
    # Operation codes
    AND = 0b000
    OR  = 0b001
    XOR = 0b010
    ADD = 0b011
    SUB = 0b100
    NOT = 0b101
    
    def __init__(self):
        """Initialize the ALU"""
        self.operations = {
            self.AND: self._and,
            self.OR: self._or,
            self.XOR: self._xor,
            self.ADD: self._add,
            self.SUB: self._sub,
            self.NOT: self._not
        }
        
    def _and(self, a, b):
        """Perform bitwise AND operation"""
        return a & b, 0  # No carry in AND operation
    
    def _or(self, a, b):
        """Perform bitwise OR operation"""
        return a | b, 0  # No carry in OR operation
    
    def _xor(self, a, b):
        """Perform bitwise XOR operation"""
        return a ^ b, 0  # No carry in XOR operation
    
    def _add(self, a, b):
        """Perform addition operation with carry"""
        result = a + b
        carry = 1 if result > 3 else 0  # Detect carry out
        return result & 0b11, carry  # Mask to 2 bits
    
    def _sub(self, a, b):
        """Perform subtraction using 2's complement"""
        # 2's complement of b (for 2-bit numbers) is (4-b)%4
        b_complement = (-b) & 0b11  # 2's complement representation
        result = (a + b_complement) & 0b11
        borrow = 1 if a < b else 0
        return result, borrow
    
    def _not(self, a, _):
        """Perform NOT operation (1's complement)"""
        # For 2-bit number, NOT is equivalent to 3-a
        return (~a) & 0b11, 0  # No carry in NOT operation
    
    def execute(self, op_code, a, b):
        """
        Execute the ALU operation
        
        Args:
            op_code (int): 3-bit operation code
            a (int): 2-bit input A (0-3)
            b (int): 2-bit input B (0-3)
            
        Returns:
            tuple: (result, carry/borrow)
        """
        # Validate inputs
        if not (0 <= a <= 3 and 0 <= b <= 3):
            raise ValueError("Inputs must be 2-bit values (0-3)")
        
        if op_code not in self.operations:
            raise ValueError(f"Invalid operation code: {op_code}")
        
        # Execute the operation
        return self.operations[op_code](a, b)


def format_binary(num, width=2):
    """Format number as binary string with specified width"""
    return bin(num)[2:].zfill(width)


def main():
    """Main function to demonstrate the ALU functionality"""
    alu = ALU()
    
    # Test all operations with different input combinations
    test_operations = [
        ("AND", ALU.AND),
        ("OR", ALU.OR),
        ("XOR", ALU.XOR),
        ("ADD", ALU.ADD),
        ("SUB", ALU.SUB),
        ("NOT", ALU.NOT)
    ]
    
    print("2-BIT ALU SIMULATOR")
    print("===================")
    
    # Generate all possible 2-bit input combinations
    inputs = [(a, b) for a in range(4) for b in range(4)]
    
    for op_name, op_code in test_operations:
        print(f"\nOperation: {op_name} (Code: {format_binary(op_code, 3)})")
        print("-" * 40)
        print("  A  |  B  | Result | Carry/Borrow")
        print("-" * 40)
        
        for a, b in inputs:
            result, carry = alu.execute(op_code, a, b)
            print(f" {format_binary(a)} | {format_binary(b)} |   {format_binary(result)}   |     {carry}")
    
    print("\nInteractive Mode:")
    while True:
        try:
            print("\nSelect operation:")
            for i, (name, _) in enumerate(test_operations):
                print(f"{i}. {name}")
            
            print("q. Quit")
            choice = input("Choice: ").strip().lower()
            
            if choice == 'q':
                break
                
            op_index = int(choice)
            if 0 <= op_index < len(test_operations):
                a = int(input("Enter A (0-3): "))
                b = int(input("Enter B (0-3): "))
                
                if 0 <= a <= 3 and 0 <= b <= 3:
                    _, op_code = test_operations[op_index]
                    result, carry = alu.execute(op_code, a, b)
                    print(f"Result: {format_binary(result)} (Carry/Borrow: {carry})")
                else:
                    print("Inputs must be 2-bit values (0-3)")
            else:
                print("Invalid choice")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
