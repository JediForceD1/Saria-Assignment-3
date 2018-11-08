
'''
Aaron McCormick
Assigment 3
9/18/2018
'''


time_tra = int(input("How many hours has your vehicle traveled?\n"))

while time_tra <=0:
    print("You cannot have a negitive or zero number.")
    time_tra = int(input("How many hours has your vehicle traveled?\n"))


speed = int(input("How fast is your vehicle traveling?\n"))

while speed <= 0:
    print("You cannot have a negitive or zero number.")
    speed = int(input("How fast is your vehicle traveling?\n"))

count = 1

while count <= time_tra:
    print("In hour ", count, " the vehicle has travled ", count * speed,  " miles.\n", end = "", sep = "")
    count += 1
