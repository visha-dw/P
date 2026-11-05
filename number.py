try:
    x=int(input("What is the value of x?\n"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer.")    