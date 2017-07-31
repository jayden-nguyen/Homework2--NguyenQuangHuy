
again = 'yes'
while again.lower() == 'yes':
    mass = float(input("Please input mass(kg): "))
    hei_cm = float(input("Please input height(cm): "))
    height = hei_cm / 100
    BMI = mass/(height ** 2)
    if BMI < 16 :
        print("Severely underweight")
    elif BMI < 18.5:
        print("Underweight")
    elif BMI < 25:
        print("Normal")
    elif BMI < 30:
        print("Overweight")
    else:
        print("Obese")
    again = input("Do you want to check for your friend :))) (answer yes or no) ?")
    
        

