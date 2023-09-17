
#Program calculates Body Mass Index (BMI) of a user.
#The program takes in user's weight and height.

weight = float(input("Hello friend! What is your weight please(kg)?: "))
height = float(input("Hello friend! What is your height please(m)^2?: "))

bmi = weight / (height**2)

if bmi <= 18.5:
    print("Hello friend you are underweight")
elif bmi < 25:
    print("Hello friend you weight is normal")
elif bmi < 30:
    print("Hello friend you are overweight")
else:
    print("Hello friend you are obese")