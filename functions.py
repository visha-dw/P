def main():
   number(get_number())

def number(n):
    for _ in range(n):
        print("Meow")



def get_number():
    while True:
       n=int(input("What's n?"))
       if n>0:
        return n
main()