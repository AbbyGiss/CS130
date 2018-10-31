##########################################################################################
# Name: Abby Gissendanner
# Date: 10-29-18
# Description: Compares the different types of searches and puts them into a table
##########################################################################################

# a function that displays the table
def tableMaker():
    print("_" * 30)
    print("n\tSeq\tBin\tPerf")
    print("_" * 30)

# a function that calculates the average number of comparisons of a sequential search on a list of size n
# -input: the list size
# -output: the average number of comparisons


# a function that calculates the maximum number of comparisons of a binary search on a list of size n
# -input: the list size
# -output: the average number of comparisons


###############################################
# MAIN PART OF THE PROGRAM
###############################################
# get user input for the minimum (make sure that it is >= 0)
minimum = int (input ("Enter minimun value:\n->"))
while (minimum < 0):
    minimum = int (input("!!!!!ERROR!!!!! Please enter a number that is >= 0:\n->"))
# get user input for the maximum (make sure that is is >= minimum)
maximum = int (input ("Enter maximum value:\n->"))
while (maximum < minimum):
    maximum = int (input("!!!!!ERROR!!!!! Please enter a number that is >= %s:\n->"%minimum))
# get user input for the interval (make sure that it is >= 1)
usr = int (input ("Enter an interval:\n->"))
while (usr < 1):
    usr = int (input("!!!!!ERROR!!!!! Please enter a number the is >= 1:\n->"))
interval = usr
# generate the table

