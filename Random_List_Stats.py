###########################################################################################
# Name: Abby Gissendanner
# Date: 11-6-18
# Description: Creates a random list using the max and min provided by the user and gives the statistics
###########################################################################################

# function that prompts the user for a list size, minimum and maximum values, creates the list, and returns it
# you must use the list functions discussed in class to add integers to the list
import math
def fillList ():
        size = int(input("How many random integers would you like to add to the list? \n--> "))
        minimum = int(input("What would you like the minimum value to be? \n--> "))
        maximum = int(input("What would you like the maximum value to be? \n--> "))
        from random import randint
        numbers = []
        for items in range (0, size):
                num = randint(minimum, maximum)
                numbers.append (num)
        return numbers
# function that receives the list as a parameter, and calculates and returns the mean
def mean (nums):
        sum_num = 0
        for numbers in nums:
                sum_num += numbers
        if (sum_num % len(nums)) == 0:
                return (sum_num / len(nums))
        else:
                return (float(sum_num / len(nums)))
# function that receives the list as a parameter, and calculates and returns the median
def median (nums):
        nums.sort ()
        n = len(nums) / 2
        if ((len(nums) % 2) == 0):
                mid = (nums [n] + nums [n -1]) / 2
        else:
                mid = nums [int(math.ceil(n))]
        return mid
# function that receives the list as a parameter, and calculates and returns the range
def number_range (nums):
        range_num = (max(nums) - min(nums))
        return range_num
###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list
nums = fillList()

# display the list
print ("The list: {}".format(nums))
# there is no need to write/call your own function for this part
# calculate and display the mean
mean = mean (nums)
print ("The mean of the list is: {}".format(mean))
# calculate and display the median
med = median(nums)
print ("The median of the list is: {}".format(med))
# calculate and display the range
number_range = range_num (nums)
print ("The range of the list is: {}".format(number_range))