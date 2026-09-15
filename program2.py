# Program to swap two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("First number:", a)
print("Second number:", b)

# Swapping
a, b = b, a

print("After swapping:")
print("First number:", a)
print("Second number:", b)
