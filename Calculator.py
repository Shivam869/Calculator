def sum(x,y):
    return x+y
def difference(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x%y

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))

print("Sum:",sum(num1,num2))
print("Difference:",difference(num1,num2))
print("Product:", multiply(num1,num2))
print("Quoteint:",division(num1,num2))