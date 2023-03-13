# Question 1
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 

def hello_username(user_name):
    """Function prints a given username"""
    print("\nHello_" + user_name.upper() + "!\n")

hello_username('username')#Call function


# Question 2
# Write a python function, first_odds 
# that prints the odd numbers from 1-100 
# and returns nothing

def first_odds():
    """Function prints odd numbers 1-100
    and returns none"""
    for val in range(1,100,2):
        print(val, end="\n")
    return  #Will return 'None' in terminal

print(first_odds(), end='\n\n')#Call function


# Question 3
# Please write a Python function, max_num_in_list 
# to return the max number of a given list.

def max_num_in_list(a_list):
    """Function finds largest number in a list"""
    max = sorted(a_list)
    print(max.pop(), end='\n\n')

a_list=[1,2,4,6,7,56,1,2,3,]#list for 
                            #proof of concept
max_num_in_list(a_list)#Call function


# Question 4
# Write a function to return 
# if the given year is a leap year. 
# A leap year is divisible by 4, 
# but not divisible by 100, 
# unless it is also divisible by 400. 
# The return should be boolean Type (true/false)

def is_leap_year(a_year):
     """Function will state if input is 
     a leap year or not"""
     if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
        return True
     else:
        return False
        
print(is_leap_year(1990))#change 1990 to check accuracy


# Question 5
# Write a function to check to see 
# if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, 
# but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type

def is_consecutive(a_list):
    """Function will check if list
    is in numerical order"""
    if a_list != sorted(a_list):
        con=False
        print(bool(con))
    else:
        con=True
        print(bool(con))

a_list=[1,2,3]#list for proof of concept
is_consecutive(a_list)#call function
