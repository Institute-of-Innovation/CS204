# Function to convert temperature
def convert_temperature(temp, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'F':
        return (temp * 9/5) + 32
    elif from_unit == 'C' and to_unit == 'K':
        return temp + 273.15
    elif from_unit == 'F' and to_unit == 'C':
        return (temp - 32) * 5/9
    elif from_unit == 'F' and to_unit == 'K':
        return (temp - 32) * 5/9 + 273.15
    elif from_unit == 'K' and to_unit == 'C':
        return temp - 273.15
    elif from_unit == 'K' and to_unit == 'F':
        return (temp - 273.15) * 9/5 + 32
    elif from_unit == to_unit:
        return temp  # No conversion needed
    else:
        return "Invalid input"

# User input
temp = float(input("Enter temperature value: "))
from_unit = input("Enter current unit (C/F/K): ").upper()
to_unit = input("Enter unit to convert to (C/F/K): ").upper()

# Convert and display result
result = convert_temperature(temp, from_unit, to_unit)
print(f"Converted temperature: {result} {to_unit}" if isinstance(result, (int, float)) else result)