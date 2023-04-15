height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

weight_integerer = int(weight)
exponent = float(height) * float(height)

result = weight_integerer / exponent
result = round(result, 0)
result = int(result)

if result < 18.5:
    print(f'Your BMI is {result}, you are underweight.')
else:
    if result > 18.5:
        if result < 25:
            print(f'Your BMI is {result}, you have a normal weight.')
        else:
            if result > 25:
                if result < 30:
                    print(f'Your BMI is {result}, you are slightly overweight.')
                else:
                    if result > 30:
                        if result < 35:
                            print(f'Your BMI is {result}, you are obese.')
                        else:
                            if result > 35:
                                print(f'Your BMI is {result}, you are clinically obese.')
