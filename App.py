def year100(age, name):
    yearborn = 2020 - age
    yearsleft = 100 - age
    final = yearborn + age + yearsleft

    return final







age = int(input("Please tell me your age"))
name = str(input( " And name:"))
print("You will be 100 years old in ", year100(age,name)," ", name)