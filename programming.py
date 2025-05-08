#!/usr/bin/env python
# coding: utf-8

# # Data Structures and Algorithms

# In[ ]:


print( "Welcome to the GPA calculator." )
print( "Please enter all your letter grades, one per line." )
print( "Enter a blank line to designate the end." )
# map from letter grade to point value
points = { "A+" :4.0, "A" :4.0, "A-" :3.67, "B+" :3.33, "B" :3.0, "B-" :2.67,
"C+" :2.33, "C" :2.0, "C" :1.67, "D+" :1.33, "D" :1.0, "F" :0.0}
num_courses = 0
total_points = 0
done = False
while not done:
  grade = input()
  if grade == "":
    done = True
  elif grade not in points:
    print(f"Unknown grade {grade} being ignored")
  else:
    num_courses += 1
    total_points += points[grade]
if num_courses > 0:
    print(f"Your GPA is {total_points / num_courses}")


# In[ ]:


temperature = 98.6


# In[ ]:


temperature = None




temperature = 98.6


# In[ ]:


original = temperature

temperature = temperature + 5.0


# In[ ]:


temperature,original


# In[ ]:


help(float)


# In[ ]:


bool()


# In[ ]:


bool(23==24)


# In[ ]:


bool(24>23)


# In[ ]:


int()


# In[ ]:


int('334')


# In[ ]:


float()


# In[ ]:


largest = 6.022 * (10 ** 23)


# In[ ]:


type(largest)


# In[ ]:


float(4)


# In[ ]:


float('3.14159')


# In[ ]:


str_one = "hello"


# In[ ]:


str_one.upper()


# In[ ]:


str_one.capitalize()


# In[ ]:


str_one[1]


# In[ ]:


str_two = 'Don\'t worry about apostrophes \n It is very interesting \n this is just amazing'
print(str_two.rjust(0))


# In[ ]:


list_one = list(str_one)


# In[ ]:


list_one[1] = 'a'


# In[ ]:


list_one


# In[ ]:


list_two = [1,2,3,4,5]


# In[ ]:


type(list_two)


# In[ ]:


tuple_one = tuple(str_one)


# In[ ]:


# tuple_one[1] = 'a'


# In[ ]:


set_one = set(str_one)
set_one


# In[ ]:


frozenset_one = frozenset(str_one)
frozenset_one


# In[ ]:


dict_one = {'A+': 4.0,
 'A': 4.0,
 'A-': 3.67,
 'B+': 3.33,
 'B': 3.0,
 'B-': 2.67,
 'C+': 2.33,
 'C': 1.67,
 'D+': 1.33,
 'D': 1.0,
 'F': 0.0}
dict(dict_one)


# In[ ]:


#not,and,or
(23 != 24 & 24 == 24) | (23 == 22)


# In[ ]:


23 != 24 and 24 == 24 or 23 == 22


# In[ ]:


#is (==), is not (!=)
23 is not 24 and 24 is 24 or 23 is 22


# In[ ]:


# <,<=,>,>=
23 <= 24 and 24 >= 24 or 23 < 22


# In[ ]:


# 5 < 'hello'


# In[ ]:


# +, -, *, /, //, %


# In[ ]:


(23 + 24) % 2


# In[ ]:


# ~,&, |, ^, <<, >>


# In[ ]:


#, in, not in


# In[ ]:


list_three = [1,2,5,6,7,8,9,10]
bool(3 in list_three)
bool(3 not in list_three)
bool(5 in list_three)


# In[ ]:


temperature = 89.7


# In[ ]:


temperature += 5


# In[ ]:


temperature


# In[ ]:


if 1 not in list_three:
  print("yeah 1 is not in list 3")
elif 3 not in list_three:
  print("oh no 3 is in list 3")
else:
  print("oh no failures")


# In[ ]:


int_one  = 23


# In[ ]:


for i in str_one:
  print(i)


# In[ ]:


len(str_one)


# In[ ]:


j = 0
while j < len(str_one):
  j+= 1


# In[ ]:


j


# In[ ]:


# my own len
def counter(data, target):
  n = 0
  for item in data:
    if item == target:
      n += 1
  return n


# In[ ]:


counter(str_one,'e')


# ## Assignment

# In[1]:


# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.
# R-1.2 Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.
# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.
# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.
# R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
# ing on Python’s comprehension syntax and the built-in sum function.
# R-1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.
# R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely-
# ing on Python’s comprehension syntax and the built-in sum function.
# R-1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for in-
# dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?
# R-1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?
# R-1.10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
# R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
# R-1.12 Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module in-
# cludes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.
# C-1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.
# C-1.14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.
# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).
# C-1.16 In our implementation of the scale function (page 25), the body of the loop
# executes the command data[j] = factor. We have discussed that numeric
# types are immutable, and that use of the = operator in this context causes
# the creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes the
# actual parameter sent by the caller?
# C-1.17 Had we implemented the scale function (page 25) as follows, does it work
# properly?
# def scale(data, factor):
#   for val in data:
#     val = factor
# Explain why or why not.
# C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
# C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.
# C-1.20 Python’s random module includes a function shuﬄe(data) that accepts a
# list of elements and randomly reorders the elements so that each possi-
# ble order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuﬄe function.
# C-1.21 Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).
# C-1.22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.
# C-1.23 Give an example of a Python code fragment that attempts to write an ele-
# ment to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”
# C-1.24 Write a short Python function that counts the number of vowels in a given
# character string.
# C-1.25 Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For exam-
# ple, if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".
# C-1.26 Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”
# C-1.27 In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementa-
# tions, from page 41, was the most efﬁcient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance ad-
# vantages.
# P-1.29 Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.
# P-1.30 Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.
# P-1.31 Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.
# P-1.32 Write a Python program that can simulate a simple calculator, using the
# console as the exclusive input and output device. That is, each input to the
# calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
# can be done on a separate line. After each such input, you should output
# to the Python console what would be displayed on your calculator.
# P-1.33 Write a Python program that simulates a handheld calculator. Your pro-
# gram should process input from the Python console representing buttons
# that are “pushed,” and then output the contents of the screen after each op-
# eration is performed. Minimally, your calculator should be able to process
# the basic arithmetic operations and a reset/clear operation.
# P-1.34 A common punishment for school children is to write out a sentence mul-
# tiple times. Write a Python stand-alone program that will write out the
# following sentence one hundred times: “I will never spam my friends
# again.” Your program should number each of the sentences and it should
# make eight different random-looking typos.
# P-1.35 The birthday paradox says that the probability that two people in a room
# will have the same birthday is more than half, provided n, the number of
# people in the room, is more than 23. This property is not really a paradox,
# but many people ﬁnd it surprising. Design a Python program that can test
# this paradox by a series of experiments on randomly generated birthdays,
# which test this paradox for n = 5, 10, 15, 20, . . . , 100.
# P-1.36 Write a Python program that inputs a list of words, separated by white-
# space, and outputs how many times each word appears in the list. You
# need not worry about efﬁciency at this point, however, as this topic is
# something that will be addressed later in this book.


# In[2]:


# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?
# Definition for a binary tree node.
from csv import reader
from queue import Empty
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    pass


# In[ ]:





# In[ ]:


print( "Welcome to the GPA calculator." )
print( "Please enter all your letter grades, one per line." )
print( "Enter a blank line to designate the end." )
# map from letter grade to point value
points = { "A+" :4.0, "A" :4.0, "A-" :3.67, "B+" :3.33, "B" :3.0, "B-" :2.67,
"C+" :2.33, "C" :2.0, "C" :1.67, "D+" :1.33, "D" :1.0, "F" :0.0}
num_courses = 0
total_points = 0
done = False
while not done:
  grade = input()
  if grade == "":
    done = True
  elif grade not in points:
    print(f"Unkown grade {grade} not in the points")
  else:
    num_courses += 1
    total_points += points[grade]
if num_courses > 0:
  print(f'Your GPA is {total_points/num_courses}')


# In[ ]:


temperature  = 98.6


# In[ ]:


# 9temperature
# False
original = temperature
temperature = temperature + 5.0


# In[ ]:


temperature,original


# In[ ]:


bool()


# In[ ]:


bool(24>23)


# In[ ]:


bool(23>24)


# In[ ]:


int()


# In[ ]:


int('334')


# In[ ]:


# int('hello')
int(-3.12)
int(-3.89)


# In[ ]:


int('7f',16)


# In[ ]:


float()


# In[ ]:


float('3.14')


# In[ ]:


str_one = 'hello'
str("hello")


# In[ ]:


str_one.upper()


# In[ ]:


str_one.capitalize()


# In[ ]:


str_one[1]


# In[ ]:


list_one = list(str_one)


# In[ ]:


list_one


# In[ ]:


list_one[1] = 'a'


# In[ ]:


list_one


# In[ ]:


tuple_one = str_one,


# In[ ]:


# tuple_one[0] = 'a'


# In[ ]:


tuple_two = list_one,


# In[ ]:


tuple_two


# In[ ]:


set_one = set(str_one)


# In[ ]:


set_one


# In[ ]:


frozenset(set_one)


# In[ ]:


points['A']


# In[ ]:


list_one = [1,2,4,5]


# In[ ]:


if 3 in list_one:
  print("3 is not in list one")
elif 1 in list_one:
  print("winner")
else:
  print("3 is in list one")


# In[ ]:


for i in list_one:
  print(i)


# In[ ]:


j = 0
while j < len(list_one):
  j += 1


# In[ ]:


j


# ## Object Oriented Programming

# In[2]:


class CreditCard:
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        return self._customer
    
    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account
    
    def get_limit(self):
        return self._limit
    
    def get_balance(self):
        return self._balance
    
    def charge(self,price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self,amount):
        self._balance -= amount


# In[11]:


cc = CreditCard("martin","equity","00200",3000)


# In[12]:


cc.charge(20)


# In[13]:


cc.get_balance()


# In[9]:


wallet = [ ]
wallet.append(CreditCard( 'John Bowman' , 'California Savings' ,'5391 0375 9387 5309' , 2500) )
wallet.append(CreditCard( 'John Bowman' , 'California Federal' ,'3485 0399 3395 1954' , 3500) )
wallet.append(CreditCard( 'John Bowman' , 'California Finance' ,'5391 0375 9387 5309' , 5000) )
for val in range(1, 17):
    wallet[0].charge(val)
    wallet[1].charge(2*val)
    wallet[2].charge(3*val)
for c in range(3):
    print('Customer = ', wallet[c].get_customer())
    print('Bank = ', wallet[c].get_bank())
    print('Account = ', wallet[c].get_account())
    print('Limit = ', wallet[c].get_limit())
    print('Balance = ', wallet[c].get_balance())
    
    while wallet[c].get_balance() > 100:
        wallet[c].make_payment(100)
        print('New balance = ', wallet[c].get_balance())
        print()


# In[10]:


class Vector:
    def __init__(self, d):
        self._coords = [0] * d
        
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self,j):
        return self._coords[j]
    
    def __setitem__(self, j, val):
        self._coords[j] = val
    
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self == other
    
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


# In[11]:


class SequenceIterator:
    
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1
        
    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration()
            
    def __iter__(self):
        return self


# In[1]:


class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')
        
        if stop is None:
            start, stop = 0, start
            
        self._length = max(0, (stop - start + step - 1) // step)
        self._start = start
        self._step = step
        
    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        if k < 0:
            k += len(self)
            
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
            
        return self._start + k * self._step


# In[16]:


class PredatoryCreditCard(CreditCard):
    OVERLIMIT_FEE = 5
    
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
    
    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE
        return success
    
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
            


# In[4]:


class Progression:
    
    def __init__(self, start=0):
        self._current = start
        
    def _advance(self):
        self._current +=1 
        
    def __next__(self):
        if self._current is None:
            raise StopIteration()
            
        else:
            answer = self._current
            self._advance()
            return answer
        
    def __iter__(self):
        return self
    
    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))


# In[5]:


class ArithmeticProgression(Progression):
    
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment
        
    def _advance(self):
        self._current += self._increment


# In[6]:


class GeometricProgression(Progression):
    
    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base
        
    def _advance(self):
        self._current *= self._base
        


# In[7]:


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first
        
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


# In[11]:


print( 'Default progression:' )
Progression( ).print_progression(10)
print( 'Arithmetic progression with increment 5:' )
ArithmeticProgression(5).print_progression(10)
print( 'Arithmetic progression with increment 5 and start 2:')
ArithmeticProgression(5, 2).print_progression(10)
print( 'Geometric progression with default base:' )
GeometricProgression( ).print_progression(10)
print( 'Geometric progression with base 3: ')
GeometricProgression(3).print_progression(10)
print( 'Fibonacci progression with default start values: ')
FibonacciProgression( ).print_progression(10)
print( 'Fibonacci progression with start values 4 and 6: ')
FibonacciProgression(4, 6).print_progression(10)


# In[14]:


from abc import ABCMeta, abstractmethod
class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""
    @abstractmethod
    def len (self):
        """Return the length of the sequence."""
        pass
    @abstractmethod
    def getitem (self, j):
        """Return the element at index j of the sequence."""
        pass
    
    
    def contains (self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                # found match
                return True
        return False
    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:
                return j
        # never found a match
        raise ValueError( "value not in sequence" )
    def count(self, val):
        """Return the number of elements equal to given value."""
        k=0
        for j in range(len(self)):
            if self[j] == val:
            # found a match
                k += 1
        return k


# ## Assignment

# In[1]:


# R-2.1 Give three examples of life-critical software applications.
# R-2.2 Give an example of a software application in which adaptability can mean
# the difference between a prolonged lifetime of sales and bankruptcy.
# R-2.3 Describe a component from a text-editor GUI and the methods that it en-
# capsulates.
# R-2.4 Write a Python class, Flower, that has three instance variables of type str,
# int, and ﬂoat, that respectively represent the name of the ﬂower, its num-
# ber of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.
# R-2.5 Use the techniques of Section 1.7 to revise the charge and make payment
# methods of the CreditCard class to ensure that the caller sends a number
# as a parameter.
# R-2.6 If the parameter to the make payment method of the CreditCard class
# were a negative number, that would have the effect of raising the balance
# on the account. Revise the implementation so that it raises a ValueError if
# a negative value is sent.
# R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new ac-
# count to zero. Modify that class so that a new account can be given a
# nonzero balance using an optional ﬁfth parameter to the constructor. The
# four-parameter constructor syntax should continue to produce an account
# with zero balance.
# R-2.8 Modify the declaration of the ﬁrst for loop in the CreditCard tests, from
# Code Fragment 2.3, so that it will eventually cause exactly one of the three
# credit cards to go over its credit limit. Which credit card is it?
# R-2.9 Implement the sub method for the Vector class of Section 2.3.3, so
# that the expression u−v returns a new vector instance representing the
# difference between two vectors.
# R-2.10 Implement the neg method for the Vector class of Section 2.3.3, so
# that the expression −v returns a new vector instance whose coordinates
# are all the negated values of the respective coordinates of v.
# R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
# v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
# a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
# Explain how the Vector class deﬁnition can be revised so that this syntax
# generates a new vector.
# R-2.12 Implement the mul method for the Vector class of Section 2.3.3, so
# that the expression v 3 returns a new vector with coordinates that are 3
# times the respective coordinates of v.
# R-2.13 Exercise R-2.12 asks for an implementation of mul , for the Vector
# class of Section 2.3.3, to provide support for the syntax v 3. Implement
# the rmul method, to provide additional support for syntax 3 v.
# R-2.14 Implement the mul method for the Vector class of Section 2.3.3, so
# that the expression u v returns a scalar that represents the dot product of
# the vectors, that is, ∑di=1 ui · vi .
# R-2.15 The Vector class of Section 2.3.3 provides a constructor that takes an in-
# teger d, and produces a d-dimensional vector with all coordinates equal to
# 0. Another convenient form for creating a new vector would be to send the
# constructor a parameter that is some iterable type representing a sequence
# of numbers, and to create a vector with dimension equal to the length of
# that sequence and coordinates equal to the sequence values. For example,
# Vector([4, 7, 5]) would produce a three-dimensional vector with coordi-
# nates <4, 7, 5>. Modify the constructor so that either of these forms is
# acceptable; that is, if a single integer is sent, it produces a vector of that
# dimension with all zeros, but if a sequence of numbers is provided, it pro-
# duces a vector with coordinates based on that sequence.
# R-2.16 Our Range class, from Section 2.3.5, relies on the formula
# max(0, (stop − start + step − 1) // step)
# to compute the number of elements in the range. It is not immediately ev-
# ident why this formula provides the correct calculation, even if assuming
# a positive step size. Justify this formula, in your own words.
# R-2.17 Draw a class inheritance diagram for the following set of classes:
# • Class Goat extends object and adds an instance variable tail and
# methods milk( ) and jump( ).
# • Class Pig extends object and adds an instance variable nose and
# methods eat(food) and wallow( ).
# • Class Horse extends object and adds instance variables height and
# color, and methods run( ) and jump( ).
# • Class Racer extends Horse and adds a method race( ).
# • Class Equestrian extends Horse, adding an instance variable weight
# and methods trot( ) and is trained( ).
# R-2.18 Give a short fragment of Python code that uses the progression classes
# from Section 2.4.2 to ﬁnd the 8th value of a Fibonacci progression that
# starts with 2 and 2 as its ﬁrst two values.
# R-2.19 When using the ArithmeticProgression class of Section 2.4.2 with an in-
# crement of 128 and a start of 0, how many calls to next can we make
# before we reach an integer of 263 or larger?
# R-2.20 What are some potential efﬁciency disadvantages of having very deep in-
# heritance trees, that is, a large set of classes, A, B, C, and so on, such that
# B extends A, C extends B, D extends C, etc.?
# R-2.21 What are some potential efﬁciency disadvantages of having very shallow
# inheritance trees, that is, a large set of classes, A, B, C, and so on, such
# that all of these classes extend a single class, Z?
# R-2.22 The collections.Sequence abstract base class does not provide support for
# comparing two sequences to each other. Modify our Sequence class from
# Code Fragment 2.14 to include a deﬁnition for the eq method, so
# that expression seq1 == seq2 will return True precisely when the two
# sequences are element by element equivalent.
# R-2.23 In similar spirit to the previous problem, augment the Sequence class with
# method lt , to support lexicographic comparison seq1 < seq2.
# C-2.24 Suppose you are on the design team for a new e-book reader. What are the
# primary classes and methods that the Python software for your reader will
# need? You should include an inheritance diagram for this code, but you
# do not need to write any actual code. Your software architecture should
# at least include ways for customers to buy new books, view their list of
# purchased books, and read their purchased books.
# C-2.25 Exercise R-2.12 uses the mul method to support multiplying a Vector
# by a number, while Exercise R-2.14 uses the mul method to support
# computing a dot product of two vectors. Give a single implementation of
# Vector. mul that uses run-time type checking to support both syntaxes
# u v and u k, where u and v designate vector instances and k represents
# a number.
# C-2.26 The SequenceIterator class of Section 2.3.4 provides what is known as a
# forward iterator. Implement a class named ReversedSequenceIterator that
# serves as a reverse iterator for any Python sequence type. The ﬁrst call to
# next should return the last element of the sequence, the second call to next
# should return the second-to-last element, and so forth.
# C-2.27 In Section 2.3.5, we note that our version of the Range class has im-
# plicit support for iteration, due to its explicit support of both len
# and getitem . The class also receives implicit support of the Boolean
# test, “k in r” for Range r. This test is evaluated based on a forward itera-
# tion through the range, as evidenced by the relative quickness of the test
# 2 in Range(10000000) versus 9999999 in Range(10000000). Provide a
# more efﬁcient implementation of the contains method to determine
# whether a particular value lies within a given range. The running time of
# your method should be independent of the length of the range.
# C-2.28 The PredatoryCreditCard class of Section 2.4.1 provides a process month
# method that models the completion of a monthly cycle. Modify the class
# so that once a customer has made ten calls to charge in the current month,
# each additional call to that function results in an additional $1 surcharge.
# C-2.29 Modify the PredatoryCreditCard class from Section 2.4.1 so that a cus-
# tomer is assigned a minimum monthly payment, as a percentage of the
# balance, and so that a late fee is assessed if the customer does not subse-
# quently pay that minimum amount before the next monthly cycle.
# C-2.30 At the close of Section 2.4.1, we suggest a model in which the CreditCard
# class supports a nonpublic method, set balance(b), that could be used
# by subclasses to affect a change to the balance, without directly accessing
# the balance data member. Implement such a model, revising both the
# CreditCard and PredatoryCreditCard classes accordingly.
# C-2.31 Write a Python class that extends the Progression class so that each value
# in the progression is the absolute value of the difference between the pre-
# vious two values. You should include a constructor that accepts a pair of
# numbers as the ﬁrst two values, using 2 and 200 as the defaults.
# C-2.32 Write a Python class that extends the Progression class so that each value
# in the progression is the square root of the previous value. (Note that
# you can no longer represent each value with an integer.) Your construc-
# tor should accept an optional parameter specifying the start value, using
# 65, 536 as a default.
# P-2.33 Write a Python program that inputs a polynomial in standard algebraic
# notation and outputs the ﬁrst derivative of that polynomial.
# P-2.34 Write a Python program that inputs a document and then outputs a bar-
# chart plot of the frequencies of each alphabet character that appears in
# that document.
# P-2.35 Write a set of Python classes that can simulate an Internet application in
# which one party, Alice, is periodically creating a set of packets that she
# wants to send to Bob. An Internet process is continually checking if Alice
# has any packets to send, and if so, it delivers them to Bob’s computer, and
# Bob is periodically checking if his computer has a packet from Alice, and,
# if so, he reads and deletes it.
# P-2.36 Write a Python program to simulate an ecosystem containing two types
# of creatures, bears and ﬁsh. The ecosystem consists of a river, which is
# modeled as a relatively large list. Each element of the list should be a
# Bear object, a Fish object, or None. In each time step, based on a random
# process, each animal either attempts to move into an adjacent list location
# or stay where it is. If two animals of the same type are about to collide in
# the same cell, then they stay where they are, but they create a new instance
# of that type of animal, which is placed in a random empty (i.e., previously
# None) location in the list. If a bear and a ﬁsh collide, however, then the
# ﬁsh dies (i.e., it disappears).
# P-2.37 Write a simulator, as in the previous project, but add a Boolean gender
# ﬁeld and a ﬂoating-point strength ﬁeld to each animal, using an Animal
# class as a base class. If two animals of the same type try to collide, then
# they only create a new instance of that type of animal if they are of differ-
# ent genders. Otherwise, if two animals of the same type and gender try to
# collide, then only the one of larger strength survives.
# P-2.38 Write a Python program that simulates a system that supports the func-
# tions of an e-book reader. You should include methods for users of your
# system to “buy” new books, view their list of purchased books, and read
# their purchased books. Your system should use actual books, which have
# expired copyrights and are available on the Internet, to populate your set
# of available books for users of your system to “purchase” and read.
# P-2.39 Develop an inheritance hierarchy based upon a Polygon class that has
# abstract methods area( ) and perimeter( ). Implement classes Triangle,
# Quadrilateral, Pentagon, Hexagon, and Octagon that extend this base
# class, with the obvious meanings for the area( ) and perimeter( ) methods.
# Also implement classes, IsoscelesTriangle, EquilateralTriangle, Rectan-
# gle, and Square, that have the appropriate inheritance relationships. Fi-
# nally, write a simple program that allows users to create polygons of the
# various types and input their geometric dimensions, and the program then
# outputs their area and perimeter. For extra effort, allow users to input
# polygons by specifying their vertex coordinates and be able to test if two
# such polygons are similar.


# ## Analysis of Algorithms

# In[4]:


from time import time
start_time = time( )
25*2000
end_time = time( )
elapsed = end_time - start_time
print(elapsed)


# In[8]:


def ﬁnd_max(data):
    """
    Return the maximum element from a nonempty Python list.
    """
    
    biggest = data[0]
    # The initial value to beat
    for val in data:
    # For each value:
        if val > biggest:
        # if it is greater than the best so far,
    
            biggest = val
            # we have found a new best (so far)
        
    return biggest


# In[11]:


# A Quadratic-Time Algorithm
# Our ﬁrst algorithm for computing preﬁx averages, named preﬁx average1, is shown
# in Code Fragment 3.2. It computes every element of A separately, using an inner
# loop to compute the partial sum.
def preﬁx_average1(S):

    """
    Return list such that, for all j, A[j] equals average of S[0], ..., S[j].
    """
    n = len(S)
    # create new list of n zeros
    A = [0] * n
    
    for j in range(n):
        total = 0
        # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j+1)
        # record the average
        
    return A


# In[13]:


def preﬁx_average2(S):
    """
    Return list such that, for all j, A[j] equals average of S[0], ..., S[j].
    """
    
    n = len(S)
    # create new list of n zeros
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1) # record the average
    
    return A


# In[14]:


def preﬁx_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]. """

    n = len(S)
    # create new list of n zeros
    A = [0] * n
    total = 0
    # compute preﬁx sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j]
        # update preﬁx sum to include S[j]
        A[j] = total / (j+1)
        # compute average based on current sum
        
    return A


# In[15]:


def disjoint1(A, B, C):
    """Return True if there is no element common to all three lists."""
    
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    # we found a common value

    return True


# In[18]:


def disjoint2(A, B, C):
    """Return True if there is no element common to all three lists."""
    
    for a in A:
        for b in B:
            if a == b:
                # only check C if we found match from A and B
                for c in C:
                    if a == c:
                        # (and thus a == b == c)
                        return False
    # we found a common value
    return True


# In[20]:


def unique1(S):
    """Return True if there are no duplicate elements in sequence S."""
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
    # found duplicate pair
    return True


# In[22]:


def unique2(S):
    """Return True if there are no duplicate elements in sequence S."""
    temp = sorted(S)
    # create a sorted copy of S
    for j in range(1, len(temp)):
        if S[j-1] == S[j]:
            return False
    # found duplicate pair
    return True


# In[24]:


def ﬁnd(S, val):
    """Return index j such that S[j] == val, or -1 if no such element."""
    n = len(S)
    j=0
    while j < n:
        if S[j] == val:
            return j
        # a match was found at index j
        j += 1
    return -1


# ## Assignment

# In[ ]:


# R-3.1 Graph the functions 8n, 4n log n, 2n2 , n3 , and 2n using a logarithmic scale
# for the x- and y-axes; that is, if the function value f (n) is y, plot this as a
# point with x-coordinate at log n and y-coordinate at log y.
# R-3.2 The number of operations executed by algorithms A and B is 8n log n and
# 2n2 , respectively. Determine n0 such that A is better than B for n ≥ n0 .
# R-3.3 The number of operations executed by algorithms A and B is 40n2 and
# 2n3 , respectively. Determine n0 such that A is better than B for n ≥ n0 .
# R-3.4 Give an example of a function that is plotted the same on a log-log scale
# as it is on a standard scale.
# R-3.5 Explain why the plot of the function nc is a straight line with slope c on a
# log-log scale.
# R-3.6 What is the sum of all the even numbers from 0 to 2n, for any positive
# integer n?
# R-3.7 Show that the following two statements are equivalent:
# (a) The running time of algorithm A is always O( f (n)).
# (b) In the worst case, the running time of algorithm A is O( f (n)).
# R-3.8 Order the following functions by asymptotic growth rate.
# 4n log n + 2n 210 2log n
# 3n + 100 log n 4n
# 2n
# n2 + 10n
# n3 n log n
# R-3.9 Show that if d(n) is O( f (n)), then ad(n) is O( f (n)), for any constant
# a > 0.
# R-3.10 Show that if d(n) is O( f (n)) and e(n) is O(g(n)), then the product d(n)e(n)
# is O( f (n)g(n)).
# R-3.11 Show that if d(n) is O( f (n)) and e(n) is O(g(n)), then d(n) + e(n) is
# O( f (n) + g(n)).
# R-3.12 Show that if d(n) is O( f (n)) and e(n) is O(g(n)), then d(n) − e(n) is not
# necessarily O( f (n) − g(n)).
# R-3.13 Show that if d(n) is O( f (n)) and f (n) is O(g(n)), then d(n) is O(g(n)).
# R-3.14 Show that O(max{ f (n), g(n)}) = O( f (n) + g(n)).
# R-3.15 Show that f (n) is O(g(n)) if and only if g(n) is Ω( f (n)).
# R-3.16 Show that if p(n) is a polynomial in n, then log p(n) is O(log n).
# R-3.17 Show that (n + 1)5 is O(n5 ).
# R-3.18 Show that 2n+1 is O(2n ).
# R-3.19 Show that n is O(n log n).
# R-3.20 Show that n2 is Ω(n log n).
# R-3.21 Show that n log n is Ω(n).
# R-3.22 Show that f (n) is O( f (n)), if f (n) is a positive nondecreasing function
# that is always greater than 1.
# R-3.23 Give a big-Oh characterization, in terms of n, of the running time of the
# example1 function shown in Code Fragment 3.10.
# R-3.24 Give a big-Oh characterization, in terms of n, of the running time of the
# example2 function shown in Code Fragment 3.10.
# R-3.25 Give a big-Oh characterization, in terms of n, of the running time of the
# example3 function shown in Code Fragment 3.10.
# R-3.26 Give a big-Oh characterization, in terms of n, of the running time of the
# example4 function shown in Code Fragment 3.10.
# R-3.27 Give a big-Oh characterization, in terms of n, of the running time of the
# example5 function shown in Code Fragment 3.10.
# R-3.28 For each function f (n) and time t in the following table, determine the
# largest size n of a problem P that can be solved in time t if the algorithm
# for solving P takes f (n) microseconds (one entry is already completed).
# 1 Second
# log n
# ≈ 10
# 1 Hour
# 1 Month
# 1 Century
# 300000
# n
# n log n
# n2
# 2n
# R-3.29 Algorithm A executes an O(log n)-time computation for each entry of an
# n-element sequence. What is its worst-case running time?
# R-3.30 Given an n-element sequence S, Algorithm B chooses log n elements in
# S at random and executes an O(n)-time calculation for each. What is the
# worst-case running time of Algorithm B?
# R-3.31 Given an n-element sequence S of integers, Algorithm C executes an
# O(n)-time computation for each even number in S, and an O(log n)-time
# computation for each odd number in S. What are the best-case and worst-
# case running times of Algorithm C?
# def example1(S):
# ”””Return the sum of the elements in sequence S.”””
# n = len(S)
# total = 0
# for j in range(n):
# # loop from 0 to n-1
# total += S[j]
# return total
# def example2(S):
# ”””Return the sum of the elements with even index in sequence S.”””
# n = len(S)
# total = 0
# for j in range(0, n, 2):
# # note the increment of 2
# total += S[j]
# return total
# def example3(S):
# ”””Return the sum of the preﬁx sums of sequence S.”””
# n = len(S)
# total = 0
# for j in range(n):
# # loop from 0 to n-1
# for k in range(1+j):
# # loop from 0 to j
# total += S[k]
# return total
# def example4(S):
# ”””Return the sum of the preﬁx sums of sequence S.”””
# n = len(S)
# preﬁx = 0
# total = 0
# for j in range(n):
# preﬁx += S[j]
# total += preﬁx
# return total
# def example5(A, B):
# # assume that A and B have equal length
# ”””Return the number of elements in B equal to the sum of preﬁx sums in A.”””
# n = len(A)
# count = 0
# for i in range(n):
# # loop from 0 to n-1
# total = 0
# for j in range(n):
# # loop from 0 to n-1
# for k in range(1+j):
# # loop from 0 to j
# total += A[k]
# if B[i] == total:
# count += 1
# return count
# R-3.32 Given an n-element sequence S, Algorithm D calls Algorithm E on each
# element S[i]. Algorithm E runs in O(i) time when it is called on element
# S[i]. What is the worst-case running time of Algorithm D?
# R-3.33 Al and Bob are arguing about their algorithms. Al claims his O(n log n)-
# time method is always faster than Bob’s O(n2 )-time method. To settle the
# issue, they perform a set of experiments. To Al’s dismay, they ﬁnd that if
# n < 100, the O(n2 )-time algorithm runs faster, and only when n ≥ 100 is
# the O(n log n)-time one better. Explain how this is possible.
# R-3.34 There is a well-known city (which will go nameless here) whose inhabi-
# tants have the reputation of enjoying a meal only if that meal is the best
# they have ever experienced in their life. Otherwise, they hate it. Assum-
# ing meal quality is distributed uniformly across a person’s life, describe
# the expected number of times inhabitants of this city are happy with their
# meals?
# C-3.35 Assuming it is possible to sort n numbers in O(n log n) time, show that it
# is possible to solve the three-way set disjointness problem in O(n log n)
# time.
# C-3.36 Describe an efﬁcient algorithm for ﬁnding the ten largest elements in a
# sequence of size n. What is the running time of your algorithm?
# C-3.37 Give an example of a positive function f (n) such that f (n) is neither O(n)
# nor Ω(n).
# C-3.38 Show that ∑ni=1 i2 is O(n3 ).
# C-3.39 Show that ∑ni=1 i/2i < 2. (Hint: Try to bound this sum term by term with
# a geometric progression.)
# C-3.40 Show that logb f (n) is Θ(log f (n)) if b > 1 is a constant.
# C-3.41 Describe an algorithm for ﬁnding both the minimum and maximum of n
# numbers using fewer than 3n/2 comparisons. (Hint: First, construct a
# group of candidate minimums and a group of candidate maximums.)
# C-3.42 Bob built a Web site and gave the URL only to his n friends, which he
# numbered from 1 to n. He told friend number i that he/she can visit the
# Web site at most i times. Now Bob has a counter, C, keeping track of the
# total number of visits to the site (but not the identities of who visits). What
# is the minimum value for C such that Bob can know that one of his friends
# has visited his/her maximum allowed number of times?
# C-3.43 Draw a visual justiﬁcation of Proposition 3.3 analogous to that of Fig-
# ure 3.3(b) for the case when n is odd.
# C-3.44 Communication security is extremely important in computer networks,
# and one way many network protocols achieve security is to encrypt mes-
# sages. Typical cryptographic schemes for the secure transmission of mes-
# sages over such networks are based on the fact that no efﬁcient algorithms
# are known for factoring large integers. Hence, if we can represent a secret
# message by a large prime number p, we can transmit, over the network,
# the number r = p · q, where q > p is another large prime number that acts
# as the encryption key. An eavesdropper who obtains the transmitted num-
# ber r on the network would have to factor r in order to ﬁgure out the secret
# message p.
# Using factoring to ﬁgure out a message is very difﬁcult without knowing
# the encryption key q. To understand why, consider the following naive
# factoring algorithm:
# for p in range(2,r):
# if r % p == 0:
# return The secret message is p!
# # if p divides r
# a. Suppose that the eavesdropper uses the above algorithm and has a
# computer that can carry out in 1 microsecond (1 millionth of a sec-
# ond) a division between two integers of up to 100 bits each. Give an
# estimate of the time that it will take in the worst case to decipher the
# secret message p if the transmitted message r has 100 bits.
# b. What is the worst-case time complexity of the above algorithm?
# Since the input to the algorithm is just one large number r, assume
# that the input size n is the number of bytes needed to store r, that is,
# n = (log2 r)/8 + 1, and that each division takes time O(n).
# C-3.45 A sequence S contains n − 1 unique integers in the range [0, n − 1], that
# is, there is one number from this range that is not in S. Design an O(n)-
# time algorithm for ﬁnding that number. You are only allowed to use O(1)
# additional space besides the sequence S itself.
# C-3.46 Al says he can prove that all sheep in a ﬂock are the same color:
# Base case: One sheep. It is clearly the same color as itself.
# Induction step: A ﬂock of n sheep. Take a sheep, a, out. The remaining
# n − 1 are all the same color by induction. Now put sheep a back in and
# take out a different sheep, b. By induction, the n − 1 sheep (now with a)
# are all the same color. Therefore, all the sheep in the ﬂock are the same
# color. What is wrong with Al’s “justiﬁcation”?
# C-3.47 Let S be a set of n lines in the plane such that no two are parallel and
# no three meet in the same point. Show, by induction, that the lines in S
# determine Θ(n2 ) intersection points.
# C-3.48 Consider the following “justiﬁcation” that the Fibonacci function, F(n)
# (see Proposition 3.20) is O(n):
# Base case (n ≤ 2): F(1) = 1 and F(2) = 2.
# Induction step (n > 2): Assume claim true for n < n. Consider n. F(n) =
# F(n − 2) + F (n − 1). By induction, F(n − 2) is O(n − 2) and F(n − 1) is
# O(n − 1). Then, F(n) is O((n − 2) + (n − 1)), by the identity presented in
# Exercise R-3.11. Therefore, F(n) is O(n).
# What is wrong with this “justiﬁcation”?
# C-3.49 Consider the Fibonacci function, F(n) (see Proposition 3.20). Show by
# induction that F(n) is Ω((3/2)n ).
# C-3.50 Let p(x) be a polynomial of degree n, that is, p(x) = ∑ni=0 ai xi .
# (a) Describe a simple O(n2 )-time algorithm for computing p(x).
# (b) Describe an O(n log n)-time algorithm for computing p(x), based upon
# a more efﬁcient calculation of xi .
# (c) Now consider a rewriting of p(x) as
# p(x) = a0 + x(a1 + x(a2 + x(a3 + · · · + x(an−1 + xan ) · · · ))),
# which is known as Horner’s method. Using the big-Oh notation, charac-
# terize the number of arithmetic operations this method executes.
# C-3.51 Show that the summation ∑ni=1 log i is O(n log n).
# C-3.52 Show that the summation ∑ni=1 log i is Ω(n log n).
# C-3.53 An evil king has n bottles of wine, and a spy has just poisoned one of
# them. Unfortunately, they do not know which one it is. The poison is very
# deadly; just one drop diluted even a billion to one will still kill. Even so,
# it takes a full month for the poison to take effect. Design a scheme for
# determining exactly which one of the wine bottles was poisoned in just
# one month’s time while expending O(log n) taste testers.
# C-3.54 A sequence S contains n integers taken from the interval [0, 4n], with repe-
# titions allowed. Describe an efﬁcient algorithm for determining an integer
# value k that occurs the most often in S. What is the running time of your
# algorithm?
# P-3.55 Perform an experimental analysis of the three algorithms preﬁx average1,
# preﬁx average2, and preﬁx average3, from Section 3.3.3. Visualize their
# running times as a function of the input size with a log-log chart.
# P-3.56 Perform an experimental analysis that compares the relative running times
# of the functions shown in Code Fragment 3.10.
# P-3.57 Perform experimental analysis to test the hypothesis that Python’s sorted
# method runs in O(n log n) time on average.
# P-3.58 For each of the three algorithms, unique1, unique2, and unique3, which
# solve the element uniqueness problem, perform an experimental analysis
# to determine the largest value of n such that the given algorithm runs in
# one minute or less.


# In[ ]:





# ## Stacks, Queues, and Dequeues

# In[7]:


class ArrayStack:
    """
    LIFO Stack implementation using a Python list as underlying storage.
    """
    def __init__ (self):
        """Create an empty stack."""
        # nonpublic list instance
        self. data = [ ]
    
    def len (self):
        """Return the number of elements in the stack."""
        return len(self. data)
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self. data) == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        # new item stored at end of list
        self. data.append(e)
        
    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        """
        if self.isempty( ):
            raise Empty( "Stack is empty" )
        # the last item in the list
        return self. data[-1]
    
    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty( ):
            raise Empty( "Stack is empty" )
        return self. data.pop( )


