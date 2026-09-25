"""
Filename: conditional_calculator.py
Author: <Garcia, Alvaro>
Created: <09/25/2026>
Instructor: Mr.Burgess
"""

print("welcome to the Conditional calculator The calculator will then perform only the operation that the user requested")
n1=int(input("enter your first number"))
op=input("enter operation (+,-,*,/ )")
n2=int(input("enter your second number"))
if op=="+":
    print(f"{n1} + {n2} = {n1+n2}")

elif op=="-":
    print(f"{n1} - {n2} = {n1-n2}")

elif op=="*":
    print(f"{n1} * {n2} = {n1*n2}")

elif op=="/":
    print(f"{n1} / {n2} = {n1/n2}")

print("thank you for using this program")