#Program to generate factorial of a number

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def main():
    print(factorial(int(raw_input("Enter a number: "))))    


if __name__ == "__main__":
    main()
    
