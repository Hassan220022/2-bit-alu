import React, { useState, useEffect } from 'react';

const ALUSimulator = () => {
  const [inputA, setInputA] = useState([false, false]); // A1, A0
  const [inputB, setInputB] = useState([false, false]); // B1, B0
  const [opSelect, setOpSelect] = useState([false, false, false]); // S2, S1, S0
  const [output, setOutput] = useState([false, false]); // Out1, Out0
  const [carryBorrow, setCarryBorrow] = useState(false);
  const [decimalA, setDecimalA] = useState(0);
  const [decimalB, setDecimalB] = useState(0);
  const [decimalOut, setDecimalOut] = useState(0);
  const [opName, setOpName] = useState("AND");

  // Convert binary array to decimal
  const binaryToDecimal = (binary) => {
    return binary.reduce((acc, bit, index) => acc + (bit ? Math.pow(2, binary.length - 1 - index) : 0), 0);
  };

  // Update decimal values when binary inputs change
  useEffect(() => {
    setDecimalA(binaryToDecimal(inputA));
    setDecimalB(binaryToDecimal(inputB));
    setDecimalOut(binaryToDecimal(output));
  }, [inputA, inputB, output]);

  // Toggle a bit in inputA
  const toggleA = (index) => {
    const newInputA = [...inputA];
    newInputA[index] = !newInputA[index];
    setInputA(newInputA);
  };

  // Toggle a bit in inputB
  const toggleB = (index) => {
    const newInputB = [...inputB];
    newInputB[index] = !newInputB[index];
    setInputB(newInputB);
  };

  // Toggle a bit in opSelect
  const toggleOpSelect = (index) => {
    const newOpSelect = [...opSelect];
    newOpSelect[index] = !newOpSelect[index];
    setOpSelect(newOpSelect);
  };

  // Perform ALU operations based on opSelect
  useEffect(() => {
    // Convert opSelect to decimal for easy comparison
    const opCode = binaryToDecimal(opSelect);
    let newOutput = [false, false];
    let newCarryBorrow = false;
    let operation = "";

    switch (opCode) {
      case 0: // AND
        newOutput = [inputA[0] && inputB[0], inputA[1] && inputB[1]];
        operation = "AND";
        break;
      case 1: // OR
        newOutput = [inputA[0] || inputB[0], inputA[1] || inputB[1]];
        operation = "OR";
        break;
      case 2: // XOR
        newOutput = [inputA[0] !== inputB[0], inputA[1] !== inputB[1]];
        operation = "XOR";
        break;
      case 3: // NOT A
        newOutput = [!inputA[0], !inputA[1]];
        operation = "NOT";
        break;
      case 4: { // ADD
        // Bit 0 addition
        newOutput[1] = inputA[1] !== inputB[1]; // XOR for sum
        const carry0 = inputA[1] && inputB[1]; // AND for carry

        // Bit 1 addition with carry
        newOutput[0] = inputA[0] !== inputB[0] !== carry0; // XOR with carry
        newCarryBorrow = (inputA[0] && inputB[0]) || 
                         ((inputA[0] || inputB[0]) && carry0);
        operation = "ADD";
        break;
      }
      case 5: { // SUB (A - B using 2's complement)
        // Invert B
        const notB = [!inputB[0], !inputB[1]];
        
        // Add 1 (for 2's complement) to LSB
        let sum1 = inputA[1] !== notB[1] !== true; // A0 XOR ~B0 XOR 1
        let carry1 = (inputA[1] && notB[1]) || 
                    ((inputA[1] || notB[1]) && true);
        
        // Add with carry
        let sum0 = inputA[0] !== notB[0] !== carry1;
        newCarryBorrow = !((inputA[0] && notB[0]) || 
                         ((inputA[0] || notB[0]) && carry1));
        
        newOutput = [sum0, sum1];
        operation = "SUB";
        break;
      }
      default:
        // Other opcodes not used
        operation = "UNKNOWN";
    }

    setOutput(newOutput);
    setCarryBorrow(newCarryBorrow);
    setOpName(operation);
  }, [inputA, inputB, opSelect]);

  return (
    <div className="flex flex-col items-center p-6 bg-gray-100 rounded-lg max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">2-Bit ALU Simulator</h1>
      
      <div className="w-full mb-8">
        <h2 className="text-lg font-semibold mb-2">Inputs</h2>
        <div className="flex justify-between mb-4">
          <div className="w-1/2 pr-2">
            <h3 className="font-medium">Input A: {decimalA}</h3>
            <div className="flex items-center mt-2">
              <div className="flex items-center mr-4">
                <span className="mr-2">A1:</span>
                <button 
                  onClick={() => toggleA(0)} 
                  className={`w-12 h-8 rounded ${inputA[0] ? 'bg-green-500' : 'bg-gray-300'}`}
                >
                  {inputA[0] ? '1' : '0'}
                </button>
              </div>
              <div className="flex items-center">
                <span className="mr-2">A0:</span>
                <button 
                  onClick={() => toggleA(1)} 
                  className={`w-12 h-8 rounded ${inputA[1] ? 'bg-green-500' : 'bg-gray-300'}`}
                >
                  {inputA[1] ? '1' : '0'}
                </button>
              </div>
            </div>
          </div>
          
          <div className="w-1/2 pl-2">
            <h3 className="font-medium">Input B: {decimalB}</h3>
            <div className="flex items-center mt-2">
              <div className="flex items-center mr-4">
                <span className="mr-2">B1:</span>
                <button 
                  onClick={() => toggleB(0)} 
                  className={`w-12 h-8 rounded ${inputB[0] ? 'bg-green-500' : 'bg-gray-300'}`}
                >
                  {inputB[0] ? '1' : '0'}
                </button>
              </div>
              <div className="flex items-center">
                <span className="mr-2">B0:</span>
                <button 
                  onClick={() => toggleB(1)} 
                  className={`w-12 h-8 rounded ${inputB[1] ? 'bg-green-500' : 'bg-gray-300'}`}
                >
                  {inputB[1] ? '1' : '0'}
                </button>
              </div>
            </div>
          </div>
        </div>
        
        <div className="mt-4">
          <h3 className="font-medium">Operation Select: {opName}</h3>
          <div className="flex items-center mt-2">
            <div className="flex items-center mr-4">
              <span className="mr-2">S2:</span>
              <button 
                onClick={() => toggleOpSelect(0)} 
                className={`w-12 h-8 rounded ${opSelect[0] ? 'bg-blue-500' : 'bg-gray-300'}`}
              >
                {opSelect[0] ? '1' : '0'}
              </button>
            </div>
            <div className="flex items-center mr-4">
              <span className="mr-2">S1:</span>
              <button 
                onClick={() => toggleOpSelect(1)} 
                className={`w-12 h-8 rounded ${opSelect[1] ? 'bg-blue-500' : 'bg-gray-300'}`}
              >
                {opSelect[1] ? '1' : '0'}
              </button>
            </div>
            <div className="flex items-center">
              <span className="mr-2">S0:</span>
              <button 
                onClick={() => toggleOpSelect(2)} 
                className={`w-12 h-8 rounded ${opSelect[2] ? 'bg-blue-500' : 'bg-gray-300'}`}
              >
                {opSelect[2] ? '1' : '0'}
              </button>
            </div>
          </div>
        </div>
      </div>
      
      <div className="w-full">
        <h2 className="text-lg font-semibold mb-2">Outputs</h2>
        <div className="flex items-center mb-4">
          <h3 className="font-medium mr-4">Result: {decimalOut}</h3>
          <div className="flex items-center mr-4">
            <span className="mr-2">Out1:</span>
            <div className={`w-12 h-8 rounded flex items-center justify-center ${output[0] ? 'bg-red-500' : 'bg-gray-300'}`}>
              {output[0] ? '1' : '0'}
            </div>
          </div>
          <div className="flex items-center">
            <span className="mr-2">Out0:</span>
            <div className={`w-12 h-8 rounded flex items-center justify-center ${output[1] ? 'bg-red-500' : 'bg-gray-300'}`}>
              {output[1] ? '1' : '0'}
            </div>
          </div>
        </div>
        
        <div className="flex items-center">
          <h3 className="font-medium mr-4">Carry/Borrow:</h3>
          <div className={`w-12 h-8 rounded flex items-center justify-center ${carryBorrow ? 'bg-purple-500' : 'bg-gray-300'}`}>
            {carryBorrow ? '1' : '0'}
          </div>
        </div>
      </div>
      
      <div className="w-full mt-8 p-4 bg-white rounded shadow">
        <h2 className="text-lg font-semibold mb-2">Operation Guide</h2>
        <ul className="text-sm">
          <li>000: A AND B - Bitwise AND operation</li>
          <li>001: A OR B - Bitwise OR operation</li>
          <li>010: A XOR B - Bitwise XOR operation</li>
          <li>011: NOT A - Bitwise NOT of input A</li>
          <li>100: A + B - Addition with carry</li>
          <li>101: A - B - Subtraction using 2's complement</li>
        </ul>
      </div>
      
      <div className="w-full mt-4 p-4 bg-blue-50 rounded shadow">
        <h2 className="text-lg font-semibold mb-2">Current Operation</h2>
        <div className="flex justify-between items-center">
          <div>
            <p><strong>Operation:</strong> {opName} (Opcode: {opSelect.map(bit => bit ? '1' : '0').join('')})</p>
            <p><strong>Inputs:</strong> A={inputA.map(bit => bit ? '1' : '0').join('')} ({decimalA}), B={inputB.map(bit => bit ? '1' : '0').join('')} ({decimalB})</p>
          </div>
          <div>
            <p><strong>Result:</strong> {output.map(bit => bit ? '1' : '0').join('')} ({decimalOut})</p>
            <p><strong>Carry/Borrow:</strong> {carryBorrow ? '1' : '0'}</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ALUSimulator;
