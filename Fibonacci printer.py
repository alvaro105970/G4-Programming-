
"""
Filename: n_fibonacci.py
Author: <Garica Alvaro>
Created: <DATE>
Instructor: Holtslander
"""
print("Welcome to the Fibonacci sequence.This program displays the standard Fibonacci sequence that is n elements long.Enter a non-negative whole number on the line below.")
def n_fibonacci():
    input("input a non-negative whole number.")
    x = 0
    y = 1

# You should not need to change any code below this point
def main():
    print("This program displays the standard Fibonacci sequence that is n elements long.")
    running = "y"
    while running == "y":
        n_fibonacci()
        running = input("Print another sequence? (y/N)\n").lower()
    print("Thank you for using this standard Fibonacci sequence printer!")

if __name__ == "__main__":
    main()
