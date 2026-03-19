# Day 8: Temperature Converter
# Converts between Celsius, Fahrenheit, and Kelvin

print("=" * 30)
print("  TEMPERATURE CONVERTER")
print("=" * 30)

# These are functions that take the parameters and return the values
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    result = (celsius * 9/5) + 32
    return result  # Here it's returning a value

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    result = (fahrenheit - 32) * 5/9
    return result

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    result = celsius + 273.15
    return result

# The main menu
while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Quit")
    
    choice = input("\nChoose (1-4): ")
    
    if choice == "1":
        # Celsius to Fahrenheit
        try:
            temp = float(input("Enter temperature in Celsius: "))
            converted = celsius_to_fahrenheit(temp)  # Call function
            print(f"{temp}°C = {converted}°F")
        except:
            print("Please enter a valid number!")
    
    elif choice == "2":
        # Fahrenheit to Celsius
        try:
            temp = float(input("Enter temperature in Fahrenheit: "))
            converted = fahrenheit_to_celsius(temp)  # Call function
            print(f"{temp}°F = {converted}°C")
        except:
            print("Please enter a valid number!")
    
    elif choice == "3":
        # Celsius to Kelvin
        try:
            temp = float(input("Enter temperature in Celsius: "))
            converted = celsius_to_kelvin(temp)  # Call function
            print(f"{temp}°C = {converted}K")
        except:
            print("Please enter a valid number!")
    
    elif choice == "4":
        print("Goodbye ")
        break
    
    else:
        print("Invalid choice")