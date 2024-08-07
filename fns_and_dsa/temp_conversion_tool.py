FAHRENHEIT_TO_CELSIUS_FACTOR  = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  

def convert_to_celsius(fahrenheit):
      return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  # Subtract 32 first

def convert_to_fahrenheit(celsius):
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
while True:
      try: 
        temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
      if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        unit_label = "°C"
        converted_unit_label = "°F"
      elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        unit_label = "°F"
        converted_unit_label = "°C"
      else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
      print(f"{temperature:.1f}{unit_label} is {converted_temp:.2f}{converted_unit_label}")
      break

