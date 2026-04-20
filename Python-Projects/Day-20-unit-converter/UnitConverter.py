# Day 20: Simple Unit Converter

print("=" * 35)
print("      UNIT CONVERTER")
print("=" * 35)

while True:
    print("\n" + "-" * 30)
    print("1. cm to inches")
    print("2. inches to cm")
    print("3. kg to pounds")
    print("4. pounds to kg")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Exit")
    print("-" * 30)
    
    choice = input("Choose (1-7): ")
    
    if choice == "1":
        # from cm to inches
        try:
            cm = float(input("Enter centimeters: "))
            inches = cm / 2.54  # NEW: conversion formula
            print(f"{cm} cm = {inches:.2f} inches")
        except:
            print("Invalid number!")
    
    elif choice == "2":
        # from inches to cm
        try:
            inches = float(input("Enter inches: "))
            cm = inches * 2.54
            print(f"{inches} inches = {cm:.2f} cm")
        except:
            print("Invalid number!")
    
    elif choice == "3":
        # from kg to pounds
        try:
            kg = float(input("Enter kilograms: "))
            pounds = kg * 2.20462
            print(f"{kg} kg = {pounds:.2f} pounds")
        except:
            print("Invalid number!")
    
    elif choice == "4":
        # from pounds to kg
        try:
            pounds = float(input("Enter pounds: "))
            kg = pounds / 2.20462
            print(f"{pounds} pounds = {kg:.2f} kg")
        except:
            print("Invalid number!")
    
    elif choice == "5":
        # from celsius to fahrenheit
        try:
            celsius = float(input("Enter Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit:.1f}°F")
        except:
            print("Invalid number!")
    
    elif choice == "6":
        # from fahrenheit to celsius
        try:
            fahrenheit = float(input("Enter Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F = {celsius:.1f}°C")
        except:
            print("Invalid number!")
    
    elif choice == "7":
        print("\nGoodbye!")
        break
    
    else:
        print("Invalid choice!")