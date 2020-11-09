#!/usr/bin/env python3

#BMI = (weight in kg / height in meters squared)
# imperial version: BMI * 703

def gather_info():
    height = float(input("What is your height? (inches or meters): "))
    weight = float(input("What is your weight? (pounds or kilograms): "))
    system = input("Are your measurement in metric or imperial units? ").lower().strip()
    return (height, weight, system)

def calc_bmi(weight, height, system="metric"):
    """
    Return the body mass index (BMI) for the given weight, height, and measurement system.
    """
    if system == "metric":
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 *  (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith("i"):
        bmi = calc_bmi(weight, system=system, height=height)
        print(f"Your BMI is: {bmi}")
        break
    elif system.startswith("m"):
        bmi = calc_bmi(weight, height)
        print(f"Your BMI is: {bmi}")
        break
    else:
        print("Error: Unknown measurement system. Please use Imperial or Metric")
