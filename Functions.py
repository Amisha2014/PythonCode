#Functions is like a set of instructions that you can ask python to follow anytime you want
#
# def say_good_morning():
#     print ("good_morning")

# def say_hello(name):
#     print ("hello " + name + "!")
#
# say_hello ("Amisha")
# say_hello ("Aakansha")


#Function with name goodbye, inside name as parameter
#anyname as argument
#print 3 times , 3 different names
#
# def goodbye (name) :
#     print ("goodBye " + name)
#
# goodbye ("Sanjana")
# goodbye ("Nediva")
# goodbye ("Gunit")
# goodbye ("Erin")
#
#
#
# def introduce (name, age = 20):
#     print ("My name is ", name)
#     print ("My age is ", age)
#
# introduce("Aakhil", 5)
# introduce("Gamini")
#
# #There are two types of functions
# #Built in functions-These are the functions that python provides
# #print()
# #int()
# #str()
# #float()
#
# #len()
#
# print(len("Amisha"))
#
#
# #User-defined function-These are the functions that we create ourselves to perform a specific task
#
# #https://www.w3schools.com/python/python_ref_functions.asp

# def add(num1,num2):
#     result=num1 +num2
#     return result
#
# sum=add(3,5)
# print("Addition result is", sum)
#
#
# def sub(num1,num2):
#     result=num1 -num2
#     return result
#
# diff=sub(30,5)
# print("Subtraction result is", diff)
#
#
# def mul(num1,num2):
#     result=num1  * num2
#     return result
#
# prod=mul(3,5)
# print("Multiplication result is", prod)

#
# def calculate_square_and_cube(num):
#     def calculate_power(power):
#         return num ** power
#
#     square = calculate_power(2)
#     cube = calculate_power(3)
#
#     return square, cube
#
# result_square, result_cube = calculate_square_and_cube(4)
# print("Square", result_square)
# print("Cube", result_cube)

# def greet_person(name):
#     def greet():
#         return "Hello," + name + "!"
#
#     return greet()
#
# message = greet_person("Amisha")
# print(message)
#
# def calculate_add_and_sub (num1, num2):
#     def addition ():
#         return num1 + num2
#
#     def subtraction ():
#         return num1 - num2
#
#     r_add = addition()
#     r_sub = subtraction ()
#
#     return r_add, r_sub
#
# result_add, result_sub = calculate_add_and_sub(10, 5)
#
# print ("Addition ", result_add)
# print ("Subtraction ", result_sub)


def make_sandwich (bread, filling):
    def add_sauce (sauce):
        return f"Adding {sauce}"

    sandwich = f"making a sandwhich with {bread} and {filling},"
    sauce = add_sauce ("tomato")
    return f"{sandwich} {sauce}"

print(make_sandwich("whole grain", "cheese"))