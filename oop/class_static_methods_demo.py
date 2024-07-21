class Calculator:
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        """Performs addition of two numbers.

        Args:
            a (int): First number.
            b (int): Second number.

        Returns:
            int: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Performs multiplication of two numbers.

        Args:
            cls (class): The Calculator class itself.
            a (int): First number.
            b (int): Second number.

        Returns:
            int: The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# You can add more methods here (e.g., subtract, divide)
