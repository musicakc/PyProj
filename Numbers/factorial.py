''' Factorial Finder - The Factorial of a positive integer, n,
is defined as the product of the sequence n, n-1, n-2, ...1 and the
factorial of zero, 0, is defined as being 1.

Recursive and iterative implementation.
'''

def factorialr(n):
    if n == 1:
        return 1
    else:
        return n * factorialr(n-1)

def factoriali(n):
    prod = 1
    for i in range(1, n+1):
        prod = prod * i
    return prod

def main():
    ans=True
    while ans:
        print ("""
        1. Recursive
        2. Iterative
        """)
        ans=raw_input("What would you like to do? ") 
        if ans=="1":
            print(factorialr(int(raw_input("Enter a number: "))))
        elif ans=="2":
          print(factoriali(int(raw_input("Enter a number: ")))) 
        elif ans !="":
          print("\n Not Valid Choice Try again") 

if __name__ == "__main__":
    main()
    
