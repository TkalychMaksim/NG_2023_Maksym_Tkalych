import math
print("Enter the arguments of equation: ")
argument_a = int(input("First argument: "))
argument_b = int(input("Second argument: "))
argument_c = int(input("Third argument: "))
discriminant = (math.pow(argument_b, 2))-(4*argument_a*argument_c)
if discriminant > 0:
    first_root = (-argument_b+math.sqrt(discriminant))/(2*argument_a)
    second_root = (-argument_b-math.sqrt(discriminant))/(2*argument_a)
    print(f"Result: x1={first_root}, x2={second_root}")
elif discriminant == 0:
    root = (-argument_b)/(2*argument_a)
    print(root)
else:
    print("This equation has no roots")