# In[11]:


def reverse_ﬁle(ﬁlename):
    """Overwrite given ﬁle with its contents line-by-line reversed."""
    S = ArrayStack( )
    original = open(ﬁlename)
    for line in original:
        # we will re-insert newlines when writing
        S.push(line.rstrip( "\n" ))
    original.close( )
    # now we overwrite with contents in LIFO order
    # reopening ﬁle overwrites original
    output = open(ﬁlename, w )
    while not S.is_empty( ):
        output.write(S.pop( ) + "\n" ) # re-insert newline characters
    output.close( )


# In[13]:


def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    # opening delimiters
    lefty = "({["
    # respective closing delims
    righty = ")}]"
    S = ArrayStack( )
    for c in expr:
        if c in lefty:
            S.push(c)
        # push left delimiter on stack
        elif c in righty:
            if S.is_empty( ):
                return False
            # nothing to match with
            if righty.index(c) != lefty.index(S.pop( )):
                return False
    # mismatched
    # were all symbols matched?
    return S.is_empty( )


# In[17]:


def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack( )
    # ﬁnd ﬁrst ’<’ character (if any)
    j = raw.ﬁnd( '<' )
    while j != -1:
    # ﬁnd next ’>’ character
        k = raw.ﬁnd( '>' , j+1)
        if k == -1:
            return False
        # invalid tag
        tag = raw[j+1:k]
        # strip away < >
        # this is opening tag
        if not tag.startswith( '/' ):
            S.push(tag)
        else:
            # this is closing tag
            if S.is_empty( ):
                return False
            # nothing to match with
            if tag[1:] != S.pop( ):
                return False
        # mismatched delimiter
        # ﬁnd next ’<’ character (if any)
    j = raw.ﬁnd( '<' , k+1)
    # were all opening tags matched?
    return S.is_empty( )


# In[18]:


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""

    # Moderate capacity for all new queues
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue."""
        self.data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self.size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self.size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self.data[self.front]
        # Help garbage collection
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self.size == len(self.data):
            # Double the array size
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    def resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        # Keep track of existing list
        old = self.data
        # Allocate list with new capacity
        self.data = [None] * cap
        walk = self.front
        
        # Only consider existing elements
        for k in range(self.size):
            # Intentionally shift indices
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        
        # Front has been realigned
        self.front = 0


# In[ ]:





# ## Assignment

# In[ ]:


# R-6.1 What values are returned during the following series of stack operations, if
# executed upon an initially empty stack? push(5), push(3), pop(), push(2),
# push(8), pop(), pop(), push(9), push(1), pop(), push(7), push(6), pop(),
# pop(), push(4), pop(), pop().
# R-6.2 Suppose an initially empty stack S has executed a total of 25 push opera-
# tions, 12 top operations, and 10 pop operations, 3 of which raised Empty
# errors that were caught and ignored. What is the current size of S?
# R-6.3 Implement a function with signature transfer(S, T) that transfers all ele-
# ments from stack S onto stack T, so that the element that starts at the top
# of S is the ﬁrst to be inserted onto T, and the element at the bottom of S
# ends up at the top of T.
# R-6.4 Give a recursive method for removing all the elements from a stack.
# R-6.5 Implement a function that reverses a list of elements by pushing them onto
# a stack in one order, and writing them back to the list in reversed order.
# R-6.6 Give a precise and complete deﬁnition of the concept of matching for
# grouping symbols in an arithmetic expression. Your deﬁnition may be
# recursive.
# R-6.7 What values are returned during the following sequence of queue opera-
# tions, if executed on an initially empty queue? enqueue(5), enqueue(3),
# dequeue(), enqueue(2), enqueue(8), dequeue(), dequeue(), enqueue(9),
# enqueue(1), dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(),
# enqueue(4), dequeue(), dequeue().
# R-6.8 Suppose an initially empty queue Q has executed a total of 32 enqueue
# operations, 10 ﬁrst operations, and 15 dequeue operations, 5 of which
# raised Empty errors that were caught and ignored. What is the current
# size of Q?
# R-6.9 Had the queue of the previous problem been an instance of ArrayQueue
# that used an initial array of capacity 30, and had its size never been greater
# than 30, what would be the ﬁnal value of the front instance variable?
# R-6.10 Consider what happens if the loop in the ArrayQueue. resize method at
# lines 53–55 of Code Fragment 6.7 had been implemented as:
# for k in range(self. size):
# self. data[k] = old[k]
# # rather than old[walk]
# Give a clear explanation of what could go wrong.
# R-6.11 Give a simple adapter that implements our queue ADT while using a
# collections.deque instance for storage.
# R-6.12 What values are returned during the following sequence of deque ADT op-
# erations, on initially empty deque? add ﬁrst(4), add last(8), add last(9),
# add ﬁrst(5), back( ), delete ﬁrst( ), delete last( ), add last(7), ﬁrst( ),
# last( ), add last(6), delete ﬁrst( ), delete ﬁrst( ).
# R-6.13 Suppose you have a deque D containing the numbers (1, 2, 3, 4, 5, 6, 7, 8),
# in this order. Suppose further that you have an initially empty queue Q.
# Give a code fragment that uses only D and Q (and no other variables) and
# results in D storing the elements in the order (1, 2, 3, 5, 4, 6, 7, 8).
# R-6.14 Repeat the previous problem using the deque D and an initially empty
# stack S.
# C-6.15 Suppose Alice has picked three distinct integers and placed them into a
# stack S in random order. Write a short, straight-line piece of pseudo-code
# (with no loops or recursion) that uses only one comparison and only one
# variable x, yet that results in variable x storing the largest of Alice’s three
# integers with probability 2/3. Argue why your method is correct.
# C-6.16 Modify the ArrayStack implementation so that the stack’s capacity is lim-
# ited to maxlen elements, where maxlen is an optional parameter to the
# constructor (that defaults to None). If push is called when the stack is at
# full capacity, throw a Full exception (deﬁned similarly to Empty).
# C-6.17 In the previous exercise, we assume that the underlying list is initially
# empty. Redo that exercise, this time preallocating an underlying list with
# length equal to the stack’s maximum capacity.
# C-6.18 Show how to use the transfer function, described in Exercise R-6.3, and
# two temporary stacks, to replace the contents of a given stack S with those
# same elements, but in reversed order.
# C-6.19 In Code Fragment 6.5 we assume that opening tags in HTML have form
# <name>, as with <li>. More generally, HTML allows optional attributes
# to be expressed as part of an opening tag. The general form used is
# <name attribute1="value1" attribute2="value2">; for example,
# a table can be given a border and additional padding by using an opening
# tag of <table border="3" cellpadding="5">. Modify Code Frag-
# ment 6.5 so that it can properly match tags, even when an opening tag
# may include one or more such attributes.
# C-6.20 Describe a nonrecursive algorithm for enumerating all permutations of the
# numbers {1, 2, . . . , n} using an explicit stack.
# C-6.21 Show how to use a stack S and a queue Q to generate all possible subsets
# of an n-element set T nonrecursively.
# C-6.22 Postﬁx notation is an unambiguous way of writing an arithmetic expres-
# sion without parentheses. It is deﬁned so that if “(exp1 ) op (exp2 )” is a
# normal, fully parenthesized expression whose operation is op, the postﬁx
# version of this is “pexp1 pexp2 op”, where pexp1 is the postﬁx version of
# exp1 and pexp2 is the postﬁx version of exp2 . The postﬁx version of a sin-
# gle number or variable is just that number or variable. For example, the
# postﬁx version of “((5 + 2) ∗ (8 − 3))/4” is “5 2 + 8 3 − ∗ 4 /”. Describe
# a nonrecursive way of evaluating an expression in postﬁx notation.
# C-6.23 Suppose you have three nonempty stacks R, S, and T . Describe a sequence
# of operations that results in S storing all elements originally in T below all
# of S’s original elements, with both sets of those elements in their original
# order. The ﬁnal conﬁguration for R should be the same as its original
# conﬁguration. For example, if R = [1, 2, 3], S = [4, 5], and T = [6, 7, 8, 9],
# the ﬁnal conﬁguration should have R = [1, 2, 3] and S = [6, 7, 8, 9, 4, 5].
# C-6.24 Describe how to implement the stack ADT using a single queue as an
# instance variable, and only constant additional local memory within the
# method bodies. What is the running time of the push(), pop(), and top()
# methods for your design?
# C-6.25 Describe how to implement the queue ADT using two stacks as instance
# variables, such that all queue operations execute in amortized O(1) time.
# Give a formal proof of the amortized bound.
# C-6.26 Describe how to implement the double-ended queue ADT using two stacks
# as instance variables. What are the running times of the methods?
# C-6.27 Suppose you have a stack S containing n elements and a queue Q that is
# initially empty. Describe how you can use Q to scan S to see if it contains a
# certain element x, with the additional constraint that your algorithm must
# return the elements back to S in their original order. You may only use S,
# Q, and a constant number of other variables.
# C-6.28 Modify the ArrayQueue implementation so that the queue’s capacity is
# limited to maxlen elements, where maxlen is an optional parameter to the
# constructor (that defaults to None). If enqueue is called when the queue
# is at full capacity, throw a Full exception (deﬁned similarly to Empty).
# C-6.29 In certain applications of the queue ADT, it is common to repeatedly
# dequeue an element, process it in some way, and then immediately en-
# queue the same element. Modify the ArrayQueue implementation to in-
# clude a rotate( ) method that has semantics identical to the combina-
# tion, Q.enqueue(Q.dequeue( )). However, your implementation should
# be more efﬁcient than making two separate calls (for example, because
# there is no need to modify size).
# C-6.30 Alice has two queues, Q and R, which can store integers. Bob gives Alice
# 50 odd integers and 50 even integers and insists that she store all 100
# integers in Q and R. They then play a game where Bob picks Q or R
# at random and then applies the round-robin scheduler, described in the
# chapter, to the chosen queue a random number of times. If the last number
# to be processed at the end of this game was odd, Bob wins. Otherwise,
# Alice wins. How can Alice allocate integers to queues to optimize her
# chances of winning? What is her chance of winning?
# C-6.31 Suppose Bob has four cows that he wants to take across a bridge, but only
# one yoke, which can hold up to two cows, side by side, tied to the yoke.
# The yoke is too heavy for him to carry across the bridge, but he can tie
# (and untie) cows to it in no time at all. Of his four cows, Mazie can cross
# the bridge in 2 minutes, Daisy can cross it in 4 minutes, Crazy can cross
# it in 10 minutes, and Lazy can cross it in 20 minutes. Of course, when
# two cows are tied to the yoke, they must go at the speed of the slower cow.
# Describe how Bob can get all his cows across the bridge in 34 minutes.
# P-6.32 Give a complete ArrayDeque implementation of the double-ended queue
# ADT as sketched in Section 6.3.2.
# P-6.33 Give an array-based implementation of a double-ended queue supporting
# all of the public behaviors shown in Table 6.4 for the collections.deque
# class, including use of the maxlen optional parameter. When a length-
# limited deque is full, provide semantics similar to the collections.deque
# class, whereby a call to insert an element on one end of a deque causes an
# element to be lost from the opposite side.
# P-6.34 Implement a program that can input an expression in postﬁx notation (see
# Exercise C-6.22) and output its value.
# P-6.35 The introduction of Section 6.1 notes that stacks are often used to provide
# “undo” support in applications like a Web browser or text editor. While
# support for undo can be implemented with an unbounded stack, many
# applications provide only limited support for such an undo history, with a
# ﬁxed-capacity stack. When push is invoked with the stack at full capacity,
# rather than throwing a Full exception (as described in Exercise C-6.16),
# a more typical semantic is to accept the pushed element at the top while
# “leaking” the oldest element from the bottom of the stack to make room.
# Give an implementation of such a LeakyStack abstraction, using a circular
# array with appropriate storage capacity. This class should have a public
# interface similar to the bounded-capacity stack in Exercise C-6.16, but
# with the desired leaky semantics when full.
# P-6.36 When a share of common stock of some company is sold, the capital
# gain (or, sometimes, loss) is the difference between the share’s selling
# price and the price originally paid to buy it. This rule is easy to under-
# stand for a single share, but if we sell multiple shares of stock bought
# over a long period of time, then we must identify the shares actually be-
# ing sold. A standard accounting principle for identifying which shares of
# a stock were sold in such a case is to use a FIFO protocol—the shares
# sold are the ones that have been held the longest (indeed, this is the de-
# fault method built into several personal ﬁnance software packages). For
# example, suppose we buy 100 shares at $20 each on day 1, 20 shares at
# $24 on day 2, 200 shares at $36 on day 3, and then sell 150 shares on day
# 4 at $30 each. Then applying the FIFO protocol means that of the 150
# shares sold, 100 were bought on day 1, 20 were bought on day 2, and 30
# were bought on day 3. The capital gain in this case would therefore be
# 100 · 10 + 20 · 6 + 30 · (−6), or $940. Write a program that takes as input
# a sequence of transactions of the form “buy x share(s) at y each”
# or “sell x share(s) at y each,” assuming that the transactions oc-
# cur on consecutive days and the values x and y are integers. Given this
# input sequence, the output should be the total capital gain (or loss) for the
# entire sequence, using the FIFO protocol to identify shares.
# P-6.37 Design an ADT for a two-color, double-stack ADT that consists of two
# stacks—one “red” and one “blue”—and has as its operations color-coded
# versions of the regular stack ADT operations. For example, this ADT
# should support both a red push operation and a blue push operation. Give
# an efﬁcient implementation of this ADT using a single array whose ca-
# pacity is set at some value N that is assumed to always be larger than the
# sizes of the red and blue stacks combined.


# In[ ]:





# ## Priority Queues

# In[1]:


class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class Item:
        """Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            # Compare items based on their keys
            return self._key < other._key

    def is_empty(self):
        """Return True if the priority queue is empty."""
        return len(self) == 0


# In[2]:


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    # Nonpublic utility
    def _find_min(self):
        """Return Position of item with minimum key."""
        # is_empty inherited from base class
        if self.is_empty():
            raise Empty("Priority queue is empty")
        
        small = self.data.first()
        walk = self.data.after(small)
        
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self.data.after(walk)
        
        return small

    def __init__(self):
        """Create a new empty Priority Queue."""
        self.data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self.data)

    def add(self, key, value):
        """Add a key-value pair."""
        self.data.add_last(self.Item(key, value))

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item = self.data.delete(p)
        return (item._key, item._value)


# In[3]:


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self.data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self.data)

    def add(self, key, value):
        """Add a key-value pair."""
        # Make new item instance
        newest = self.Item(key, value)
        # Walk backward looking for smaller key
        walk = self.data.last()
        
        while walk is not None and newest < walk.element():
            walk = self.data.before(walk)
        
        if walk is None:
            # New key is smallest
            self.data.add_first(newest)
        else:
            # Newest goes after walk
            self.data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        
        p = self.data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        
        item = self.data.delete(self.data.first())
        return (item._key, item._value)


