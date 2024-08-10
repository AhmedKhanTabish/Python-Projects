

# conversion of Fahrenheit to Celsius
temp_in = input("Is your temperature in Celsius or Fahrenheit: ")
converse_type = input("To which unit do you want to convert your value (Kelvin, Celsius, Fahrenheit): ")
if converse_type == "Kelvin":
    if temp_in == "Celsius" or "celsius" or "C":
        celsius = int(input("enter the temperature in celsius : "))
        Kelvin = temp_in + 273
        print(Kelvin)
    elif temp_in == "Fahrenheit" or "fahrenheit" or "F":
        fahrenheit = int(input("enter the temperature in fahrenheit : "))
        Kelvin = ((fahrenheit - 32) * 5 / 9) + 273
        print(Kelvin)
    else:
        print('INVALID INPUT', "Please enter the temperature in correct units")
elif converse_type == "Celsius" and temp_in == ("Fahrenheit" or "fahrenheit" or "F"):  # conversion of Fahrenheit to Celsius
    fahrenheit = int(input("enter the temperature in fahrenheit : "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(celsius)
elif converse_type == "Fahrenheit" and temp_in == "Celsius" or "celsius" or "C":    # conversion of Celsius to Fahrenheit
    celsius = int(input("enter the temperature in celsius : "))
    fahrenheit = celsius * 9 / 5 + 32
    print(fahrenheit)