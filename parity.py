def main():
    x=int(input("Whats the value of x:"))
    if is_even(x):
     print("even")
    else:
       print("odd")
       
def is_even(x):
       if x%2==0:
          return True
       else:
          return False
main()