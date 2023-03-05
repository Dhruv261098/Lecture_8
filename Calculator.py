

def my_calculator (a,b,operation_type):
    if operation_type == "addition":
        return addition(x=a, y=b)
    if operation_type == "substraction":
        return substraction(x=a, y=b)
    if operation_type == "multiplication":
        return multiplication(x=a, y=b)

def addition (x,y):
    return x + y

def substraction (x,y):
    return x-y

def multiplication (x,y):
    return x * y

# To take input from user (input funvtion)
user_input_a = float(input("The value of a:"))
user_input_b = float(input("The value of b:"))
user_input_type = input("The operation type")

print("The ans is: ", my_calculator(a = 5,b= 6,operation_type= "addition"))
print("The Ans is: ", my_calculator(a=user_input_a,b=user_input_b, operation_type=user_input_type))