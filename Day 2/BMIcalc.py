# body mass index calculator
input("Welcome to the BMI calculator. Press Enter to continue.")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = weight / height ** 2
print(f"Your BMI is {bmi:.2f}")