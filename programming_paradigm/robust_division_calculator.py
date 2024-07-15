def safe_divide(numerator, denominator):
  """
  Performs division with error handling for division by zero and non-numeric inputs.

  Args:
      numerator: The numerator (dividend) for the division.
      denominator: The denominator (divisor) for the division.

  Returns:
      A string message indicating the result or error encountered.
  """
  try:
    # Attempt conversion to floats for numeric division
    result = float(numerator) / float(denominator)
    return f"The result of the division is {result:.2f}"
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  except ValueError:
    return "Error: Please enter numeric values only."

