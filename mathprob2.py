print("Please enter your weight and height for your Body Mass Index!")
weight =int(input("Weight :"))
height =float(input("Height :"))

bmi =weight/(height**2)
print("Your Body Mass Index is {}".format(bmi))
