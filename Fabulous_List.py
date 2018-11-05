###########################################################################################
# Name: Abby Gissendanner
# Date: 10-31-18
# Description: Make a list and sort it out
###########################################################################################


def listMaker ():
    i = 0 #initializing the list size
    size = int(input("How many integers would you like to add to the list? \n-> "))
    while (i < size): 
        theList.append(int(input("Enter an integer: ")))
        i += 1


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list
theList = [] #initializing the list itself
listMaker()
sortedlist = sorted(theList)
print "The original list: " , theList
print "The length of the list is: " , len(theList)
print "The minimum value of the list is: " , sortedlist[0]
print "The maximum value of the list is: " , sortedlist[-1]
theList.reverse()
print "The reversed list: " , theList
print "The sorted list: " , sortedlist


# display information about the list using the list functions discussed in class
# there is no need to write/call your own functions here

