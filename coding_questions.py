# Question 1: 
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 
# The first line of code has been defined as below:

def hello_name(user_name):
    username_caps = user_name.upper()
    print("Hello, " + username_caps + "!")

hello_name("mr. president")



# Question 2
# Write a function, first_odds that prints the odd numbers 
# from 1-100 and returns nothing

def first_odds():
    for num in range (1, 101, 2):
        print(num)

first_odds()



# Question 3
# Write a function, max_num_in_list to return the max number of a given list.
# start with 1st spot in a list = [0]
# this will rewrite the max number as the number to compare with next: if num > max: max= num (put on TWO lines! & check indent)
# not print! use return - check indent  
# The first line of code has been defined as below:

def max_num_in_list(a_list):

    max = a_list[0]
    for num in a_list:
        if num > max:
            max = num
    return max

max_num_in_list([1, 7, 12, 5, 365, 14, 6, 18])



# Question 4
# Write a function to return if the given year is a leap year. A leap year is 
# divisible by 4 but not by 100, unless it is also divisible by 400.
# The return should be boolean Type (true/false).

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
    
leap_year(2000) 
leap_year(1989)
leap_year(2222)

# SyntaxError with elif
# missing something! 
# I think I fixed it by adding return True under the if



# Question 5
# Write a function to see if all numbers in a list are consecutive. 
# Hint: Transitive property of addition. If a number is equal to the next number, then...
# The return should be boolean Type. = T or F

def consecutive_nums(a_list):
    for num in a_list:
        if a_list[0]+1 == a_list([0]+1):
            return True
        else:
            return False
        
consecutive_nums([1,2,3,4,5,6,7])
consecutive_nums([3,6,9,12,15,18])