# In[6]:


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap."""

    # ------------------------------ Nonpublic Behaviors ------------------------------
    
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self.data)  # Index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self.data)  # Index beyond end of list?

    def _swap(self, i, j):
        """Swap the elements at indices i and j of the array."""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self.data[j] < self.data[parent]:
            self._swap(j, parent)
            # Recur at position of parent
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            # Although right may be smaller
            small_child = left
            
            if self._has_right(j):
                right = self._right(j)
                if self.data[right] < self.data[left]:
                    small_child = right
            
            if self.data[small_child] < self.data[j]:
                self._swap(j, small_child)
                # Recur at position of small child
                self._downheap(small_child)

    # ------------------------------ Public Behaviors ------------------------------
    
#     def __init__(self):
#         """Create a new empty Priority Queue."""
#         self.data = []

    def __init__(self, contents=()):
        """Create a new priority queue.
        By default, the queue will be empty. If contents is given, it should be 
        as an iterable sequence of (k,v) tuples specifying the initial contents.
        """
        # Initialize data with given contents
        self.data = [self.Item(k, v) for k, v in contents]

        # Heapify if there are more than one item
        if len(self.data) > 1:
            self.heapify()

    def heapify(self):
        """Transform the list into a heap."""
        start = self._parent(len(self.data) - 1)
        for j in range(start, -1, -1):
            self._downheap(j)

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self.data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self.data.append(self.Item(key, value))
        # Upheap newly added position
        self._upheap(len(self.data) - 1)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        
        item = self.data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty("Priority queue is empty.")
        
        # Put minimum item at the end
        self._swap(0, len(self.data) - 1)
        
        # Remove it from the list
        item = self.data.pop()
        
        # Then fix new root
        self._downheap(0)
        
        return (item._key, item._value)


# In[7]:


def pq_sort(C):
    """Sort a collection of elements stored in a positional list."""
    n = len(C)
    P = HeapPriorityQueue()  # Assuming PriorityQueue is defined elsewhere

    # Remove elements from C and add them to the priority queue
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)  # Use element as both key and value

    # Remove elements from the priority queue and add them back to C
    for j in range(n):
        (k, v) = P.remove_min()  # Get the smallest element
        C.add_last(v)  # Store the smallest remaining element in C


# In[8]:


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    # ------------------------------ Nested Locator Class ------------------------------
    
    class Locator(HeapPriorityQueue.Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = '_index'  # Add index as an additional field

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    # ------------------------------ Nonpublic Behaviors ------------------------------
    
    # Override swap to record new indices
    def _swap(self, i, j):
        # Perform the swap
        super()._swap(i, j)
        # Reset locator index (post-swap)
        self.data[i]._index = i
        self.data[j]._index = j

    def _bubble(self, j):
        if j > 0 and self.data[j] < self.data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        """Add a key-value pair."""
        token = self.Locator(key, value, len(self.data))  # Initialize locator index
        self.data.append(token)
        self._upheap(len(self.data) - 1)
        return token

    def update(self, loc, newkey, newval):
        """Update the key and value for the entry identified by Locator loc."""
        j = loc._index
        if not (0 <= j < len(self) and self.data[j] is loc):
            raise ValueError("Invalid locator")
        
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        """Remove and return the (k,v) pair identified by Locator loc."""
        j = loc._index
        if not (0 <= j < len(self) and self.data[j] is loc):
            raise ValueError("Invalid locator")
        
        if j == len(self) - 1:
            # Item at last position; just remove it
            self.data.pop()
        else:
            # Swap item to the last position
            self._swap(j, len(self.data) - 1)
            # Remove it from the list
            self.data.pop()
            # Fix item displaced by the swap
            self._bubble(j)
        
        return (loc._key, loc._value)


# ## Assignment

# In[9]:


# R-9.1 How long would it take to remove the log n smallest elements from a
# heap that contains n entries, using the remove min operation?
# R-9.2 Suppose you label each position p of a binary tree T with a key equal to
# its preorder rank. Under what circumstances is T a heap?
# R-9.3 What does each remove min call return within the following sequence of
# priority queue ADT methods: add(5,A), add(4,B), add(7,F), add(1,D),
# remove min( ), add(3,J), add(6,L), remove min( ), remove min( ),
# add(8,G), remove min( ), add(2,H), remove min( ), remove min( )?
# R-9.4 An airport is developing a computer simulation of air-trafﬁc control that
# handles events such as landings and takeoffs. Each event has a time stamp
# that denotes the time when the event will occur. The simulation program
# needs to efﬁciently perform the following two fundamental operations:
# • Insert an event with a given time stamp (that is, add a future event).
# • Extract the event with smallest time stamp (that is, determine the
# next event to process).
# Which data structure should be used for the above operations? Why?
# R-9.5 The min method for the UnsortedPriorityQueue class executes in O(n)
# time, as analyzed in Table 9.2. Give a simple modiﬁcation to the class so
# that min runs in O(1) time. Explain any necessary modiﬁcations to other
# methods of the class.
# R-9.6 Can you adapt your solution to the previous problem to make remove min
# run in O(1) time for the UnsortedPriorityQueue class? Explain your an-
# swer.
# R-9.7 Illustrate the execution of the selection-sort algorithm on the following
# input sequence: (22, 15, 36, 44, 10, 3, 9, 13, 29, 25).
# R-9.8 Illustrate the execution of the insertion-sort algorithm on the input se-
# quence of the previous problem.
# R-9.9 Give an example of a worst-case sequence with n elements for insertion-
# sort, and show that insertion-sort runs in Ω(n2 ) time on such a sequence.
# R-9.10 At which positions of a heap might the third smallest key be stored?
# R-9.11 At which positions of a heap might the largest key be stored?
# R-9.12 Consider a situation in which a user has numeric keys and wishes to have
# a priority queue that is maximum-oriented. How could a standard (min-
# oriented) priority queue be used for such a purpose?
# R-9.13 Illustrate the execution of the in-place heap-sort algorithm on the follow-
# ing input sequence: (2, 5, 16, 4, 10, 23, 39, 18, 26, 15).
# R-9.14 Let T be a complete binary tree such that position p stores an element
# with key f (p), where f (p) is the level number of p (see Section 8.3.2). Is
# tree T a heap? Why or why not?
# R-9.15 Explain why the description of down-heap bubbling does not consider the
# case in which position p has a right child but not a left child.
# R-9.16 Is there a heap H storing seven entries with distinct keys such that a pre-
# order traversal of H yields the entries of H in increasing or decreasing
# order by key? How about an inorder traversal? How about a postorder
# traversal? If so, give an example; if not, say why.
# R-9.17 Let H be a heap storing 15 entries using the array-based representation of
# a complete binary tree. What is the sequence of indices of the array that
# are visited in a preorder traversal of H? What about an inorder traversal
# of H? What about a postorder traversal of H?
# R-9.18 Show that the sum
# n
# ∑ log i,
# i=1
# which appears in the analysis of heap-sort, is Ω(n log n).
# R-9.19 Bill claims that a preorder traversal of a heap will list its keys in nonde-
# creasing order. Draw an example of a heap that proves him wrong.
# R-9.20 Hillary claims that a postorder traversal of a heap will list its keys in non-
# increasing order. Draw an example of a heap that proves her wrong.
# R-9.21 Show all the steps of the algorithm for removing the entry (16, X ) from the
# heap of Figure 9.1, assuming the entry had been identiﬁed with a locator.
# R-9.22 Show all the steps of the algorithm for replacing key of entry (5, A) with
# 18 in the heap of Figure 9.1, assuming the entry had been identiﬁed with
# a locator.
# R-9.23 Draw an example of a heap whose keys are all the odd numbers from 1 to
# 59 (with no repeats), such that the insertion of an entry with key 32 would
# cause up-heap bubbling to proceed all the way up to a child of the root
# (replacing that child’s key with 32).
# R-9.24 Describe a sequence of n insertions in a heap that requires Ω(n log n) time
# to process.
# R-9.25 Complete Figure 9.9 by showing all the steps of the in-place heap-sort
# algorithm. Show both the array and the associated heap at the end of each
# step.
# C-9.26 Show how to implement the stack ADT using only a priority queue and
# one additional integer instance variable.
# C-9.27 Show how to implement the FIFO queue ADT using only a priority queue
# and one additional integer instance variable.
# C-9.28 Professor Idle suggests the following solution to the previous problem.
# Whenever an item is inserted into the queue, it is assigned a key that is
# equal to the current size of the queue. Does such a strategy result in FIFO
# semantics? Prove that it is so or provide a counterexample.
# C-9.29 Reimplement the SortedPriorityQueue using a Python list. Make sure to
# maintain remove min’s O(1) performance.
# C-9.30 Give a nonrecursive implementation of the upheap method for the class
# HeapPriorityQueue.
# C-9.31 Give a nonrecursive implementation of the downheap method for the
# class HeapPriorityQueue.
# C-9.32 Assume that we are using a linked representation of a complete binary
# tree T , and an extra reference to the last node of that tree. Show how to
# update the reference to the last node after operations add or remove min
# in O(log n) time, where n is the current number of nodes of T . Be sure
# and handle all possible cases, as illustrated in Figure 9.12.
# C-9.33 When using a linked-tree representation for a heap, an alternative method
# for ﬁnding the last node during an insertion in a heap T is to store, in the
# last node and each leaf node of T , a reference to the leaf node immedi-
# ately to its right (wrapping to the ﬁrst node in the next lower level for the
# rightmost leaf node). Show how to maintain such references in O(1) time
# per operation of the priority queue ADT assuming that T is implemented
# with a linked structure.
# Figure 9.12: Updating the last node in a complete binary tree after operation add or
# remove. Node w is the last node before operation add or after operation remove.
# Node z is the last node after operation add or before operation remove.
# C-9.34 We can represent a path from the root to a given node of a binary tree
# by means of a binary string, where 0 means “go to the left child” and 1
# means “go to the right child.” For example, the path from the root to the
# node storing (8,W ) in the heap of Figure 9.12a is represented by “101.”
# Design an O(log n)-time algorithm for ﬁnding the last node of a complete
# binary tree with n nodes, based on the above representation. Show how
# this algorithm can be used in the implementation of a complete binary tree
# by means of a linked structure that does not keep a reference to the last
# node.
# C-9.35 Given a heap T and a key k, give an algorithm to compute all the entries
# in T having a key less than or equal to k. For example, given the heap of
# Figure 9.12a and query k = 7, the algorithm should report the entries with
# keys 2, 4, 5, 6, and 7 (but not necessarily in this order). Your algorithm
# should run in time proportional to the number of entries returned, and
# should not modify the heap
# C-9.36 Provide a justiﬁcation of the time bounds in Table 9.4.
# C-9.37 Give an alternative analysis of bottom-up heap construction by showing
# the following summation is O(1), for any positive integer h:
# h
# ∑ i/2i .
# i=1
# C-9.38 Suppose two binary trees, T1 and T2 , hold entries satisfying the heap-order
# property (but not necessarily the complete binary tree property). Describe
# a method for combining T1 and T2 into a binary tree T , whose nodes hold
# the union of the entries in T1 and T2 and also satisfy the heap-order prop-
# erty. Your algorithm should run in time O(h1 + h2 ) where h1 and h2 are
# the respective heights of T1 and T2 .
# C-9.39 Implement a heappushpop method for the HeapPriorityQueue class, with
# semantics akin to that described for the heapq module in Section 9.3.7.
# C-9.40 Implement a heapreplace method for the HeapPriorityQueue class, with
# semantics akin to that described for the heapq module in Section 9.3.7.
# C-9.41 Tamarindo Airlines wants to give a ﬁrst-class upgrade coupon to their top
# log n frequent ﬂyers, based on the number of miles accumulated, where
# n is the total number of the airlines’ frequent ﬂyers. The algorithm they
# currently use, which runs in O(n log n) time, sorts the ﬂyers by the number
# of miles ﬂown and then scans the sorted list to pick the top log n ﬂyers.
# Describe an algorithm that identiﬁes the top logn ﬂyers in O(n) time.
# C-9.42 Explain how the k largest elements from an unordered collection of size n
# can be found in time O(n + k log n) using a maximum-oriented heap.
# C-9.43 Explain how the k largest elements from an unordered collection of size n
# can be found in time O(n log k) using O(k) auxiliary space.
# C-9.44 Given a class, PriorityQueue, that implements the minimum-oriented pri-
# ority queue ADT, provide an implementation of a MaxPriorityQueue class
# that adapts to provide a maximum-oriented abstraction with methods add,
# max, and remove max. Your implementation should not make any as-
# sumption about the internal workings of the original PriorityQueue class,
# nor the type of keys that might be used.
# C-9.45 Write a key function for nonnegative integers that determines order based
# on the number of 1’s in each integer’s binary expansion.
# C-9.46 Give an alternative implementation of the pq sort function, from Code
# Fragment 9.7, that accepts a key function as an optional parameter.
# C-9.47 Describe an in-place version of the selection-sort algorithm for an array
# that uses only O(1) space for instance variables in addition to the array.
# C-9.48 Assuming the input to the sorting problem is given in an array A, describe
# how to implement the insertion-sort algorithm using only the array A and
# at most a constant number of additional variables.
# C-9.49 Give an alternate description of the in-place heap-sort algorithm using
# the standard minimum-oriented priority queue (instead of a maximum-
# oriented one).
# C-9.50 An online computer system for trading stocks needs to process orders of
# the form “buy 100 shares at $x each” or “sell 100 shares at $y each.” A
# buy order for $x can only be processed if there is an existing sell order
# with price $y such that y ≤ x. Likewise, a sell order for $y can only be
# processed if there is an existing buy order with price $x such that y ≤ x.
# If a buy or sell order is entered but cannot be processed, it must wait for a
# future order that allows it to be processed. Describe a scheme that allows
# buy and sell orders to be entered in O(log n) time, independent of whether
# or not they can be immediately processed.
# C-9.51 Extend a solution to the previous problem so that users are allowed to
# update the prices for their buy or sell orders that have yet to be processed.
# C-9.52 A group of children want to play a game, called Unmonopoly, where in
# each turn the player with the most money must give half of his/her money
# to the player with the least amount of money. What data structure(s)
# should be used to play this game efﬁciently? Why?
# P-9.53 Implement the in-place heap-sort algorithm. Experimentally compare its
# running time with that of the standard heap-sort that is not in-place.
# P-9.54 Use the approach of either Exercise C-9.42 or C-9.43 to reimplement the
# top method of the FavoritesListMTF class from Section 7.6.2. Make sure
# that results are generated from largest to smallest.
# P-9.55 Write a program that can process a sequence of stock buy and sell orders
# as described in Exercise C-9.50.
# P-9.56 Let S be a set of n points in the plane with distinct integer x- and y-
# coordinates. Let T be a complete binary tree storing the points from S
# at its external nodes, such that the points are ordered left to right by in-
# creasing x-coordinates. For each node v in T , let S(v) denote the subset of
# S consisting of points stored in the subtree rooted at v. For the root r of
# T , deﬁne top(r) to be the point in S = S(r) with maximum y-coordinate.
# For every other node v, deﬁne top(r) to be the point in S with highest y-
# coordinate in S(v) that is not also the highest y-coordinate in S(u), where
# u is the parent of v in T (if such a point exists). Such labeling turns T into
# a priority search tree. Describe a linear-time algorithm for turning T into
# a priority search tree. Implement this approach.
# P-9.57 One of the main applications of priority queues is in operating systems—
# for scheduling jobs on a CPU. In this project you are to build a program
# that schedules simulated CPU jobs. Your program should run in a loop,
# each iteration of which corresponds to a time slice for the CPU. Each job
# is assigned a priority, which is an integer between −20 (highest priority)
# and 19 (lowest priority), inclusive. From among all jobs waiting to be pro-
# cessed in a time slice, the CPU must work on a job with highest priority.
# In this simulation, each job will also come with a length value, which is an
# integer between 1 and 100, inclusive, indicating the number of time slices
# that are needed to process this job. For simplicity, you may assume jobs
# cannot be interrupted—once it is scheduled on the CPU, a job runs for a
# number of time slices equal to its length. Your simulator must output the
# name of the job running on the CPU in each time slice and must process
# a sequence of commands, one per time slice, each of which is of the form
# “add job name with length n and priority p” or “no new job this slice”.
# P-9.58 Develop a Python implementation of an adaptable priority queue that is
# based on an unsorted list and supports location-aware entries.


# In[ ]:





# ## Trees

# In[31]:


class Tree:
    """Abstract base class representing a tree structure."""

    # ------------------------------- nested Position class -------------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError("must be implemented by subclass")

        def eq(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("must be implemented by subclass")

        def ne(self, other):
            """Return True if other does not represent the same location."""
            return not self.eq(other)  # opposite of eq

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError("must be implemented by subclass")

    def positions(self):
        """Generate an iteration of all positions in the tree."""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("must be implemented by subclass")

    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height1(self):
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def height2(self, p):
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.
           If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        # start height2 recursion
        return self.height2(p)


# In[32]:


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # --------------------- additional abstract methods ---------------------
    def left(self, p):
        """Return a Position representing p's left child.
        
        Return None if p does not have a left child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Return a Position representing p's right child.
        
        Return None if p does not have a right child.
        """
        raise NotImplementedError("must be implemented by subclass")

    # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            # p must be the root; root has no sibling
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)  # possibly None
            else:
                return self.left(parent)  # possibly None

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


# In[ ]:





# In[33]:


class LinkedBinaryTree(BinaryTree):
    # Lightweight, nonpublic class for storing a node.
    class Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    # -------------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self.make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self.validate(p)
        return self.make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self.validate(p)
        return self.make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self.validate(p)
        return self.make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self.validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
           Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError("Root exists")

        self._size = 1
        self._root = self.Node(e)
        return self.make_position(self._root)

    def add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
           Return the Position of new node.
           Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self.validate(p)

        if node._left is not None:
            raise ValueError("Left child exists")

        self._size += 1
        node._left = self.Node(e, node)
        return self.make_position(node._left)

    def add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
           Return the Position of new node.
           Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self.validate(p)

        if node._right is not None:
            raise ValueError("Right child exists")

        self._size += 1
        node._right = self.Node(e, node)
        return self.make_position(node._right)

    def replace(self, p, e):
        """Replace the element at position p with e and return old element."""
        node = self.validate(p)

        old = node._element
        node._element = e

        return old

    def delete(self, p):
        """Delete the node at Position p and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self.validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")

        child = node._left if node._left else node._right

        if child is not None:
            child._parent = node._parent

        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        node._parent = node

        return node._element

    def attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self.validate(p)

        if not self.is_leaf(p):
            raise ValueError("Position must be leaf")

        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")

        self._size += len(t1) + len(t2)

        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0

        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self.subtree_preorder(self.root()):
                yield p

    def subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p
        for c in self.children(p):
            for other in self.subtree_preorder(c):
                yield other

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.preorder()

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self.subtree_postorder(self.root()):
                yield p

    def subtree_postorder(self, p):
        """Generate a postorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):
            for other in self.subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self.subtree_inorder(self.root()):
                yield p

    def subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:
            for other in self.subtree_inorder(self.left(p)):
                yield other

        yield p

        if self.right(p) is not None:
            for other in self.subtree_inorder(self.right(p)):
                yield other


# In[ ]:





# In[23]:


class EulerTour:
    """Abstract base class for performing Euler tour of a tree.
    
    Hook methods `hook_previsit` and `hook_postvisit` may be overridden by subclasses.
    """

    def __init__(self, tree):
        """Prepare an Euler tour template for the given tree."""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed."""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post visit of root."""
        if len(self.tree()) > 0:
            # Start the recursion
            return self.tour(self.tree().root(), 0, [])

    def tour(self, p, d, path):
        """Perform tour of subtree rooted at Position p.

        Parameters:
        p: Position of current node being visited
        d: Depth of p in the tree
        path: List of indices of children on path from root to p
        """
        # Pre-visit p
        self.hook_previsit(p, d, path)
        
        results = []
        path.append(0)  # Add new index to end of path before recursion
        
        for c in self.tree().children(p):
            # Recur on child's subtree
            results.append(self.tour(c, d + 1, path))
            path[-1] += 1  # Increment index
        
        path.pop()  # Remove extraneous index from end of path
        
        # Post-visit p
        answer = self.hook_postvisit(p, d, path, results)
        return answer

    # Can be overridden
    def hook_previsit(self, p, d, path):
        pass

    # Can be overridden
    def hook_postvisit(self, p, d, path, results):
        pass


# In[24]:


class BinaryEulerTour(EulerTour):
    """Abstract base class for performing Euler tour of a binary tree.

    This version includes an additional hook `hook_invisit` that is called after the tour
    of the left subtree (if any), yet before the tour of the right subtree (if any).

    Note: Right child is always assigned index 1 in path, even if no left sibling.
    """

    def tour(self, p, d, path):
        results = [None, None]  # will update with results of recursions
        
        # Pre-visit for p
        self.hook_previsit(p, d, path)
        
        # Consider left child
        if self.tree().left(p) is not None:
            path.append(0)
            results[0] = self.tour(self.tree().left(p), d + 1, path)
            path.pop()
        
        # In-visit for p
        self.hook_invisit(p, d, path)
        
        # Consider right child
        if self.tree().right(p) is not None:
            path.append(1)
            results[1] = self.tour(self.tree().right(p), d + 1, path)
            path.pop()
        
        # Post-visit p
        answer = self.hook_postvisit(p, d, path, results)
        return answer

    # Can be overridden
    def hook_invisit(self, p, d, path):
        pass


# In[25]:


class BinaryLayout(BinaryEulerTour):
    """Class for computing (x, y) coordinates for each node of a binary tree."""

    def __init__(self, tree):
        # Must call the parent constructor
        super().__init__(tree)
        # Initialize count of processed nodes
        self.count = 0

    def hook_invisit(self, p, d, path):
        # x-coordinate serialized by count
        p.element().setX(self.count)
        p.element().setY(d)  # y-coordinate is depth
        # Advance count of processed nodes
        self.count += 1


# In[34]:


class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """Create an expression tree.

        In a single parameter form, token should be a leaf value (e.g., 42),
        and the expression tree will have that value at an isolated node.

        In a three-parameter version, token should be an operator,
        and left and right should be existing ExpressionTree instances
        that become the operands for the binary operator.
        """
        # LinkedBinaryTree initialization
        super().__init__()

        if not isinstance(token, str):
            raise TypeError("Token must be a string")

        # Use inherited method to add root
        self.add_root(token)

        if left is not None:
            # Presumably three-parameter form
            if token not in "+-*x/":
                raise ValueError("Token must be a valid operator")
            self.attach(self.root(), left, right)  # Use inherited method

    def __str__(self):
        """Return string representation of the expression."""
        pieces = []  # Sequence of piecewise strings to compose
        self.parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element()))  # Leaf value as a string
        else:
            result.append('(')  # Opening parenthesis
            # Left subtree
            self.parenthesize_recur(self.left(p), result)
            result.append(p.element())  # Operator
            # Right subtree
            self.parenthesize_recur(self.right(p), result)
            result.append(')')  # Closing parenthesis

    def evaluate(self):
        """Return the numeric result of the expression."""
        return self.evaluate_recur(self.root())

    def evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())  # We assume element is numeric
        else:
            op = p.element()
            left_val = self.evaluate_recur(self.left(p))
            right_val = self.evaluate_recur(self.right(p))
            
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            elif op in ('x', '*'):
                return left_val * right_val  # Treat 'x' or '*' as multiplication
            else:
                raise ValueError(f"Invalid operator: {op}")


# In[27]:


def build_expression_tree(tokens):
    """Returns an ExpressionTree based on a tokenized expression."""
    S = []  # We use Python list as stack

    for t in tokens:
        # t is an operator symbol
        if t in "+-*x/":
            S.append(t)  # Push the operator symbol
        
        # Consider t to be a literal
        elif t not in "()":
            S.append(ExpressionTree(t))  # Push trivial tree storing value
        
        elif t == ")":
            right = S.pop()  # Right subtree as per LIFO
            op = S.pop()     # Operator symbol
            left = S.pop()   # Left subtree
            S.append(ExpressionTree(op, left, right))  # Re-push tree
        
        # We ignore a left parenthesis

    return S.pop()  # Return the final expression tree


# In[ ]:





# ## Assignments

# In[29]:


# R-8.1 The following questions refer to the tree of Figure 8.3.
# a. Which node is the root?
# b. What are the internal nodes?
# c. How many descendants does node cs016/ have?
# d. How many ancestors does node cs016/ have?
# e. What are the siblings of node homeworks/?
# f. Which nodes are in the subtree rooted at node projects/?
# g. What is the depth of node papers/?
# h. What is the height of the tree?
# R-8.2 Show a tree achieving the worst-case running time for algorithm depth.
# R-8.3 Give a justiﬁcation of Proposition 8.4.
# R-8.4 What is the running time of a call to T. height2(p) when called on a
# position p distinct from the root of T? (See Code Fragment 8.5.)
# R-8.5 Describe an algorithm, relying only on the BinaryTree operations, that
# counts the number of leaves in a binary tree that are the left child of their
# respective parent.
# R-8.6 Let T be an n-node binary tree that may be improper. Describe how to
# represent T by means of a proper binary tree T  with O(n) nodes.
# R-8.7 What are the minimum and maximum number of internal and external
# nodes in an improper binary tree with n nodes?
# R-8.8 Answer the following questions so as to justify Proposition 8.8.
# a. What is the minimum number of external nodes for a proper binary
# tree with height h? Justify your answer.
# b. What is the maximum number of external nodes for a proper binary
# tree with height h? Justify your answer.
# c. Let T be a proper binary tree with height h and n nodes. Show that
# log(n + 1) − 1 ≤ h ≤ (n − 1)/2.
# d. For which values of n and h can the above lower and upper bounds
# on h be attained with equality?
# R-8.9 Give a proof by induction of Proposition 8.9.
# R-8.10 Give a direct implementation of the num children method within the class
# BinaryTree.
# R-8.11 Find the value of the arithmetic expression associated with each subtree
# of the binary tree of Figure 8.8.
# R-8.12 Draw an arithmetic expression tree that has four external nodes, storing
# the numbers 1, 5, 6, and 7 (with each number stored in a distinct external
# node, but not necessarily in this order), and has three internal nodes, each
# storing an operator from the set {+, −, ×, /}, so that the value of the root
# is 21. The operators may return and act on fractions, and an operator may
# be used more than once.
# R-8.13 Draw the binary tree representation of the following arithmetic expres-
# sion: “(((5 + 2) ∗ (2 − 1))/((2 + 9) + ((7 − 2) − 1)) ∗ 8)”.
# R-8.14 Justify Table 8.2, summarizing the running time of the methods of a tree
# represented with a linked structure, by providing, for each method, a de-
# scription of its implementation, and an analysis of its running time.
# R-8.15 The LinkedBinaryTree class provides only nonpublic versions of the up-
# date methods discussed on page 319. Implement a simple subclass named
# MutableLinkedBinaryTree that provides public wrapper functions for each
# of the inherited nonpublic update methods.
# R-8.16 Let T be a binary tree with n nodes, and let f () be the level numbering
# function of the positions of T , as given in Section 8.3.2.
# a. Show that, for every position p of T , f (p) ≤ 2n − 2.
# b. Show an example of a binary tree with seven nodes that attains the
# above upper bound on f (p) for some position p.
# R-8.17 Show how to use the Euler tour traversal to compute the level number
# f (p), as deﬁned in Section 8.3.2, of each position in a binary tree T .
# R-8.18 Let T be a binary tree with n positions that is realized with an array rep-
# resentation A, and let f () be the level numbering function of the positions
# of T , as given in Section 8.3.2. Give pseudo-code descriptions of each of
# the methods root, parent, left, right, is leaf, and is root.
# R-8.19 Our deﬁnition of the level numbering function f (p), as given in Sec-
# tion 8.3.2, began with the root having number 0. Some authors prefer
# to use a level numbering g(p) in which the root is assigned number 1, be-
# cause it simpliﬁes the arithmetic for ﬁnding neighboring positions. Redo
# Exercise R-8.18, but assuming that we use a level numbering g(p) in
# which the root is assigned number 1.
# R-8.20 Draw a binary tree T that simultaneously satisﬁes the following:
# • Each internal node of T stores a single character.
# • A preorder traversal of T yields EXAMFUN.
# • An inorder traversal of T yields MAFXUEN.
# R-8.21 In what order are positions visited during a preorder traversal of the tree
# of Figure 8.8?
# R-8.22 In what order are positions visited during a postorder traversal of the tree
# of Figure 8.8?
# R-8.23 Let T be an ordered tree with more than one node. Is it possible that the
# preorder traversal of T visits the nodes in the same order as the postorder
# traversal of T ? If so, give an example; otherwise, explain why this cannot
# occur. Likewise, is it possible that the preorder traversal of T visits the
# nodes in the reverse order of the postorder traversal of T ? If so, give an
# example; otherwise, explain why this cannot occur.
# R-8.24 Answer the previous question for the case when T is a proper binary tree
# with more than one node.
# R-8.25 Consider the example of a breadth-ﬁrst traversal given in Figure 8.17.
# Using the annotated numbers from that ﬁgure, describe the contents of
# the queue before each pass of the while loop in Code Fragment 8.14. To
# get started, the queue has contents {1} before the ﬁrst pass, and contents
# {2, 3, 4} before the second pass.
# R-8.26 The collections.deque class supports an extend method that adds a col-
# lection of elements to the end of the queue at once. Reimplement the
# breadthﬁrst method of the Tree class to take advantage of this feature.
# R-8.27 Give the output of the function parenthesize(T, T.root( )), as described
# in Code Fragment 8.25, when T is the tree of Figure 8.8.
# R-8.28 What is the running time of parenthesize(T, T.root( )), as given in Code
# Fragment 8.25, for a tree T with n nodes?
# R-8.29 Describe, in pseudo-code, an algorithm for computing the number of de-
# scendants of each node of a binary tree. The algorithm should be based
# on the Euler tour traversal.
# R-8.30 The build expression tree method of the ExpressionTree class requires
# input that is an iterable of string tokens. We used a convenient exam-
# ple, (((3+1)x4)/((9-5)+2)) , in which each character is its own to-
# ken, so that the string itself sufﬁced as input to build expression tree.
# In general, a string, such as (35 + 14) , must be explicitly tokenized
# into list [ ( , 35 , + , 14 , ) ] so as to ignore whitespace and to
# recognize multidigit numbers as a single token. Write a utility method,
# tokenize(raw), that returns such a list of tokens for a raw string.
# C-8.31 Deﬁne the internal path length, I(T ), of a tree T to be the sum of the
# depths of all the internal positions in T . Likewise, deﬁne the external path
# length, E(T ), of a tree T to be the sum of the depths of all the external
# positions in T . Show that if T is a proper binary tree with n positions, then
# E(T ) = I(T ) + n − 1.
# C-8.32 Let T be a (not necessarily proper) binary tree with n nodes, and let D be
# the sum of the depths of all the external nodes of T . Show that if T has the
# minimum number of external nodes possible, then D is O(n) and if T has
# the maximum number of external nodes possible, then D is O(n log n).
# C-8.33 Let T be a (possibly improper) binary tree with n nodes, and let D be the
# sum of the depths of all the external nodes of T . Describe a conﬁguration
# for T such that D is Ω(n2 ). Such a tree would be the worst case for the
# asymptotic running time of method height1 (Code Fragment 8.4).
# C-8.34 For a tree T , let nI denote the number of its internal nodes, and let nE
# denote the number of its external nodes. Show that if every internal node
# in T has exactly 3 children, then nE = 2nI + 1.
# C-8.35 Two ordered trees T  and T  are said to be isomorphic if one of the fol-
# lowing holds:
# • Both T  and T  are empty.
# • The roots of T  and T  have the same number k ≥ 0 of subtrees, and
# the ith such subtree of T  is isomorphic to the ith such subtree of T 
# for i = 1, . . . , k.
# Design an algorithm that tests whether two given ordered trees are iso-
# morphic. What is the running time of your algorithm?
# C-8.36 Show that there are more than 2n improper binary trees with n internal
# nodes such that no pair are isomorphic (see Exercise C-8.35).
# C-8.37 If we exclude isomorphic trees (see Exercise C-8.35), exactly how many
# proper binary trees exist with exactly 4 leaves?
# C-8.38 Add support in LinkedBinaryTree for a method, delete subtree(p), that
# removes the entire subtree rooted at position p, making sure to maintain
# the count on the size of the tree. What is the running time of your imple-
# mentation?
# C-8.39 Add support in LinkedBinaryTree for a method, swap(p,q), that has the
# effect of restructuring the tree so that the node referenced by p takes the
# place of the node referenced by q, and vice versa. Make sure to properly
# handle the case when the nodes are adjacent.
# C-8.40 We can simplify parts of our LinkedBinaryTree implementation if we
# make use of of a single sentinel node, referenced as the sentinel member
# of the tree instance, such that the sentinel is the parent of the real root of
# the tree, and the root is referenced as the left child of the sentinel. Fur-
# thermore, the sentinel will take the place of None as the value of the left
# or right member for a node without such a child. Give a new imple-
# mentation of the update methods delete and attach, assuming such a
# representation.
# C-8.41 Describe how to clone a LinkedBinaryTree instance representing a proper
# binary tree, with use of the attach method.
# C-8.42 Describe how to clone a LinkedBinaryTree instance representing a (not
# necessarily proper) binary tree, with use of the add left and add right
# methods.
# C-8.43 We can deﬁne a binary tree representation T  for an ordered general tree
# T as follows (see Figure 8.23):
# • For each position p of T , there is an associated position p of T  .
# • If p is a leaf of T , then p in T  does not have a left child; otherwise
# the left child of p is q , where q is the ﬁrst child of p in T .
# • If p has a sibling q ordered immediately after it in T , then q is the
# right child of p in T ; otherwise p does not have a right child.
# Given such a representation T  of a general ordered tree T , answer each
# of the following questions:
# a. Is a preorder traversal of T  equivalent to a preorder traversal of T ?
# b. Is a postorder traversal of T  equivalent to a postorder traversal of T ?
# c. Is an inorder traversal of T  equivalent to one of the standard traver-
# sals of T ? If so, which one?
# A
# A
# B
# E
# C
# F
# B
# D
# G
# E
# C
# F
# D
# G
# (a)
# (b)
# Figure 8.23: Representation of a tree with a binary tree: (a) tree T ; (b) binary tree
# T  for T . The dashed edges connect nodes of T  that are siblings in T .
# C-8.44 Give an efﬁcient algorithm that computes and prints, for every position p
# of a tree T , the element of p followed by the height of p’s subtree.
# C-8.45 Give an O(n)-time algorithm for computing the depths of all positions of
# a tree T , where n is the number of nodes of T .
# C-8.46 The path length of a tree T is the sum of the depths of all positions in T .
# Describe a linear-time method for computing the path length of a tree T .
# C-8.47 The balance factor of an internal position p of a proper binary tree is the
# difference between the heights of the right and left subtrees of p. Show
# how to specialize the Euler tour traversal of Section 8.4.6 to print the
# balance factors of all the internal nodes of a proper binary tree.
# C-8.48 Given a proper binary tree T , deﬁne the reﬂection of T to be the binary
# tree T  such that each node v in T is also in T  , but the left child of v in T
# is v’s right child in T  and the right child of v in T is v’s left child in T  .
# Show that a preorder traversal of a proper binary tree T is the same as the
# postorder traversal of T ’s reﬂection, but in reverse order.
# C-8.49 Let the rank of a position p during a traversal be deﬁned such that the ﬁrst
# element visited has rank 1, the second element visited has rank 2, and so
# on. For each position p in a tree T , let pre(p) be the rank of p in a preorder
# traversal of T , let post(p) be the rank of p in a postorder traversal of T , let
# depth(p) be the depth of p, and let desc(p) be the number of descendants
# of p, including p itself. Derive a formula deﬁning post(p) in terms of
# desc(p), depth(p), and pre(p), for each node p in T .
# C-8.50 Design algorithms for the following operations for a binary tree T :
# • preorder next(p): Return the position visited after p in a preorder
# traversal of T (or None if p is the last node visited).
# • inorder next(p): Return the position visited after p in an inorder
# traversal of T (or None if p is the last node visited).
# • postorder next(p): Return the position visited after p in a postorder
# traversal of T (or None if p is the last node visited).
# What are the worst-case running times of your algorithms?
# C-8.51 To implement the preorder method of the LinkedBinaryTree class, we re-
# lied on the convenience of Python’s generator syntax and the yield state-
# ment. Give an alternative implementation of preorder that returns an ex-
# plicit instance of a nested iterator class. (See Section 2.3.4 for discussion
# of iterators.)
# C-8.52 Algorithm preorder draw draws a binary tree T by assigning x- and y-
# coordinates to each position p such that x(p) is the number of nodes pre-
# ceding p in the preorder traversal of T and y(p) is the depth of p in T .
# a. Show that the drawing of T produced by preorder draw has no pairs
# of crossing edges.
# b. Redraw the binary tree of Figure 8.22 using preorder draw.
# C-8.53 Redo the previous problem for the algorithm postorder draw that is simi-
# lar to preorder draw except that it assigns x(p) to be the number of nodes
# preceding position p in the postorder traversal.
# C-8.54 Design an algorithm for drawing general trees, using a style similar to the
# inorder traversal approach for drawing binary trees.
# C-8.55 Exercise P-4.27 described the walk function of the os module. This func-
# tion performs a traversal of the implicit tree represented by the ﬁle system.
# Read the formal documentation for the function, and in particular its use
# of an optional Boolean parameter named topdown. Describe how its be-
# havior relates to tree traversal algorithms described in this chapter.
# C-8.56 The indented parenthetic representation of a tree T is a variation of the
# parenthetic representation of T (see Code Fragment 8.25) that uses inden-
# tation and line breaks as illustrated in Figure 8.24. Give an algorithm that
# prints this representation of a tree.
# C-8.57 Let T be a binary tree with n positions. Deﬁne a Roman position to be
# a position p in T , such that the number of descendants in p’s left subtree
# differ from the number of descendants in p’s right subtree by at most 5.
# Describe a linear-time method for ﬁnding each position p of T , such that
# p is not a Roman position, but all of p’s descendants are Roman.
# C-8.58 Let T be a tree with n positions. Deﬁne the lowest common ancestor
# (LCA) between two positions p and q as the lowest position in T that has
# both p and q as descendants (where we allow a position to be a descendant
# of itself ). Given two positions p and q, describe an efﬁcient algorithm for
# ﬁnding the LCA of p and q. What is the running time of your algorithm?
# C-8.59 Let T be a binary tree with n positions, and, for any position p in T , let d p
# denote the depth of p in T . The distance between two positions p and q
# in T is d p + dq − 2da , where a is the lowest common ancestor (LCA) of p
# and q. The diameter of T is the maximum distance between two positions
# in T . Describe an efﬁcient algorithm for ﬁnding the diameter of T . What
# is the running time of your algorithm?
# C-8.60 Suppose each position p of a binary tree T is labeled with its value f (p) in
# a level numbering of T . Design a fast method for determining f (a) for the
# lowest common ancestor (LCA), a, of two positions p and q in T , given
# f (p) and f (q). You do not need to ﬁnd position a, just value f (a).
# C-8.61 Give an alternative implementation of the build expression tree method
# of the ExpressionTree class that relies on recursion to perform an implicit
# Euler tour of the tree that is being built.
# C-8.62 Note that the build expression tree function of the ExpressionTree class
# is written in such a way that a leaf token can be any string; for exam-
# ple, it parses the expression (a*(b+c)) . However, within the evaluate
# method, an error would occur when attempting to convert a leaf token to
# a number. Modify the evaluate method to accept an optional Python dic-
# tionary that can be used to map such string variables to numeric values,
# with a syntax such as T.evaluate({ a :3, b :1, c :5}). In this way,
# the same algebraic expression can be evaluated using different values.
# C-8.63 As mentioned in Exercise C-6.22, postﬁx notation is an unambiguous way
# of writing an arithmetic expression without parentheses. It is deﬁned so
# that if “(exp1 ) op (exp2 )” is a normal (inﬁx) fully parenthesized expres-
# sion with operation op, then its postﬁx equivalent is “pexp1 pexp2 op”,
# where pexp1 is the postﬁx version of exp1 and pexp2 is the postﬁx ver-
# sion of exp2 . The postﬁx version of a single number or variable is just
# that number or variable. So, for example, the postﬁx version of the inﬁx
# expression “((5 + 2) ∗ (8 − 3))/4” is “5 2 + 8 3 − ∗ 4 /”. Implement a
# postﬁx method of the ExpressionTree class of Section 8.5 that produces
# the postﬁx notation for the given expression.
# P-8.64 Implement the binary tree ADT using the array-based representation de-
# scribed in Section 8.3.2.
# P-8.65 Implement the tree ADT using a linked structure as described in Sec-
# tion 8.3.3. Provide a reasonable set of update methods for your tree.
# P-8.66 The memory usage for the LinkedBinaryTree class can be streamlined by
# removing the parent reference from each node, and instead having each
# Position instance keep a member, path, that is a list of nodes representing
# the entire path from the root to that position. (This generally saves mem-
# ory because there are typically relatively few stored position instances.)
# Reimplement the LinkedBinaryTree class using this strategy.
# P-8.67 A slicing ﬂoor plan divides a rectangle with horizontal and vertical sides
# using horizontal and vertical cuts. (See Figure 8.25a.) A slicing ﬂoor plan
# can be represented by a proper binary tree, called a slicing tree, whose
# internal nodes represent the cuts, and whose external nodes represent the
# basic rectangles into which the ﬂoor plan is decomposed by the cuts. (See
# Figure 8.25b.) The compaction problem for a slicing ﬂoor plan is deﬁned
# as follows. Assume that each basic rectangle of a slicing ﬂoor plan is
# assigned a minimum width w and a minimum height h. The compaction
# problem is to ﬁnd the smallest possible height and width for each rectangle
# of the slicing ﬂoor plan that is compatible with the minimum dimensions
# Figure 8.25: (a) Slicing ﬂoor plan; (b) slicing tree associated with the ﬂoor plan.
# of the basic rectangles. Namely, this problem requires the assignment of
# values h(p) and w(p) to each position p of the slicing tree such that:
# ⎧
# if p is a leaf whose basic rectangle has
# ⎪
# w
# ⎪
# ⎪
# ⎪
# minimum width w
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# if p is an internal position, associated with
# ⎪
# ⎪
# ⎨ max(w(), w(r)) a horizontal cut, with left child  and right
# w(p) =
# child r
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# if p is an internal position, associated with
# ⎪
# ⎪
# ⎪
# ⎪
# w()
# +
# w(r)
# ⎪
# a vertical cut, with left child  and right
# ⎪
# ⎪
# ⎪
# ⎩
# child r
# h(p) =
# ⎧
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎨
# hif p is a leaf node whose basic rectangle
# has minimum height h
# h() + h(r)if p is an internal position, associated with
# a horizontal cut, with left child  and right
# child r
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# ⎪
# if p is an internal position, associated with
# ⎪
# ⎪
# ⎪
# max(h(),
# h(r))
# ⎪
# a vertical cut, with left child  and right
# ⎪
# ⎪
# ⎪
# ⎩
# child r
# Design a data structure for slicing ﬂoor plans that supports the operations:
# • Create a ﬂoor plan consisting of a single basic rectangle.
# • Decompose a basic rectangle by means of a horizontal cut.
# • Decompose a basic rectangle by means of a vertical cut.
# • Assign minimum height and width to a basic rectangle.
# • Draw the slicing tree associated with the ﬂoor plan.
# • Compact and draw the ﬂoor plan.
# P-8.68 Write a program that can play Tic-Tac-Toe effectively. (See Section 5.6.)
# To do this, you will need to create a game tree T , which is a tree where
# each position corresponds to a game conﬁguration, which, in this case,
# is a representation of the Tic-Tac-Toe board. (See Section 8.4.2.) The
# root corresponds to the initial conﬁguration. For each internal position p
# in T , the children of p correspond to the game states we can reach from
# p’s game state in a single legal move for the appropriate player, A (the
# ﬁrst player) or B (the second player). Positions at even depths correspond
# to moves for A and positions at odd depths correspond to moves for B.
# Leaves are either ﬁnal game states or are at a depth beyond which we do
# not want to explore. We score each leaf with a value that indicates how
# good this state is for player A. In large games, like chess, we have to use a
# heuristic scoring function, but for small games, like Tic-Tac-Toe, we can
# construct the entire game tree and score leaves as +1, 0, −1, indicating
# whether player A has a win, draw, or lose in that conﬁguration. A good
# algorithm for choosing moves is minimax. In this algorithm, we assign a
# score to each internal position p in T , such that if p represents A’s turn, we
# compute p’s score as the maximum of the scores of p’s children (which
# corresponds to A’s optimal play from p). If an internal node p represents
# B’s turn, then we compute p’s score as the minimum of the scores of p’s
# children (which corresponds to B’s optimal play from p).
# P-8.69 Implement the tree ADT using the binary tree representation described in
# Exercise C-8.43. You may adapt the LinkedBinaryTree implementation.
# P-8.70 Write a program that takes as input a general tree T and a position p of T
# and converts T to another tree with the same set of position adjacencies,
# but now with p as its root.


# In[ ]:





# ## Graph

# In[1]:


#------------------------- nested Vertex class -------------------------
class Vertex:
    """Lightweight vertex structure for a graph."""
    
    __slots__ = '_element',  # Corrected to use __slots__ properly

    def __init__(self, x):
        """Do not call constructor directly. Use Graph's insert_vertex(x)."""
        self._element = x  # Changed from self.element to self._element

    def element(self):
        """Return element associated with this vertex."""
        return self._element  # Changed from self.element to self._element

    # Will allow vertex to be a map/set key
    def __hash__(self):
        return hash(id(self))


