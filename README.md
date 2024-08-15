# RISC-V Custom Vector Extension Simulation
![image](image.jpg)


This project simulates a simplified version of a custom vector extension that could be realized on a RISC-V architecture. The main functionality includes loading data into a vector register and performing vector addition.

## Project Structure
- `main.py` - Contains the implementation of the RISC-V custom extension.
- `test_vector_extension.py` - Contains unit tests for validating the functionality of the vector extension.

## Requirements
- Python 3.x
- NumPy library (install with `pip install numpy`)

## How to Run the Project
1. Clone this repository to your local machine.
2. Open your terminal and navigate to the project directory.
3. Run the main program:
   ```
   python main.py
   ```  
   This will demonstrate vector addition using the custom RISC-V extension simulation.
4. Run the tests to validate the implementation:
   ```
   python test_vector_extension.py
   ```  
   You should see a message indicating all tests passed.

## Features
- **Loading data into vector registers**: Supports basic loading of data for operations.
- **Performing vector addition**: Demonstrates the functionality of adding two vectors.
- **Testing for compatibility**: Ensures that vectors can only be added if they are of the same length.

## Future Improvements
- Implement more vector operations such as subtraction, multiplication, etc.
- Expand the simulation to include additional features of RISC-V vector extensions.
- Create a more detailed hardware simulation using an HDL (Hardware Description Language).

## License
This project is open-source and available under the MIT License.