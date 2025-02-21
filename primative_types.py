# Primitive types: data types, for example: int, flaot, bool.
# Every time i'm working with a variable, i have to determine its type. 

n1 = input('Type a number: ') # I didn't especify the type, so here this return a string data type.

print(type(n1))

n2=int(input('Type another number: ')) # here i specified the data type

print(type(n2))

n3=input('Type a number: ')
n4=input('Type another number: ')
sum=(n3+n4) # Here i didn't add these numbers, i concatanated them. To add them, I need to determine the variable into 'int"
print(sum)

n5=int(input('Type a number: '))
n6=int(input('Type another one: '))
sum2=(n5+n6)
print('The sum of {} and {} is {}'.format(n5,n6,sum2))



