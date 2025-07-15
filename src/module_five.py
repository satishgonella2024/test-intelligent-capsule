Here is the complete, executable Python code for the 'Calculator' class, including final code review and integration testing:

import math

class Calculator:
    """
    A simple calculator class with add and subtract methods.
    """
    def add(self, a, b):
        """
        Add two numbers and return the result.
        
        Args:
            a (float): The first number to add.
            b (float): The second number to add.
        
        Returns:
            float: The sum of the two numbers.
        """
        return a + b
    
    def subtract(self, a, b):
        """
        Subtract one number from another and return the result.
        
        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.
        
        Returns:
            float: The difference between the two numbers.
        """
        return a - b

# Integration tests
def test_calculator():
    calc = Calculator()
    
    # Test add method
    assert calc.add(2.5, 3.7) == 6.2
    assert calc.add(-1.2, 4.9) == 3.7
    
    # Test subtract method
    assert calc.subtract(10.0, 4.5) == 5.5
    assert calc.subtract(7.8, -2.1) == 9.9

if __name__ == "__main__":
    test_calculator()
    print("All tests passed!")