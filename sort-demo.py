# imports
from random import randint
from time import sleep
from os import system, fdopen
import sys
from copy import copy

# for some reason Python insists on over zealous output buffering
# this prevents that
sys.stdout = fdopen(sys.stdout.fileno(), 'w', 0)

# console colors
AUTO = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6

# color assignments
COMP = MAGENTA
SORTED = GREEN
UNSORTED = RED
DEFAULT = YELLOW
ACTION = GREEN
ALG_NAME = CYAN

# globals
alg = None
orig_list = None
nums = None
n = None
totComps = None
delay = None

def color(val):
  sys.stdout.write("\x1b[3{}m".format(val))

def write(val, space='  '):
  sys.stdout.write(str(val) + space)
  
def header(passNum):
  system('clear')
  color(ALG_NAME)
  print '**', alg, '**\n'
  color(DEFAULT)
  print "Original: ", orig_list, '\n'
  print "Pass " + str(passNum) + ':  ',
  
def conclusion(passes):
  color(DEFAULT)
  print
  print "Total comparisons:", str(totComps)
  print "Total passes: ", str(passes)
  
def animateBubbleSwap(i, comp1, comp2):  
  spacing = ['  ', '', '', '  ']
  c1 = nums[comp1]
  c2 = nums[comp2]
  
  sleep(delay / 2.0)

  for a in range(4):
    header(i+1)

    color(UNSORTED)
    for k in range(0,comp1):
      write(nums[k])
    
    color(COMP)
    write(c1, spacing[a])
    write(c2)
    
    color(UNSORTED)
    for k in range(comp2+1,n-i):
      write(nums[k])
    
    color(SORTED)
    for k in range(n-i,n):
      write(nums[k])
      
    sleep(delay / 2.0)
    
    if a == 1:
      c1 = nums[comp2]
      c2 = nums[comp1]  
  
def animateSelectionSwap(i, minPos):
  for s in range((minPos - i)*2+1, -1, -3):
    # HEADER
    header(i+1)

    # LINE 1
    color(SORTED)
    for k in range(0,i):
      write(nums[k])
      
    write(' ')
      
    color(UNSORTED)
    for k in range(i+1, minPos):
      write(nums[k])
      
    color(COMP)
    write(' ')

    color(UNSORTED)
    for k in range(minPos+1, n):
      write(nums[k])
      
    print
    
    # LINE 2
    print "        ",

    color(SORTED)
    for k in range(0,i):
      write(' ')
      
    write(' ', '')
    color(COMP)
    write(nums[i], ' ')
    write(' ' * s, '')
    write(nums[minPos], '')

    # delay
    sleep(delay / 2.0)
    
  #minPos, j = j, minPos
  
  for s in range(0, (minPos - i)*2, 3):
    # HEADER
    header(i+1)

    # LINE 1
    color(SORTED)
    for k in range(0,i):
      write(nums[k])
      
    write(' ')
      
    color(UNSORTED)
    for k in range(i+1, minPos):
      write(nums[k])
      
    color(COMP)
    write(' ')

    color(UNSORTED)
    for k in range(minPos+1, n):
      write(nums[k])
      
    print
    
    # LINE 2
    print "        ",

    color(SORTED)
    for k in range(0,i):
      write(' ')
      
    write(' ', '')
    color(COMP)
    write(nums[minPos], '  ')
    write(' ' * s, '')
    write(nums[i], '')

    # delay
    sleep(delay / 2.0)

  # last run
  s = (minPos - i)*2
  # HEADER
  header(i+1)

  # LINE 1
  color(SORTED)
  for k in range(0,i):
    write(nums[k])
    
  write(' ')
    
  color(UNSORTED)
  for k in range(i+1, minPos):
    write(nums[k])
    
  color(COMP)
  write(' ')

  color(UNSORTED)
  for k in range(minPos+1, n):
    write(nums[k])
    
  print
  
  # LINE 2
  print "        ",

  color(SORTED)
  for k in range(0,i):
    write(' ')
    
  write(' ', '')
  color(COMP)
  write(nums[minPos], '  ')
  write(' ' * s, '')
  write(nums[i], '')

  # delay
  sleep(delay / 2.0)

