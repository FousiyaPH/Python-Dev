height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#converting weight and height to float type
height_as_float = float(height)
weight_as_float = float(weight)



#calculate bmi
bmi =round(weight_as_float/height_as_float**2)
print(bmi)
