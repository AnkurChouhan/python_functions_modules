import math

def calculate_math_operations():
    try:
        num = float(input("Enter a number: "))
        if num <= 0:
            print("For logarithm, enter a positive number.")
        else:
            print(f"Square root of {num}: {math.sqrt(num)}")
            print(f"Natural logarithm (ln) of {num}: {math.log(num)}")
            print(f"Sine of {num} (in radians): {math.sin(num)}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    calculate_math_operations()