def animateInsertionSwap(i, minPos):
  for s in range((minPos - i)*2+1, -1, -3):
    # HEADER
    header(i+1)

    # LINE 1
    color(SORTED)
    for k in range(0,i):
      write(nums[k])
      
    write(' ')
      
    color(UNSORTED)
    for k in range(i+1, minPos):
      write(nums[k])
      
    color(COMP)
    write(' ')

    color(UNSORTED)
    for k in range(minPos+1, n):
      write(nums[k])
      
    print
    
    # LINE 2
    print "        ",

    color(SORTED)
    for k in range(0,i):
      write(' ')
      
    write(' ', '')
    color(COMP)
    write(nums[i], ' ')
    write(' ' * s, '')
    write(nums[minPos], '')

    # delay
    sleep(delay / 2.0)
    
  #minPos, j = j, minPos
  
  for s in range(0, (minPos - i)*2, 3):
    # HEADER
    header(i+1)

    # LINE 1
    color(SORTED)
    for k in range(0,i):
      write(nums[k])
      
    write(' ')
      
    color(UNSORTED)
    for k in range(i+1, minPos):
      write(nums[k])
      
    color(COMP)
    write(' ')

    color(UNSORTED)
    for k in range(minPos+1, n):
      write(nums[k])
      
    print
    
    # LINE 2
    print "        ",

    color(SORTED)
    for k in range(0,i):
      write(' ')
      
    write(' ', '')
    color(COMP)
    write(nums[minPos], '  ')
    write(' ' * s, '')
    write(nums[i], '')

    # delay
    sleep(delay / 2.0)

  # last run
  s = (minPos - i)*2
  # HEADER
  header(i+1)

  # LINE 1
  color(SORTED)
  for k in range(0,i):
    write(nums[k])
    
  write(' ')
    
  color(UNSORTED)
  for k in range(i+1, minPos):
    write(nums[k])
    
  color(COMP)
  write(' ')

  color(UNSORTED)
  for k in range(minPos+1, n):
    write(nums[k])
    
  print
  
  # LINE 2
  print "        ",

  color(SORTED)
  for k in range(0,i):
    write(' ')
    
  write(' ', '')
  color(COMP)
  write(nums[minPos], '  ')
  write(' ' * s, '')
  write(nums[i], '')

  # delay
  sleep(delay / 2.0)
    
# make original list
def makeRandList(length):
  lst = []
  for i in range(length):
    lst.append(randint(0,9))
    
  return lst

# bubble
def bubble():
  global alg, totComps
  alg = 'Bubble Sort'
  for i in range(n-1):
    for j in range(n-i-1):
      header(i+1)
      
      color(UNSORTED)
      for k in range(0,j):
        write(nums[k])
      
      color(COMP)
      write(nums[j])
      write(nums[j+1])
      
      color(UNSORTED)
      for k in range(j+2,n-i):
        write(nums[k])
      
      color(SORTED)
      for k in range(n-i,n):
        write(nums[k])
        
      color(ACTION)
      print
      print ' ' * (len('Pass: X  ') + (j*3) - 1),
      sleep(delay / 2.0)
      if nums[j] > nums[j+1]:
        print 'SWAP!'
        animateBubbleSwap(i, j, j+1)
        nums[j], nums[j+1] = nums[j+1], nums[j]
      else:
        print 'NO SWAP!'
        
      color(DEFAULT)
      totComps += 1
      print
      print 'Comparisons: ', totComps

      sleep(delay)
      
  header(i+1)

  color(SORTED)
  print nums
  
  conclusion(i+1)

# optimized bubble
def opt_bubble():
  global alg, totComps
  alg = 'Optimized Bubble Sort'
  for i in range(n-1):
    numSwapsThisPass = 0
    for j in range(n-i-1):
      header(i+1)
      
      color(UNSORTED)
      for k in range(0,j):
        write(nums[k])
      
      color(COMP)
      write(nums[j])
      write(nums[j+1])
      
      color(UNSORTED)
      for k in range(j+2,n-i):
        write(nums[k])
      
      color(SORTED)
      for k in range(n-i,n):
        write(nums[k])
        
      color(ACTION)
      print
      print ' ' * (len('Pass: X  ') + (j*3) - 1),
      sleep(delay / 2.0)
      if nums[j] > nums[j+1]:
        print 'SWAP!'
        numSwapsThisPass += 1
        animateBubbleSwap(i, j, j+1)
        nums[j], nums[j+1] = nums[j+1], nums[j]
      else:
        print 'NO SWAP!'
        
      color(DEFAULT)
      totComps += 1
      print
      print 'Comparisons: ', totComps

      sleep(delay)
      
    if numSwapsThisPass == 0:
      color(CYAN)
      print 'No swaps during this pass = EARLY EXIT!'
      sleep(delay*2)
      break
      
  header(i+1)

  color(SORTED)
  print nums
  
  conclusion(i+1)
    
