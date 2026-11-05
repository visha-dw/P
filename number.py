try:
    x=int(input("What is the value of x?\n"))
except ValueError:
    print("x is not an integer.") 
else: 
    print(f"x is {x}")