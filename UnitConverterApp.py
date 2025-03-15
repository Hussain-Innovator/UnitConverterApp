def length_conversion(value, from_unit, to_unit):
    """Converts length between meters, feet, and inches."""
    conversion_rates = {
        "meters": 1,
        "feet": 3.28084,
        "inches": 39.3701
    }

    if from_unit not in conversion_rates or to_unit not in conversion_rates:
        return "Invalid unit selection!"

    # Convert to meters first, then to the target unit
    value_in_meters = value / conversion_rates[from_unit]
    converted_value = value_in_meters * conversion_rates[to_unit]

    return round(converted_value, 4)


def temperature_conversion(value, from_unit, to_unit):
    """Converts temperature between Celsius and Fahrenheit."""
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return round((value * 9/5) + 32, 2)
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return round((value - 32) * 5/9, 2)
    else:
        return "Invalid unit selection!"


# Execution Loop
while True:
    print("\n🔹 Unit Converter 🔹")
    print("1️⃣ Length Conversion (meters, feet, inches)")
    print("2️⃣ Temperature Conversion (Celsius, Fahrenheit)")
    print("3️⃣ Exit")

    choice = input("Select an option (1/2/3): ").strip()

    if choice == "1":
        try:
            value = float(input("Enter the length value: "))
            from_unit = input("From unit (meters, feet, inches): ").strip().lower()
            to_unit = input("To unit (meters, feet, inches): ").strip().lower()

            result = length_conversion(value, from_unit, to_unit)
            print(f"✅ Converted Value: {result} {to_unit}")

        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")

    elif choice == "2":
        try:
            value = float(input("Enter the temperature: "))
            from_unit = input("From unit (Celsius or Fahrenheit): ").strip()
            to_unit = input("To unit (Celsius or Fahrenheit): ").strip()

            result = temperature_conversion(value, from_unit, to_unit)
            print(f"✅ Converted Value: {result} {to_unit}")

        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")

    elif choice == "3":
        print("🚀 Exiting the program. Have a great day!")
        break

    else:
        print("❌ Invalid choice! Please enter 1, 2, or 3.")
