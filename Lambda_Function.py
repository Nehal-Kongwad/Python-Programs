add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b
n1 = int(input("Enter the first number :- "))
n2 = int(input("Enter the second number := "))
print(f"{n1} + {n2} = " ,add(n1,n2))
print(f"{n1} - {n2} = " ,sub(n1,n2))
print(f"{n1} * {n2} = " ,mul(n1,n2))
print(f"{n1} / {n2} = " ,div(n1,n2))
