def main():
        x=get_x()
        print(f"Value of x is {x}")

def get_x():
   while True:
      try:
         return int(input("What is the value of x?\n"))
      except ValueError:
         pass 
main()

    