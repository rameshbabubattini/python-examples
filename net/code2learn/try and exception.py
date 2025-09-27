a = input("Enter a number: ")
b = input("Enter another number: ")

try:
    c = int(a) + int(b)
except Exception as e:
    print('Error', e)
    c = -1
else:
    print("No error occurred.")
finally:
    print(f"The sum {a} + {b} = {c}")