# selection
def selection():
  global alg, totComps
  alg = 'Selection Sort'
  for i in range(n-1):
    minPos = i
    for j in range(i+1,n):
      header(i+1)
      
      color(SORTED)
      for k in range(0,i):
        write(nums[k])
        
      color(UNSORTED)
      for k in range(i, minPos):
        write(nums[k])
        
      color(COMP)
      write(nums[minPos])
      
      color(UNSORTED)
      for k in range(minPos+1, j):
        write(nums[k])
        
      color(COMP)
      write(nums[j])
      
      color(UNSORTED)
      for k in range(j+1, n):
        write(nums[k])
      
      color(COMP)
      print
      print ' ' * (len('Pass: X  ') + (minPos * 3 - 1)),
      print '^'
      print
      color(COMP)
      print 'Action: ',
      sleep(delay / 2.0)
      if nums[j] < nums[minPos]:
        print 'New Minimum Found'
        minPos = j
      else:
        print 'Same Minimum As Before'
      
      color(DEFAULT)
      totComps += 1
      print
      print 'Comparisons: ', totComps
      
      sleep(delay)
    
    if i != minPos:
      animateSelectionSwap(i, minPos)
      nums[i], nums[minPos] = nums[minPos], nums[i]
  
  header(i+1)

  color(SORTED)
  print nums
  
  conclusion(i+1)
  
# insertion
def insertion():
  global alg, totComps
  alg = 'Insertion Sort'
  
  # first frame - all unsorted
  header(1)

  color(UNSORTED)
  for i in range(n):
    write(nums[i])
    
  sleep(delay)
  
  # second frame - first num auto sorted
  header(1)

  color(SORTED)
  write(nums[0])
  
  write('')
  
  color(UNSORTED)
  for i in range(1, n):
    write(nums[i])
  
  sleep(delay)
  
  # remaining frames
  for i in range(1,n):
    j = i - 1
    numToInsert = nums[i]
    totComps += 1
    
    # find the position of the comp
    while j >= 0 and numToInsert < nums[j]:
      header(i)
      
      color(SORTED)
      for k in range(0,j+1):
        write(nums[k])
        
      color(COMP)
      write(numToInsert)
      
      color(SORTED)
      for k in range(j+2,i+1):
        write(nums[k])
      
      write('')
      
      color(UNSORTED)
      for k in range(i+1, n):
        write(nums[k])
        
      color(DEFAULT)
      print
      print 'Comparisons: ', totComps
      
      nums[j + 1] = nums[j]
      j -= 1
      totComps += 1
      
      sleep(delay)
      
      # finish comp pos found - still show comp before partially sorted list
      if j < 0 or numToInsert >= nums[j]:
        header(i)
      
        color(SORTED)
        for k in range(0,j+1):
          write(nums[k])
          
        color(COMP)
        write(numToInsert)
        
        color(SORTED)
        for k in range(j+2,i+1):
          write(nums[k])
        
        write('')
        
        color(UNSORTED)
        for k in range(i+1, n):
          write(nums[k])
          
        color(DEFAULT)
        print
        print 'Comparisons: ', totComps
        
        sleep(delay)
      
    # show partially sorted list - current comp finished
    nums[j + 1] = numToInsert
    
    header(i+1)

    color(SORTED)
    for k in range(0,i+1):
      write(nums[k])
      
    write('')
    
    color(UNSORTED)
    for k in range(i+1, n):
      write(nums[k])
      
    color(DEFAULT)
    print
    print 'Comparisons: ', totComps

    sleep(delay)

  header(n-1)

  color(SORTED)
  print nums
    
  conclusion(n-1)

# main
def main():
  global nums, n, orig_list, totComps, delay
  
  length = -1
  while length < 1 or length > 20:
    length = input("How many numbers (1 to 20)? ")
    
  choice = raw_input("Use random numbers (yes/no)? ")
  choice = choice.lower()
  if choice == 'yes' or choice == 'y':
    choice = 'no'
    while choice == 'no' or choice == 'n':
      lst = makeRandList(length)
      print "list = ", lst
      choice = raw_input("Is this list ok (yes/no)? ")
      choice = choice.lower()
  else:
    lst = []
    for n in range(length):
      num = input("Enter a number: ")
      lst.append(num)
    print "original list " + str(lst)

  nums = lst
  n = len(nums)
  orig_list = copy(lst)
  
  delay = input("How many seconds is the delay (can be a float)? ")

  print
  print "Sort Algorithm to Use:"
  print "1: Bubble sort"
  print "2: Optimized Bubble sort"
  print "3: Insertion sort"
  print "4: Selection sort"

  sys.stdout.flush()
  choice = input("? ")

  totComps = 0
  if choice == 1:
    bubble()
  elif choice == 2:
    opt_bubble()
  elif choice == 3:
    insertion()
  elif choice == 4:
    selection()
  else:
    print "invalid choice"

if __name__ == '__main__':
  main()