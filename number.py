try:
    
    x=int(input("What is the value of x?\n"))
except ValueError:
    print("x is not an integer.") 
#this line will be executed anyhow but x as stir cannot be executed so it gives error       
print(f"x is {x}")