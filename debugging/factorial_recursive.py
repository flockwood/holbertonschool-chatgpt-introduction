#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 factorial.py <number>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        f = factorial(n)
        print(f)
    except ValueError as e:
        print(f"Error: {e}")
