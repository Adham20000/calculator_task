#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def multiply(x, y):
    return x * y

def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return not is_even(num)

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def fibonacci(n):
    if n <= 0:
        return "Error: Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    print("Python Calculator")
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Multiply")
        print("5. Check Even and Odd")
        print("6. Factorial")
        print("7. Fibonacci")
        print("8. Exit")
        
        choice = int(input("Enter the option number: "))

        if choice == 1:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", add(x, y))
        elif choice == 2:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", subtract(x, y))
        elif choice == 3:
            x = float(input("Enter dividend: "))
            y = float(input("Enter divisor: "))
            result = divide(x, y)
            if isinstance(result, str):
                print(result)
            else:
                print("Result:", result)
        elif choice == 4:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print("Result:", multiply(x, y))
        elif choice == 5:
            num = int(input("Enter a number: "))
            print("Even:", is_even(num))
            print("Odd:", is_odd(num))
        elif choice == 6:
            num = int(input("Enter a non-negative integer: "))
            print("Result:", factorial(num))
        elif choice == 7:
            num = int(input("Enter a positive integer: "))
            print("Result:", fibonacci(num))
        elif choice == 8:
            print("Exiting the calculator.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

