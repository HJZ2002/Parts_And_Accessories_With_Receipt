print("WELCOME TO TIRE SIZE & PURCHASE SYSTEM\n")

# ===============================
# Tire Size Calculator
# ===============================
print("TIRE SIZE CALCULATOR")
while True:
    try:
        width = int(input("Enter tire width (e.g. 205): "))
        aspect = int(input("Enter aspect ratio (e.g. 55): "))
        rim = int(input("Enter rim diameter (e.g. 16): "))
        break
    except ValueError:
        print("Invalid input! Only numbers are allowed. Please try again.\n")

try:
    diameter = ((width * (aspect / 100) * 2) / 25.4) + rim
    diameter = round(diameter, 2)
    print(f"Tire Diameter: {diameter} inches\n")
except Exception as error:
    print(f"Error during calculation: {error}")
    diameter = None

# ===============================
# Tire Purchase Info
# ===============================
print("PURCHASE SECTION")
tire_name = input("Enter tire name: ")

while True:
    try:
        price = float(input("Enter price per tire (e.g. 89.99): $"))
        quantity = int(input("Enter quantity: "))
        break
    except ValueError:
        print("Invalid input! Use numbers only. Price can have decimals; quantity must be a whole number.\n")

