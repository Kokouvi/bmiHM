# Program showing how to calculate BMI

import math

weight = 65

## Need the value in height suared

height = math.pow(1.80, 2) 

BMI = round(weight / height, 2)

print("Your Body Weight is", BMI, "kg/msquared", "(Normal)")