#------------------------- nested Edge class -------------------------
class Edge:
    """Lightweight edge structure for a graph."""
    
    __slots__ = '_origin', '_destination', '_element'  # Corrected to use __slots__ properly

    def __init__(self, u, v, x):
        """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
        self._origin = u  # Changed from self.origin to self._origin
        self._destination = v  # Changed from self.destination to self._destination
        self._element = x  # Changed from self.element to self._element

    def endpoints(self):
        """Return (u,v) tuple for vertices u and v."""
        return (self._origin, self._destination)  # Changed from self.origin to self._origin

    def opposite(self, v):
        """Return the vertex that is opposite v on this edge."""
        return self._destination if v is self._origin else self._origin  # Changed from self.destination to self._destination

    def element(self):
        """Return element associated with this edge."""
        return self._element  # Changed from self.element to self._element

    # Will allow edge to be a map/set key
    def __hash__(self):
        return hash((self._origin, self._destination))  # Changed from self.origin to self._origin


# In[2]:


class Graph:
    """Representation of a simple graph using an adjacency map."""

    def __init__(self, directed=False):
        """Create an empty graph (undirected, by default).
        
        Graph is directed if optional parameter is set to True.
        """
        self.outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self.incoming = {} if directed else self.outgoing

    def is_directed(self):
        """Return True if this is a directed graph; False if undirected.

        Property is based on the original declaration of the graph, not its contents.
        """
        return self.incoming is not self.outgoing  # directed if maps are distinct

    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self.outgoing)

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self.outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph."""
        total = sum(len(self.outgoing[v]) for v in self.outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2

    def edges(self):
        """Return a set of all edges of the graph."""
        result = set()
        # avoid double-reporting edges of undirected graph
        for secondary_map in self.outgoing.values():
            # add edges to resulting set
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        # returns None if v not adjacent
        return self.outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        """Return number of (outgoing) edges incident to vertex v in the graph.
        
        If graph is directed, optional parameter used to count incoming edges.
        """
        adj = self.outgoing if outgoing else self.incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """Return all (outgoing) edges incident to vertex v in the graph.
        
        If graph is directed, optional parameter used to request incoming edges.
        """
        adj = self.outgoing if outgoing else self.incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x."""
        v = Vertex(x)  # Assuming Vertex class is defined elsewhere
        self.outgoing[v] = {}
        if self.is_directed():
            # need distinct map for incoming edges
            self.incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x."""
        e = Edge(u, v, x)  # Assuming Edge class is defined elsewhere
        self.outgoing[u][v] = e
        if self.is_directed():
            self.incoming[v][u] = e  # Only add incoming edge for directed graphs


# In[3]:


def DFS(g, u, discovered):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be "discovered" prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    # for every outgoing edge from u
    for e in g.incident_edges(u):  # Corrected method name
        v = e.opposite(u)
        if v not in discovered:
            # v is an unvisited vertex
            discovered[v] = e  # e is the tree edge that discovered v
            DFS(g, v, discovered)  # recursively explore from v


# In[4]:


def construct_path(u, v, discovered):
    """Construct a path from vertex u to vertex v using the discovered edges.

    The discovered dictionary maps each vertex to the edge that was used to
    discover it during a graph traversal.
    """
    path = []  # Empty path by default

    if v in discovered:
        # We build the list from v to u and then reverse it at the end
        path.append(v)
        walk = v

        while walk != u:
            e = discovered[walk]  # Find edge leading to walk
            parent = e.opposite(walk)  # Get the parent vertex
            path.append(parent)  # Add parent to the path
            walk = parent  # Move to the parent

        path.reverse()  # Reorient path from u to v

    return path


# In[5]:


def DFS_complete(g):
    """Perform DFS for the entire graph and return a forest as a dictionary.

    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.)
    """
    forest = {}  # Initialize the forest

    for u in g.vertices():
        if u not in forest:
            forest[u] = None  # u will be the root of a tree
            DFS(g, u, forest)  # Perform DFS starting from u

    return forest


# In[6]:


def BFS(g, s, discovered):
    """Perform BFS of the undiscovered portion of Graph g starting at Vertex s.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    level = [s]  # First level includes only s

    while len(level) > 0:
        # Prepare to gather newly found vertices
        next_level = []  # Corrected variable name

        for u in level:
            for e in g.incident_edges(u):  # Corrected method name
                v = e.opposite(u)
                if v not in discovered:
                    # v is an unvisited vertex
                    discovered[v] = e  # e is the tree edge that discovered v
                    next_level.append(v)  # Add v to the next level

        # Relabel 'next' level to become current
        level = next_level


# In[7]:


from copy import deepcopy  # Ensure you import deepcopy from the copy module

def floyd_warshall(g):
    """Return a new graph that is the transitive closure of g."""
    closure = deepcopy(g)  # Create a deep copy of the graph
    verts = list(closure.vertices())  # Make an indexable list of vertices
    n = len(verts)

    for k in range(n):
        for i in range(n):
            # Verify that edge (i, k) exists in the partial closure
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    # Verify that edge (k, j) exists in the partial closure
                    if i != j and k != j and closure.get_edge(verts[k], verts[j]) is not None:
                        # If (i, j) not yet included, add it to the closure
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])  # Corrected method name

    return closure


# In[8]:


def topological_sort(g):
    """Return a list of vertices of directed acyclic graph g in topological order.

    If graph g has a cycle, the result will be incomplete.
    """
    topo = []  # A list of vertices placed in topological order
    ready = []  # List of vertices that have no remaining constraints
    incount = {}  # Keep track of in-degree for each vertex

    # Initialize in-degree count for each vertex
    for u in g.vertices():
        incount[u] = g.degree(u, False)  # Parameter requests incoming degree
        if incount[u] == 0:
            # If u has no incoming edges, it is free of constraints
            ready.append(u)

    while len(ready) > 0:
        u = ready.pop()  # u is free of constraints
        topo.append(u)   # Add u to the topological order

        # Consider all outgoing neighbors of u
        for e in g.incident_edges(u):  # Corrected method name
            v = e.opposite(u)
            incount[v] -= 1  # v has one less constraint without u
            if incount[v] == 0:
                ready.append(v)

    return topo


# In[9]:


def shortest_path_lengths(g, src):
    """Compute shortest-path distances from src to reachable vertices of g.

    Graph g can be undirected or directed, but must be weighted such that
    e.element() returns a numeric weight for each edge e.

    Return dictionary mapping each reachable vertex to its distance from src.
    """
    d = {}  # d[v] is the distance from src to v
    cloud = {}  # Map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()  # Vertex v will have key d[v]
    pqlocator = {}  # Map from vertex to its pq locator

    # For each vertex v of the graph, add an entry to the priority queue,
    # with the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')  # Corrected syntax for positive infinity
        pqlocator[v] = pq.add(d[v], v)  # Save locator for future updates

    while not pq.is_empty():  # Corrected method name
        key, u = pq.remove_min()  # Corrected method name
        cloud[u] = key  # Its correct d[u] value
        del pqlocator[u]  # u is no longer in pq

        # Outgoing edges (u, v)
        for e in g.incident_edges(u):  # Corrected method name
            v = e.opposite(u)
            if v not in cloud:
                # Perform relaxation step on edge (u, v)
                wgt = e.element()  # Corrected method name
                if d[u] + wgt < d[v]:  # Better path to v?
                    d[v] = d[u] + wgt  # Update the distance
                    pq.update(pqlocator[v], d[v], v)  # Update the pq entry

    return cloud


# In[10]:


def shortest_path_tree(g, s, d):
    """Reconstruct shortest-path tree rooted at vertex s, given distance map d.

    Return tree as a map from each reachable vertex v (other than s) to the
    edge e = (u, v) that is used to reach v from its parent u in the tree.
    """
    tree = {}  # Initialize the tree

    for v in d:
        if v is not s:
            # Consider INCOMING edges
            for e in g.incident_edges(v, False):  # Corrected method name
                u = e.opposite(v)
                wgt = e.element()  # Get the weight of the edge

                if d[v] == d[u] + wgt:  # Check if this edge is part of the shortest path
                    tree[v] = e  # Edge e is used to reach v

    return tree


# In[11]:


def MST_PrimJarnik(g):
    """Compute a minimum spanning tree of weighted graph g.

    Return a list of edges that comprise the MST (in arbitrary order).
    """
    d = {}  # d[v] is bound on distance to tree
    tree = []  # List of edges in spanning tree
    pq = AdaptableHeapPriorityQueue()  # d[v] maps to value (v, e=(u,v))
    pqlocator = {}  # Map from vertex to its pq locator

    # For each vertex v of the graph, add an entry to the priority queue,
    # with the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if len(d) == 0:
            # This is the first node
            d[v] = 0  # Make it the root
        else:
            # Positive infinity
            d[v] = float('inf')  # Corrected syntax for positive infinity
            
        pqlocator[v] = pq.add(d[v], (v, None))  # Add vertex to priority queue

    while not pq.is_empty():  # Corrected method name
        key, value = pq.remove_min()  # Corrected method name
        u, edge = value  # Unpack tuple from pq
        del pqlocator[u]  # u is no longer in pq

        if edge is not None:
            tree.append(edge)  # Add edge to tree

        for link in g.incident_edges(u):  # Corrected method name
            v = link.opposite(u)
            if v in pqlocator:  # Thus v not yet in tree
                # See if edge (u, v) better connects v to the growing tree
                wgt = link.element()  # Get the weight of the edge
                if wgt < d[v]:  # Better edge to v?
                    d[v] = wgt  # Update the distance
                    pq.update(pqlocator[v], d[v], (v, link))  # Update the pq entry

    return tree


# In[12]:


def MST_Kruskal(g):
    """Compute a minimum spanning tree of a graph using Kruskal's algorithm.

    Return a list of edges that comprise the MST.
    
    The elements of the graph's edges are assumed to be weights.
    """
    tree = []  # List of edges in spanning tree
    pq = HeapPriorityQueue()  # Entries are edges in G, with weights as key
    forest = Partition()  # Keeps track of forest clusters
    position = {}  # Map each node to its Partition entry

    # Initialize the partition for each vertex
    for v in g.vertices():
        position[v] = forest.make_group(v)

    # Add all edges to the priority queue
    for e in g.edges():
        pq.add(e.element(), e)  # Edge’s element is assumed to be its weight

    size = g.vertex_count()  # Corrected method name
    while len(tree) != size - 1 and not pq.is_empty():  # Corrected method name
        # Tree not spanning and unprocessed edges remain
        weight, edge = pq.remove_min()  # Corrected method name
        u, v = edge.endpoints()  # Get endpoints of the edge
        a = forest.find(position[u])  # Find the set containing u
        b = forest.find(position[v])  # Find the set containing v

        if a != b:  # If they are in different sets, union them
            tree.append(edge)  # Add edge to the MST
            forest.union(a, b)  # Union the two sets

    return tree


# In[13]:


class Partition:
    """Union-find structure for maintaining disjoint sets."""

    #------------------------- nested Position class -------------------------
    class Position:
        __slots__ = '_container', '_element', '_size', '_parent'

        def __init__(self, container, e):
            """Create a new position that is the leader of its own group."""
            # Reference to Partition instance
            self._container = container
            self._element = e
            self._size = 1  # Convention for a group leader
            self._parent = self  # Leader's parent is itself

        def element(self):
            """Return element stored at this position."""
            return self._element

    #------------------------- public Partition methods -------------------------
    
    def make_group(self, e):
        """Makes a new group containing element e, and returns its Position."""
        return self.Position(self, e)

    def find(self, p):
        """Finds the group containing p and returns the position of its leader."""
        if p._parent != p:  # Check if p is not its own parent
            p._parent = self.find(p._parent)  # Path compression
        return p._parent

    def union(self, p, q):
        """Merges the groups containing elements p and q (if distinct)."""
        a = self.find(p)
        b = self.find(q)
        
        if a != b:  # Only merge if different groups
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size


# In[14]:


# R-14.1 Draw a simple undirected graph G that has 12 vertices, 18 edges, and 3
# connected components.
# R-14.2 If G is a simple undirected graph with 12 vertices and 3 connected com-
# ponents, what is the largest number of edges it might have?
# R-14.3 Draw an adjacency matrix representation of the undirected graph shown
# in Figure 14.1.
# R-14.4 Draw an adjacency list representation of the undirected graph shown in
# Figure 14.1.
# R-14.5 Draw a simple, connected, directed graph with 8 vertices and 16 edges
# such that the in-degree and out-degree of each vertex is 2. Show that there
# is a single (nonsimple) cycle that includes all the edges of your graph, that
# is, you can trace all the edges in their respective directions without ever
# lifting your pencil. (Such a cycle is called an Euler tour.)
# R-14.6 Suppose we represent a graph G having n vertices and m edges with the
# edge list structure. Why, in this case, does the insert vertex method run
# in O(1) time while the remove vertex method runs in O(m) time?
# R-14.7 Give pseudo-code for performing the operation insert edge(u,v,x) in O(1)
# time using the adjacency matrix representation.
# R-14.8 Repeat Exercise R-14.7 for the adjacency list representation, as described
# in the chapter.
# R-14.9 Can edge list E be omitted from the adjacency matrix representation while
# still achieving the time bounds given in Table 14.1? Why or why not?
# R-14.10 Can edge list E be omitted from the adjacency list representation while
# still achieving the time bounds given in Table 14.3? Why or why not?
# R-14.11 Would you use the adjacency matrix structure or the adjacency list struc-
# ture in each of the following cases? Justify your choice.
# a. The graph has 10,000 vertices and 20,000 edges, and it is important
# to use as little space as possible.
# b. The graph has 10,000 vertices and 20,000,000 edges, and it is im-
# portant to use as little space as possible.
# c. You need to answer the query get edge(u,v) as fast as possible, no
# matter how much space you use.
# R-14.12 Explain why the DFS traversal runs in O(n2 ) time on an n-vertex simple
# graph that is represented with the adjacency matrix structure.
# R-14.13 In order to verify that all of its nontree edges are back edges, redraw the
# graph from Figure 14.8b so that the DFS tree edges are drawn with solid
# lines and oriented downward, as in a standard portrayal of a tree, and with
# all nontree edges drawn using dashed lines.
# R-14.14 A simple undirected graph is complete if it contains an edge between every
# pair of distinct vertices. What does a depth-ﬁrst search tree of a complete
# graph look like?
# R-14.15 Recalling the deﬁnition of a complete graph from Exercise R-14.14, what
# does a breadth-ﬁrst search tree of a complete graph look like?
# R-14.16 Let G be an undirected graph whose vertices are the integers 1 through 8,
# and let the adjacent vertices of each vertex be given by the table below:
# vertex adjacent vertices
# 1
# (2, 3, 4)
# 2
# (1, 3, 4)
# 3
# (1, 2, 4)
# 4
# (1, 2, 3, 6)
# 5
# (6, 7, 8)
# 6
# (4, 5, 7)
# 7
# (5, 6, 8)
# 8
# (5, 7)
# Assume that, in a traversal of G, the adjacent vertices of a given vertex are
# returned in the same order as they are listed in the table above.
# a. Draw G.
# b. Give the sequence of vertices of G visited using a DFS traversal
# starting at vertex 1.
# c. Give the sequence of vertices visited using a BFS traversal starting
# at vertex 1.
# R-14.17 Draw the transitive closure of the directed graph shown in Figure 14.2.
# R-14.18 If the vertices of the graph from Figure 14.11 are numbered as (v1 = JFK,
# v2 = LAX, v3 = MIA, v4 = BOS, v5 = ORD, v6 = SFO, v7 = DFW), in
# what order would edges be added to the transitive closure during the
# Floyd-Warshall algorithm?
# R-14.19 How many edges are in the transitive closure of a graph that consists of a
# simple directed path of n vertices?
# R-14.20 Given an n-node complete binary tree T , rooted at a given position, con-
#  having the nodes of T as its vertices. For each
# sider a directed graph G
#  from the parent to the
# parent-child pair in T , create a directed edge in G
# 
# child. Show that the transitive closure of G has O(n log n) edges.
# R-14.21 Compute a topological ordering for the directed graph drawn with solid
# edges in Figure 14.3d.
# R-14.22 Bob loves foreign languages and wants to plan his course schedule for the
# following years. He is interested in the following nine language courses:
# LA15, LA16, LA22, LA31, LA32, LA126, LA127, LA141, and LA169.
# The course prerequisites are:
# • LA15: (none)
# • LA16: LA15
# • LA22: (none)
# • LA31: LA15
# • LA32: LA16, LA31
# • LA126: LA22, LA32
# • LA127: LA16
# • LA141: LA22, LA16
# • LA169: LA32
# In what order can Bob take these courses, respecting the prerequisites?
# R-14.23 Draw a simple, connected, weighted graph with 8 vertices and 16 edges,
# each with unique edge weights. Identify one vertex as a “start” vertex and
# illustrate a running of Dijkstra’s algorithm on this graph.
# R-14.24 Show how to modify the pseudo-code for Dijkstra’s algorithm for the case
# when the graph is directed and we want to compute shortest directed paths
# from the source vertex to all the other vertices.
# R-14.25 Draw a simple, connected, undirected, weighted graph with 8 vertices and
# 16 edges, each with unique edge weights. Illustrate the execution of the
# Prim-Jarnı́k algorithm for computing the minimum spanning tree of this
# graph.
# R-14.26 Repeat the previous problem for Kruskal’s algorithm.
# R-14.27 There are eight small islands in a lake, and the state wants to build seven
# bridges to connect them so that each island can be reached from any other
# one via one or more bridges. The cost of constructing a bridge is propor-
# tional to its length. The distances between pairs of islands are given in the
# following table.
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 12345678
# -
# -
# -
# -
# -
# -
# -
# -240
# -
# -
# -
# -
# -
# -
# -210
# 265
# -
# -
# -
# -
# -
# -340
# 175
# 260
# -
# -
# -
# -
# -280
# 215
# 115
# 160
# -
# -
# -
# -200
# 180
# 350
# 330
# 360
# -
# -
# -345
# 185
# 435
# 295
# 400
# 175
# -
# -120
# 155
# 195
# 230
# 170
# 205
# 305
# -
# Find which bridges to build to minimize the total construction cost.
# R-14.28 Describe the meaning of the graphical conventions used in Figure 14.9
# illustrating a DFS traversal. What do the line thicknesses signify? What
# do the arrows signify? How about dashed lines?
# R-14.29 Repeat Exercise R-14.28 for Figure 14.8 that illustrates a directed DFS
# traversal.
# R-14.30 Repeat Exercise R-14.28 for Figure 14.10 that illustrates a BFS traversal.
# R-14.31 Repeat Exercise R-14.28 for Figure 14.11 illustrating the Floyd-Warshall
# algorithm.
# R-14.32 Repeat Exercise R-14.28 for Figure 14.13 that illustrates the topological
# sorting algorithm.
# R-14.33 Repeat Exercise R-14.28 for Figures 14.15 and 14.16 illustrating Dijkstra’s
# algorithm.
# R-14.34 Repeat Exercise R-14.28 for Figures 14.20 and 14.21 that illustrate the
# Prim-Jarnı́k algorithm.
# R-14.35 Repeat Exercise R-14.28 for Figures 14.22 through 14.24 that illustrate
# Kruskal’s algorithm.
# R-14.36 George claims he has a fast way to do path compression in a partition
# structure, starting at a position p. He puts p into a list L, and starts follow-
# ing parent pointers. Each time he encounters a new position, q, he adds q
# to L and updates the parent pointer of each node in L to point to q’s parent.
# Show that George’s algorithm runs in Ω(h2 ) time on a path of length h.
# C-14.37 Give a Python implementation of the remove vertex(v) method for our
# adjacency map implementation of Section 14.2.5, making sure your im-
# plementation works for both directed and undirected graphs. Your method
# should run in O(deg(v)) time.
# C-14.38 Give a Python implementation of the remove edge(e) method for our ad-
# jacency map implementation of Section 14.2.5, making sure your imple-
# mentation works for both directed and undirected graphs. Your method
# should run in O(1) time.
# C-14.39 Suppose we wish to represent an n-vertex graph G using the edge list
# structure, assuming that we identify the vertices with the integers in the set
# {0, 1, . . . , n − 1}. Describe how to implement the collection E to support
# O(log n)-time performance for the get edge(u, v) method. How are you
# implementing the method in this case?
# C-14.40 Let T be the spanning tree rooted at the start vertex produced by the depth-
# ﬁrst search of a connected, undirected graph G. Argue why every edge of
# G not in T goes from a vertex in T to one of its ancestors, that is, it is a
# back edge.
# C-14.41 Our solution to reporting a path from u to v in Code Fragment 14.6 could
# be made more efﬁcient in practice if the DFS process ended as soon as v
# is discovered. Describe how to modify our code base to implement this
# optimization.
# C-14.42 Let G be an undirected graph G with n vertices and m edges. Describe
# an O(n + m)-time algorithm for traversing each edge of G exactly once in
# each direction.
#  if one
# C-14.43 Implement an algorithm that returns a cycle in a directed graph G,
# exists.
# C-14.44 Write a function, components(g), for undirected graph g, that returns a
# dictionary mapping each vertex to an integer that serves as an identiﬁer for
# its connected component. That is, two vertices should be mapped to the
# same identiﬁer if and only if they are in the same connected component.
# C-14.45 Say that a maze is constructed correctly if there is one path from the start
# to the ﬁnish, the entire maze is reachable from the start, and there are no
# loops around any portions of the maze. Given a maze drawn in an n × n
# grid, how can we determine if it is constructed correctly? What is the
# running time of this algorithm?
# C-14.46 Computer networks should avoid single points of failure, that is, network
# vertices that can disconnect the network if they fail. We say an undi-
# rected, connected graph G is biconnected if it contains no vertex whose
# removal would divide G into two or more connected components. Give an
# algorithm for adding at most n edges to a connected graph G, with n ≥ 3
# vertices and m ≥ n − 1 edges, to guarantee that G is biconnected. Your
# algorithm should run in O(n + m) time.
# C-14.47 Explain why all nontree edges are cross edges, with respect to a BFS tree
# constructed for an undirected graph.
# C-14.48 Explain why there are no forward nontree edges with respect to a BFS tree
# constructed for a directed graph.
# C-14.49 Show that if T is a BFS tree produced for a connected graph G, then, for
# each vertex v at level i, the path of T between s and v has i edges, and any
# other path of G between s and v has at least i edges.
# C-14.50 Justify Proposition 14.16.
# C-14.51 Provide an implementation of the BFS algorithm that uses a FIFO queue,
# rather than a level-by-level formulation, to manage vertices that have been
# discovered until the time when their neighbors are considered.
# C-14.52 A graph G is bipartite if its vertices can be partitioned into two sets X and
# Y such that every edge in G has one end vertex in X and the other in Y .
# Design and analyze an efﬁcient algorithm for determining if an undirected
# graph G is bipartite (without knowing the sets X and Y in advance).
# C-14.53 An Euler tour of a directed graph G
#  exactly once according to its direction.
# cycle that traverses each edge of G
# 
# Such a tour always exists if G is connected and the in-degree equals the
#  Describe an O(n + m)-time algorithm for
# out-degree of each vertex in G.
# 
# ﬁnding an Euler tour of such a directed graph G.
# C-14.54 A company named RT&T has a network of n switching stations connected
# by m high-speed communication links. Each customer’s phone is directly
# connected to one station in his or her area. The engineers of RT&T have
# developed a prototype video-phone system that allows two customers to
# see each other during a phone call. In order to have acceptable image
# quality, however, the number of links used to transmit video signals be-
# tween the two parties cannot exceed 4. Suppose that RT&T’s network is
# represented by a graph. Design an efﬁcient algorithm that computes, for
# each station, the set of stations it can reach using no more than 4 links.
# C-14.55 The time delay of a long-distance call can be determined by multiplying
# a small ﬁxed constant by the number of communication links on the tele-
# phone network between the caller and callee. Suppose the telephone net-
# work of a company named RT&T is a tree. The engineers of RT&T want
# to compute the maximum possible time delay that may be experienced in
# a long-distance call. Given a tree T , the diameter of T is the length of
# a longest path between two nodes of T . Give an efﬁcient algorithm for
# computing the diameter of T .
# C-14.56 Tamarindo University and many other schools worldwide are doing a joint
# project on multimedia. A computer network is built to connect these
# schools using communication links that form a tree. The schools decide
# to install a ﬁle server at one of the schools to share data among all the
# schools. Since the transmission time on a link is dominated by the link
# setup and synchronization, the cost of a data transfer is proportional to the
# number of links used. Hence, it is desirable to choose a “central” location
# for the ﬁle server. Given a tree T and a node v of T , the eccentricity of v
# is the length of a longest path from v to any other node of T . A node of T
# with minimum eccentricity is called a center of T .
# a. Design an efﬁcient algorithm that, given an n-node tree T , computes
# a center of T .
# b. Is the center unique? If not, how many distinct centers can a tree
# have?
#  is compact if there is some
# C-14.57 Say that an n-vertex directed acyclic graph G
# 
# way of numbering the vertices of G with the integers from 0 to n − 1 such
#  contains the edge (i, j) if and only if i < j, for all i, j in [0, n − 1].
# that G
#  is compact.
# Give an O(n2 )-time algorithm for detecting if
# be a weighted directed graph with n vertices. Design a variation
# C-14.58 Let G
# of Floyd-Warshall’s algorithm for computing the lengths of the shortest
# paths from each vertex to every other vertex in O(n3 ) time.
# C-14.59 Design an efﬁcient algorithm for ﬁnding a longest directed path from a
#  Specify the
# vertex s to a vertex t of an acyclic weighted directed graph G.
# graph representation used and any auxiliary data structures used. Also,
# analyze the time complexity of your algorithm.
# C-14.60 An independent set of an undirected graph G = (V, E) is a subset I of V
# such that no two vertices in I are adjacent. That is, if u and v are in I, then
# (u, v) is not in E. A maximal independent set M is an independent set
# such that, if we were to add any additional vertex to M, then it would not
# be independent any more. Every graph has a maximal independent set.
# (Can you see this? This question is not part of the exercise, but it is worth
# thinking about.) Give an efﬁcient algorithm that computes a maximal
# independent set for a graph G. What is this method’s running time?
# C-14.61 Give an example of an n-vertex simple graph G that causes Dijkstra’s
# algorithm to run in Ω(n2 log n) time when its implemented with a heap.
#  with negative-weight
# C-14.62 Give an example of a weighted directed graph G
# edges, but no negative-weight cycle, such that Dijkstra’s algorithm incor-
# rectly computes the shortest-path distances from some start vertex s.
# C-14.63 Consider the following greedy strategy for ﬁnding a shortest path from
# vertex start to vertex goal in a given connected graph.
# 1: Initialize path to start.
# 2: Initialize set visited to {start}.
# 3: If start=goal, return path and exit. Otherwise, continue.
# 4: Find the edge (start,v) of minimum weight such that v is adjacent to
# start and v is not in visited.
# 5: Add v to path.
# 6: Add v to visited.
# 7: Set start equal to v and go to step 3.
# Does this greedy strategy always ﬁnd a shortest path from start to goal?
# Either explain intuitively why it works, or give a counterexample.
# C-14.64 Our implementation of shortest path lengths in Code Fragment 14.13 re-
# lies on use of “inﬁnity” as a numeric value, to represent the distance bound
# for vertices that are not (yet) known to be reachable from the source.
# Reimplement that function without such a sentinel, so that vertices, other
# than the source, are not added to the priority queue until it is evident that
# they are reachable.
# C-14.65 Show that if all the weights in a connected weighted graph G are distinct,
# then there is exactly one minimum spanning tree for G.
# C-14.66 An old MST method, called Barůvka’s algorithm, works as follows on a
# graph G having n vertices and m edges with distinct weights:
# Let T be a subgraph of G initially containing just the vertices in V .
# while T has fewer than n − 1 edges do
# for each connected component Ci of T do
# Find the lowest-weight edge (u, v) in E with u in Ci and v not in
# Ci .
# Add (u, v) to T (unless it is already in T ).
# return T
# Prove that this algorithm is correct and that it runs in O(m log n) time.
# C-14.67 Let G be a graph with n vertices and m edges such that all the edge weights
# in G are integers in the range [1, n]. Give an algorithm for ﬁnding a mini-
# mum spanning tree for G in O(m log∗ n) time.
# C-14.68 Consider a diagram of a telephone network, which is a graph G whose ver-
# tices represent switching centers, and whose edges represent communica-
# tion lines joining pairs of centers. Edges are marked by their bandwidth,
# and the bandwidth of a path is equal to the lowest bandwidth among the
# path’s edges. Give an algorithm that, given a network and two switch-
# ing centers a and b, outputs the maximum bandwidth of a path between a
# and b.
# C-14.69 NASA wants to link n stations spread over the country using communica-
# tion channels. Each pair of stations has a different bandwidth available,
# which is known a priori. NASA wants to select n − 1 channels (the mini-
# mum possible) in such a way that all the stations are linked by the channels
# and the total bandwidth (deﬁned as the sum of the individual bandwidths
# of the channels) is maximum. Give an efﬁcient algorithm for this prob-
# lem and determine its worst-case time complexity. Consider the weighted
# graph G = (V, E), where V is the set of stations and E is the set of chan-
# nels between the stations. Deﬁne the weight w(e) of an edge e in E as the
# bandwidth of the corresponding channel.
# C-14.70 Inside the Castle of Asymptopia there is a maze, and along each corridor
# of the maze there is a bag of gold coins. The amount of gold in each
# bag varies. A noble knight, named Sir Paul, will be given the opportunity
# to walk through the maze, picking up bags of gold. He may enter the
# maze only through a door marked “ENTER” and exit through another
# door marked “EXIT.” While in the maze he may not retrace his steps.
# Each corridor of the maze has an arrow painted on the wall. Sir Paul may
# only go down the corridor in the direction of the arrow. There is no way
# to traverse a “loop” in the maze. Given a map of the maze, including the
# amount of gold in each corridor, describe an algorithm to help Sir Paul
# pick up the most gold.
# C-14.71 Suppose you are given a timetable, which consists of:
# • A set A of n airports, and for each airport a in A, a minimum con-
# necting time c(a).
# • A set F of m ﬂights, and the following, for each ﬂight f in F:
# ◦ Origin airport a1 ( f ) in A
# ◦ Destination airport a2 ( f ) in A
# ◦ Departure time t1 ( f )
# ◦ Arrival time t2 ( f )
# Describe an efﬁcient algorithm for the ﬂight scheduling problem. In this
# problem, we are given airports a and b, and a time t, and we wish to com-
# pute a sequence of ﬂights that allows one to arrive at the earliest possible
# time in b when departing from a at or after time t. Minimum connecting
# times at intermediate airports must be observed. What is the running time
# of your algorithm as a function of n and m?
#  with n vertices, and let M be the
# C-14.72 Suppose we are given a directed graph G
# 
# n × n adjacency matrix corresponding to G.
# a. Let the product of M with itself (M 2 ) be deﬁned, for 1 ≤ i, j ≤ n, as
# follows:
# M 2 (i, j) = M(i, 1)  M(1, j) ⊕ · · · ⊕ M(i, n)  M(n, j),
# where “⊕” is the Boolean or operator and “” is Boolean and.
# Given this deﬁnition, what does M 2 (i, j) = 1 imply about the ver-
# tices i and j? What if M 2 (i, j) = 0?
# b. Suppose M 4 is the product of M 2 with itself. What do the entries of
# M 4 signify? How about the entries of M 5 = (M 4 )(M)? In general,
# what information is contained in the matrix M p ?
#  is weighted and assume the following:
# c. Now suppose that G
# 1: for 1 ≤ i ≤ n, M(i, i) = 0.
# 2: for 1 ≤ i, j ≤ n, M(i, j) = weight(i, j) if (i, j) is in E.
# 3: for 1 ≤ i, j ≤ n, M(i, j) = ∞ if (i, j) is not in E.
# Also, let M 2 be deﬁned, for 1 ≤ i, j ≤ n, as follows:
# M 2 (i, j) = min{M(i, 1) + M(1, j), . . . , M(i, n) + M(n, j)}.
# If M 2 (i, j) = k, what may we conclude about the relationship be-
# tween vertices i and j?
# C-14.73 Karen has a new way to do path compression in a tree-based union/ﬁnd
# partition data structure starting at a position p. She puts all the positions
# that are on the path from p to the root in a set S. Then she scans through
# S and sets the parent pointer of each position in S to its parent’s parent
# pointer (recall that the parent pointer of the root points to itself ). If this
# pass changed the value of any position’s parent pointer, then she repeats
# this process, and goes on repeating this process until she makes a scan
# through S that does not change any position’s parent value. Show that
# Karen’s algorithm is correct and analyze its running time for a path of
# length h.
# P-14.74 Use an adjacency matrix to implement a class supporting a simpliﬁed
# graph ADT that does not include update methods. Your class should in-
# clude a constructor method that takes two collections—a collection V of
# vertex elements and a collection E of pairs of vertex elements—and pro-
# duces the graph G that these two collections represent.
# P-14.75 Implement the simpliﬁed graph ADT described in Project P-14.74, using
# the edge list structure.
# P-14.76 Implement the simpliﬁed graph ADT described in Project P-14.74, using
# the adjacency list structure.
# P-14.77 Extend the class of Project P-14.76 to support the update methods of the
# graph ADT.
# P-14.78 Design an experimental comparison of repeated DFS traversals versus
# the Floyd-Warshall algorithm for computing the transitive closure of a
# directed graph.
# P-14.79 Perform an experimental comparison of two of the minimum spanning
# tree algorithms discussed in this chapter (Kruskal and Prim-Jarnı́k). De-
# velop an extensive set of experiments to test the running times of these
# algorithms using randomly generated graphs.
# P-14.80 One way to construct a maze starts with an n × n grid such that each grid
# cell is bounded by four unit-length walls. We then remove two boundary
# unit-length walls, to represent the start and ﬁnish. For each remaining
# unit-length wall not on the boundary, we assign a random value and cre-
# ate a graph G, called the dual, such that each grid cell is a vertex in G
# and there is an edge joining the vertices for two cells if and only if the
# cells share a common wall. The weight of each edge is the weight of the
# corresponding wall. We construct the maze by ﬁnding a minimum span-
# ning tree T for G and removing all the walls corresponding to edges in
# T . Write a program that uses this algorithm to generate mazes and then
# solves them. Minimally, your program should draw the maze and, ideally,
# it should visualize the solution as well
# P-14.81 Write a program that builds the routing tables for the nodes in a computer
# network, based on shortest-path routing, where path distance is measured
# by hop count, that is, the number of edges in a path. The input for this
# problem is the connectivity information for all the nodes in the network,
# as in the following example:
# 241.12.31.14 : 241.12.31.15 241.12.31.18 241.12.31.19
# which indicates three network nodes that are connected to 241.12.31.14,
# that is, three nodes that are one hop away. The routing table for the node at
# address A is a set of pairs (B,C), which indicates that, to route a message
# from A to B, the next node to send to (on the shortest path from A to B)
# is C. Your program should output the routing table for each node in the
# network, given an input list of node connectivity lists, each of which is
# input in the syntax as shown above, one per line.


# In[ ]:
class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    # -------------------------- nested Node class --------------------------
    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next=None):
            """Initialize node’s fields.
            
            Args:
                element: Reference to user’s element.
                next: Reference to next node (default is None).
            """
            self._element = element  # reference to user’s element
            self._next = next        # reference to next node

    # ------------------------------- stack methods -------------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None  # reference to the head node
        self._size = 0     # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        # create and link a new node
        self._head = self.Node(e, self._head)
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")  # Use a generic exception for simplicity
        # top of stack is at head of list
        return self._head._element

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty")  # Use a generic exception for simplicity
        answer = self._head._element
        # bypass the former top node
        self._head = self._head._next
        self._size -= 1
        return answer


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next=None):
            """Initialize node’s fields.
            
            Args:
                element: Reference to user’s element.
                next: Reference to next node (default is None).
            """
            self._element = element  # reference to user’s element
            self._next = next        # reference to next node

    def __init__(self):
        """Create an empty queue."""
        self._head = None  # reference to the head node
        self._tail = None  # reference to the tail node
        self._size = 0     # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        
        Raise Exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")  # Use a generic exception for simplicity
        # front aligned with head of list
        return self._head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        
        Raise Exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")  # Use a generic exception for simplicity
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        
        # special case: queue is now empty
        if self.is_empty():
            # removed head had been the tail
            self._tail = None
            
        return answer

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        # node will be new tail node
        newest = self.Node(e, None)
        
        if self.is_empty():
            # special case: previously empty
            self._head = newest
        else:
            self._tail._next = newest  # link new node after tail
            
        # update reference to tail node
        self._tail = newest
        self._size += 1

class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next=None):
            """Initialize node’s fields.
            
            Args:
                element: Reference to user’s element.
                next: Reference to next node (default is None).
            """
            self._element = element  # reference to user’s element
            self._next = next        # reference to next node

    def __init__(self):
        """Create an empty queue."""
        self._tail = None  # will represent tail of queue
        self._size = 0     # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        
        Raise Exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")  # Use a generic exception for simplicity
        head = self._tail._next  # front aligned with head of list
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        
        Raise Exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception("Queue is empty")  # Use a generic exception for simplicity
        
        old_head = self._tail._next
        
        # Removing only element
        if self._size == 1:
            # Queue becomes empty
            self._tail = None
        else:
            # Bypass the old head
            self._tail._next = old_head._next
        
        self._size -= 1
        return old_head._element

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        
        # Node will be new tail node
        newest = self.Node(e)
        
        if self.is_empty():
            # Initialize circularly
            newest._next = newest
        else:
            # New node points to head
            newest._next = self._tail._next
        
        # Old tail points to new node
        self._tail._next = newest
        
        # New node becomes the tail
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        
        if self._size > 0:
            self._tail = self._tail._next  # old head becomes new tail


class DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        
        __slots__ = '_element', '_prev', '_next'  # streamline memory usage

        def __init__(self, element, prev=None, next=None):
            """Initialize node’s fields.
            
            Args:
                element: Reference to user’s element.
                prev: Reference to previous node (default is None).
                next: Reference to next node (default is None).
            """
            self._element = element  # reference to user’s element
            self._prev = prev        # reference to previous node
            self._next = next        # reference to next node

    def __init__(self):
        """Create an empty list."""
        self._header = self.Node(None)  # sentinel header
        self._trailer = self.Node(None)  # sentinel trailer
        # trailer is after header
        self._header._next = self._trailer
        # header is before trailer
        self._trailer._prev = self._header
        self._size = 0  # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self.Node(e, predecessor, successor)  # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        
        # record deleted element
        element = node._element
        
        # deprecate node
        node._prev = node._next = node._element = None
        
        return element


class LinkedDeque(DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")  # Use a generic exception for simplicity
        # real item just after header
        return self._header._next._element

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty")  # Use a generic exception for simplicity
        # real item just before trailer
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self.insert_between(e, self._header, self._header._next)  # after header

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self.insert_between(e, self._trailer._prev, self._trailer)  # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque.
        
        Raise Exception if the deque is empty.
        """
        if self.is_empty():
            raise Exception("Deque is empty")  # Use a generic exception for simplicity
        # use inherited method
        return self.delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque.
        
        Raise Exception if the deque is empty.
        """
        if self.is_empty():
            raise Exception("Deque is empty")  # Use a generic exception for simplicity
        # use inherited method
        return self.delete_node(self._trailer._prev)




class PositionalList(DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # -------------------------- nested Position class --------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self.container = container
            self.node = node

        def element(self):
            """Return the element stored at this Position."""
            return self.node._element

        def eq(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other.node is self.node

        def ne(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # opposite of eq

    # ------------------------------- utility method -------------------------------
    def validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p.container is not self:
            raise ValueError("p does not belong to this container")
        # convention for deprecated nodes
        if p.node._next is None:
            raise ValueError("p is no longer valid")
        return p.node

    # ------------------------------- utility method -------------------------------
    def make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None  # boundary violation
        else:
            return self.Position(self, node)  # legitimate position

    # ------------------------------- accessors -------------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self.make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self.make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self.validate(p)
        return self.make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self.validate(p)
        return self.make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------------- mutators -------------------------------
    # override inherited version to return Position rather than Node
    def insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super().insert_between(e, predecessor, successor)
        return self.make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self.insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self.insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self.validate(p)
        return self.insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self.validate(p)
        return self.insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self.validate(p)
        # inherited method returns element
        return self.delete_node(original)

    def replace(self, p, e):
        """Replace the element at Position p with e.
        
        Return the element formerly at Position p.
        """
        original = self.validate(p)
        
        # temporarily store old element
        old_value = original.element()
        
        # replace with new element
        original.node._element = e
        
        # return the old element value
        return old_value


def insertion_sort(L):
    """Sort PositionalList of comparable elements into nondecreasing order."""
    if len(L) > 1:
        # otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)  # next item to place
            value = pivot.element()
            
            if value >= marker.element():
                # pivot is already sorted
                marker = pivot  # pivot becomes new marker
            else:
                # must relocate pivot
                walk = marker
                
                # find leftmost item greater than value
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                
                L.delete(pivot)  # remove pivot from its current position
                # reinsert value before walk
                L.add_before(walk, value)


class FavoritesList:
    """List of elements ordered from most frequently accessed to least."""

    # ------------------------------ nested Item class ------------------------------
    class Item:
        __slots__ = '_value', '_count'  # streamline memory usage

        def __init__(self, e):
            """Initialize the user's element and access count."""
            self._value = e  # the user's element
            self._count = 0  # access count initially zero

    # ------------------------------- nonpublic utilities -------------------------------
    def __find_position(self, e):
        """Search for element e and return its Position (or None if not found)."""
        walk = self.data.first()
        while walk is not None and walk.element()._value != e:
            walk = self.data.after(walk)
        return walk

    def __move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self.data.first():
            cnt = p.element()._count
            walk = self.data.before(p)

            # must shift forward
            if cnt > walk.element()._count:
                while (walk != self.data.first() and
                       cnt > self.data.before(walk).element()._count):
                    walk = self.data.before(walk)
                
                # delete/reinsert
                self.data.add_before(walk, self.data.delete(p))

    # ------------------------------- public methods -------------------------------
    def __init__(self):
        """Create an empty list of favorites."""
        # will be list of Item instances
        self.data = PositionalList()

    def __len__(self):
        """Return number of entries on favorites list."""
        return len(self.data)

    def is_empty(self):
        """Return True if list is empty."""
        return len(self.data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        # try to locate existing element
        p = self.__find_position(e)
        
        if p is None:
            p = self.data.add_last(self.Item(e))  # if new, place at end
        
        # always increment count
        p.element()._count += 1
        
        # consider moving forward
        self.__move_up(p)

    def remove(self, e):
        """Remove element e from the list of favorites."""
        # try to locate existing element
        p = self.__find_position(e)
        
        if p is not None:
            # delete, if found
            self.data.delete(p)

    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        
        walk = self.data.first()
        
        for j in range(k):
            item = walk.element()  # element of list is Item
            
            # report user’s element
            yield item._value
            
            walk = self.data.after(walk)


class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic."""

    # We override move_up to provide move-to-front semantics
    def move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self.data.first():
            # delete/reinsert
            self.data.add_first(self.data.delete(p))

    # We override top because list is no longer sorted
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")

        # We begin by making a copy of the original list
        temp = PositionalList()  # Create a temporary positional list
        
        # Positional lists support iteration
        for item in self.data:
            temp.add_last(item)

        # We repeatedly find, report, and remove element with largest count
        for j in range(k):
            # Find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)

            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)

            # We have found the element with highest count
            # Report element to user
            yield highPos.element()._value
            
            # Remove the reported element from the temporary list
            temp.delete(highPos)



# R-7.1 Give an algorithm for ﬁnding the second-to-last node in a singly linked
# list in which the last node is indicated by a next reference of None.
# R-7.2 Describe a good algorithm for concatenating two singly linked lists L and
# M, given only references to the ﬁrst node of each list, into a single list L
# that contains all the nodes of L followed by all the nodes of M.
# R-7.3 Describe a recursive algorithm that counts the number of nodes in a singly
# linked list.
# R-7.4 Describe in detail how to swap two nodes x and y (and not just their con-
# tents) in a singly linked list L given references only to x and y. Repeat
# this exercise for the case when L is a doubly linked list. Which algorithm
# takes more time?
# R-7.5 Implement a function that counts the number of nodes in a circularly
# linked list.
# R-7.6 Suppose that x and y are references to nodes of circularly linked lists,
# although not necessarily the same list. Describe a fast algorithm for telling
# if x and y belong to the same list.
# R-7.7 Our CircularQueue class of Section 7.2.2 provides a rotate( ) method that
# has semantics equivalent to Q.enqueue(Q.dequeue( )), for a nonempty
# queue. Implement such a method for the LinkedQueue class of Sec-
# tion 7.1.2 without the creation of any new nodes.
# R-7.8 Describe a nonrecursive method for ﬁnding, by link hopping, the middle
# node of a doubly linked list with header and trailer sentinels. In the case
# of an even number of nodes, report the node slightly left of center as the
# “middle.” (Note: This method must only use link hopping; it cannot use a
# counter.) What is the running time of this method?
# R-7.9 Give a fast algorithm for concatenating two doubly linked lists L and M,
# with header and trailer sentinel nodes, into a single list L .
# R-7.10 There seems to be some redundancy in the repertoire of the positional
# list ADT, as the operation L.add ﬁrst(e) could be enacted by the alter-
# native L.add before(L.ﬁrst( ), e). Likewise, L.add last(e) might be per-
# formed as L.add after(L.last( ), e). Explain why the methods add ﬁrst
# and add last are necessary.
# R-7.11 Implement a function, with calling syntax max(L), that returns the max-
# imum element from a PositionalList instance L containing comparable
# elements.
# R-7.12 Redo the previously problem with max as a method of the PositionalList
# class, so that calling syntax L.max( ) is supported.
# R-7.13 Update the PositionalList class to support an additional method ﬁnd(e),
# which returns the position of the (ﬁrst occurrence of ) element e in the list
# (or None if not found).
# R-7.14 Repeat the previous process using recursion. Your method should not
# contain any loops. How much space does your method use in addition to
# the space used for L?
# R-7.15 Provide support for a reversed method of the PositionalList class that
# is similar to the given iter , but that iterates the elements in reversed
# order.
# R-7.16 Describe an implementation of the PositionalList methods add last and
# add before realized by using only methods in the set {is empty, ﬁrst, last,
# prev, next, add after, and add ﬁrst}.
# R-7.17 In the FavoritesListMTF class, we rely on public methods of the positional
# list ADT to move an element of a list at position p to become the ﬁrst ele-
# ment of the list, while keeping the relative order of the remaining elements
# unchanged. Internally, that combination of operations causes one node to
# be removed and a new node to be inserted. Augment the PositionalList
# class to support a new method, move to front(p), that accomplishes this
# goal more directly, by relinking the existing node.
# R-7.18 Given the set of element {a, b, c, d, e, f } stored in a list, show the ﬁnal state
# of the list, assuming we use the move-to-front heuristic and access the el-
# ements according to the following sequence: (a, b, c, d, e, f , a, c, f , b, d, e).
# R-7.19 Suppose that we have made kn total accesses to the elements in a list L of
# n elements, for some integer k ≥ 1. What are the minimum and maximum
# number of elements that have been accessed fewer than k times?
# R-7.20 Let L be a list of n items maintained according to the move-to-front heuris-
# tic. Describe a series of O(n) accesses that will reverse L.
# R-7.21 Suppose we have an n-element list L maintained according to the move-
# to-front heuristic. Describe a sequence of n2 accesses that is guaranteed
# to take Ω(n3 ) time to perform on L.
# R-7.22 Implement a clear( ) method for the FavoritesList class that returns the list
# to empty.
# R-7.23 Implement a reset counts( ) method for the FavoritesList class that resets
# all elements’ access counts to zero (while leaving the order of the list
# unchanged).
# www.it-ebooks.infoChapter 7. Linked Lists
# 296
# Creativity
# C-7.24 Give a complete implementation of the stack ADT using a singly linked
# list that includes a header sentinel.
# C-7.25 Give a complete implementation of the queue ADT using a singly linked
# list that includes a header sentinel.
# C-7.26 Implement a method, concatenate(Q2) for the LinkedQueue class that
# takes all elements of LinkedQueue Q2 and appends them to the end of the
# original queue. The operation should run in O(1) time and should result
# in Q2 being an empty queue.
# C-7.27 Give a recursive implementation of a singly linked list class, such that an
# instance of a nonempty list stores its ﬁrst element and a reference to a list
# of remaining elements.
# C-7.28 Describe a fast recursive algorithm for reversing a singly linked list.
# C-7.29 Describe in detail an algorithm for reversing a singly linked list L using
# only a constant amount of additional space and not using any recursion.
# C-7.30 Exercise P-6.35 describes a LeakyStack abstraction. Implement that ADT
# using a singly linked list for storage.
# C-7.31 Design a forward list ADT that abstracts the operations on a singly linked
# list, much as the positional list ADT abstracts the use of a doubly linked
# list. Implement a ForwardList class that supports such an ADT.
# C-7.32 Design a circular positional list ADT that abstracts a circularly linked list
# in the same way that the positional list ADT abstracts a doubly linked list,
# with a notion of a designated “cursor” position within the list.
# C-7.33 Modify the DoublyLinkedBase class to include a reverse method that re-
# verses the order of the list, yet without creating or destroying any nodes.
# C-7.34 Modify the PositionalList class to support a method swap(p, q) that causes
# the underlying nodes referenced by positions p and q to be exchanged for
# each other. Relink the existing nodes; do not create any new nodes.
# C-7.35 To implement the iter method of the PositionalList class, we relied on the
# convenience of Python’s generator syntax and the yield statement. Give
# an alternative implementation of iter by designing a nested iterator class.
# (See Section 2.3.4 for discussion of iterators.)
# C-7.36 Give a complete implementation of the positional list ADT using a doubly
# linked list that does not include any sentinel nodes.
# C-7.37 Implement a function that accepts a PositionalList L of n integers sorted
# in nondecreasing order, and another value V , and determines in O(n) time
# if there are two elements of L that sum precisely to V . The function should
# return a pair of positions of such elements, if found, or None otherwise.
# www.it-ebooks.info7.8. Exercises
# 297
# C-7.38 There is a simple, but inefﬁcient, algorithm, called bubble-sort, for sorting
# a list L of n comparable elements. This algorithm scans the list n−1 times,
# where, in each scan, the algorithm compares the current element with the
# next one and swaps them if they are out of order. Implement a bubble sort
# function that takes a positional list L as a parameter. What is the running
# time of this algorithm, assuming the positional list is implemented with a
# doubly linked list?
# C-7.39 To better model a FIFO queue in which entries may be deleted before
# reaching the front, design a PositionalQueue class that supports the com-
# plete queue ADT, yet with enqueue returning a position instance and sup-
# port for a new method, delete(p), that removes the element associated
# with position p from the queue. You may use the adapter design pattern
# (Section 6.1.2), using a PositionalList as your storage.
# C-7.40 Describe an efﬁcient method for maintaining a favorites list L, with move-
# to-front heuristic, such that elements that have not been accessed in the
# most recent n accesses are automatically purged from the list.
# C-7.41 Exercise C-5.29 introduces the notion of a natural join of two databases.
# Describe and analyze an efﬁcient algorithm for computing the natural join
# of a linked list A of n pairs and a linked list B of m pairs.
# C-7.42 Write a Scoreboard class that maintains the top 10 scores for a game ap-
# plication using a singly linked list, rather than the array that was used in
# Section 5.5.1.
# C-7.43 Describe a method for performing a card shufﬂe of a list of 2n elements,
# by converting it into two lists. A card shufﬂe is a permutation where a list
# L is cut into two lists, L1 and L2 , where L1 is the ﬁrst half of L and L2 is the
# second half of L, and then these two lists are merged into one by taking
# the ﬁrst element in L1 , then the ﬁrst element in L2 , followed by the second
# element in L1 , the second element in L2 , and so on.
# Projects
# P-7.44 Write a simple text editor that stores and displays a string of characters
# using the positional list ADT, together with a cursor object that highlights
# a position in this string. A simple interface is to print the string and then
# to use a second line of output to underline the position of the cursor. Your
# editor should support the following operations:
# • left: Move cursor left one character (do nothing if at beginning).
# • right: Move cursor right one character (do nothing if at end).
# • insert c: Insert the character c just after the cursor.
# • delete: Delete the character just after the cursor (do nothing at end).
# www.it-ebooks.infoChapter 7. Linked Lists
# 298
# P-7.45 An array A is sparse if most of its entries are empty (i.e., None). A list
# L can be used to implement such an array efﬁciently. In particular, for
# each nonempty cell A[i], we can store an entry (i, e) in L, where e is the
# element stored at A[i]. This approach allows us to represent A using O(m)
# storage, where m is the number of nonempty entries in A. Provide such
# a SparseArray class that minimally supports methods getitem (j) and
# setitem (j, e) to provide standard indexing operations. Analyze the
# efﬁciency of these methods.
# P-7.46 Although we have used a doubly linked list to implement the positional
# list ADT, it is possible to support the ADT with an array-based imple-
# mentation. The key is to use the composition pattern and store a sequence
# of position items, where each item stores an element as well as that ele-
# ment’s current index in the array. Whenever an element’s place in the array
# is changed, the recorded index in the position must be updated to match.
# Given a complete class providing such an array-based implementation of
# the positional list ADT. What is the efﬁciency of the various operations?
# P-7.47 Implement a CardHand class that supports a person arranging a group of
# cards in his or her hand. The simulator should represent the sequence of
# cards using a single positional list ADT so that cards of the same suit are
# kept together. Implement this strategy by means of four “ﬁngers” into the
# hand, one for each of the suits of hearts, clubs, spades, and diamonds,
# so that adding a new card to the person’s hand or playing a correct card
# from the hand can be done in constant time. The class should support the
# following methods:
# • add card(r, s): Add a new card with rank r and suit s to the hand.
# • play(s): Remove and return a card of suit s from the player’s hand;
# if there is no card of suit s, then remove and return an arbitrary card
# from the hand.
# iter ( ): Iterate through all cards currently in the hand.
# •
# • all of suit(s): Iterate through all cards of suit s that are currently in
# the hand.

#HashTable


# Initialize an empty dictionary to store word frequencies
freq = {}
filename='data/abc.txt'
# Open the file and read its contents
for piece in open(filename).read().lower().split():
    # Only consider alphabetic characters within this piece
    word = ''.join(c for c in piece if c.isalpha())
    
    if word:  # Require at least one alphabetic character
        freq[word] = 1 + freq.get(word, 0)

# Initialize variables to track the most frequent word and its count
max_word = ''
max_count = 0

# Iterate through the frequency dictionary to find the most frequent word
for w, c in freq.items():  # (key, value) tuples represent (word, count)
    if c > max_count:
        max_word = w
        max_count = c

# Print the results
print("The most frequent word is:", max_word)
print("Its number of occurrences is:", max_count)



from collections.abc import MutableMapping

class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic Item class."""

    # ------------------------------- nested Item class -------------------------------
    class Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = '_key', '_value'  # streamline memory usage

        def __init__(self, k, v):
            """Initialize the key-value pair."""
            self._key = k
            self._value = v

        def __eq__(self, other):
            """Compare items based on their keys."""
            return self._key == other._key

        def __ne__(self, other):
            """Return True if items are not equal."""
            return not (self == other)  # opposite of eq

        def __lt__(self, other):
            """Compare items based on their keys."""
            return self._key < other._key


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        # list of Item instances
        self.table = []

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self.table:
            if k == item._key:
                return item._value
        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self.table:
            # Found a match:
            if k == item._key:
                # reassign value
                item._value = v
                return  # and quit
        # did not find match for key
        self.table.append(self.Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self.table)):
            # Found a match:
            if k == self.table[j]._key:
                # remove item
                self.table.pop(j)
                return  # and quit
        raise KeyError("Key Error: " + repr(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self.table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self.table:
            # yield the KEY
            yield item._key



def hash_code(s):
    mask = (1 << 32) - 1  # Use a minus sign instead of a special character
    h = 0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(character)
    return h


def __hash__ (self):
    return hash( (self._red, self._green, self._blue) )

from random import randrange, seed

class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map."""
        self.table = [None] * cap  # Initialize the table with None
        # number of entries in the map
        self.n = 0
        # prime for MAD compression
        self.prime = p
        # scale from 1 to p-1 for MAD
        self.scale = 1 + randrange(p - 1)
        # shift from 0 to p-1 for MAD
        self.shift = randrange(p)

    def hash_function(self, k):
        """Compute the hash value for key k."""
        return (hash(k) * self.scale + self.shift) % self.prime % len(self.table)

    def __len__(self):
        """Return the number of entries in the map."""
        return self.n

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        j = self.hash_function(k)
        # may raise KeyError
        return self.bucket_getitem(j, k)

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        j = self.hash_function(k)
        # subroutine maintains self.n
        self.bucket_setitem(j, k, v)
        
        # keep load factor <= 0.5
        if self.n > len(self.table) // 2:
            # number 2^x - 1 is often prime
            self.resize(2 * len(self.table) - 1)

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        j = self.hash_function(k)
        # may raise KeyError
        self.bucket_delitem(j, k)
        self.n -= 1

    def resize(self, c):
        """Resize bucket array to capacity c."""
        old = list(self.items())  # use iteration to record existing items
        # then reset table to desired capacity
        self.table = [None] * c  # Initialize new table with None
        # n recomputed during subsequent adds
        self.n = 0
        for (k, v) in old:
            self[k] = v  # Reinsert items into the resized table


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution."""

    def bucket_getitem(self, j, k):
        """Return value associated with key k in bucket j (raise KeyError if not found)."""
        bucket = self.table[j]
        if bucket is None:
            # No match found
            raise KeyError("Key Error: " + repr(k))
        return bucket[k]  # May raise KeyError if k is not found in the bucket

    def bucket_setitem(self, j, k, v):
        """Assign value v to key k in bucket j, overwriting existing value if present."""
        if self.table[j] is None:
            # Bucket is new to the table
            self.table[j] = UnsortedTableMap()
        oldsize = len(self.table[j])
        self.table[j][k] = v  # Key was new to the table
        if len(self.table[j]) > oldsize:
            # Increase overall map size as a new key was added
            self.n += 1

    def bucket_delitem(self, j, k):
        """Remove item associated with key k in bucket j (raise KeyError if not found)."""
        bucket = self.table[j]
        if bucket is None:
            # No match found
            raise KeyError("Key Error: " + repr(k))
        del bucket[k]  # May raise KeyError if k is not found in the bucket

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for bucket in self.table:
            if bucket is not None:
                # A nonempty slot
                for key in bucket:
                    yield key

class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    
    AVAIL = object()  # sentinel marks locations of previous deletions

    def is_available(self, j):
        """Return True if index j is available in table."""
        return self.table[j] is None or self.table[j] is ProbeHashMap.AVAIL

    def find_slot(self, j, k):
        """Search for key k in bucket at index j.

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        """
        first_avail = None
        while True:
            if self.is_available(j):
                if first_avail is None:
                    first_avail = j  # mark this as first available
                if self.table[j] is None:
                    return (False, first_avail)  # search has failed
                elif k == self.table[j]._key:
                    return (True, j)  # found a match
            # keep looking (cyclically)
            j = (j + 1) % len(self.table)

    def bucket_getitem(self, j, k):
        """Return value associated with key k in bucket at index j (raise KeyError if not found)."""
        found, s = self.find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        return self.table[s]._value

    def bucket_setitem(self, j, k, v):
        """Assign value v to key k in bucket at index j, overwriting existing value if present."""
        found, s = self.find_slot(j, k)
        if not found:
            self.table[s] = self.Item(k, v)  # Create a new item
            self.n += 1  # Increase the count of items
        else:
            self.table[s]._value = v  # Update existing value

    def bucket_delitem(self, j, k):
        """Remove item associated with key k in bucket at index j (raise KeyError if not found)."""
        found, s = self.find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        self.table[s] = ProbeHashMap.AVAIL  # Mark the slot as available

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for j in range(len(self.table)):
            if not self.is_available(j):
                yield self.table[j]._key  # Yield the key from non-empty slots


class SortedTableMap(MapBase):
    """Map implementation using a sorted table."""

    # ----------------------------- nonpublic behaviors -----------------------------
    def find_index(self, k, low, high):
        """Return index of the leftmost item with key greater than or equal to k.

        Return high + 1 if no such item qualifies.
        That is, j will be returned such that:
        all items of slice table[low:j] have key < k
        all items of slice table[j:high+1] have key >= k
        """
        if high < low:
            return high + 1  # no element qualifies
        else:
            mid = (low + high) // 2
            if k == self.table[mid]._key:
                return mid  # found exact match
            elif k < self.table[mid]._key:
                return self.find_index(k, low, mid - 1)  # search left
            else:
                return self.find_index(k, mid + 1, high)  # search right

    # ----------------------------- public behaviors -----------------------------
    def __init__(self):
        """Create an empty map."""
        self.table = []

    def __len__(self):
        """Return number of items in the map."""
        return len(self.table)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        j = self.find_index(k, 0, len(self.table) - 1)
        if j == len(self.table) or self.table[j]._key != k:
            raise KeyError("Key Error: " + repr(k))
        return self.table[j]._value

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        j = self.find_index(k, 0, len(self.table) - 1)
        if j < len(self.table) and self.table[j]._key == k:
            # reassign value
            self.table[j]._value = v
        else:
            # add new item
            self.table.insert(j, self.Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        j = self.find_index(k, 0, len(self.table) - 1)
        if j == len(self.table) or self.table[j]._key != k:
            raise KeyError("Key Error: " + repr(k))
        # delete item
        self.table.pop(j)

    def __iter__(self):
        """Generate keys of the map ordered from minimum to maximum."""
        for item in self.table:
            yield item._key

    def reversed(self):
        """Generate keys of the map ordered from maximum to minimum."""
        for item in reversed(self.table):
            yield item._key

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        if len(self.table) > 0:
            return (self.table[0]._key, self.table[0]._value)
        else:
            return None

    def find_max(self):
        """Return (key,value) pair with maximum key (or None if empty)."""
        if len(self.table) > 0:
            return (self.table[-1]._key, self.table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k."""
        j = self.find_index(k, 0, len(self.table) - 1)
        if j < len(self.table):
            return (self.table[j]._key, self.table[j]._value)
        else:
            return None

    def find_lt(self, k):
        """Return (key,value) pair with greatest key strictly less than k."""
        j = self.find_index(k, 0, len(self.table) - 1)
        if j > 0:
            return (self.table[j - 1]._key, self.table[j - 1]._value)  # Note use of j-1
        else:
            return None

    def find_gt(self, k):
        """Return (key,value) pair with least key strictly greater than k."""
        j = self.find_index(k, 0, len(self.table) - 1)
        
        if j < len(self.table) and self.table[j]._key == k:
            j += 1  # advance past match
        
        if j < len(self.table):
            return (self.table[j]._key, self.table[j]._value)
        
        return None

    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop.
        
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        
        if start is None:
            j = 0
        else:
            # find first result
            j = self.find_index(start, 0, len(self.table) - 1)
        
        while j < len(self.table) and (stop is None or self.table[j]._key < stop):
            yield (self.table[j]._key, self.table[j]._value)
            j += 1



class CostPerformanceDatabase:
    """Maintain a database of maximal (cost, performance) pairs."""

    def __init__(self):
        """Create an empty database."""
        # or a more efficient sorted map
        self.M = SortedTableMap()

    def best(self, c):
        """Return (cost, performance) pair with largest cost not exceeding c.

        Return None if there is no such pair.
        """
        return self.M.find_le(c)

    def add(self, c, p):
        """Add new entry with cost c and performance p."""
        # Determine if (c, p) is dominated by an existing pair
        # other is at least as cheap as c
        other = self.M.find_le(c)
        
        if other is not None and other[1] >= p:  # if its performance is as good
            return  # (c, p) is dominated, so ignore
        
        # Else, add (c, p) to database
        self.M[c] = p
        
        # Now remove any pairs that are dominated by (c, p)
        # Other more expensive than c
        other = self.M.find_gt(c)
        
        while other is not None and other[1] <= p:
            del self.M[other[0]]
            other = self.M.find_gt(c)


class MultiMap:
    """A multimap class built upon use of an underlying map for storage."""
    
    MapType = dict  # Map type; can be redefined by subclass

    def __init__(self):
        """Create a new empty multimap instance."""
        # Create map instance for storage
        self.map = self.MapType()
        self.n = 0

    def __iter__(self):
        """Iterate through all (k, v) pairs in multimap."""
        for k, secondary in self.map.items():
            for v in secondary:
                yield (k, v)

    def add(self, k, v):
        """Add pair (k, v) to multimap."""
        # Create empty list if needed
        container = self.map.setdefault(k, [])
        container.append(v)
        self.n += 1

    def pop(self, k):
        """Remove and return arbitrary (k, v) with key k (or raise KeyError)."""
        # May raise KeyError
        secondary = self.map[k]
        v = secondary.pop()
        if len(secondary) == 0:
            # No pairs left
            del self.map[k]
        self.n -= 1
        return (k, v)

    def find(self, k):
        """Return arbitrary (k, v) pair with given key (or raise KeyError)."""
        # May raise KeyError
        secondary = self.map[k]
        return (k, secondary[0])

    def find_all(self, k):
        """Generate iteration of all (k, v) pairs with given key."""
        # Empty list by default
        secondary = self.map.get(k, [])
        for v in secondary:
            yield (k, v)


"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = {}
        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for char in ransomNote:
            if char in char_count and char_count[char] > 0:
                char_count[char] -= 1
            else:
                return False
        
        return True
    
"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t

            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s
        
        return True

"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count+=1
        return count


"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.

"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        required = {'b':1,'a':1,'l':2,'o':2,'n':1}
        char_count = {}
        for char in text:
            if char in required:
                char_count[char] = char_count.get(char, 0) + 1

        max_instances = float('inf')
        for char, count in required.items():
            if char in char_count:
                max_instances = min(max_instances, char_count[char]//count)
            else:
                return 0
        return max_instances

"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
 

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Constraints:

0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
"""
class MyHashMap:

    def __init__(self):
        self.data = [-1]*1000001

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# R-10.1 Give a concrete implementation of the pop method in the context of the
# MutableMapping class, relying only on the ﬁve primary abstract methods
# of that class.
# R-10.2 Give a concrete implementation of the items( ) method in the context of
# the MutableMapping class, relying only on the ﬁve primary abstract meth-
# ods of that class. What would its running time be if directly applied to the
# UnsortedTableMap subclass?
# R-10.3 Give a concrete implementation of the items( ) method directly within the
# UnsortedTableMap class, ensuring that the entire iteration runs in O(n)
# time.
# R-10.4 What is the worst-case running time for inserting n key-value pairs into an
# initially empty map M that is implemented with the UnsortedTableMap
# class?
# R-10.5 Reimplement the UnsortedTableMap class from Section 10.1.5, using the
# PositionalList class from Section 7.4 rather than a Python list.
# R-10.6 Which of the hash table collision-handling schemes could tolerate a load
# factor above 1 and which could not?
# R-10.7 Our Position classes for lists and trees support the eq method so that
# two distinct position instances are considered equivalent if they refer to the
# same underlying node in a structure. For positions to be allowed as keys
# in a hash table, there must be a deﬁnition for the hash method that
# is consistent with this notion of equivalence. Provide such a hash
# method.
# R-10.8 What would be a good hash code for a vehicle identiﬁcation number that
# is a string of numbers and letters of the form “9X9XX99X9XX999999,”
# where a “9” represents a digit and an “X” represents a letter?
# R-10.9 Draw the 11-entry hash table that results from using the hash function,
# h(i) = (3i + 5) mod 11, to hash the keys 12, 44, 13, 88, 23, 94, 11, 39, 20,
# 16, and 5, assuming collisions are handled by chaining.
# R-10.10 What is the result of the previous exercise, assuming collisions are han-
# dled by linear probing?
# R-10.11 Show the result of Exercise R-10.9, assuming collisions are handled by
# quadratic probing, up to the point where the method fails.
# www.it-ebooks.info10.6. Exercises
# 453
# R-10.12 What is the result of Exercise R-10.9 when collisions are handled by dou-
# ble hashing using the secondary hash function h (k) = 7 − (k mod 7)?
# R-10.13 What is the worst-case time for putting n entries in an initially empty hash
# table, with collisions resolved by chaining? What is the best case?
# R-10.14 Show the result of rehashing the hash table shown in Figure 10.6 into a
# table of size 19 using the new hash function h(k) = 3k mod 17.
# R-10.15 Our HashMapBase class maintains a load factor λ ≤ 0.5. Reimplement
# that class to allow the user to specify the maximum load, and adjust the
# concrete subclasses accordingly.
# R-10.16 Give a pseudo-code description of an insertion into a hash table that uses
# quadratic probing to resolve collisions, assuming we also use the trick of
# replacing deleted entries with a special “deactivated entry” object.
# R-10.17 Modify our ProbeHashMap to use quadratic probing.
# R-10.18 Explain why a hash table is not suited to implement a sorted map.
# R-10.19 Describe how a sorted list implemented as a doubly linked list could be
# used to implement the sorted map ADT.
# R-10.20 What is the worst-case asymptotic running time for performing n deletions
# from a SortedTableMap instance that initially contains 2n entries?
# R-10.21 Consider the following variant of the ﬁnd index method from Code Frag-
# ment 10.8, in the context of the SortedTableMap class:
# def ﬁnd index(self, k, low, high):
# if high < low:
# return high + 1
# else:
# mid = (low + high) // 2
# if self. table[mid]. key < k:
# return self. ﬁnd index(k, mid + 1, high)
# else:
# return self. ﬁnd index(k, low, mid − 1)
# Does this always produce the same result as the original version? Justify
# your answer.
# R-10.22 What is the expected running time of the methods for maintaining a max-
# ima set if we insert n pairs such that each pair has lower cost and perfor-
# mance than one before it? What is contained in the sorted map at the end
# of this series of operations? What if each pair had a lower cost and higher
# performance than the one before it?
# R-10.23 Draw an example skip list S that results from performing the following
# series of operations on the skip list shown in Figure 10.13: del S[38],
# S[48] = x , S[24] = y , del S[55]. Record your coin ﬂips, as well.
# www.it-ebooks.infoChapter 10. Maps, Hash Tables, and Skip Lists
# 454
# R-10.24 Give a pseudo-code description of the
# using a skip list.
# delitem
# map operation when
# R-10.25 Give a concrete implementation of the pop method, in the context of a
# MutableSet abstract base class, that relies only on the ﬁve core set behav-
# iors described in Section 10.5.2.
# R-10.26 Give a concrete implementation of the isdisjoint method in the context
# of the MutableSet abstract base class, relying only on the ﬁve primary
# abstract methods of that class. Your algorithm should run in O(min(n, m))
# where n and m denote the respective cardinalities of the two sets.
# R-10.27 What abstraction would you use to manage a database of friends’ birth-
# days in order to support efﬁcient queries such as “ﬁnd all friends whose
# birthday is today” and “ﬁnd the friend who will be the next to celebrate a
# birthday”?
# Creativity
# C-10.28 On page 406 of Section 10.1.3, we give an implementation of the method
# setdefault as it might appear in the MutableMapping abstract base class.
# While that method accomplishes the goal in a general fashion, its efﬁ-
# ciency is less than ideal. In particular, when the key is new, there will be
# a failed search due to the initial use of getitem , and then a subse-
# quent insertion via setitem . For a concrete implementation, such as
# the UnsortedTableMap, this is twice the work because a complete scan
# of the table will take place during the failed getitem , and then an-
# other complete scan of the table takes place due to the implementation of
# setitem . A better solution is for the UnsortedTableMap class to over-
# ride setdefault to provide a direct solution that performs a single search.
# Give such an implementation of UnsortedTableMap.setdefault.
# C-10.29 Repeat Exercise C-10.28 for the ProbeHashMap class.
# C-10.30 Repeat Exercise C-10.28 for the ChainHashMap class.
# C-10.31 For an ideal compression function, the capacity of the bucket array for a
# hash table should be a prime number. Therefore, we consider the problem
# of locating a prime number in a range [M, 2M]. Implement a method for
# ﬁnding such a prime by using the sieve algorithm. In this algorithm, we
# allocate a 2M cell Boolean array A, such that cell i is associated with the
# integer i. We then initialize the array cells to all be “true” and we “mark
# off” all the cells that are multiples of 2, 3, 5, √
# 7, and so on. This process
# can stop after it reaches a number larger than 2M.
# √ (Hint: Consider a
# bootstrapping method for ﬁnding the primes up to 2M.)
# www.it-ebooks.info10.6. Exercises
# 455
# C-10.32 Perform experiments on our ChainHashMap and ProbeHashMap classes
# to measure its efﬁciency using random key sets and varying limits on the
# load factor (see Exercise R-10.15).
# C-10.33 Our implementation of separate chaining in ChainHashMap conserves
# memory by representing empty buckets in the table as None, rather than
# as empty instances of a secondary structure. Because many of these buck-
# ets will hold a single item, a better optimization is to have those slots of
# the table directly reference the Item instance, and to reserve use of sec-
# ondary containers for buckets that have two or more items. Modify our
# implementation to provide this additional optimization.
# C-10.34 Computing a hash code can be expensive, especially for lengthy keys. In
# our hash table implementations, we compute the hash code when ﬁrst in-
# serting an item, and recompute each item’s hash code each time we resize
# our table. Python’s dict class makes an interesting trade-off. The hash
# code is computed once, when an item is inserted, and the hash code is
# stored as an extra ﬁeld of the item composite, so that it need not be recom-
# puted. Reimplement our HashTableBase class to use such an approach.
# C-10.35 Describe how to perform a removal from a hash table that uses linear
# probing to resolve collisions where we do not use a special marker to
# represent deleted elements. That is, we must rearrange the contents so that
# it appears that the removed entry was never inserted in the ﬁrst place.
# C-10.36 The quadratic probing strategy has a clustering problem related to the way
# it looks for open slots. Namely, when a collision occurs at bucket h(k), it
# checks buckets A[(h(k) + i2 ) mod N], for i = 1, 2, . . . , N − 1.
# a. Show that i2 mod N will assume at most (N + 1)/2 distinct values,
# for N prime, as i ranges from 1 to N − 1. As a part of this justiﬁca-
# tion, note that i2 mod N = (N − i)2 mod N for all i.
# b. A better strategy is to choose a prime N such that N mod 4 = 3 and
# then to check the buckets A[(h(k) ± i2 ) mod N] as i ranges from 1
# to (N − 1)/2, alternating between plus and minus. Show that this
# alternate version is guaranteed to check every bucket in A.
# C-10.37 Refactor our ProbeHashMap design so that the sequence of secondary
# probes for collision resolution can be more easily customized. Demon-
# strate your new framework by providing separate concrete subclasses for
# linear probing and quadratic probing.
# C-10.38 Design a variation of binary search for performing the multimap opera-
# tion ﬁnd all(k) implemented with a sorted search table that includes du-
# plicates, and show that it runs in time O(s + log n), where n is the number
# of elements in the dictionary and s is the number of items with given key k.
# www.it-ebooks.info456
# Chapter 10. Maps, Hash Tables, and Skip Lists
# C-10.39 Although keys in a map are distinct, the binary search algorithm can be
# applied in a more general setting in which an array stores possibly duplica-
# tive elements in nondecreasing order. Consider the goal of identifying the
# index of the leftmost element with key greater than or equal to given k.
# Does the ﬁnd index method as given in Code Fragment 10.8 guarantee
# such a result? Does the ﬁnd index method as given in Exercise R-10.21
# guarantee such a result? Justify your answers.
# C-10.40 Suppose we are given two sorted search tables S and T , each with n entries
# (with S and T being implemented with arrays). Describe an O(log2 n)-
# time algorithm for ﬁnding the kth smallest key in the union of the keys
# from S and T (assuming no duplicates).
# C-10.41 Give an O(log n)-time solution for the previous problem.
# C-10.42 Suppose that each row of an n × n array A consists of 1’s and 0’s such that,
# in any row of A, all the 1’s come before any 0’s in that row. Assuming A
# is already in memory, describe a method running in O(n log n) time (not
# O(n2 ) time!) for counting the number of 1’s in A.
# C-10.43 Given a collection C of n cost-performance pairs (c, p), describe an algo-
# rithm for ﬁnding the maxima pairs of C in O(n log n) time.
# C-10.44 Show that the methods above(p) and prev(p) are not actually needed to
# efﬁciently implement a map using a skip list. That is, we can imple-
# ment insertions and deletions in a skip list using a strictly top-down, scan-
# forward approach, without ever using the above or prev methods. (Hint:
# In the insertion algorithm, ﬁrst repeatedly ﬂip the coin to determine the
# level where you should start inserting the new entry.)
# C-10.45 Describe how to modify a skip-list representation so that index-based
# operations, such as retrieving the item at index j, can be performed in
# O(log n) expected time.
# C-10.46 For sets S and T , the syntax S ˆ T returns a new set that is the symmet-
# ric difference, that is, a set of elements that are in precisely one of S or
# T . This syntax is supported by the special xor method. Provide an
# implementation of that method in the context of the MutableSet abstract
# base class, relying only on the ﬁve primary abstract methods of that class.
# C-10.47 In the context of the MutableSet abstract base class, describe a concrete
# implementation of the and method, which supports the syntax S & T
# for computing the intersection of two existing sets.
# C-10.48 An inverted ﬁle is a critical data structure for implementing a search en-
# gine or the index of a book. Given a document D, which can be viewed
# as an unordered, numbered list of words, an inverted ﬁle is an ordered list
# of words, L, such that, for each word w in L, we store the indices of the
# places in D where w appears. Design an efﬁcient algorithm for construct-
# ing L from D.
# www.it-ebooks.info10.6. Exercises
# 457
# C-10.49 Python’s collections module provides an OrderedDict class that is unre-
# lated to our sorted map abstraction. An OrderedDict is a subclass of the
# standard hash-based dict class that retains the expected O(1) performance
# for the primary map operations, but that also guarantees that the iter
# method reports items of the map according to ﬁrst-in, ﬁrst-out (FIFO)
# order. That is, the key that has been in the dictionary the longest is re-
# ported ﬁrst. (The order is unaffected when the value for an existing key
# is overwritten.) Describe an algorithmic approach for achieving such per-
# formance.
# Projects
# P-10.50 Perform a comparative analysis that studies the collision rates for various
# hash codes for character strings, such as various polynomial hash codes
# for different values of the parameter a. Use a hash table to determine
# collisions, but only count collisions where different strings map to the
# same hash code (not if they map to the same location in this hash table).
# Test these hash codes on text ﬁles found on the Internet.
# P-10.51 Perform a comparative analysis as in the previous exercise, but for 10-digit
# telephone numbers instead of character strings.
# P-10.52 Implement an OrderedDict class, as described in Exercise C-10.49, en-
# suring that the primary map operations run in O(1) expected time.
# P-10.53 Design a Python class that implements the skip-list data structure. Use
# this class to create a complete implementation of the sorted map ADT.
# P-10.54 Extend the previous project by providing a graphical animation of the
# skip-list operations. Visualize how entries move up the skip list during
# insertions and are linked out of the skip list during removals. Also, in a
# search operation, visualize the scan-forward and drop-down actions.
# P-10.55 Write a spell-checker class that stores a lexicon of words, W , in a Python
# set, and implements a method, check(s), which performs a spell check
# on the string s with respect to the set of words, W . If s is in W , then
# the call to check(s) returns a list containing only s, as it is assumed to
# be spelled correctly in this case. If s is not in W , then the call to check(s)
# returns a list of every word in W that might be a correct spelling of s. Your
# program should be able to handle all the common ways that s might be a
# misspelling of a word in W , including swapping adjacent characters in a
# word, inserting a single character in between two adjacent characters in a
# word, deleting a single character from a word, and replacing a character in
# a word with another character. For an extra challenge, consider phonetic
# substitutions as well.


## Arrays

import sys  # provides getsizeof function

# Initialize an empty list
data = []

# Set the value of n (for demonstration purposes, let's assume n = 10)
n = 10  # You can change this value as needed

for k in range(n):
    a = len(data)  # number of elements
    b = sys.getsizeof(data)  # actual size in bytes
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None)  # Append None to the list



import ctypes  # provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        # count actual elements
        self.n = 0
        # default array capacity
        self.capacity = 1
        # low-level array
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """Return number of elements stored in the array."""
        return self.n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self.n:
            raise IndexError("Invalid index")
        # retrieve from array
        return self.A[k]

    def append(self, obj):
        """Add object to end of the array."""
        # not enough room
        if self.n == self.capacity:
            # so double capacity
            self.resize(2 * self.capacity)
        
        self.A[self.n] = obj
        self.n += 1

    # Nonpublic utility
    def resize(self, c):
        """Resize internal array to capacity c."""
        # new (bigger) array
        B = self.make_array(c)
        
        # for each existing value
        for k in range(self.n):
            B[k] = self.A[k]
        
        # use the bigger array
        self.A = B
        self.capacity = c

    # Nonpublic utility
    def make_array(self, c):
        """Return new array with capacity c."""
        # see ctypes documentation
        return (c * ctypes.py_object)()  # Corrected syntax for creating an array

from time import time  # import time function from time module

def compute_average(n):
    """Perform n appends to an empty list and return average time elapsed."""
    data = []
    start = time()  # record the start time (in seconds)
    
    for k in range(n):
        data.append(None)
    
    end = time()  # record the end time (in seconds)
    
    return (end - start) / n  # return average time per append


class GameEntry:
    """Represents one entry of a list of high scores."""

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):
        """Return the name of the player."""
        return self.name

    def get_score(self):
        """Return the score of the player."""
        return self.score

    def __str__(self):
        """Return a string representation of the GameEntry."""
        return "({0}, {1})".format(self.name, self.score)  # e.g., (Bob, 98)


class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity.
        
        All entries are initially None.
        """
        # Reserve space for future scores
        self.board = [None] * capacity  # Corrected to use multiplication for list initialization
        # Number of actual entries
        self.n = 0

    def __getitem__(self, k):
        """Return entry at index k."""
        return self.board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        return "\n".join(str(self.board[j]) for j in range(self.n))

    def add(self, entry):
        """Consider adding entry to high scores."""
        score = entry.get_score()  # Corrected method name

        # Does new entry qualify as a high score?
        # Answer is yes if board not full or score is higher than last entry
        good = self.n < len(self.board) or score > self.board[-1].get_score()  # Corrected negative indexing

        if good:
            # No score drops from list
            if self.n < len(self.board):
                # So overall number increases
                self.n += 1
            
            # Shift lower scores rightward to make room for new entry
            j = self.n - 1
            while j > 0 and self.board[j - 1].get_score() < score:  # Corrected indexing
                # Shift entry from j-1 to j
                self.board[j] = self.board[j - 1]
                j -= 1  # Decrement j
            
            # When done, add new entry
            self.board[j] = entry


def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):  # from 1 to n-1
        cur = A[k]  # current element to be inserted
        j = k  # find correct index j for current
        
        while j > 0 and A[j - 1] > cur:  # element A[j-1] must be after current
            A[j] = A[j - 1]
            j -= 1  # decrement j
        
        A[j] = cur  # insert current element at the correct position


class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        # Temp array for encryption
        encoder = [None] * 26  # Corrected to use multiplication for list initialization
        # Temp array for decryption
        decoder = [None] * 26
        
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))  # Use single quotes for 'A'
            decoder[k] = chr((k - shift) % 26 + ord('A'))  # Use single quotes for 'A'
        
        # Will store as string
        self.forward = ''.join(encoder)  # Corrected to use join method properly
        self.backward = ''.join(decoder)

    def encrypt(self, message):
        """Return string representing encrypted message."""
        return self.transform(message, self.forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self.transform(secret, self.backward)

    def transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original)
        
        for k in range(len(msg)):
            if msg[k].isupper():
                # Index from 0 to 25
                j = ord(msg[k]) - ord('A')  # Use single quotes for 'A'
                msg[k] = code[j]  # Replace this character
        
        return ''.join(msg)  # Corrected to use join method properly

cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
coded = cipher.encrypt(message)
print("Secret:", coded)  # Fixed print statement formatting
answer = cipher.decrypt(coded)
print("Message:", answer)  # Fixed print statement formatting


class TicTacToe:
    """Management of a Tic-Tac-Toe game (does not do strategy)."""

    def __init__(self):
        """Start a new game."""
        self.board = [[' ' for j in range(3)] for i in range(3)]  # Corrected to initialize a 3x3 board
        self.player = 'X'  # Use strings for player marks

    def mark(self, i, j):
        """Put an X or O mark at position (i,j) for next player's turn."""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid board position")
        if self.board[i][j] != ' ':
            raise ValueError("Board position occupied")
        if self.winner() is not None:
            raise ValueError("Game is already complete")
        
        self.board[i][j] = self.player
        
        # Switch players
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def is_win(self, mark):
        """Check whether the board configuration is a win for the given player."""
        board = self.board  # Local variable for shorthand
        return (mark == board[0][0] == board[0][1] == board[0][2] or  # Row 0
                mark == board[1][0] == board[1][1] == board[1][2] or  # Row 1
                mark == board[2][0] == board[2][1] == board[2][2] or  # Row 2
                mark == board[0][0] == board[1][0] == board[2][0] or  # Column 0
                mark == board[0][1] == board[1][1] == board[2][1] or  # Column 1
                mark == board[0][2] == board[1][2] == board[2][2] or  # Column 2
                mark == board[0][0] == board[1][1] == board[2][2] or  # Diagonal
                mark == board[0][2] == board[1][1] == board[2][0])    # Reverse diagonal

    def winner(self):
        """Return mark of winning player, or None to indicate a tie."""
        for mark in ['X', 'O']:
            if self.is_win(mark):
                return mark
        return None

    def __str__(self):
        """Return string representation of current game board."""
        rows = [' | '.join(self.board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)



"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

#https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_index = 0

        # move all non zero elements to the front of the array
        for i, x in enumerate(nums):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1

        # fill remaining positions with zeros
        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0
            
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow+1

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
        
        return max_profit

"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""     
#https://leetcode.com/problems/rotate-array/  
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n 

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n-1)
        reverse(0, k -1)
        reverse(k, n-1)

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""
#https://leetcode.com/problems/product-of-array-except-self/description/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        output = [1] * length

        prefix_product = 1
        for i in range(length):
            output[i] = prefix_product
            prefix_product *= nums[i]
        
        suffix_product = 1
        for i in range(length-1, -1, -1):
            output[i] *= suffix_product
            suffix_product *= nums[i]

        return output
    
"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

"""
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
        
        return total_profit
            
            
            
"""
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
Example 3:

Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.

"""
#https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total_count = 0
        current_zeros = 0
        
        for num in nums:
            if num == 0:
                current_zeros += 1  # Increment count of consecutive zeros
            else:
                # If we encounter a non-zero, calculate subarrays from current zeros
                if current_zeros > 0:
                    total_count += (current_zeros * (current_zeros + 1)) // 2
                    current_zeros = 0  # Reset for next sequence of zeros

        # Handle case where the array ends with zeros
        if current_zeros > 0:
            total_count += (current_zeros * (current_zeros + 1)) // 2
        
        return total_count


"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

"""
#https://leetcode.com/problems/increasing-triplet-subsequence/description/
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False

"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

"""
#https://leetcode.com/problems/first-missing-positive/description/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
            
        return n + 1
    
"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        
        return ans


"""
Given a positive integer n, write a function that returns the number of 
set bits
 in its binary representation (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

Example 3:

Input: n = 2147483645

Output: 30

Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

 

Constraints:

1 <= n <= 231 - 1
 

Follow up: If this function is called many times, how would you optimize it?
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
        
            n >>= 1
        return count
    

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
    

"""
Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 

Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 

Constraints:

The input must be a binary string of length 32
 

Follow up: If this function is called many times, how would you optimize it?
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1
            result |= (n & 1)
            n >>= 1
        return result
    
"""
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
 

Constraints:

0 <= left <= right <= 231 - 1
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
        

"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
 

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_result = 0
        for num in nums:
            xor_result ^= num
        set_bit = xor_result & -xor_result
        num1, num2 = 0,0
        for num in nums:
            if num & set_bit:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000

"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            sum_without_carry = a ^ b
            carry = (a & b) << 1
            a = sum_without_carry
            b = carry
        return a
    
# R-5.1 Execute the experiment from Code Fragment 5.1 and compare the results
# on your system to those we report in Code Fragment 5.2.
# R-5.2 In Code Fragment 5.1, we perform an experiment to compare the length of
# a Python list to its underlying memory usage. Determining the sequence
# of array sizes requires a manual inspection of the output of that program.
# Redesign the experiment so that the program outputs only those values of
# k at which the existing capacity is exhausted. For example, on a system
# consistent with the results of Code Fragment 5.2, your program should
# output that the sequence of array capacities are 0, 4, 8, 16, 25, . . . .
# R-5.3 Modify the experiment from Code Fragment 5.1 in order to demonstrate
# that Python’s list class occasionally shrinks the size of its underlying array
# when elements are popped from a list.
# R-5.4 Our DynamicArray class, as given in Code Fragment 5.3, does not support
# use of negative indices with getitem . Update that method to better
# match the semantics of a Python list.
# R-5.5 Redo the justiﬁcation of Proposition 5.1 assuming that the the cost of
# growing the array from size k to size 2k is 3k cyber-dollars. How much
# should each append operation be charged to make the amortization work?
# R-5.6 Our implementation of insert for the DynamicArray class, as given in
# Code Fragment 5.5, has the following inefﬁciency. In the case when a re-
# size occurs, the resize operation takes time to copy all the elements from
# an old array to a new array, and then the subsequent loop in the body of
# insert shifts many of those elements. Give an improved implementation
# of the insert method, so that, in the case of a resize, the elements are
# shifted into their ﬁnal position during that operation, thereby avoiding the
# subsequent shifting.
# R-5.7 Let A be an array of size n ≥ 2 containing integers from 1 to n − 1, inclu-
# sive, with exactly one repeated. Describe a fast algorithm for ﬁnding the
# integer in A that is repeated.
# R-5.8 Experimentally evaluate the efﬁciency of the pop method of Python’s list
# class when using varying indices as a parameter, as we did for insert on
# page 205. Report your results akin to Table 5.5.
# www.it-ebooks.info5.7. Exercises
# 225
# R-5.9 Explain the changes that would have to be made to the program of Code
# Fragment 5.11 so that it could perform the Caesar cipher for messages
# that are written in an alphabet-based language other than English, such as
# Greek, Russian, or Hebrew.
# R-5.10 The constructor for the CaesarCipher class in Code Fragment 5.11 can
# be implemented with a two-line body by building the forward and back-
# ward strings using a combination of the join method and an appropriate
# comprehension syntax. Give such an implementation.
# R-5.11 Use standard control structures to compute the sum of all numbers in an
# n × n data set, represented as a list of lists.
# R-5.12 Describe how the built-in sum function can be combined with Python’s
# comprehension syntax to compute the sum of all numbers in an n × n data
# set, represented as a list of lists.
# Creativity
# C-5.13 In the experiment of Code Fragment 5.1, we begin with an empty list. If
# data were initially constructed with nonempty length, does this affect the
# sequence of values at which the underlying array is expanded? Perform
# your own experiments, and comment on any relationship you see between
# the initial length and the expansion sequence.
# C-5.14 The shuﬄe method, supported by the random module, takes a Python
# list and rearranges it so that every possible ordering is equally likely.
# Implement your own version of such a function. You may rely on the
# randrange(n) function of the random module, which returns a random
# number between 0 and n − 1 inclusive.
# C-5.15 Consider an implementation of a dynamic array, but instead of copying
# the elements into an array of double the size (that is, from N to 2N) when
# its capacity is reached, we copy the elements into an array with N/4
# additional cells, going from capacity N to capacity N + N/4. Prove that
# performing a sequence of n append operations still runs in O(n) time in
# this case.
# C-5.16 Implement a pop method for the DynamicArray class, given in Code Frag-
# ment 5.3, that removes the last element of the array, and that shrinks the
# capacity, N, of the array by half any time the number of elements in the
# array goes below N/4.
# C-5.17 Prove that when using a dynamic array that grows and shrinks as in the
# previous exercise, the following series of 2n operations takes O(n) time:
# n append operations on an initially empty array, followed by n pop oper-
# ations.
# www.it-ebooks.info226
# Chapter 5. Array-Based Sequences
# C-5.18 Give a formal proof that any sequence of n append or pop operations on
# an initially empty dynamic array takes O(n) time, if using the strategy
# described in Exercise C-5.16.
# C-5.19 Consider a variant of Exercise C-5.16, in which an array of capacity N is
# resized to capacity precisely that of the number of elements, any time the
# number of elements in the array goes strictly below N/4. Give a formal
# proof that any sequence of n append or pop operations on an initially
# empty dynamic array takes O(n) time.
# C-5.20 Consider a variant of Exercise C-5.16, in which an array of capacity N, is
# resized to capacity precisely that of the number of elements, any time the
# number of elements in the array goes strictly below N/2. Show that there
# exists a sequence of n operations that requires Ω(n2 ) time to execute.
# C-5.21 In Section 5.4.2, we described four different ways to compose a long
# string: (1) repeated concatenation, (2) appending to a temporary list and
# then joining, (3) using list comprehension with join, and (4) using genera-
# tor comprehension with join. Develop an experiment to test the efﬁciency
# of all four of these approaches and report your ﬁndings.
# C-5.22 Develop an experiment to compare the relative efﬁciency of the extend
# method of Python’s list class versus using repeated calls to append to
# accomplish the equivalent task.
# C-5.23 Based on the discussion of page 207, develop an experiment to compare
# the efﬁciency of Python’s list comprehension syntax versus the construc-
# tion of a list by means of repeated calls to append.
# C-5.24 Perform experiments to evaluate the efﬁciency of the remove method of
# Python’s list class, as we did for insert on page 205. Use known values so
# that all removals occur either at the beginning, middle, or end of the list.
# Report your results akin to Table 5.5.
# C-5.25 The syntax data.remove(value) for Python list data removes only the ﬁrst
# occurrence of element value from the list. Give an implementation of a
# function, with signature remove all(data, value), that removes all occur-
# rences of value from the given list, such that the worst-case running time
# of the function is O(n) on a list with n elements. Not that it is not efﬁcient
# enough in general to rely on repeated calls to remove.
# C-5.26 Let B be an array of size n ≥ 6 containing integers from 1 to n − 5, inclu-
# sive, with exactly ﬁve repeated. Describe a good algorithm for ﬁnding the
# ﬁve integers in B that are repeated.
# C-5.27 Given a Python list L of n positive integers, each represented with k =
# log n + 1 bits, describe an O(n)-time method for ﬁnding a k-bit integer
# not in L.
# C-5.28 Argue why any solution to the previous problem must run in Ω(n) time.
# www.it-ebooks.infoChapter Notes
# 227
# C-5.29 A useful operation in databases is the natural join. If we view a database
# as a list of ordered pairs of objects, then the natural join of databases A
# and B is the list of all ordered triples (x, y, z) such that the pair (x, y) is in
# A and the pair (y, z) is in B. Describe and analyze an efﬁcient algorithm
# for computing the natural join of a list A of n pairs and a list B of m pairs.
# C-5.30 When Bob wants to send Alice a message M on the Internet, he breaks M
# into n data packets, numbers the packets consecutively, and injects them
# into the network. When the packets arrive at Alice’s computer, they may
# be out of order, so Alice must assemble the sequence of n packets in order
# before she can be sure she has the entire message. Describe an efﬁcient
# scheme for Alice to do this, assuming that she knows the value of n. What
# is the running time of this algorithm?
# C-5.31 Describe a way to use recursion to add all the numbers in an n × n data
# set, represented as a list of lists.
# Projects
# P-5.32 Write a Python function that takes two three-dimensional numeric data
# sets and adds them componentwise.
# P-5.33 Write a Python program for a matrix class that can add and multiply two-
# dimensional arrays of numbers, assuming the dimensions agree appropri-
# ately for the operation.
# P-5.34 Write a program that can perform the Caesar cipher for English messages
# that include both upper- and lowercase characters.
# P-5.35 Implement a class, SubstitutionCipher, with a constructor that takes a
# string with the 26 uppercase letters in an arbitrary order and uses that for
# the forward mapping for encryption (akin to the self. forward string in
# our CaesarCipher class of Code Fragment 5.11). You should derive the
# backward mapping from the forward version.
# P-5.36 Redesign the CaesarCipher class as a subclass of the SubstitutionCipher
# from the previous problem.
# P-5.37 Design a RandomCipher class as a subclass of the SubstitutionCipher
# from Exercise P-5.35, so that each instance of the class relies on a random
# permutation of letters for its mapping.



## RECURSION
def factorial(n):
    """Return the factorial of n, an integer >= 0."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # Corrected to use the multiplication operator

def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)."""
    line = '-' * tick_length  # Create a line of dashes based on tick length
    if tick_label:
        line += ' ' + tick_label  # Add the tick label if provided
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    # Stop when length drops to 0
    if center_length > 0:
        # Recursively draw top ticks
        draw_interval(center_length - 1)
        # Draw center tick
        draw_line(center_length)
        # Recursively draw bottom ticks
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    """Draw an English ruler with given number of inches and major tick length."""
    # Draw inch 0 line
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        # Draw interior ticks for inch
        draw_interval(major_length - 1)
        # Draw inch j line and label
        draw_line(major_length, str(j))

# Example usage:
draw_ruler(3, 5)  # Draw a ruler with 3 inches and major ticks of length 5


def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        return False  # Interval is empty; no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            # Found a match
            return True
        elif target < data[mid]:
            # Recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)  # Corrected subtraction operator
        else:
            # Recur on the portion right of the middle
            return binary_search(data, target, mid + 1, high)



import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendants."""
    total = os.path.getsize(path)  # Account for direct usage
    
    if os.path.isdir(path):
        # If this is a directory,
        for filename in os.listdir(path):
            # Then for each child:
            childpath = os.path.join(path, filename)  # Compose full path to child
            # Add child's usage to total
            total += disk_usage(childpath)  # Corrected function name to use underscore

    # Descriptive output (optional)
    print("{0:<7} {1}".format(total, path))  # Fixed formatting
    return total

# Example usage (uncomment to test)
# print(disk_usage('/path/to/directory'))

def unique3(S, start, stop):
    """Return True if there are no duplicate elements in slice S[start:stop]."""
    if stop - start <= 1:
        return True  # At most one item
    elif not unique3(S, start, stop - 1):
        return False  # First part has duplicate
    elif not unique3(S, start + 1, stop):
        return False  # Second part has duplicate
    else:
        return S[start] != S[stop - 1]  # Check if the first and last elements are different


def good_fibonacci(n):
    """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)

def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]  # Corrected function name and spacing


def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]."""
    if start < stop - 1:  # If at least 2 elements:
        # Swap first and last
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)  # Recur for the next pair


def power(x, n):
    """Compute the value x^n for integer n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)  # Corrected to use the multiplication operator


