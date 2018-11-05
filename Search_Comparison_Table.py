##########################################################################################
# Name: Abby Gissendanner
# Date: 10-29-18
# Description: Compares the different types of searches and puts them into a table
##########################################################################################
#Imports:
import math
#
# a function that displays the table
def tableMaker ():
    print ("_" * 30)
    print ("n\tSeq\tBin\tPerf")
    print ("_" * 30)
    n = minimum
    while (n < maximum):
        seqPerf = int(seqCalc(n))
        binPerf = int(binCalc(n))
        perfNum = int(perfDiff(n))
        print ("%s\t%s\t%s\t%s"%(n, seqPerf, binPerf, perfNum))
        n += interval
#
# a function that calculates the average number of comparisons of a sequential search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def seqCalc (size):
    if size == 0:
        return 0
    if size > 0:
        avrg = math.floor(size/2)
        return avrg
#
# a function that calculates the maximum number of comparisons of a binary search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def binCalc (size):
    if size == 0:
        return 0
    if size > 0:
        avrg = math.ceil(math.log(size + 1,2))
        return avrg
#
def perfDiff (size):
    if size == 0:
        return 0
    if size > 0:
        diff = int(seqCalc(size)/binCalc(size))
        return diff
#
###############################################
# MAIN PART OF THE PROGRAM
###############################################
# get user input for the minimum (make sure that it is >= 0)
minimum = int (input ("Enter minimun value:\n-> "))
while (minimum < 0):
    minimum = int (input("!!!!!ERROR!!!!! Please enter a number that is >= 0:\n-> "))
#   
# get user input for the maximum (make sure that is is >= minimum)
maximum = int (input ("Enter maximum value:\n-> "))
while (maximum < minimum):
    maximum = int (input("!!!!!ERROR!!!!! Please enter a number that is >= %s:\n-> "%minimum))
#
# get user input for the interval (make sure that it is >= 1)
usr = int (input ("Enter an interval:\n-> "))
while (usr < 1):
    usr = int (input("!!!!!ERROR!!!!! Please enter a number the is >= 1:\n-> "))
interval = usr
#
# generate the table
tableMaker()
#