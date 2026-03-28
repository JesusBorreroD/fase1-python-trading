try:
    temp_1 = float(input("Ingrese la temperatura a convertir: "))
except ValueError:
    print("Error: debes ingresar un número válido.")
    exit()

escala_1 = input("Es Fahrenheit (F) o Celsius (C)?: ").upper().strip()

if escala_1 == "C":
    temp_2 = ((9/5) * temp_1) + 32
    print(f"La temperatura equivale a {temp_2:.2f}°F")
elif escala_1 == "F":
    temp_2 = (5/9) * (temp_1 - 32)
    print(f"La temperatura equivale a {temp_2:.2f}°C")
else:
    print("Escala incorrecta. Usa 'C' o 'F'.")
