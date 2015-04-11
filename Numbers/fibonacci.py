'''
Fibonacci Sequence :
Enter a number and have the program generate the Fibonacci sequence to that
number or to the Nth number.
'''


import sys

def fib(n):
    a=0
    b=1
    series = [1]

    for x in range(0, n):
        c = a + b
        print c
        a = b
        b = c

        
if __name__ == "__main__":
    fib(int(raw_input("Enter a number: ")))