def partial_power(x, n):
    """Compute the value x^n for integer n."""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)  # Rely on truncated division
        result = partial * partial  # Corrected to use multiplication operator
        if n % 2 == 1:
            # If n is odd, include extra factor of x
            result *= x  # Multiply by x for odd n
        return result

def binary_sum(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start:stop]."""
    if start >= stop:
        # Zero elements in slice
        return 0
    elif start == stop - 1:
        # One element in slice
        return S[start]
    else:
        # Two or more elements in slice
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)  # Corrected function name


def binary_search_iterative(data, target):
    """Return True if target is found in the given Python list."""
    low = 0
    high = len(data) - 1  # Corrected to use standard minus sign

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            # Found a match
            return True
        elif target < data[mid]:
            high = mid - 1  # Corrected to use standard minus sign
            # Only consider values left of mid
        else:
            low = mid + 1  # Only consider values right of mid

    return False


def reverse_iterative(S):
    """Reverse elements in sequence S."""
    start, stop = 0, len(S)
    
    while start < stop - 1:  # Corrected to use standard minus sign
        S[start], S[stop - 1] = S[stop - 1], S[start]  # Corrected to use standard minus sign
        start, stop = start + 1, stop - 1  # Corrected to use standard minus sign


# R-4.1 Describe a recursive algorithm for ﬁnding the maximum element in a se-
# quence, S, of n elements. What is your running time and space usage?
# R-4.2 Draw the recursion trace for the computation of power(2, 5), using the
# traditional function implemented in Code Fragment 4.11.
# R-4.3 Draw the recursion trace for the computation of power(2, 18), using the
# repeated squaring algorithm, as implemented in Code Fragment 4.12.
# R-4.4 Draw the recursion trace for the execution of function reverse(S, 0, 5)
# (Code Fragment 4.10) on S = [4, 3, 6, 2, 6].
# R-4.5 Draw the recursion trace for the execution of function PuzzleSolve(3, S,U )
# (Code Fragment 4.14), where S is empty and U = {a, b, c, d}.
# R-4.6 Describe a recursive function for computing the nth Harmonic number,
# Hn = ∑ni=1 1/i.
# R-4.7 Describe a recursive function for converting a string of digits into the in-
# teger it represents. For example, 13531 represents the integer 13, 531.
# R-4.8 Isabel has an interesting way of summing up the values in a sequence A of
# n integers, where n is a power of two. She creates a new sequence B of half
# the size of A and sets B[i] = A[2i] + A[2i + 1], for i = 0, 1, . . . , (n/2) − 1. If
# B has size 1, then she outputs B[0]. Otherwise, she replaces A with B, and
# repeats the process. What is the running time of her algorithm?
# Creativity
# C-4.9 Write a short recursive Python function that ﬁnds the minimum and max-
# imum values in a sequence without using any loops.
# C-4.10 Describe a recursive algorithm to compute the integer part of the base-two
# logarithm of n using only addition and integer division.
# C-4.11 Describe an efﬁcient recursive function for solving the element unique-
# ness problem, which runs in time that is at most O(n2 ) in the worst case
# without using sorting.
# C-4.12 Give a recursive algorithm to compute the product of two positive integers,
# m and n, using only addition and subtraction.
# www.it-ebooks.info4.7. Exercises
# 181
# C-4.13 In Section 4.2 we prove by induction that the number of lines printed by
# a call to draw interval(c) is 2c − 1. Another interesting question is how
# many dashes are printed during that process. Prove by induction that the
# number of dashes printed by draw interval(c) is 2c+1 − c − 2.
# C-4.14 In the Towers of Hanoi puzzle, we are given a platform with three pegs, a,
# b, and c, sticking out of it. On peg a is a stack of n disks, each larger than
# the next, so that the smallest is on the top and the largest is on the bottom.
# The puzzle is to move all the disks from peg a to peg c, moving one disk
# at a time, so that we never place a larger disk on top of a smaller one.
# See Figure 4.15 for an example of the case n = 4. Describe a recursive
# algorithm for solving the Towers of Hanoi puzzle for arbitrary n. (Hint:
# Consider ﬁrst the subproblem of moving all but the nth disk from peg a to
# another peg using the third as “temporary storage.”)
# Figure 4.15: An illustration of the Towers of Hanoi puzzle.
# C-4.15 Write a recursive function that will output all the subsets of a set of n
# elements (without repeating any subsets).
# C-4.16 Write a short recursive Python function that takes a character string s and
# outputs its reverse. For example, the reverse of pots&pans would be
# snap&stop .
# C-4.17 Write a short recursive Python function that determines if a string s is a
# palindrome, that is, it is equal to its reverse. For example, racecar and
# gohangasalamiimalasagnahog are palindromes.
# C-4.18 Use recursion to write a Python function for determining if a string s has
# more vowels than consonants.
# C-4.19 Write a short recursive Python function that rearranges a sequence of in-
# teger values so that all the even values appear before all the odd values.
# C-4.20 Given an unsorted sequence, S, of integers and an integer k, describe a
# recursive algorithm for rearranging the elements in S so that all elements
# less than or equal to k come before any elements larger than k. What is
# the running time of your algorithm on a sequence of n values?
# www.it-ebooks.infoChapter 4. Recursion
# 182
# C-4.21 Suppose you are given an n-element sequence, S, containing distinct in-
# tegers that are listed in increasing order. Given a number k, describe a
# recursive algorithm to ﬁnd two integers in S that sum to k, if such a pair
# exists. What is the running time of your algorithm?
# C-4.22 Develop a nonrecursive implementation of the version of power from
# Code Fragment 4.12 that uses repeated squaring.
# Projects
# P-4.23 Implement a recursive function with signature ﬁnd(path, ﬁlename) that
# reports all entries of the ﬁle system rooted at the given path having the
# given ﬁle name.
# P-4.24 Write a program for solving summation puzzles by enumerating and test-
# ing all possible conﬁgurations. Using your program, solve the three puz-
# zles given in Section 4.4.3.
# P-4.25 Provide a nonrecursive implementation of the draw interval function for
# the English ruler project of Section 4.1.2. There should be precisely 2c − 1
# lines of output if c represents the length of the center tick. If incrementing
# a counter from 0 to 2c − 2, the number of dashes for each tick line should
# be exactly one more than the number of consecutive 1’s at the end of the
# binary representation of the counter.
# P-4.26 Write a program that can solve instances of the Tower of Hanoi problem
# (from Exercise C-4.14).
# P-4.27 Python’s os module provides a function with signature walk(path) that
# is a generator yielding the tuple (dirpath, dirnames, ﬁlenames) for each
# subdirectory of the directory identiﬁed by string path, such that string
# dirpath is the full path to the subdirectory, dirnames is a list of the names
# of the subdirectories within dirpath, and ﬁlenames is a list of the names
# of non-directory entries of dirpath. For example, when visiting the cs016
# subdirectory of the ﬁle system shown in Figure 4.6, the walk would yield
# ( /user/rt/courses/cs016 , [ homeworks , programs ], [ grades ]).
# Give your own implementation of such a walk function.


## SEARCH TREES
class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree."""

    # ---------------------------- override Position class ----------------------------
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """Return key of map's key-value pair."""
            return self.element().key()

        def value(self):
            """Return value of map's key-value pair."""
            return self.element().value()

    # ------------------------------- nonpublic utilities -------------------------------
    def subtree_search(self, p, k):
        """Return Position of p's subtree having key k, or last node searched."""
        if k == p.key():
            # Found match
            return p
        elif k < p.key():
            # Search left subtree
            if self.left(p) is not None:
                return self.subtree_search(self.left(p), k)
        else:
            # Search right subtree
            if self.right(p) is not None:
                return self.subtree_search(self.right(p), k)
        
        return p  # Unsuccessful search

    def subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p."""
        walk = p
        while self.left(walk) is not None:
            # Keep walking left
            walk = self.left(walk)
        return walk

    def subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p."""
        walk = p
        while self.right(walk) is not None:
            # Keep walking right
            walk = self.right(walk)
        return walk

    def first(self):
        """Return the first Position in the tree (or None if empty)."""
        return self.subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last Position in the tree (or None if empty)."""
        return self.subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Return the Position just before p in the natural order.
        Return None if p is the first position.
        """
        # Validate position
        self.validate(p)
        
        if self.left(p):
            return self.subtree_last_position(self.left(p))
        else:
            # Walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the Position just after p in the natural order.
        Return None if p is the last position.
        """
        # Symmetric to before(p)
        if self.right(p):
            return self.subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """Return position with key k, or else neighbor (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self.subtree_search(self.root(), k)
            # Hook for balanced tree subclasses
            self.rebalance_access(p)
            return p

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k.
        Return None if there does not exist such a key.
        """
        if self.is_empty():
            return None
        else:
            # May not find exact match
            p = self.find_position(k)
            if p.key() < k:
                # p’s key is too small
                p = self.after(p)
                
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through maximum key of map.
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                # We initialize p with logic similar to find_ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)

            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        if self.is_empty():
            raise KeyError(f"Key Error: {repr(k)}")
        
        else:
            p = self.subtree_search(self.root(), k)
            # Hook for balanced tree subclasses
            self.rebalance_access(p)

            if k != p.key():
                raise KeyError(f"Key Error: {repr(k)}")
            
            return p.value()

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        if self.is_empty():
            # From LinkedBinaryTree
            leaf = self.add_root(self.Item(k, v))
            
        else:
            p = self.subtree_search(self.root(), k)

            if p.key() == k:
                # Replace existing item’s value
                p.element().value = v
                
                # Hook for balanced tree subclasses
                self.rebalance_access(p)
                
                return
            
            item = self.Item(k, v)

            if p.key() < k:
                leaf = self.add_right(p, item)  # Inherited from LinkedBinaryTree
            else:
                leaf = self.add_left(p, item)  # Inherited from LinkedBinaryTree
            
            # Hook for balanced tree subclasses
            self.rebalance_insert(leaf)

    def __iter__(self):
        """Generate an iteration of all keys in the map in order."""
        p = self.first()
        
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove the item at given Position."""
        
        # Inherited from LinkedBinaryTree
        self.validate(p)

        if self.left(p) and self.right(p):
            # P has two children
            replacement = self.subtree_last_position(self.left(p))
            
            # From LinkedBinaryTree
            self.replace(p, replacement.element())
            
            p = replacement
        
        # Now P has at most one child
        parent = self.parent(p)

         # Inherited from LinkedBinaryTree
         # Delete node P 
         # If root deleted, parent is None 
        super().delete(p)  
         
        # Rebalance tree after deletion 
        self.rebalance_delete(parent)

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self.subtree_search(self.root(), k)

            if k == p.key():
                # rely on positional version 
                self.delete(p)  
                return  
            
        raise KeyError(f"Key Error: {repr(k)}")


    def relink(self, parent, child, make_left_child):
        """Relink parent node with child node (we allow child to be None)."""
        # Make it a left child
        if make_left_child:
            parent.left = child
        else:
            # Make it a right child
            parent.right = child
        
        if child is not None:
            # Make child point to parent
            child.parent = parent

    def rotate(self, p):
        """Rotate Position p above its parent."""
        x = p.node  # The node at position p
        y = x.parent  # Parent of x (assumed to exist)
        z = y.parent  # Grandparent of x (possibly None)

        if z is None:
            # x becomes root
            self.root = x
            x.parent = None
        else:
            # x becomes a direct child of z
            self.relink(z, x, y == z.left)

        # Now rotate x and y, including transfer of middle subtree
        if x == y.left:
            # x's right becomes left child of y
            self.relink(y, x.right, True)
            # y becomes right child of x
            self.relink(x, y, False)
        else:
            # x's left becomes right child of y
            self.relink(y, x.left, False)
            # y becomes left child of x
            self.relink(x, y, True)

    def restructure(self, x):
        """Perform trinode restructure of Position x with parent/grandparent."""
        y = self.parent(x)  # Parent of x
        z = self.parent(y)  # Grandparent of y

        if (x == self.right(y)) == (y == self.right(z)):  # Matching alignments
            # Single rotation (of y)
            self.rotate(y)
            return y  # y is new subtree root
        else:
            # Opposite alignments: double rotation (of x)
            self.rotate(x)
            self.rotate(x)
            return x  # x is new subtree root


class AVLTreeMap(TreeMap):
    """Sorted map implementation using an AVL tree."""

    # -------------------------- nested Node class --------------------------
    class Node(TreeMap.Node):
        """Node class for AVL maintains height value for balancing."""
        __slots__ = '_height'  # Additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            # Height will be recomputed during balancing
            self.height = 0

    # ------------------------- positional-based utility methods -------------------------
    def recompute_height(self, p):
        """Recompute the height of the node at position p."""
        p.node.height = 1 + max(p.node.left_height(), p.node.right_height())

    def is_balanced(self, p):
        """Check if the subtree rooted at position p is balanced."""
        return abs(p.node.left_height() - p.node.right_height()) <= 1

    def tall_child(self, p, favor_left=False):  # Parameter controls tiebreaker
        """Return the taller child of position p."""
        if p.node.left_height() + (1 if favor_left else 0) > p.node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def tall_grandchild(self, p):
        """Return the taller grandchild of position p."""
        child = self.tall_child(p)
        # If child is on left, favor left grandchild; else favor right grandchild
        alignment = (child == self.left(p))
        return self.tall_child(child, alignment)

    def rebalance(self, p):
        """Rebalance the subtree rooted at position p."""
        while p is not None:
            old_height = p.node.height
            # Imbalance detected!
            if not self.is_balanced(p):
                # Perform trinode restructuring and set p to resulting root,
                # and recompute new local heights after the restructuring
                p = self.restructure(self.tall_grandchild(p))
                self.recompute_height(self.left(p))
                self.recompute_height(self.right(p))
                # Adjust for recent changes
                self.recompute_height(p)
            
            # Has height changed?
            if p.node.height == old_height:
                break  # No further changes needed
            else:
                p = self.parent(p)  # Repeat with parent

    # ---------------------------- override balancing hooks ----------------------------
    def rebalance_insert(self, p):
        """Override insert hook to rebalance after insertion."""
        self.rebalance(p)

    def rebalance_delete(self, p):
        """Override delete hook to rebalance after deletion."""
        self.rebalance(p)

class SplayTreeMap(TreeMap):
    """Sorted map implementation using a splay tree."""

    # --------------------------------- splay operation --------------------------------
    def splay(self, p):
        """Splay the node at position p to the root of the tree."""
        while p != self.root():
            parent = self.parent(p)
            grand = self.parent(parent)
            if grand is None:
                # Zig case
                self.rotate(p)
            elif (parent == self.left(grand)) == (p == self.left(parent)):
                # Zig-zig case
                # Move PARENT up
                self.rotate(parent)
                # Then move p up
                self.rotate(p)
            else:
                # Zig-zag case
                # Move p up
                self.rotate(p)
                # Move p up again
                self.rotate(p)

    # ---------------------------- override balancing hooks ----------------------------
    def rebalance_insert(self, p):
        """Override insert hook to splay after insertion."""
        self.splay(p)

    def rebalance_delete(self, p):
        """Override delete hook to splay after deletion."""
        if p is not None:
            self.splay(p)

    def rebalance_access(self, p):
        """Override access hook to splay after access."""
        self.splay(p)


class RedBlackTreeMap(TreeMap):
    """Sorted map implementation using a red-black tree."""

    class Node(TreeMap.Node):
        """Node class for red-black tree maintains bit that denotes color."""
        __slots__ = '_red'  # Add additional data member to the Node class

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            # New node is red by default
            self.red = True

    # ------------------------- positional-based utility methods -------------------------
    # We consider a nonexistent child to be trivially black
    def set_red(self, p):
        """Set the color of node p to red."""
        p.node.red = True

    def set_black(self, p):
        """Set the color of node p to black."""
        p.node.red = False

    def set_color(self, p, make_red):
        """Set the color of node p based on make_red flag."""
        p.node.red = make_red

    def is_red(self, p):
        """Check if node p is red."""
        return p is not None and p.node.red

    def is_red_leaf(self, p):
        """Check if node p is a red leaf."""
        return self.is_red(p) and self.is_leaf(p)

    def get_red_child(self, p):
        """Return a red child of p (or None if no such child)."""
        for child in (self.left(p), self.right(p)):
            if self.is_red(child):
                return child
        return None

    # ------------------------- support for insertions -------------------------
    def rebalance_insert(self, p):
        """Rebalance after insertion. New node is always red."""
        self.resolve_red(p)

    def resolve_red(self, p):
        """Resolve any red violations after insertion."""
        if self.is_root(p):
            self.set_black(p)
        else:
            parent = self.parent(p)
            if self.is_red(parent):
                uncle = self.sibling(parent)
                if not self.is_red(uncle):
                    middle = self.restructure(p)
                    self.set_black(middle)
                    self.set_red(self.left(middle))
                    self.set_red(self.right(middle))
                else:
                    grand = self.parent(parent)
                    self.set_red(grand)
                    self.set_black(self.left(grand))
                    self.set_black(self.right(grand))
                    self.resolve_red(grand)

    # ------------------------- support for deletions -------------------------
    def rebalance_delete(self, p):
        """Rebalance after deletion."""
        if len(self) == 1:
            # Special case: ensure that root is black
            self.set_black(self.root())
        elif p is not None:
            n = self.num_children(p)
            if n == 1:
                # Deficit exists unless child is a red leaf
                c = next(self.children(p))
                if not self.is_red_leaf(c):
                    self.fix_deficit(p, c)
            elif n == 2:
                # Removed black node with red child
                if self.is_red_leaf(self.left(p)):
                    self.set_black(self.left(p))
                else:
                    self.set_black(self.right(p))

    def fix_deficit(self, z, y):
        """Resolve black deficit at z, where y is the root of z's heavier subtree."""
        if not self.is_red(y):  # y is black; will apply Case 1 or 2
            x = self.get_red_child(y)
            if x is not None:  # Case 1: y is black and has red child x; do "transfer"
                old_color = self.is_red(z)
                middle = self.restructure(x)
                # middle gets old color of z
                self.set_color(middle, old_color)
                # Children become black
                self.set_black(self.left(middle))
                self.set_black(self.right(middle))
            else:  # Case 2: y is black but no red children; recolor as "fusion"
                self.set_red(y)
                if self.is_red(z):
                    # This resolves the problem
                    self.set_black(z)
                elif not self.is_root(z):
                    self.fix_deficit(self.parent(z), self.sibling(z))  # Recur upward
        else:  # Case 3: y is red; rotate misaligned 3-node and repeat
            self.rotate(y)
            self.set_black(y)
            self.set_red(z)
            if z == self.right(y):
                self.fix_deficit(z, self.left(z))
            else:
                self.fix_deficit(z, self.right(z))



# R-11.1 If we insert the entries (1, A), (2, B), (3,C), (4, D), and (5, E), in this order,
# into an initially empty binary search tree, what will it look like?
# R-11.2 Insert, into an empty binary search tree, entries with keys 30, 40, 24, 58,
# 48, 26, 11, 13 (in this order). Draw the tree after each insertion.
# R-11.3 How many different binary search trees can store the keys {1, 2, 3}?
# R-11.4 Dr. Amongus claims that the order in which a ﬁxed set of entries is inserted
# into a binary search tree does not matter—the same tree results every time.
# Give a small example that proves he is wrong.
# R-11.5 Dr. Amongus claims that the order in which a ﬁxed set of entries is inserted
# into an AVL tree does not matter—the same AVL tree results every time.
# Give a small example that proves he is wrong.
# R-11.6 Our implementation of the TreeMap. subtree search utility, from Code
# Fragment 11.4, relies on recursion. For a large unbalanced tree, Python’s
# default limit on recursive depth may be prohibitive. Give an alternative
# implementation of that method that does not rely on the use of recursion.
# R-11.7 Do the trinode restructurings in Figures 11.12 and 11.14 result in single
# or double rotations?
# R-11.8 Draw the AVL tree resulting from the insertion of an entry with key 52
# into the AVL tree of Figure 11.14b.
# R-11.9 Draw the AVL tree resulting from the removal of the entry with key 62
# from the AVL tree of Figure 11.14b.
# R-11.10 Explain why performing a rotation in an n-node binary tree when using
# the array-based representation of Section 8.3.2 takes Ω(n) time.
# R-11.11 Give a schematic ﬁgure, in the style of Figure 11.13, showing the heights
# of subtrees during a deletion operation in an AVL tree that triggers a tri-
# node restructuring for the case in which the two children of the node de-
# noted as y start with equal heights. What is the net effect of the height of
# the rebalanced subtree due to the deletion operation?
# R-11.12 Repeat the previous problem, considering the case in which y’s children
# start with different heights.
# www.it-ebooks.info11.7. Exercises
# 529
# R-11.13 The rules for a deletion in an AVL tree speciﬁcally require that when the
# two subtrees of the node denoted as y have equal height, child x should be
# chosen to be “aligned” with y (so that x and y are both left children or both
# right children). To better understand this requirement, repeat Exercise R-
# 11.11 assuming we picked the misaligned choice of x. Why might there
# be a problem in restoring the AVL property with that choice?
# R-11.14 Perform the following sequence of operations in an initially empty splay
# tree and draw the tree after each set of operations.
# a. Insert keys 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, in this order.
# b. Search for keys 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, in this order.
# c. Delete keys 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, in this order.
# R-11.15 What does a splay tree look like if its entries are accessed in increasing
# order by their keys?
# R-11.16 Is the search tree of Figure 11.23(a) a (2, 4) tree? Why or why not?
# R-11.17 An alternative way of performing a split at a node w in a (2, 4) tree is
# to partition w into w and w , with w being a 2-node and w a 3-node.
# Which of the keys k1 , k2 , k3 , or k4 do we store at w’s parent? Why?
# R-11.18 Dr. Amongus claims that a (2, 4) tree storing a set of entries will always
# have the same structure, regardless of the order in which the entries are
# inserted. Show that he is wrong.
# R-11.19 Draw four different red-black trees that correspond to the same (2, 4) tree.
# R-11.20 Consider the set of keys K = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}.
# a. Draw a (2, 4) tree storing K as its keys using the fewest number of
# nodes.
# b. Draw a (2, 4) tree storing K as its keys using the maximum number
# of nodes.
# R-11.21 Consider the sequence of keys (5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1). Draw
# the result of inserting entries with these keys (in the given order) into
# a. An initially empty (2, 4) tree.
# b. An initially empty red-black tree.
# R-11.22 For the following statements about red-black trees, provide a justiﬁcation
# for each true statement and a counterexample for each false one.
# a. A subtree of a red-black tree is itself a red-black tree.
# b. A node that does not have a sibling is red.
# c. There is a unique (2, 4) tree associated with a given red-black tree.
# d. There is a unique red-black tree associated with a given (2, 4) tree.
# R-11.23 Explain why you would get the same output in an inorder listing of the
# entries in a binary search tree, T , independent of whether T is maintained
# to be an AVL tree, splay tree, or red-black tree.
# www.it-ebooks.infoChapter 11. Search Trees
# 530
# R-11.24 Consider a tree T storing 100,000 entries. What is the worst-case height
# of T in the following cases?
# a. T is a binary search tree.
# b. T is an AVL tree.
# c. T is a splay tree.
# d. T is a (2, 4) tree.
# e. T is a red-black tree.
# R-11.25 Draw an example of a red-black tree that is not an AVL tree.
# R-11.26 Let T be a red-black tree and let p be the position of the parent of the
# original node that is deleted by the standard search tree deletion algorithm.
# Prove that if p has zero children, the removed node was a red leaf.
# R-11.27 Let T be a red-black tree and let p be the position of the parent of the
# original node that is deleted by the standard search tree deletion algorithm.
# Prove that if p has one child, the deletion has caused a black deﬁcit at p,
# except for the case when the one remaining child is a red leaf.
# R-11.28 Let T be a red-black tree and let p be the position of the parent of the
# original node that is deleted by the standard search tree deletion algorithm.
# Prove that if p has two children, the removed node was black and had one
# red child.
# Creativity
# C-11.29 Explain how to use an AVL tree or a red-black tree to sort n comparable
# elements in O(n log n) time in the worst case.
# C-11.30 Can we use a splay tree to sort n comparable elements in O(n log n) time
# in the worst case? Why or why not?
# C-11.31 Repeat Exercise C-10.28 for the TreeMap class.
# C-11.32 Show that any n-node binary tree can be converted to any other n-node
# binary tree using O(n) rotations.
# C-11.33 For a key k that is not found in binary search tree T , prove that both the
# greatest key less than k and the least key greater than k lie on the path
# traced by the search for k.
# C-11.34 In Section 11.1.2 we claim that the ﬁnd range method of a binary search
# tree executes in O(s + h) time where s is the number of items found within
# the range and h is the height of the tree. Our implementation, in Code
# Fragment 11.6 begins by searching for the starting key, and then repeat-
# edly calling the after method until reaching the end of the range. Each call
# to after is guaranteed to run in O(h) time. This suggests a weaker O(sh)
# bound for ﬁnd range, since it involves O(s) calls to after. Prove that this
# implementation achieves the stronger O(s + h) bound.
# www.it-ebooks.info11.7. Exercises
# 531
# C-11.35 Describe how to perform an operation remove range(start, stop) that re-
# moves all the items whose keys fall within range(start, stop) in a sorted
# map that is implemented with a binary search tree T , and show that this
# method runs in time O(s + h), where s is the number of items removed
# and h is the height of T .
# C-11.36 Repeat the previous problem using an AVL tree, achieving a running time
# of O(s log n). Why doesn’t the solution to the previous problem trivially
# result in an O(s + log n) algorithm for AVL trees?
# C-11.37 Suppose we wish to support a new method count range(start, stop) that
# determines how many keys of a sorted map fall in the speciﬁed range. We
# could clearly implement this in O(s + h) time by adapting our approach to
# ﬁnd range. Describe how to modify the search tree structure to support
# O(h) worst-case time for count range.
# C-11.38 If the approach described in the previous problem were implemented as
# part of the TreeMap class, what additional modiﬁcations (if any) would be
# necessary to a subclass such as AVLTreeMap in order to maintain support
# for the new method?
# C-11.39 Draw a schematic of an AVL tree such that a single remove operation
# could require Ω(log n) trinode restructurings (or rotations) from a leaf to
# the root in order to restore the height-balance property.
# C-11.40 In our AVL implementation, each node stores the height of its subtree,
# which is an arbitrarily large integer. The space usage for an AVL tree
# can be reduced by instead storing the balance factor of a node, which is
# deﬁned as the height of its left subtree minus the height of its right subtree.
# Thus, the balance factor of a node is always equal to −1, 0, or 1, except
# during an insertion or removal, when it may become temporarily equal to
# −2 or +2. Reimplement the AVLTreeMap class storing balance factors
# rather than subtree heights.
# C-11.41 If we maintain a reference to the position of the leftmost node of a bi-
# nary search tree, then operation ﬁnd min can be performed in O(1) time.
# Describe how the implementation of the other map methods need to be
# modiﬁed to maintain a reference to the leftmost position.
# C-11.42 If the approach described in the previous problem were implemented as
# part of the TreeMap class, what additional modiﬁcations (if any) would
# be necessary to a subclass such as AVLTreeMap in order to accurately
# maintain the reference to the leftmost position?
# C-11.43 Describe a modiﬁcation to the binary search tree implementation having
# worst-case O(1)-time performance for methods after(p) and before(p)
# without adversely affecting the asymptotics of any other methods.
# www.it-ebooks.infoChapter 11. Search Trees
# 532
# C-11.44 If the approach described in the previous problem were implemented as
# part of the TreeMap class, what additional modiﬁcations (if any) would
# be necessary to a subclass such as AVLTreeMap in order to maintain the
# efﬁciency?
# C-11.45 For a standard binary search tree, Table 11.1 claims O(h)-time perfor-
# mance for the delete(p) method. Explain why delete(p) would run in
# O(1) time if given a solution to Exercise C-11.43.
# C-11.46 Describe a modiﬁcation to the binary search tree data structure that would
# support the following two index-based operations for a sorted map in O(h)
# time, where h is the height of the tree.
# at index(i): Return the position p of the item at index i of a sorted map.
# index of(p): Return the index i of the item at position p of a sorted map.
# C-11.47 Draw a splay tree, T1 , together with the sequence of updates that produced
# it, and a red-black tree, T2 , on the same set of ten entries, such that a
# preorder traversal of T1 would be the same as a preorder traversal of T2 .
# C-11.48 Show that the nodes that become temporarily unbalanced in an AVL tree
# during an insertion may be nonconsecutive on the path from the newly
# inserted node to the root.
# C-11.49 Show that at most one node in an AVL tree becomes temporarily un-
# balanced after the immediate deletion of a node as part of the standard
# delitem map operation.
# C-11.50 Let T and U be (2, 4) trees storing n and m entries, respectively, such
# that all the entries in T have keys less than the keys of all the entries in
# U . Describe an O(log n + log m)-time method for joining T and U into a
# single tree that stores all the entries in T and U .
# C-11.51 Repeat the previous problem for red-black trees T and U .
# C-11.52 Justify Proposition 11.7.
# C-11.53 The Boolean indicator used to mark nodes in a red-black tree as being
# “red” or “black” is not strictly needed when we have distinct keys. De-
# scribe a scheme for implementing a red-black tree without adding any
# extra space to standard binary search tree nodes.
# C-11.54 Let T be a red-black tree storing n entries, and let k be the key of an entry
# in T . Show how to construct from T , in O(log n) time, two red-black trees
# T  and T  , such that T  contains all the keys of T less than k, and T 
# contains all the keys of T greater than k. This operation destroys T .
# C-11.55 Show that the nodes of any AVL tree T can be colored “red” and “black”
# so that T becomes a red-black tree.
# www.it-ebooks.info11.7. Exercises
# 533
# C-11.56 The standard splaying step requires two passes, one downward pass to
# ﬁnd the node x to splay, followed by an upward pass to splay the node
# x. Describe a method for splaying and searching for x in one downward
# pass. Each substep now requires that you consider the next two nodes
# in the path down to x, with a possible zig substep performed at the end.
# Describe how to perform the zig-zig, zig-zag, and zig steps.
# C-11.57 Consider a variation of splay trees, called half-splay trees, where splaying
# a node at depth d stops as soon as the node reaches depth d/2. Perform
# an amortized analysis of half-splay trees.
# C-11.58 Describe a sequence of accesses to an n-node splay tree T , where n is odd,
# that results in T consisting of a single chain of nodes such that the path
# down T alternates between left children and right children.
# C-11.59 As a positional structure, our TreeMap implementation has a subtle ﬂaw.
# A position instance p associated with an key-value pair (k, v) should re-
# main valid as long as that item remains in the map. In particular, that
# position should be unaffected by calls to insert or delete other items in the
# collection. Our algorithm for deleting an item from a binary search tree
# may fail to provide such a guarantee, in particular because of our rule for
# using the inorder predecessor of a key as a replacement when deleting a
# key that is located in a node with two children. Given an explicit series of
# Python commands that demonstrates such a ﬂaw.
# C-11.60 How might the TreeMap implementation be changed to avoid the ﬂaw
# described in the previous problem?
# Projects
# P-11.61 Perform an experimental study to compare the speed of our AVL tree,
# splay tree, and red-black tree implementations for various sequences of
# operations.
# P-11.62 Redo the previous exercise, including an implementation of skip lists.
# (See Exercise P-10.53.)
# P-11.63 Implement the Map ADT using a (2, 4) tree. (See Section 10.1.1.)
# P-11.64 Redo the previous exercise, including all methods of the Sorted Map ADT.
# (See Section 10.3.)
# P-11.65 Redo Exercise P-11.63 providing positional support, as we did for bi-
# nary search trees (Section 11.1.1), so as to include methods ﬁrst( ), last( ),
# before(p), after(p), and ﬁnd position(k). Each item should have a dis-
# tinct position in this abstraction, even though several items may be stored
# at a single node of a tree.
# www.it-ebooks.infoChapter 11. Search Trees
# 534
# P-11.66 Write a Python class that can take any red-black tree and convert it into its
# corresponding (2, 4) tree and can take any (2, 4) tree and convert it into its
# corresponding red-black tree.
# P-11.67 In describing multisets and multimaps in Section 10.5.3, we describe a
# general approach for adapting a traditional map by storing all duplicates
# within a secondary container as a value in the map. Give an alternative
# implementation of a multimap using a binary search tree such that each
# entry of the map is stored at a distinct node of the tree. With the existence
# of duplicates, we redeﬁne the search tree property so that all items in the
# left subtree of a position p with key k have keys that are less than or equal
# to k, while all items in the right subtree of p have keys that are greater than
# or equal to k. Use the public interface given in Code Fragment 10.17.
# P-11.68 Prepare an implementation of splay trees that uses top-down splaying as
# described in Exercise C-11.56. Perform extensive experimental studies to
# compare its performance to the standard bottom-up splaying implemented
# in this chapter.
# P-11.69 The mergeable heap ADT is an extension of the priority queue ADT
# consisting of operations add(k, v), min( ), remove min( ) and merge(h),
# where the merge(h) operations performs a union of the mergeable heap h
# with the present one, incorporating all items into the current one while
# emptying h. Describe a concrete implementation of the mergeable heap
# ADT that achieves O(log n) performance for all its operations, where n
# denotes the size of the resulting heap for the merge operation.
# P-11.70 Write a program that performs a simple n-body simulation, called “Jump-
# ing Leprechauns.” This simulation involves n leprechauns, numbered 1 to
# n. It maintains a gold value gi for each leprechaun i, which begins with
# each leprechaun starting out with a million dollars worth of gold, that is,
# gi = 1 000 000 for each i = 1, 2, . . . , n. In addition, the simulation also
# maintains, for each leprechaun, i, a place on the horizon, which is repre-
# sented as a double-precision ﬂoating-point number, xi . In each iteration
# of the simulation, the simulation processes the leprechauns in order. Pro-
# cessing a leprechaun i during this iteration begins by computing a new
# place on the horizon for i, which is determined by the assignment
# xi = xi + rgi ,
# where r is a random ﬂoating-point number between −1 and 1. The lep-
# rechaun i then steals half the gold from the nearest leprechauns on either
# side of him and adds this gold to his gold value, gi . Write a program that
# can perform a series of iterations in this simulation for a given number,
# n, of leprechauns. You must maintain the set of horizon positions using a
# sorted map data structure described in this chapter.



## SORTING AND SELECTION
def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0  # Initialize indices for S1 and S2
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]  # Copy ith element of S1 as next item of S
            i += 1
        else:
            S[i + j] = S2[j]  # Copy jth element of S2 as next item of S
            j += 1

