try:
    #the left side doesnt get any value as right side has immediate value error.
    x=int(input("What is the value of x?\n"))
except ValueError:
    print("x is not an integer.")    
print(f"x is {x}")