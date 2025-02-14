# In this review, I'm seeing some concepts as Data Types, variables, operators, functions

# Data Types
# 1) int: usually numbers without a fractional component, like (1, 2, 3, -5)
# 2) float: numbers with fractions (1.2, 0.6)
# 3) bool: it represents true or false values 
# 4) str: it represents a sequence of characteres, as words, phrases, digits (hello, 44+33,3)

 # Variables: piece of memory where we keep some data. To create a variable, we must follow some naming rules.

nome= 'leonardo' 
print(nome) # here, I wrote a command that when executed, the value of the variable 'nome', will appear on the screen

# The operators have a priority to be followed, arithmetic, relational and logical ones. And when they have the same order priority, we have the term 'associativaty'. Associativity is when we execute some operation first. For example:
print(1**2 + 2**2) # this expression has a right associativity, that is, we do the right operation first

# Functions: To create a function we type 'def' and the name of the function. Next, the parameters, for example:
def somar(n1,n2):
    return n1+n2 #using return we can send the result back to the function, to use it later in a variable or store it
 
resultado=somar (1,2) # here, i assigned the result of the function to a variable
print(resultado)
  