def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return  # List is already sorted

    # Divide
    mid = n // 2
    S1 = S[0:mid]  # Copy of first half
    S2 = S[mid:n]  # Copy of second half

    # Conquer (with recursion)
    merge_sort(S1)  # Sort copy of first half
    merge_sort(S2)  # Sort copy of second half

    # Merge results
    merge(S1, S2, S)



def merge_queue(S1, S2, S):
    """Merge two sorted queue instances S1 and S2 into empty queue S."""
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())

    # Move remaining elements of S1 to S
    while not S1.is_empty():
        S.enqueue(S1.dequeue())

    # Move remaining elements of S2 to S
    while not S2.is_empty():
        S.enqueue(S2.dequeue())

def merge_sort_queue(S):
    """Sort the elements of queue S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return  # Queue is already sorted

    # Divide
    S1 = LinkedQueue()  # or any other queue implementation
    S2 = LinkedQueue()

    while len(S1) < n // 2:
        # Move the first n//2 elements to S1
        S1.enqueue(S.dequeue())

    # Move the rest to S2
    while not S.is_empty():
        S2.enqueue(S.dequeue())

    # Conquer (with recursion)
    # Sort first half
    merge_sort(S1)
    # Sort second half
    merge_sort(S2)

    # Merge results
    merge(S1, S2, S)


import math

def merge_non_recursive(src, result, start, inc):
    """Merge src[start:start+inc] and src[start+inc:start+2*inc] into result."""
    end1 = start + inc  # boundary for run 1
    end2 = min(start + 2 * inc, len(src))  # boundary for run 2
    x, y, z = start, start + inc, start  # index into run 1, run 2, result

    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]
            x += 1  # copy from run 1 and increment x
        else:
            result[z] = src[y]
            y += 1  # copy from run 2 and increment y
        z += 1  # increment z to reflect new result

    if x < end1:
        result[z:end2] = src[x:end1]  # copy remainder of run 1 to output
    elif y < end2:
        result[z:end2] = src[y:end2]  # copy remainder of run 2 to output

def merge_sort_non_recursive(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    logn = math.ceil(math.log(n, 2))  # Calculate log base 2 of n

    # Make temporary storage for dest
    src, dest = S, [None] * n

    for i in (2 ** k for k in range(logn)):  # pass i creates all runs of length 2^i
        # Each pass merges two length i runs
        for j in range(0, n, 2 * i):
            merge(src, dest, j, i)
        
        src, dest = dest, src  # Reverse roles of lists

    if S is not src:
        S[0:n] = src[0:n]  # Copy sorted elements back to S


def quick_sort(S):
    """Sort the elements of queue S using the quick-sort algorithm."""
    n = len(S)
    if n < 2:
        return  # Queue is already sorted

    # Divide
    p = S.first()  # Using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()  # Divide S into L, E, and G

    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue())  # Elements less than pivot
        elif p < S.first():
            G.enqueue(S.dequeue())  # Elements greater than pivot
        else:
            E.enqueue(S.dequeue())  # Elements equal to pivot

    # Conquer (with recursion)
    quick_sort(L)  # Sort elements less than p
    quick_sort(G)  # Sort elements greater than p

    # Concatenate results
    while not L.is_empty():
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue(G.dequeue())


def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
    if a >= b:
        return  # Range is trivially sorted

    pivot = S[b]  # Last element of range is pivot
    left = a  # Will scan rightward
    right = b - 1  # Will scan leftward

    while left <= right:
        # Scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # Scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        
        if left <= right:
            # Scans did not strictly cross
            S[left], S[right] = S[right], S[left]  # Swap values
            left, right = left + 1, right - 1  # Shrink range

    # Put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]

    # Make recursive calls
    inplace_quick_sort(S, a, left - 1)  # Sort elements less than pivot
    inplace_quick_sort(S, left + 1, b)  # Sort elements greater than pivot


class Item:
    """Class to hold a key-value pair for decoration."""
    def __init__(self, key, value):
        self.key = key
        self.value = value

def decorated_merge_sort(data, key=None):
    """Demonstration of the decorate-sort-undecorate pattern."""
    if key is not None:
        for j in range(len(data)):
            # Decorate each element
            data[j] = Item(key(data[j]), data[j])
    
    merge_sort(data)  # Sort with existing algorithm

    if key is not None:
        for j in range(len(data)):
            # Undecorate each element
            data[j] = data[j].value





import random

def quick_select(S, k):
    """Return the kth smallest element of list S, for k from 1 to len(S)."""
    if len(S) == 1:
        return S[0]  # Base case: only one element

    pivot = random.choice(S)  # Pick random pivot element from S
    L = [x for x in S if x < pivot]  # Elements less than pivot
    E = [x for x in S if x == pivot]  # Elements equal to pivot
    G = [x for x in S if pivot < x]  # Elements greater than pivot

    if k <= len(L):
        # kth smallest lies in L
        return quick_select(L, k)
    elif k <= len(L) + len(E):
        return pivot  # kth smallest is equal to pivot
    else:
        j = k - len(L) - len(E)  # New selection parameter
        # kth smallest is jth in G
        return quick_select(G, j)

# R-12.1 Give a complete justiﬁcation of Proposition 12.1.
# R-12.2 In the merge-sort tree shown in Figures 12.2 through 12.4, some edges are
# drawn as arrows. What is the meaning of a downward arrow? How about
# an upward arrow?
# R-12.3 Show that the running time of the merge-sort algorithm on an n-element
# sequence is O(n log n), even when n is not a power of 2.
# R-12.4 Is our array-based implementation of merge-sort given in Section 12.2.2
# stable? Explain why or why not.
# R-12.5 Is our linked-list-based implementation of merge-sort given in Code Frag-
# ment 12.3 stable? Explain why or why not.
# R-12.6 An algorithm that sorts key-value entries by key is said to be straggling
# if, any time two entries ei and e j have equal keys, but ei appears before e j
# in the input, then the algorithm places ei after e j in the output. Describe a
# change to the merge-sort algorithm in Section 12.2 to make it straggling.
# R-12.7 Suppose we are given two n-element sorted sequences A and B each with
# distinct elements, but potentially some elements that are in both sequences.
# Describe an O(n)-time method for computing a sequence representing the
# union A ∪ B (with no duplicates) as a sorted sequence.
# R-12.8 Suppose we modify the deterministic version of the quick-sort algorithm
# so that, instead of selecting the last element in an n-element sequence as
# the pivot, we choose the element at index n/2. What is the running time
# of this version of quick-sort on a sequence that is already sorted?
# R-12.9 Consider a modiﬁcation of the deterministic version of the quick-sort al-
# gorithm where we choose the element at index n/2 as our pivot. De-
# scribe the kind of sequence that would cause this version of quick-sort to
# run in Ω(n2 ) time.
# R-12.10 Show that the best-case running time of quick-sort on a sequence of size
# n with distinct elements is Ω(n log n).
# R-12.11 Suppose function inplace quick sort is executed on a sequence with du-
# plicate elements. Prove that the algorithm still correctly sorts the input
# sequence. What happens in the partition step when there are elements
# equal to the pivot? What is the running time of the algorithm if all the
# input elements are equal?
# www.it-ebooks.info12.8. Exercises
# 575
# R-12.12 If the outermost while loop of our implementation of inplace quick sort
# (line 7 of Code Fragment 12.6) were changed to use condition left < right
# (rather than left <= right), there would be a ﬂaw. Explain the ﬂaw and
# give a speciﬁc input sequence on which such an implementation fails.
# R-12.13 If the conditional at line 14 of our inplace quick sort implementation of
# Code Fragment 12.6 were changed to use condition left < right (rather
# than left <= right), there would be a ﬂaw. Explain the ﬂaw and give a
# speciﬁc input sequence on which such an implementation fails.
# R-12.14 Following our analysis of randomized quick-sort in Section 12.3.1, show
# that the probability that a given input element x belongs to more than
# 2 log n subproblems in size group i is at most 1/n2 .
# R-12.15 Of the n! possible inputs to a given comparison-based sorting algorithm,
# what is the absolute maximum number of inputs that could be correctly
# sorted with just n comparisons?
# R-12.16 Jonathan has a comparison-based sorting algorithm that sorts the ﬁrst k
# elements of a sequence of size n in O(n) time. Give a big-Oh characteri-
# zation of the biggest that k can be?
# R-12.17 Is the bucket-sort algorithm in-place? Why or why not?
# R-12.18 Describe a radix-sort method for lexicographically sorting a sequence S of
# triplets (k, l, m), where k, l, and m are integers in the range [0, N − 1], for
# some N ≥ 2. How could this scheme be extended to sequences of d-tuples
# (k1 , k2 , . . . , kd ), where each ki is an integer in the range [0, N − 1]?
# R-12.19 Suppose S is a sequence of n values, each equal to 0 or 1. How long will
# it take to sort S with the merge-sort algorithm? What about quick-sort?
# R-12.20 Suppose S is a sequence of n values, each equal to 0 or 1. How long will
# it take to sort S stably with the bucket-sort algorithm?
# R-12.21 Given a sequence S of n values, each equal to 0 or 1, describe an in-place
# method for sorting S.
# R-12.22 Give an example input list that requires merge-sort and heap-sort to take
# O(n log n) time to sort, but insertion-sort runs in O(n) time. What if you
# reverse this list?
# R-12.23 What is the best algorithm for sorting each of the following: general com-
# parable objects, long character strings, 32-bit integers, double-precision
# ﬂoating-point numbers, and bytes? Justify your answer.
# R-12.24 Show that the worst-case running time of quick-select on an n-element
# sequence is Ω(n2 ).
# www.it-ebooks.infoChapter 12. Sorting and Selection
# 576
# Creativity
# C-12.25 Linda claims to have an algorithm that takes an input sequence S and
# produces an output sequence T that is a sorting of the n elements in S.
# a. Give an algorithm, is sorted, that tests in O(n) time if T is sorted.
# b. Explain why the algorithm is sorted is not sufﬁcient to prove a par-
# ticular output T to Linda’s algorithm is a sorting of S.
# c. Describe what additional information Linda’s algorithm could out-
# put so that her algorithm’s correctness could be established on any
# given S and T in O(n) time.
# C-12.26 Describe and analyze an efﬁcient method for removing all duplicates from
# a collection A of n elements.
# C-12.27 Augment the PositionalList class (see Section 7.4) to support a method
# named merge with the following behavior. If A and B are PositionalList
# instances whose elements are sorted, the syntax A.merge(B) should merge
# all elements of B into A so that A remains sorted and B becomes empty.
# Your implementation must accomplish the merge by relinking existing
# nodes; you are not to create any new nodes.
# C-12.28 Augment the PositionalList class (see Section 7.4) to support a method
# named sort that sorts the elements of a list by relinking existing nodes;
# you are not to create any new nodes. You may use your choice of sorting
# algorithm.
# C-12.29 Implement a bottom-up merge-sort for a collection of items by placing
# each item in its own queue, and then repeatedly merging pairs of queues
# until all items are sorted within a single queue.
# C-12.30 Modify our in-place quick-sort implementation of Code Fragment 12.6 to
# be a randomized version of the algorithm, as discussed in Section 12.3.1.
# C-12.31 Consider a version of deterministic quick-sort where we pick as our pivot
# the median of the d last elements in the input sequence of n elements, for
# a ﬁxed, constant odd number d ≥ 3. What is the asymptotic worst-case
# running time of quick-sort in this case?
# C-12.32 Another way to analyze randomized quick-sort is to use a recurrence
# equation. In this case, we let T (n) denote the expected running time
# of randomized quick-sort, and we observe that, because of the worst-case
# partitions for good and bad splits, we can write
# T (n) ≤
# 1
# 1
# (T (3n/4) + T (n/4)) + (T (n − 1)) + bn,
# 2
# 2
# where bn is the time needed to partition a list for a given pivot and concate-
# nate the result sublists after the recursive calls return. Show, by induction,
# that T (n) is O(n log n).
# www.it-ebooks.info12.8. Exercises
# 577
# C-12.33 Our high-level description of quick-sort describes partitioning the ele-
# ments into three sets L, E, and G, having keys less than, equal to, or
# greater than the pivot, respectively. However, our in-place quick-sort im-
# plementation of Code Fragment 12.6 does not gather all elements equal
# to the pivot into a set E. An alternative strategy for an in-place, three-
# way partition is as follows. Loop through the elements from left to right
# maintaining indices i, j, and k and the invariant that all elements of slice
# S[0:i] are strictly less than the pivot, all elements of slice S[i:j] are equal
# to the pivot, and all elements of slice S[j:k] are strictly greater than the
# pivot; elements of S[k:n] are yet unclassiﬁed. In each pass of the loop,
# classify one additional element, performing a constant number of swaps
# as needed. Implement an in-place quick-sort using this strategy.
# C-12.34 Suppose we are given an n-element sequence S such that each element in S
# represents a different vote for president, where each vote is given as an in-
# teger representing a particular candidate, yet the integers may be arbitrar-
# ily large (even if the number of candidates is not). Design an O(n log n)-
# time algorithm to see who wins the election S represents, assuming the
# candidate with the most votes wins.
# C-12.35 Consider the voting problem from Exercise C-12.34, but now suppose that
# we know the number k < n of candidates running, even though the integer
# IDs for those candidates can be arbitrarily large. Describe an O(n log k)-
# time algorithm for determining who wins the election.
# C-12.36 Consider the voting problem from Exercise C-12.34, but now suppose the
# integers 1 to k are used to identify k < n candidates. Design an O(n)-time
# algorithm to determine who wins the election.
# C-12.37 Show that any comparison-based sorting algorithm can be made to be
# stable without affecting its asymptotic running time.
# C-12.38 Suppose we are given two sequences A and B of n elements, possibly
# containing duplicates, on which a total order relation is deﬁned. Describe
# an efﬁcient algorithm for determining if A and B contain the same set of
# elements. What is the running time of this method?
# C-12.39 Given an array A of n integers in the range [0, n2 − 1], describe a simple
# method for sorting A in O(n) time.
# C-12.40 Let S1 , S2 , . . . , Sk be k different sequences whose elements have integer
# keys in the range [0, N − 1], for some parameter N ≥ 2. Describe an algo-
# rithm that produces k respective sorted sequences in O(n + N) time, were
# n denotes the sum of the sizes of those sequences.
# C-12.41 Given a sequence S of n elements, on which a total order relation is de-
# ﬁned, describe an efﬁcient method for determining whether there are two
# equal elements in S. What is the running time of your method?
# www.it-ebooks.infoChapter 12. Sorting and Selection
# 578
# C-12.42 Let S be a sequence of n elements on which a total order relation is de-
# ﬁned. Recall that an inversion in S is a pair of elements x and y such
# that x appears before y in S but x > y. Describe an algorithm running in
# O(n log n) time for determining the number of inversions in S.
# C-12.43 Let S be a sequence of n integers. Describe a method for printing out all
# the pairs of inversions in S in O(n + k) time, where k is the number of such
# inversions.
# C-12.44 Let S be a random permutation of n distinct integers. Argue that the ex-
# pected running time of insertion-sort on S is Ω(n2 ). (Hint: Note that half
# of the elements ranked in the top half of a sorted version of S are expected
# to be in the ﬁrst half of S.)
# C-12.45 Let A and B be two sequences of n integers each. Given an integer m,
# describe an O(n log n)-time algorithm for determining if there is an integer
# a in A and an integer b in B such that m = a + b.
# C-12.46 Given a set of n integers, describe and analyze a fast method for ﬁnding
# the log n  integers closest to the median.
# C-12.47 Bob has a set A of n nuts and a set B of n bolts, such that each nut in A
# has a unique matching bolt in B. Unfortunately, the nuts in A all look the
# same, and the bolts in B all look the same as well. The only kind of a
# comparison that Bob can make is to take a nut-bolt pair (a, b), such that a
# is in A and b is in B, and test it to see if the threads of a are larger, smaller,
# or a perfect match with the threads of b. Describe and analyze an efﬁcient
# algorithm for Bob to match up all of his nuts and bolts.
# C-12.48 Our quick-select implementation can be made more space-efﬁcient by ini-
# tially computing only the counts for sets L, E, and G, creating only the new
# subset that will be needed for recursion. Implement such a version.
# C-12.49 Describe an in-place version of the quick-select algorithm in pseudo-code,
# assuming that you are allowed to modify the order of elements.
# C-12.50 Show how to use a deterministic O(n)-time selection algorithm to sort a
# sequence of n elements in O(n log n) worst-case time.
# C-12.51 Given an unsorted sequence S of n comparable elements, and an integer k,
# give an O(n log k) expected-time algorithm for ﬁnding the O(k) elements
# that have rank n/k, 2 n/k, 3 n/k, and so on.
# C-12.52 Space aliens have given us a function, alien split, that can take a sequence
# S of n integers and partition S in O(n) time into sequences S1 , S2 , . . . , Sk of
# size at most n/k each, such that the elements in Si are less than or equal
# to every element in Si+1 , for i = 1, 2, . . . , k − 1, for a ﬁxed number, k < n.
# Show how to use alien split to sort S in O(n log n/ log k) time.
# C-12.53 Read documenation of the reverse keyword parameter of Python’s sorting
# functions, and describe how the decorate-sort-undecorate paradigm could
# be used to implement it, without assuming anything about the key type.
# www.it-ebooks.info12.8. Exercises
# 579
# C-12.54 Show that randomized quick-sort runs in O(n log n) time with probability
# at least 1− 1/n, that is, with high probability, by answering the following:
# a. For each input element x, deﬁne Ci, j (x) to be a 0/1 random variable
# that is 1 if and only if element x is in j + 1 subproblems that belong
# to size group i. Argue why we need not deﬁne Ci, j for j > n.
# b. Let Xi, j be a 0/1 random variable that is 1 with probability 1/2 j ,
# independent of any other events, and let L = log4/3 n. Argue why
# L−1 n
# n
# ∑L−1
# i=0 ∑ j=0 Ci, j (x) ≤ ∑i=0 ∑ j=0 Xi, j .
# n
# n
# c. Show that the expected value of ∑L−1
# i=0 ∑ j=0 Xi, j is (2 − 1/2 )L.
# L
# n
# d. Show that the probability that ∑i=0 ∑ j=0 Xi, j > 4L is at most 1/n2 ,
# using the Chernoff bound that states that if X is the sum of a ﬁnite
# number of independent 0/1 random variables with expected value
# μ > 0, then Pr(X > 2μ) < (4/e)−μ , where e = 2.71828128. . ..
# e. Argue why the previous claim proves randomized quick-sort runs in
# O(n log n) time with probability at least 1 − 1/n.
# C-12.55 We can make the quick-select algorithm deterministic, by choosing the
# pivot of an n-element sequence as follows:
# Partition the set S into n/5 groups of size 5 each (except pos-
# sibly for one group). Sort each little set and identify the median
# element in this set. From this set of n/5 “baby” medians, ap-
# ply the selection algorithm recursively to ﬁnd the median of the
# baby medians. Use this element as the pivot and proceed as in
# the quick-select algorithm.
# Show that this deterministic quick-select algorithm runs in O(n) time by
# answering the following questions (please ignore ﬂoor and ceiling func-
# tions if that simpliﬁes the mathematics, for the asymptotics are the same
# either way):
# a. How many baby medians are less than or equal to the chosen pivot?
# How many are greater than or equal to the pivot?
# b. For each baby median less than or equal to the pivot, how many
# other elements are less than or equal to the pivot? Is the same true
# for those greater than or equal to the pivot?
# c. Argue why the method for ﬁnding the deterministic pivot and using
# it to partition S takes O(n) time.
# d. Based on these estimates, write a recurrence equation to bound the
# worst-case running time t(n) for this selection algorithm (note that in
# the worst case there are two recursive calls—one to ﬁnd the median
# of the baby medians and one to recur on the larger of L and G).
# e. Using this recurrence equation, show by induction that t(n) is O(n).
# www.it-ebooks.infoChapter 12. Sorting and Selection
# 580
# Projects
# P-12.56 Implement a nonrecursive, in-place version of the quick-sort algorithm, as
# described at the end of Section 12.3.2.
# P-12.57 Experimentally compare the performance of in-place quick-sort and a ver-
# sion of quick-sort that is not in-place.
# P-12.58 Perform a series of benchmarking tests on a version of merge-sort and
# quick-sort to determine which one is faster. Your tests should include
# sequences that are “random” as well as “almost” sorted.
# P-12.59 Implement deterministic and randomized versions of the quick-sort al-
# gorithm and perform a series of benchmarking tests to see which one is
# faster. Your tests should include sequences that are very “random” looking
# as well as ones that are “almost” sorted.
# P-12.60 Implement an in-place version of insertion-sort and an in-place version of
# quick-sort. Perform benchmarking tests to determine the range of values
# of n where quick-sort is on average better than insertion-sort.
# P-12.61 Design and implement a version of the bucket-sort algorithm for sorting
# a list of n entries with integer keys taken from the range [0, N − 1], for
# N ≥ 2. The algorithm should run in O(n + N) time.
# P-12.62 Design and implement an animation for one of the sorting algorithms de-
# scribed in this chapter. Your animation should illustrate the key properties
# of this algorithm in an intuitive manner.


## TEXT PROCESSING
def find_brute(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)  # Introduce convenient notations
    for i in range(n - m + 1):  # Try every potential starting index within T
        k = 0  # An index into pattern P
        while k < m and T[i + k] == P[k]:  # kth character of P matches
            k += 1
        if k == m:
            # If we reached the end of pattern,
            return i  # Substring T[i:i+m] matches P
    return -1  # If no match found

import random

def find_boyer_moore(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)  # Introduce convenient notations
    if m == 0:
        return 0  # Trivial search for empty string

    last = {}  # Build 'last' dictionary
    for k in range(m):
        last[P[k]] = k  # Later occurrence overwrites

    # Align end of pattern at index m-1 of text
    i = m - 1  # An index into T
    k = m - 1  # An index into P

    while i < n:
        if T[i] == P[k]:  # A matching character
            if k == 0:
                return i  # Pattern begins at index i of text
            else:
                i -= 1  # Examine previous character in T
                k -= 1  # Move to previous character in P
        else:
            j = last.get(T[i], -1)  # last(T[i]) is -1 if not found
            i += m - min(k, j + 1)  # Case analysis for jump step
            k = m - 1  # Restart at end of pattern

    return -1  # Pattern not found


def compute_kmp_fail(P):
    """Precompute the failure function for KMP algorithm."""
    m = len(P)
    fail = [0] * m
    k = 0  # Length of the previous longest prefix suffix

    for j in range(1, m):
        while k > 0 and P[k] != P[j]:
            k = fail[k - 1]  # Fall back to the previous longest prefix suffix
        if P[k] == P[j]:
            k += 1
        fail[j] = k

    return fail

def find_kmp(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)."""
    n, m = len(T), len(P)  # Introduce convenient notations
    if m == 0:
        return 0  # Trivial search for empty string

    # Rely on utility to precompute
    fail = compute_kmp_fail(P)
    
    j = 0  # Index into text
    k = 0  # Index into pattern

    while j < n:
        if T[j] == P[k]:  # P[0:k+1] matched thus far
            if k == m - 1:  # Match is complete
                return j - m + 1  # Return starting index of match
            j += 1  # Try to extend match
            k += 1
        elif k > 0:
            k = fail[k - 1]  # Reuse suffix of P[0:k]
        else:
            j += 1

    return -1  # No match found

