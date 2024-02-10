# Print a header for the temperature unit converter
print("TEMPERATURE UNIT CONVERTER")

# Get the input temperature value and unit from the user
temp = float(input("Enter the temperature value you want to convert: "))
unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ").lower()

# Perform the conversion operation based on the user input
if unit == "c":
    # Convert Celsius to Fahrenheit
    converted_temp = (temp * 9/5) + 32
    original_unit, target_unit = "Celsius", "Fahrenheit"
elif unit == "f":
    # Convert Fahrenheit to Celsius
    converted_temp = (temp - 32) * 5/9
    original_unit, target_unit = "Fahrenheit", "Celsius"
else:
    # Handle invalid unit input
    print("Invalid unit. Please enter 'C' or 'F'.")
    exit()

# Display the converted temperature
print(f"{temp} {original_unit} is equal to {converted_temp:.2f} {target_unit}.")
