class Calculator:
    """
    A simple calculator class that provides addition and subtraction operations.

    Attributes:
        None

    Methods:
        add(self, a: float, b: float) -> float:
            Adds two numbers and returns the result.

            Args:
                a (float): The first number to add.
                b (float): The second number to add.

            Returns:
                float: The sum of the two input numbers.

            Raises:
                TypeError: If either `a` or `b` is not a number.

        subtract(self, a: float, b: float) -> float:
            Subtracts one number from another and returns the result.

            Args:
                a (float): The number to subtract from.
                b (float): The number to subtract.

            Returns:
                float: The difference between the two input numbers.

            Raises:
                TypeError: If either `a` or `b` is not a number.
    """

    def add(self, a: float, b: float) -> float:
        """
        Adds two numbers and returns the result.

        Args:
            a (float): The first number to add.
            b (float): The second number to add.

        Returns:
            float: The sum of the two input numbers.

        Raises:
            TypeError: If either `a` or `b` is not a number.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers.")
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtracts one number from another and returns the result.

        Args:
            a (float): The number to subtract from.
            b (float): The number to subtract.

        Returns:
            float: The difference between the two input numbers.

        Raises:
            TypeError: If either `a` or `b` is not a number.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers.")
        return a - b