def matrix_chain(d):
    """d is a list of n+1 numbers such that size of kth matrix is d[k]-by-d[k+1].
    
    Return an n-by-n table such that N[i][j] represents the minimum number of
    multiplications needed to compute the product of Ai through Aj inclusive.
    """
    n = len(d) - 1  # Number of matrices
    # Initialize n-by-n result to zero
    N = [[0] * n for i in range(n)]

    for b in range(1, n):  # Number of products in subchain
        for i in range(n - b):  # Start of subchain
            j = i + b  # End of subchain
            N[i][j] = min(N[i][k] + N[k + 1][j] + d[i] * d[k + 1] * d[j + 1] for k in range(i, j))

    return N


def LCS(X, Y):
    """Return table such that L[j][k] is length of LCS for X[0:j] and Y[0:k]."""
    n, m = len(X), len(Y)  # Introduce convenient notations
    # (n+1) x (m+1) table
    L = [[0] * (m + 1) for _ in range(n + 1)]

    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:
                # Align this match
                L[j + 1][k + 1] = L[j][k] + 1
            else:
                # Choose to ignore one character
                L[j + 1][k + 1] = max(L[j][k + 1], L[j + 1][k])

    return L


def LCS_solution(X, Y, L):
    """Return the longest common substring of X and Y, given LCS table L."""
    solution = []
    j, k = len(X), len(Y)

    while L[j][k] > 0:  # Common characters remain
        if X[j - 1] == Y[k - 1]:
            solution.append(X[j - 1])  # Match found
            j -= 1
            k -= 1
        elif L[j - 1][k] >= L[j][k - 1]:
            j -= 1  # Move up in the table
        else:
            k -= 1  # Move left in the table

    # Return left-to-right version
    return ''.join(reversed(solution))

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Search for a complete word in the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """Check if there is any word in the Trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Example Usage
def main_trie():
    trie = Trie()
    
    # Insert words into the Trie
    trie.insert("apple")
    trie.insert("app")
    
    # Search for words
    print(trie.search("apple"))  # Output: True
    print(trie.search("app"))     # Output: True
    print(trie.search("appl"))    # Output: False
    
    # Check for prefixes
    print(trie.starts_with("app")) # Output: True
    print(trie.starts_with("appl")) # Output: True
    print(trie.starts_with("a"))    # Output: True
    print(trie.starts_with("b"))    # Output: False




"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
"""
#https://leetcode.com/problems/is-subsequence/description/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m,n = len(s), len(t)
        i,j = 0,0

        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i==m
    
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
#https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = ''.join(char.lower() for char in s if char.isalnum())
        return True if filtered_chars == filtered_chars[::-1] else False
    


