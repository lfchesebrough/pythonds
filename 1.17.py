




# Research the __radd__ method. How does it differ from __add__? When is it used? Implement __radd__.

# Repeat the last question but this time consider the __iadd__ method.

# Research the __repr__ method. How does it differ from __str__? When is it used? Implement __repr__.


def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:


# In many ways it would be better if all fractions were maintained in lowest 
# terms right from the start. Modify the constructor for the Fraction class so tha
# t GCD is used to reduce fractions immediately. Notice that this means the __add__ function
#  no longer needs to reduce. Make the necessary modifications.

# Modify the constructor for the fraction class so that it checks to make sure that the numerator 
# and denominator are both integers. If either is not an integer the constructor should raise an 
# exception.


# In the definition of fractions we assumed that negative fractions have a negative numerator and a
#  positive denominator. Using a negative denominator would cause some of the relational operators
#  to give incorrect results. In general, this is an unnecessary constraint. Modify the constructor 
# to allow the user to pass a negative denominator so that all of the operators continue 
# to work properly.

     def __init__(self,top,bottom):
         try:
             if isinstance(top, int) and isinstance(bottom, int):
                 if bottom < 0:
                     bottom *= -1
                     top *= -1
                 common = gcd(top,bottom)
                 self.num = top//common
                 self.den = bottom//common
             
             else: 
                 raise ValueError

         except ValueError:
             print("At least one of the numerator and denominator is not an integer, as required")

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

# Implement the simple methods getNum and getDen that will return the numerator and 
# denominator of a fraction.

     def getNum(self):
         print(self.num)
         return self.num

     def getDen(self):
         print(self.den)
         return self.den

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum,newden)

# Implement the remaining simple arithmetic operators (__sub__, __mul__, and __truediv__).
     def __sub__(self,otherfraction):
         newnum = self.num*otherfraction.den - \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum,newden)

     def __mul__(self,otherfraction):
         newnum = self.num*otherfraction.num
         newden = self.den * otherfraction.den
         return Fraction(newnum,newden)

     def __truediv__(self,otherfraction):
         newnum = self.num*otherfraction.den
         newden = self.den * otherfraction.num
         return Fraction(newnum,newden)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum

         # Implement the remaining relational operators (__gt__, __ge__, __lt__, __le__, and __ne__)
     def __gt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum > secondnum     
     
     def __ge__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum >= secondnum     
     
     def __lt__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum < secondnum     
     
     def __le__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum <= secondnum

     def __ne__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum != secondnum

x = Fraction(3,-7)
y = Fraction(2,5)
z = x + y
q = x + y
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(z == q)
print(x > y)

# Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to the
#  circuit hierarchy. How much additional coding did you need to do?

# The most simple arithmetic circuit is known as the half-adder. Research the
#  simple half-adder circuit. Implement this circuit.

# Now extend that circuit and implement an 8 bit full-adder.


# The circuit simulation shown in this chapter works in a backward direction. 
# In other words, given a circuit, the output is produced by working back through 
# the input values, which in turn cause other outputs to be queried. This continues
#  until external input lines are found, at which point the user is asked for values.
#  Modify the implementation so that the action is in the forward direction; upon
#  receiving inputs the circuit produces an output.

# Design a class to represent a playing card. Now design a class to represent a
#  deck of cards. Using these two classes, implement a favorite card game.

# Find a Sudoku puzzle in the local newspaper. Write a program to solve the puzzle.