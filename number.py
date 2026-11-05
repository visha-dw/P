def main():
        x=get_x()
        print(f"Value of x is {x}")

def get_x():
   while True:
      try:
         x=int(input("What is the value of x?\n"))
      except ValueError:
         print("x is not an integer.") 
      else: 
         break
   return x
main()

    