"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""
#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        base = strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]

        return base

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
#https://leetcode.com/problems/zigzag-conversion/description/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for row in range(numRows)]
        index = 0
        step = 1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step =- 1
            index += step
        
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        
        return ''.join(rows)


"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.

"""
#https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution:
    def reverseWords(self, s: str) -> str:
        strs = [[i] for i in s.split()]
        dat = []
        for i in strs[::-1]:
            dat.append(''.join(i))
        return ' '.join(dat)


"""
You are given an array of unique strings words where words[i] is six letters long. One word of words was chosen as a secret word.

You are also given the helper object Master. You may call Master.guess(word) where word is a six-letter-long string, and it must be from words. Master.guess(word) returns:

-1 if word is not from words, or
an integer representing the number of exact matches (value and position) of your guess to the secret word.
There is a parameter allowedGuesses for each test case where allowedGuesses is the maximum number of times you can call Master.guess(word).

For each test case, you should call Master.guess with the secret word without exceeding the maximum number of allowed guesses. You will get:

"Either you took too many guesses, or you did not find the secret word." if you called Master.guess more than allowedGuesses times or if you did not call Master.guess with the secret word, or
"You guessed the secret word correctly." if you called Master.guess with the secret word with the number of calls to Master.guess less than or equal to allowedGuesses.
The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using the bruteforce method).

 

Example 1:

Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
Output: You guessed the secret word correctly.
Explanation:
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.
Example 2:

Input: secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
Output: You guessed the secret word correctly.
Explanation: Since there are two words, you can guess both.
 

Constraints:

1 <= words.length <= 100
words[i].length == 6
words[i] consist of lowercase English letters.
All the strings of wordlist are unique.
secret exists in words.
10 <= allowedGuesses <= 30
"""
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def guess(self, word: str) -> int:
        pass  # Implementation is hidden

class Solution:
    def findSecretWord(self, words: list[str], master: Master) -> None:
        def pair_matches(a: str, b: str) -> int:
            return sum(c1 == c2 for c1, c2 in zip(a, b))
        
        def most_overlap_word() -> str:
            counts = [[0] * 26 for _ in range(6)]
            for word in candidates:
                for i, c in enumerate(word):
                    counts[i][ord(c) - ord('a')] += 1
            best_score = -1
            best_word = candidates[0]
            for word in candidates:
                score = 0
                for i, c in enumerate(word):
                    score += counts[i][ord(c) - ord('a')]
                if score > best_score:
                    best_score = score
                    best_word = word
            return best_word
        
        candidates = words[:]
        
        while candidates:
            guess_word = most_overlap_word()
            matches = master.guess(guess_word)
            if matches == 6:
                return
            candidates = [word for word in candidates if pair_matches(guess_word, word) == matches]

# R-13.1 List the preﬁxes of the string P ="aaabbaaa" that are also sufﬁxes of P.
# R-13.2 What is the longest (proper) preﬁx of the string "cgtacgttcgtacg" that
# is also a sufﬁx of this string?
# R-13.3 Draw a ﬁgure illustrating the comparisons done by brute-force pattern
# matching for the text "aaabaadaabaaa" and pattern "aabaaa".
# R-13.4 Repeat the previous problem for the Boyer-Moore algorithm, not counting
# the comparisons made to compute the last(c) function.
# R-13.5 Repeat Exercise R-13.3 for the Knuth-Morris-Pratt algorithm, not count-
# ing the comparisons made to compute the failure function.
# R-13.6 Compute a map representing the last function used in the Boyer-Moore
# pattern-matching algorithm for characters in the pattern string:
# "the quick brown fox jumped over a lazy cat".
# R-13.7 Compute a table representing the Knuth-Morris-Pratt failure function for
# the pattern string "cgtacgttcgtac".
# R-13.8 What is the best way to multiply a chain of matrices with dimensions that
# are 10 × 5, 5 × 2, 2 × 20, 20 × 12, 12 × 4, and 4 × 60? Show your work.
# R-13.9 In Figure 13.8, we illustrate that GTTTAA is a longest common subse-
# quence for the given strings X and Y . However, that answer is not unique.
# Give another common subsequence of X and Y having length six.
# R-13.10 Show the longest common subsequence array L for the two strings:
# X= "skullandbones"
# Y= "lullabybabies"
# What is a longest common subsequence between these strings?
# R-13.11 Draw the frequency array and Huffman tree for the following string:
# "dogs do not spot hot pots or cats".
# R-13.12 Draw a standard trie for the following set of strings:
# { abab, baba, ccccc, bbaaaa, caa, bbaacc, cbcc, cbca }.
# R-13.13 Draw a compressed trie for the strings given in the previous problem.
# R-13.14 Draw the compact representation of the sufﬁx trie for the string:
# "minimize minime".
# www.it-ebooks.infoChapter 13. Text Processing
# 614
# Creativity
# C-13.15 Describe an example of a text T of length n and a pattern P of length
# m such that force the brute-force pattern-matching algorithm achieves a
# running time that is Ω(nm).
# C-13.16 Adapt the brute-force pattern-matching algorithm in order to implement a
# function, rﬁnd brute(T,P), that returns the index at which the rightmost
# occurrence of pattern P within text T , if any.
# C-13.17 Redo the previous problem, adapting the Boyer-Moore pattern-matching
# algorithm appropriately to implement a function rﬁnd boyer moore(T,P).
# C-13.18 Redo Exercise C-13.16, adapting the Knuth-Morris-Pratt pattern-matching
# algorithm appropriately to implement a function rﬁnd kmp(T,P).
# C-13.19 The count method of Python’s str class reports the maximum number of
# nonoverlapping occurrences of a pattern within a string. For example, the
# call abababa .count( aba ) returns 2 (not 3). Adapt the brute-force
# pattern-matching algorithm to implement a function, count brute(T,P),
# with similar outcome.
# C-13.20 Redo the previous problem, adapting the Boyer-Moore pattern-matching
# algorithm in order to implement a function count boyer moore(T,P).
# C-13.21 Redo Exercise C-13.19, adapting the Knuth-Morris-Pratt pattern-matching
# algorithm appropriately to implement a function count kmp(T,P).
# C-13.22 Give a justiﬁcation of why the compute kmp fail function (Code Frag-
# ment 13.4) runs in O(m) time on a pattern of length m.
# C-13.23 Let T be a text of length n, and let P be a pattern of length m. Describe an
# O(n+m)-time method for ﬁnding the longest preﬁx of P that is a substring
# of T .
# C-13.24 Say that a pattern P of length m is a circular substring of a text T of length
# n > m if P is a (normal) substring of T , or if P is equal to the concatenation
# of a sufﬁx of T and a preﬁx of T , that is, if there is an index 0 ≤ k < m,
# such that P = T [n − m + k : n] + T [0 : k]. Give an O(n + m)-time algorithm
# for determining whether P is a circular substring of T .
# C-13.25 The Knuth-Morris-Pratt pattern-matching algorithm can be modiﬁed to
# run faster on binary strings by redeﬁning the failure function as:
# f (k) = the largest j < k such that P[0 : j] pj is a sufﬁx of P[1 : k + 1],
# where pj denotes the complement of the jth bit of P. Describe how to
# modify the KMP algorithm to be able to take advantage of this new failure
# function and also give a method for computing this failure function. Show
# that this method makes at most n comparisons between the text and the
# pattern (as opposed to the 2n comparisons needed by the standard KMP
# algorithm given in Section 13.2.3).
# www.it-ebooks.info13.6. Exercises
# 615
# C-13.26 Modify the simpliﬁed Boyer-Moore algorithm presented in this chapter
# using ideas from the KMP algorithm so that it runs in O(n + m) time.
# C-13.27 Design an efﬁcient algorithm for the matrix chain multiplication problem
# that outputs a fully parenthesized expression for how to multiply the ma-
# trices in the chain using the minimum number of operations.
# C-13.28 A native Australian named Anatjari wishes to cross a desert carrying only
# a single water bottle. He has a map that marks all the watering holes along
# the way. Assuming he can walk k miles on one bottle of water, design an
# efﬁcient algorithm for determining where Anatjari should reﬁll his bottle
# in order to make as few stops as possible. Argue why your algorithm is
# correct.
# C-13.29 Describe an efﬁcient greedy algorithm for making change for a speciﬁed
# value using a minimum number of coins, assuming there are four denomi-
# nations of coins (called quarters, dimes, nickels, and pennies), with values
# 25, 10, 5, and 1, respectively. Argue why your algorithm is correct.
# C-13.30 Give an example set of denominations of coins so that a greedy change-
# making algorithm will not use the minimum number of coins.
# C-13.31 In the art gallery guarding problem we are given a line L that repre-
# sents a long hallway in an art gallery. We are also given a set X =
# {x0 , x1 , . . . , xn−1 } of real numbers that specify the positions of paintings
# in this hallway. Suppose that a single guard can protect all the paintings
# within distance at most 1 of his or her position (on both sides). Design
# an algorithm for ﬁnding a placement of guards that uses the minimum
# number of guards to guard all the paintings with positions in X .
# C-13.32 Let P be a convex polygon, a triangulation of P is an addition of diag-
# onals connecting the vertices of P so that each interior face is a triangle.
# The weight of a triangulation is the sum of the lengths of the diagonals.
# Assuming that we can compute lengths and add and compare them in con-
# stant time, give an efﬁcient algorithm for computing a minimum-weight
# triangulation of P.
# C-13.33 Let T be a text string of length n. Describe an O(n)-time method for
# ﬁnding the longest preﬁx of T that is a substring of the reversal of T .
# C-13.34 Describe an efﬁcient algorithm to ﬁnd the longest palindrome that is a
# sufﬁx of a string T of length n. Recall that a palindrome is a string that is
# equal to its reversal. What is the running time of your method?
# C-13.35 Given a sequence S = (x0 , x1 , . . . , xn−1 ) of numbers, describe an O(n2 )-
# time algorithm for ﬁnding a longest subsequence T = (xi0 , xi1 , . . . , xik−1 )
# of numbers, such that i j < i j+1 and xi j > xi j+1 . That is, T is a longest
# decreasing subsequence of S.
# C-13.36 Give an efﬁcient algorithm for determining if a pattern P is a subsequence
# (not substring) of a text T . What is the running time of your algorithm?
# www.it-ebooks.infoChapter 13. Text Processing
# 616
# C-13.37 Deﬁne the edit distance between two strings X and Y of length n and m,
# respectively, to be the number of edits that it takes to change X into Y . An
# edit consists of a character insertion, a character deletion, or a character
# replacement. For example, the strings "algorithm" and "rhythm" have
# edit distance 6. Design an O(nm)-time algorithm for computing the edit
# distance between X and Y .
# C-13.38 Let X and Y be strings of length n and m, respectively. Deﬁne B( j, k) to
# be the length of the longest common substring of the sufﬁx X [n − j :n] and
# the sufﬁx Y [m − k :m]. Design an O(nm)-time algorithm for computing all
# the values of B( j, k) for j = 1, . . . , n and k = 1, . . . , m.
# C-13.39 Anna has just won a contest that allows her to take n pieces of candy out
# of a candy store for free. Anna is old enough to realize that some candy is
# expensive, while other candy is relatively cheap, costing much less. The
# jars of candy are numbered 0, 1, . . ., m − 1, so that jar j has n j pieces in
# it, with a price of c j per piece. Design an O(n + m)-time algorithm that
# allows Anna to maximize the value of the pieces of candy she takes for
# her winnings. Show that your algorithm produces the maximum value for
# Anna.
# C-13.40 Let three integer arrays, A, B, and C, be given, each of size n. Given an
# arbitrary integer k, design an O(n2 log n)-time algorithm to determine if
# there exist numbers, a in A, b in B, and c in C, such that k = a + b + c.
# C-13.41 Give an O(n2 )-time algorithm for the previous problem.
# C-13.42 Given a string X of length n and a string Y of length m, describe an O(n +
# m)-time algorithm for ﬁnding the longest preﬁx of X that is a sufﬁx of Y .
# C-13.43 Give an efﬁcient algorithm for deleting a string from a standard trie and
# analyze its running time.
# C-13.44 Give an efﬁcient algorithm for deleting a string from a compressed trie
# and analyze its running time.
# C-13.45 Describe an algorithm for constructing the compact representation of a
# sufﬁx trie, given its noncompact representation, and analyze its running
# time.
# Projects
# P-13.46 Use the LCS algorithm to compute the best sequence alignment between
# some DNA strings, which you can get online from GenBank.
# P-13.47 Write a program that takes two character strings (which could be, for ex-
# ample, representations of DNA strands) and computes their edit distance,
# showing the corresponding pieces. (See Exercise C-13.37.)
# www.it-ebooks.info13.6. Exercises
# 617
# P-13.48 Perform an experimental analysis of the efﬁciency (number of character
# comparisons performed) of the brute-force and KMP pattern-matching al-
# gorithms for varying-length patterns.
# P-13.49 Perform an experimental analysis of the efﬁciency (number of charac-
# ter comparisons performed) of the brute-force and Boyer-Moore pattern-
# matching algorithms for varying-length patterns.
# P-13.50 Perform an experimental comparison of the relative speeds of the brute-
# force, KMP, and Boyer-Moore pattern-matching algorithms. Document
# the relative running times on large text documents that are then searched
# using varying-length patterns.
# P-13.51 Experiment with the efﬁciency of the ﬁnd method of Python’s str class
# and develop a hypothesis about which pattern-matching algorithm it uses.
# Try using inputs that are likely to cause both best-case and worst-case
# running times for various algorithms. Describe your experiments and your
# conclusions.
# P-13.52 Implement a compression and decompression scheme that is based on
# Huffman coding.
# P-13.53 Create a class that implements a standard trie for a set of ASCII strings.
# The class should have a constructor that takes a list of strings as an argu-
# ment, and the class should have a method that tests whether a given string
# is stored in the trie.
# P-13.54 Create a class that implements a compressed trie for a set of ASCII strings.
# The class should have a constructor that takes a list of strings as an argu-
# ment, and the class should have a method that tests whether a given string
# is stored in the trie.
# P-13.55 Create a class that implements a preﬁx trie for an ASCII string. The class
# should have a constructor that takes a string as an argument, and a method
# for pattern matching on the string.
# P-13.56 Implement the simpliﬁed search engine described in Section 13.5.4 for
# the pages of a small Web site. Use all the words in the pages of the site
# as index terms, excluding stop words such as articles, prepositions, and
# pronouns.
# P-13.57 Implement a search engine for the pages of a small Web site by adding
# a page-ranking feature to the simpliﬁed search engine described in Sec-
# tion 13.5.4. Your page-ranking feature should return the most relevant
# pages ﬁrst. Use all the words in the pages of the site as index terms, ex-
# cluding stop words, such as articles, prepositions, and pronouns.



## MEMORY
# R-15.1 Julia just bought a new computer that uses 64-bit integers to address mem-
# ory cells. Argue why Julia will never in her life be able to upgrade the
# main memory of her computer so that it is the maximum-size possible,
# assuming that you have to have distinct atoms to represent different bits.
# R-15.2 Describe, in detail, algorithms for adding an item to, or deleting an item
# from, an (a, b) tree.
# R-15.3 Suppose T is a multiway tree in which each internal node has at least ﬁve
# and at most eight children. For what values of a and b is T a valid (a, b)
# tree?
# R-15.4 For what values of d is the tree T of the previous exercise an order-d
# B-tree?
# R-15.5 Consider an initially empty memory cache consisting of four pages. How
# many page misses does the LRU algorithm incur on the following page
# request sequence: (2, 3, 4, 1, 2, 5, 1, 3, 5, 4, 1, 2, 3)?
# R-15.6 Consider an initially empty memory cache consisting of four pages. How
# many page misses does the FIFO algorithm incur on the following page
# request sequence: (2, 3, 4, 1, 2, 5, 1, 3, 5, 4, 1, 2, 3)?
# R-15.7 Consider an initially empty memory cache consisting of four pages. What
# is the maximum number of page misses that the random algorithm incurs
# on the following page request sequence: (2, 3, 4, 1, 2, 5, 1, 3, 5, 4, 1, 2, 3)?
# Show all of the random choices the algorithm made in this case.
# R-15.8 Draw the result of inserting, into an initially empty order-7 B-tree, entries
# with keys (4, 40, 23, 50, 11, 34, 62, 78, 66, 22, 90, 59, 25, 72, 64, 77, 39, 12),
# in this order.
# Creativity
# C-15.9 Describe an efﬁcient external-memory algorithm for removing all the du-
# plicate entries in an array list of size n.
# C-15.10 Describe an external-memory data structure to implement the stack ADT
# so that the total number of disk transfers needed to process a sequence of
# k push and pop operations is O(k/B).
# www.it-ebooks.info718
# Chapter 15. Memory Management and B-Trees
# C-15.11 Describe an external-memory data structure to implement the queue ADT
# so that the total number of disk transfers needed to process a sequence of
# k enqueue and dequeue operations is O(k/B).
# C-15.12 Describe an external-memory version of the PositionalList ADT (Sec-
# tion 7.4), with block size B, such that an iteration of a list of length n is
# completed using O(n/B) transfers in the worst case, and all other methods
# of the ADT require only O(1) transfers.
# C-15.13 Change the rules that deﬁne red-black trees so that each red-black tree T
# has a corresponding (4, 8) tree, and vice versa.
# C-15.14 Describe a modiﬁed version of the B-tree insertion algorithm so that each
# time we create an overﬂow because of a split of a node w, we redistribute
# keys among all of w’s siblings, so that each sibling holds roughly the same
# number of keys (possibly cascading the split up to the parent of w). What
# is the minimum fraction of each block that will always be ﬁlled using this
# scheme?
# C-15.15 Another possible external-memory map implementation is to use a skip
# list, but to collect consecutive groups of O(B) nodes, in individual blocks,
# on any level in the skip list. In particular, we deﬁne an order-d B-skip
# list to be such a representation of a skip list structure, where each block
# contains at least d/2 list nodes and at most d list nodes. Let us also
# choose d in this case to be the maximum number of list nodes from a level
# of a skip list that can ﬁt into one block. Describe how we should modify
# the skip-list insertion and removal algorithms for a B-skip list so that the
# expected height of the structure is O(log n/ log B).
# C-15.16 Describe how to use a B-tree to implement the partition (union-ﬁnd) ADT
# (from Section 14.7.3) so that the union and ﬁnd operations each use at
# most O(log n/ log B) disk transfers.
# C-15.17 Suppose we are given a sequence S of n elements with integer keys such
# that some elements in S are colored “blue” and some elements in S are
# colored “red.” In addition, say that a red element e pairs with a blue
# element f if they have the same key value. Describe an efﬁcient external-
# memory algorithm for ﬁnding all the red-blue pairs in S. How many disk
# transfers does your algorithm perform?
# C-15.18 Consider the page caching problem where the memory cache can hold m
# pages, and we are given a sequence P of n requests taken from a pool
# of m + 1 possible pages. Describe the optimal strategy for the ofﬂine
# algorithm and show that it causes at most m + n/m page misses in total,
# starting from an empty cache.
# C-15.19 Describe an efﬁcient external-memory algorithm that determines whether
# an array of n integers contains a value occurring more than n/2 times.
# www.it-ebooks.infoChapter Notes
# 719
# C-15.20 Consider the page caching strategy based on the least frequently used
# (LFU) rule, where the page in the cache that has been accessed the least
# often is the one that is evicted when a new page is requested. If there are
# ties, LFU evicts the least frequently used page that has been in the cache
# the longest. Show that there is a sequence P of n requests that causes LFU
# to miss Ω(n) times for a cache of m pages, whereas the optimal algorithm
# will miss only O(m) times.
# C-15.21 Suppose that instead of having the node-search function f (d) = 1 in an
# order-d B-tree T , we have f (d) = log d. What does the asymptotic run-
# ning time of performing a search in T now become?
# Projects
# P-15.22 Write a Python class that simulates the best-ﬁt, worst-ﬁt, ﬁrst-ﬁt, and next-
# ﬁt algorithms for memory management. Determine experimentally which
# method is the best under various sequences of memory requests.
# P-15.23 Write a Python class that implements all the methods of the ordered map
# ADT by means of an (a, b) tree, where a and b are integer constants passed
# as parameters to a constructor.
# P-15.24 Implement the B-tree data structure, assuming a block size of 1024 and
# integer keys. Test the number of “disk transfers” needed to process a
# sequence of map operations.

# hash combined tuple
# %%



## Projects
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Grades: {self.grades}"


class Node:
    def __init__(self, student):
        self.student = student
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, student):
        new_node = Node(student)
        new_node.next = self.head
        self.head = new_node

    def remove_student(self, student_id):
        current = self.head
        previous = None
        while current is not None:
            if current.student.student_id == student_id:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    def display_students(self):
        current = self.head
        while current is not None:
            print(current.student)
            current = current.next


class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title


class CourseList:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        for course in self.courses:
            print(f"Course ID: {course.course_id}, Title: {course.title}")


def main_student_management_system():
    students = StudentList()
    courses = CourseList()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Add Course")
        print("4. Assign Grade")
        print("5. Display Students")
        print("6. Display Courses")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            students.add_student(Student(sid, name))
            print(f"Added student: {name}")

        elif choice == '2':
            sid = input("Enter Student ID to remove: ")
            if students.remove_student(sid):
                print(f"Removed student with ID {sid}.")
            else:
                print("Student not found.")

        elif choice == '3':
            cid = input("Enter Course ID: ")
            title = input("Enter Course Title: ")
            courses.add_course(Course(cid, title))
            print(f"Added course: {title}")

        elif choice == '4':
            sid = input("Enter Student ID to assign grade: ")
            course_title = input("Enter Course Title: ")
            grade = input("Enter Grade: ")
            
            # Find the student and assign the grade
            current_student_node = students.head
            while current_student_node is not None:
                if current_student_node.student.student_id == sid:
                    current_student_node.student.add_grade(course_title, grade)
                    print(f"Assigned grade {grade} for {course_title} to {current_student_node.student.name}.")
                    break
                current_student_node = current_student_node.next

        elif choice == '5':
            print("\nStudents List:")
            students.display_students()

        elif choice == '6':
            print("\nCourses List:")
            courses.display_courses()

        elif choice == '0':
            break
        
        else:
            print("Invalid choice. Please try again.")



import os
import heapq
from collections import defaultdict
from pathlib import Path

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    def make_frequency_dict(self, text):
        frequency = defaultdict(int)
        for char in text:
            frequency[char] += 1
        return frequency

    def build_heap(self, frequency):
        for key in frequency:
            node = Node(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        if root is None:
            return
        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def encode(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    def decode(self, encoded_text):
        current_code = ""
        decoded_text = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""
        return decoded_text


class FileZipper:
    def __init__(self):
        self.huffman_coding = HuffmanCoding()

    def compress_file(self, file_path):
        with open(file_path, 'r') as file:
            text = file.read()

        frequency_dict = self.huffman_coding.make_frequency_dict(text)
        self.huffman_coding.build_heap(frequency_dict)
        self.huffman_coding.merge_nodes()
        self.huffman_coding.make_codes()

        encoded_text = self.huffman_coding.encode(text)

        # Write the encoded text to a new file
        compressed_file_path = f"{file_path}.huff"
        
        with open(compressed_file_path, 'w') as compressed_file:
            compressed_file.write(encoded_text)

        print(f"Compressed {file_path} to {compressed_file_path}")

    def decompress_file(self, compressed_file_path):
        with open(compressed_file_path, 'r') as file:
            encoded_text = file.read()

        decoded_text = self.huffman_coding.decode(encoded_text)

        # Write the decoded text to a new file
        original_file_path = compressed_file_path.replace('.huff', '.txt')
        
        with open(original_file_path, 'w') as original_file:
            original_file.write(decoded_text)

        print(f"Decompressed {compressed_file_path} to {original_file_path}")


def main_zipper():
    zipper = FileZipper()
    
    while True:
        print("\nFile Zipper")
        print("1. Compress File")
        print("2. Decompress File")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the path of the file to compress: ")
            if Path(file_path).is_file():
                zipper.compress_file(file_path)
            else:
                print("File not found.")

        elif choice == '2':
            compressed_file_path = input("Enter the path of the compressed file: ")
            if Path(compressed_file_path).is_file():
                zipper.decompress_file(compressed_file_path)
            else:
                print("File not found.")

        elif choice == '0':
            break
        
        else:
            print("Invalid choice. Please try again.")



class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def suggest(self, prefix):
        suggestions = []
        self._find_words_from_node(self.root, prefix, suggestions)
        return suggestions

    def _find_words_from_node(self, node, prefix, suggestions):
        if node.is_end_of_word:
            suggestions.append(prefix)
        
        for char, child_node in node.children.items():
            self._find_words_from_node(child_node, prefix + char, suggestions)


class SpellChecker:
    def __init__(self, dictionary_file):
        self.trie = Trie()
        self.load_dictionary(dictionary_file)

    def load_dictionary(self, dictionary_file):
        """Load dictionary from a file into the trie."""
        with open(dictionary_file, 'r') as file:
            for line in file:
                word = line.strip().lower()
                self.trie.insert(word)

    def check_word(self, word):
        """Check if the word is in the dictionary."""
        return self.trie.search(word.lower())

    def suggest_corrections(self, misspelled_word):
        """Suggest corrections for a misspelled word."""
        suggestions = []
        
        # Generate suggestions based on prefixes
        for i in range(len(misspelled_word)):
            # Suggest by removing one character
            suggestion = misspelled_word[:i] + misspelled_word[i+1:]
            if self.check_word(suggestion):
                suggestions.append(suggestion)

            # Suggest by replacing one character
            for char in 'abcdefghijklmnopqrstuvwxyz':
                suggestion = misspelled_word[:i] + char + misspelled_word[i+1:]
                if self.check_word(suggestion) and suggestion != misspelled_word:
                    suggestions.append(suggestion)

            # Suggest by adding one character
            for char in 'abcdefghijklmnopqrstuvwxyz':
                suggestion = misspelled_word[:i] + char + misspelled_word[i:]
                if self.check_word(suggestion):
                    suggestions.append(suggestion)

        return list(set(suggestions))  # Remove duplicates

    def check_text(self, text):
        """Check the entire text for spelling errors."""
        words = text.split()
        misspelled = {}

        for word in words:
            if not self.check_word(word):
                suggestions = self.suggest_corrections(word)
                misspelled[word] = suggestions

        return misspelled


def main_spellchecker():
    # Load the dictionary (make sure you have a text file with valid words)
    spell_checker = SpellChecker('dictionary.txt')

    while True:
        print("\nSimple Spell Checker")
        text = input("Enter text to check (or type 'exit' to quit): ")

        if text.lower() == 'exit':
            break

        misspelled_words = spell_checker.check_text(text)

        if not misspelled_words:
            print("No spelling errors found!")
        else:
            print("Misspelled words and suggestions:")
            for word, suggestions in misspelled_words.items():
                print(f"{word}: {suggestions}")

# %%
