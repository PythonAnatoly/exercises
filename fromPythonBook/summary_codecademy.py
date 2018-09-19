# The Summary and Exercises from the Codecademy.com

# = FILE INPUT/OUTPUT =

# You can open files in write-only mode ("w"), read-only mode ("r"), read and write mode ("r+"), and append mode ("a", which adds any new data you write to the file to the end of the file).

'''
my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("C:/Python34/text2.txt", "r+")

for item in my_list:
	f.write(str(item) + "\n")

f.close()
'''

'''
# Reading
my_file = open("C:/Python34/text2.txt", "r")

print (my_file.read())

my_file.close()
'''

'''
# 5/9 Read by line
my_file = open('C:/Python34/text.txt', 'r')

print (my_file.readline())
print (my_file.readline())
print (my_file.readline())

my_file.close()
'''

# 7/9 The 'with' and 'as' Keywords (for automatically closing file)
'''
with open('C:/Python34/text2.txt', 'r') as my_file:
	print (my_file.read())
'''
# 9/9 By checking file_object.closed, we'll know whether our file is closed and can call close() on it if it's still open.
'''
with open('C:/Python34/text2.txt', 'r') as my_file:
	print (my_file.read())
	
if my_file.closed == False:
	my_file.close()
	
print (my_file.closed)
'''

# How to remove some strings from file: I must to try this method. This is not from codecademy.com this is from another site
'''
f=open(file).readlines()
for i in [0,0,-1]:
    f.pop(i)
with open(file,'w') as F:
    F.writelines(f)
'''

# -= ABOUT CLASSES =-
# Introduction to Classes

#1/18
'''
class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()
'''

# 3/18
'''
class Animal(object):
	def	__init__(self):
		pass
'''

# 4/18 Let's Not Get Too Selfish
"""
Excellent! Let's make one more tweak to our class definition, then go ahead and instantiate (create) our first object.

So far, __init__() only takes one parameter: self. This is a Python convention; there's nothing magic about the word self. However, it's overwhelmingly common to use self as the first parameter in __init__(), so you should do this so that other people will understand your code.

The part that is magic is the fact that self is the first parameter passed to __init__(). Python will use the first parameter that __init__() receives to refer to the object being created; this is why it's often called self, since this parameter gives the object being created its identity.
"""
'''
Instructions
Let's do two things in the editor:

Pass __init__() a second parameter, name.
In the body of __init__(), let the function know that name refers to the created object's name by typing self.name = name. (This will become crystal clear in the next section.)
'''
'''
class Animal(object):
    def __init__(self, name):
        self.name = name
'''
# 5/18 Instantiating Your First Object
'''
class Square(object):
	def __init__(self):
		self.sides = 4
		
my_shape = Square()
	
print (my_shape.sides)
'''
'''
class Animal(object):
	def __init__(self, name, size):
		self.name = name
		self.size = size

zebra = Animal("Jeffrey", "middle")
leo = Animal("Leo", "big")
python = Animal("Python", "long")

print (zebra.name, zebra.size) 
print (leo.name)
print (python.name)
'''

# 6/18 More on __init__() and self

'''
Now that you're starting to understand how classes and objects work, it's worth delving a bit more into __init__() and self. They can be confusing!

As mentioned, you can think of __init__() as the method that "boots up" a class' instance object: the init bit is short for "initialize."

The first argument __init__() gets is used to refer to the instance object, and by convention, that argument is called self. If you add additional arguments—for instance, a name and age for your animal—setting each of those equal to self.name and self.age in the body of __init__() will make it so that when you create an instance object of your Animal class, you need to give each instance a name and an age, and those will be associated with the particular instance you create.

Instructions
Check out the examples in the editor. See how __init__() "boots up" each object to expect a name and an age, then uses self.name and self.age to assign those names and ages to each object? Add a third attribute, is_hungry to __init__(), and click Save & Submit Code to see the results.
'''
'''
# Class definition
class Animals(object):
	def __init__(self, name, age, is_hungry):
		self.name = name
		self.age = age
		self.is_hungry = is_hungry
		
zebra = Animals('Zebra', 2, False)
giraffe = Animals('Giraffe', 3, False)
tiger = Animals('Tiger', 4, True)

print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (tiger.name, tiger.age, tiger.is_hungry)
'''


# 7/18 
'''
class Animal(object):
    """Makes cute animals."""
    is_alive = True # this is a member variable
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print (zebra.name, zebra.age, zebra.is_alive)
print (giraffe.name, giraffe.age, giraffe.is_alive)
print (panda.name, panda.age, panda.is_alive)
'''

# 8/18 A Methodical Approach
#When a class has its own functions, those functions are called methods. You've already seen one such method: __init__(). But you can also define your own methods!

#When a class has its own functions, those functions are called methods. You've already seen one such method: __init__(). But you can also define your own methods!

#Instructions
#Add a method, description, to your Animal class. Using two separate print statements, it should print out the name and age of the animal it's called on. Then, create an instance of Animal, hippo (with whatever name and age you like), and call its description method.
'''
class Animal(object):
	"""Makes cute animals."""
	is_alive = True
	def __init__(self, name, age):
		self.name = name
		self.age = age
	# Add your method here!
	def description (self):
		print (self.name)
		print (self.age)
		
hippo = Animal("hippo", 21)

Animal.description(hippo)
'''

# 9/18 They're Multiplying!
# A class can have any number of member variables. These are variables that are available to all members of a class.
'''
class Animal(object):
	"""Makes cute animals."""
	is_alive = True
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
hippo = Animal("Hippo", 21)
cat = Animal('Tom', 4)

print (hippo.is_alive)
print (cat.is_alive)

hippo.is_alive = False

print (hippo.is_alive)
print (cat.is_alive)
'''
# 1. In the example above, we create two instances of an Animal.
# 2. Then we print out True, the default value stored in hippo's is_alive member variable.
# 3. Next, we set that to False and print it out to make sure.
# 4. Finally, we print out True, the value stored in cat's is_alive member variable. We only changed the variable in hippo, not in cat.


# 10/18 
#  This code is a more realistic demonstration of the kind of classes and objects you might find in commercial software. Here we have a basic ShoppingCart class for creating shopping cart objects for website customers; though basic, it's similar to what you'd see in a real program.
'''
class ShoppingCart(object):
	"""Creates shopping cart objects
	for users of our fine website."""
	items_in_cart = {}
	print (items_in_cart)
	def __init__(self, customer_name):
		self.customer_name = customer_name

	def add_item(self, product, price):
		"""Add product to the cart."""
		if not product in self.items_in_cart:
			self.items_in_cart[product] = price
			print (product + " added.")
		else:
			print (product + " is already in the cart.")

	def remove_item(self, product):
		"""Remove product from the cart."""
		if product in self.items_in_cart:
			del self.items_in_cart[product]
			print (product + " removed.")
		else:
			print (product + " is not in the cart.")
my_cart = ShoppingCart("Anatoly")
my_cart.add_item("Door", 100)
my_cart.add_item("Table", 2)
my_cart.add_item("Door", 100)
my_cart.add_item("Pen", 3)
print (ShoppingCart.items_in_cart)
my_cart.remove_item('Pen')
print (ShoppingCart.items_in_cart)
'''

#11/18
#Inheritance is a tricky concept, so let's go through it step by step.

#Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an is-a relationship. For example, a Panda is a bear, so a Panda class could inherit from a Bear class. However, a Toyota is not a Tractor, so it shouldn't inherit from the Tractor class (even if they have a lot of attributes and methods in common). Instead, both Toyota and Tractor could ultimately inherit from the same Vehicle class.

# Check out the code in the editor. We've defined a class, Customer, as well as a ReturningCustomer class that inherits from Customer. Note that we don't define the display_cart method in the body of ReturningCustomer, but it will still have access to that method via inheritance. Click Save & Submit Code to see for yourself!

'''
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print ("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print ("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
'''

# Inheritance Syntax 12/18
#In Python, inheritance works like this:
'''
class DerivedClass(BaseClass):
	# code goes here
'''
#where DerivedClass is the new class you're making and BaseClass is the class from which that new class inherits.
'''
class Shape(object):
	def __init__(self, number_of_sides):
		self.number_of_sides = number_of_sides

class Triangle(Shape):
	def __init__(self, side1, side2, side3):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3
'''

# 13/18 Override
# Sometimes you'll want one class that inherits from another to not only take on the methods and attributes of its parent, but to override one or more of them.
'''
class Employee(object):
	def __init__(self, name):
		self.name = name
	def greet(self, other):
		print ("Hello, %s " % other.name)
		
class CEO(Employee):
	def greet(self, other):
		print ("Get back to work, %s!" % other.name)

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo) # print Hello Emily
ceo.greet(emp) 
'''

'''
class Employee(object):
	"""Models real-life employees!"""
	def __init__(self, employee_name):
		self.employee_name = employee_name
		#print (employee_name)
	def calculate_wage(self, hours):
		self.hours = hours
		print (self.employee_name, " ", hours * 20.00)

# Add your code below!
class PartTimeEmployee(Employee):
	def calculate_wage(self, hours):
		self.hours = hours # Because PartTimeEmployee.calculate_wage overrides Employee.calculate_wage, it still needs to set self.hours = hours.
		print (self.employee_name, " ", hours * 30.00)

a = Employee("Andry")
b = PartTimeEmployee("Boby")
a.calculate_wage(1)
b.calculate_wage(1)
'''

#14/18 
#On the flip side, sometimes you'll be working with a derived class (or subclass) and realize that you've overwritten a method or attribute defined in that class' base class (also called a parent or superclass) that you actually need. Have no fear! You can directly access the attributes or methods of a superclass with Python's built-in super call.

# The syntax looks like this:
'''
class Derived(Base):
   def m(self):
       return super(Derived, self).m()
'''
# Where m() is a method from the base class.
'''
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)
		
milton = PartTimeEmployee("AnyName")
print (milton.full_time_wage(10))
'''

# 16/18
'''
class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False
'''
# 17/18
'''
class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        if (self.angle1 + self.angle2 + self.angle3) == 180:
            return True
        else:
            return False
            
my_triangle = Triangle(90, 30, 60)
print (my_triangle.number_of_sides)
print (my_triangle.check_angles())
'''

# == CLASSES ==

# 1/11 Class basics 
#Classes can be very useful for storing complicated objects with their own methods and variables. Defining a class is much like defining a function, but we use the class keyword instead. We also use the word object in parentheses because we want our classes to inherit the object class. This means that our class has all the properties of an object, which is the simplest, most basic class. Later we'll see that classes can inherit other, more complicated classes. An empty class would look like this:
'''
class ClassName(object):
    # class statements go here
'''

# 2/11 Create an instance of a class
# We can use classes to create new objects, which we say are instances of those classes. Creating a new instance of a class is as easy as saying:
'''
newObject = ClassName()
'''

# 3/11 Class member variables
#Classes can have member variables that store information about each class object. We call them member variables since they are information that belongs to the class object.
'''
class Car(object):
    condition = 'new' # this is member variable
    def __init__(self):
        pass

my_car = Car()
'''

# Calling class member variables
#Each class object we create has its own set of member variables. Since we've created an object my_car that is an instance of the Car class, my_car should already have a member variable named condition. This attribute gets assigned a value as soon as my_car is created.

#Instructions
#At the end of your code, use a print statement to display the condition of my_car.
'''
class Car(object):
    condition = 'new' # this is member variable
    def __init__(self):
        pass

my_car = Car()
print (my_car.condition)
'''

# 7/11
'''
class Car(object):
	condition = "new"
	def __init__(self, model, color, mpg):
		self.model = model
		self.color = color
		self.mpg   = mpg

	def display_car(self):
		return "This is a %s %s with %s MPG." %  (self.color, self.model, self.mpg)

my_car = Car("DeLorean", "silver", 88)
print (my_car.display_car())
'''

# 8/11 Modifying member variables
#We can modify variables that belong to a class the same way that we initialize those member variables. This can be useful when we want to change the value a variable takes on based on something that happens inside of a class method.
# Instructions
# Inside the Car class, add a method drive_car() that sets self.condition to the string "used".
# Print the condition of your car.
# Then drive your car by calling the drive_car() method.
# Finally, print the condition of your car again to see how its value changes.
'''
class Car(object):
	condition = "new"
	def __init__(self, model, color, mpg):
		self.model = model
		self.color = color
		self.mpg   = mpg

	def display_car(self):
		return "This is a %s %s with %s MPG." %  (self.color, self.model, self.mpg)
	
	def drive_car(self):
		self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print (my_car.condition)
my_car.drive_car()
print (my_car.condition)
'''

# 9/11 Inheritance
#One of the benefits of classes is that we can create more complicated classes that inherit variables or methods from their parent classes. This saves us time and helps us build more complicated objects, since these child classes can also include additional variables or methods.

#We define a "child" class that inherits all of the variables and functions from its "parent" class like so:
'''
class ChildClass(ParentClass):
    # new variables and functions go here
'''

# Normally we use object as the parent class because it is the most basic type of class, but by specifying a different class, we can inherit more complicated functionality.
'''
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." %  (self.color, self.model, self.mpg)
    
    def drive_car(self):
        self.condition = "used"
        
my_car = Car("DeLorean", "silver", 88)
print (my_car.condition)
my_car.drive_car()
print (my_car.condition)

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.battery_type = battery_type
        self.model = model
        self.color = color
        self.mpg   = mpg
        
my_car = ElectricCar("red", 'Mers', 22, 'molten salt')
'''
# -= END ABOUT CLASSES =-













# Advanced Topics in Python
# INTRODUCTION TO BITWISE OPERATORS

# Firs example
'''
print (5 >> 4)  # Right Shift
print (5 << 1)  # Left Shift
print (8 & 5 )  # Bitwise AND
print (9 | 4)   # Bitwise OR
print (12 ^ 42) # Bitwise XOR
print (~88)     # Bitwise NOT
'''
# Lesson I0: The Base 2 Number Systems 
## You can also represent numbers in base 8 and base 16 using the oct() and hex() functions. 

'''
print (0b1011)
print (bin(1))
'''
'''
n = 15
print (n)
print (bin(n)) # 2
print (oct(n)) # 8 
print (hex(n)) # 16 
'''

# int() convert
	#int("110", 2)
	# ==> 6
	#When given a string containing a number and the base that number is in, the function will return the value of that number converted to base ten.
'''
print (int("1",2))
print (int("10",2))
print (int("111",2))
print (int("0b100",2))
print (int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print (int("11001001",2))
s = hex(1234921234)
print (s)
print (int(s,16))
'''

# Left shift (>>) and Right Shift (>>)
'''
print (int('1',2))
print (int('01',2))
print (int('001',2))
print (int('0001',2))

print (0b1 << 2)
print (0b01 << 2)
print (0b001 << 2)
print (0b0001 >> 2)

print (0b0010100)
print (0b10100 >> 3)
print (20 >> 3)
'''

# The bitwise AND (&) operator
"""
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1

a:	00101010	42
b:	00001111	15       
===================
a & b:	00001010	10

0b111 (7) & 0b1010 (10) = 0b10 (2)
"""

# The bitwise OR (|) operator
'''
0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1

a:	00101010  42
b:	00001111  15       
================
a | b:  00101111	47

111 (7) | 1010 (10) = 1111 (14)
'''

# The XOR (^)(exclusive or) operator
"""
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0 

a:	00101010	42
b:	00001111	15       
================
a ^ b:	00100101	37

111 (7) ^ 1010 (10) = 1101 (13)
"""

# The bitwise NOT operator (~) 
##  ...this is equivalent to adding one to the number and then making it negative.
'''
print (~1)		# this return -2
print (~2)		# this return -3
print (~3)		# this return -4
print (~42)		# this return -43
print (~123)	# this return -124
'''
"""
The bitwise NOT operator in C++ is the tilde character ~. Unlike & and |, the bitwise NOT operator is applied to a single operand to its right. Bitwise NOT changes each bit to its opposite: 0 becomes 1, and 1 becomes 0. For example:
    0  1    operand1
   ----------
    1  0   ~ operand1
    int a = 103;    // binary:  0000000001100111
    int b = ~a;     // binary:  1111111110011000 = -104
"""
'''
n = 0b1010
print (0b1010)
print (bin(n))

n = 0b111
print (~n)
print (bin(~n))

x = bin(103)
print (int(x, 2))
'''

'''
print (int('00110100',2))
print (bin(52))
n = ~0b00110100
print (n)
print (bin(n))
'''

# Bit Mask
'''
num  = 0b1100
mask = 0b0100
desired = num & mask
print (desired) #0100
if desired > 0:
    print ("Bit was on")
'''
	
'''
def check_bit4(x):
    mask = 0b1000
    n = x & mask
    if n > 0:
        return 'on'
    else:
        return 'off'  
print (check_bit4(0b1))
'''

#14/14
'''
def flip_bit(number,n):
    mask=(0b1<<n-1)
    return bin(number^mask)
'''


































# Dictionary.items()
'''
movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}

print (movies.items())
'''
# Slicing strings
'''
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print (message)
'''





























# = ABOUT LAMBDA =
# Python supports an interesting syntax that lets you define one-line mini-functions on the fly. Borrowed from Lisp, these so-called lambda functions can be used anywhere a function is required.

def anyf(x):
	a = x*2
	return a

g = lambda x: x * 2
print (g(5)) 
# This is a lambda function that accomplishes the same thing as the normal function above it. Note the abbreviated syntax here: there are no parentheses around the argument list, and the return keyword is missing (it is implied, since the entire function can only be one expression). Also, the function has no name, but it can be called through the variable it is assigned to.

print ((lambda x: x*100)(4)) # You can use a lambda function without even assigning it to a variable. This may not be the most useful thing in the world, but it just goes to show that a lambda is just an in-line function.




# Filter. lambda
'''
my_list = list(range(16))
print (filter(lambda x: x % 3 == 0, my_list))


def f(x):
    return x % 3 == 0
l = list(filter(f, range(16)))
print (l)

nl = [n for n in range(16) if n%3 == 0]
print (nl)

####
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print (filter(lambda x: x == "Python", languages)) #Python 2
print([n for n in languages if n == "Python"]) 

####
cubes = [x**3 for x in range(1, 11)]
print (cubes)
print (filter(lambda x: x % 3 == 0, cubes)) #Python 2
print ([n for n in cubes if n % 3 == 0])

squares = [n**2 for n in range(1,11)]
print(filter(lambda x: x >= 30 and x <= 70, squares)) # Python 2
print([n for n in squares if n >= 30 and n <= 70])




# Why don't work filter in python 3 
# http://stackoverflow.com/questions/12319025/filters-in-python

# It looks like you're using python 3.x. In python3, filter, map, zip, etc return an object which is iterable, but not a list. In other words,

# filter(func,data) #python 2.x
# is equivalent to:

# list(filter(func,data)) #python 3.x
# I think it was changed because you (often) want to do the filtering in a lazy sense -- You don't need to consume all of the memory to create a list up front, as long as the iterator returns the same thing a list would during iteration.

# If you're familiar with list comprehensions and generator expressions, the above filter is now (almost) equivalent to the following in python3.x:

# ( x for x in data if func(x) ) 
# As opposed to:

# [ x for x in data if func(x) ]
# in python 2.x

###
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print (message)

message = (n for n in garbled if n != "X")
print (message)

for n in garbled:
	if n != "X":
		print (n, end = " ")


'''

# = END ABOUT LAMBDA =


























# == 	 LISTS ==

# creating a list by range()
'''
new_list = range(10) # for python 2
print (new_list)

new_list = list(range(10))
print (new_list)

list_2 = [n for n in range(5)]
print (list_2)

list_even = [n for n in range(12) if n % 2 == 0] # creating list with even integers
print (list_even)
'''



# List Comprehension Syntax

'''

list_1 = [n for n in range(6)]
print ("list_1: ", list_1)

list_2 = [n for n in range(4,14)]
print ("list_2: ", list_2)

list_3 = [n for n in range(0,6)]
print ("list_3: ", list_3)

print (list_2.index(7)) # getting index of item
print (list_2[0]) # print item according index

list_4 = [n*2 for n in range (7)] 
print (list_4)

list_5 = [n*2 for n in range (12) if (n*2)%3 == 0] # creating list with doubled numbers that are evenly divisible by three.
print (list_5)

list_6 = [n for n in range(9) if n%3 == 0]
print (list_6)

list_7 = [n for n in range (24) if n%4 == 0]
print (list_7)

list_even_squares = [n**2 for n in range(2,11) if (n**2)%2 == 0]
print (list_even_squares)

cubes_by_four = [n**3 for n in range (1,11) if (n**3)%4 == 0]
print (cubes_by_four)

c = ['c' for x in range (7) if x > 3]
print (c)

a = list(range(1,11)) # 11 won't be included in list
print ("list 'a': ",a)

# List Slicing Syntax
#List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:

#[start:end:stride]
#Where "start" describes where the slice starts (inclusive), "end" is where it ends (exclusive), and "stride" describes the space between items in the sliced list. For example, a stride of 2 would select every other item from the original list to place in the sliced list.

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print (l[2:9:2])
L2 = [n for n in range(10)]
print (L2[0:10:3])
print (L2[1:10:2])

'''

# Omitting indices (of lists)
'''
lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print (lst)
print (lst[:3])
print (lst[3:])
print (lst[::2])
'''

# Reversing a List
'''
lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print (lst)
print (lst[::-1])

my_list = list(range(1, 11))
print (my_list)

backwards = my_list[::-1]
print (backwards)

a = [n*2 for n in range(1,11) if n % 2 == 0]
print (a[::-1])
'''

#Stride Length
'''
x = [n for n in range(101)]
print (x)
a = x[::10]
print (a)
'''

# Practice 11/18
'''
to_21 = [n for n in range(1,22)]
print (to_21)

odds = [n for n in range(1,22) if n % 2 != 0]
print (odds)

odds2 = list(range(1,22))
odds2 = odds2[::2]
print (odds2)

middle_third = to_21[7:14]
print (middle_third)
'''

'''
# List with two conditions
threes_and_fives = [n for n in range(1,16) if n % 5 == 0 or n % 3 == 0]
print (threes_and_fives)
'''
# == END ABOUT LISTS ==





































# .items() .keys() .values()
'''
my_dict = { "One" : 13, "Two" : 2, 4 : "Hello", 4 : 4, '4' : 'four' }
print (my_dict.items())
print (my_dict.keys())
print (my_dict.values())
'''

# The 'in' Operator
# For iterating over lists, tuples, dictionaries, and strings, Python also includes a special keyword: in. You can use in very intuitively, like so:
'''
for number in range(5):
    print (number)

d = { "name": "Eric", "age": 26 }
for key in d:
    print (key, d[key])

for letter in "Eric":
    print (letter)  # note the comma!
'''

















# Exam Statistics 
'''
grades = [100, 100, 90, 40, 89, 100, 85, 70, 50, 79, 60, 85, 94.5]
def print_grades(grades):
	for n in grades:
		print (n)

def grades_sum(grades):
	total = 0
	for n in grades:
		total += n
	return total
	
def grades_average(grades):
	average = grades_sum(grades)/float(len(grades))
	return average
	
def grades_variance(scores): 
	average = grades_average(scores)
	varience = 0
	for score in scores:
		varience += (average - score) ** 2
	return varience/len(scores)
# read more about Standard Deviation and Variance you can here http://www.mathsisfun.com/data/standard-deviation.html

def grades_std_deviation(variance):
    return variance ** 0.5
variance = grades_variance(grades)


print_grades(grades)
print ("Sum of grades: ", grades_sum(grades))
print ("Average grade: ", grades_average(grades))
print ("Variance: ", (grades_variance(grades)))
print ("Standart deviation: ", grades_std_deviation(variance))
'''


# Practice Makes Perfect
### median
'''
def median(lst):
	lst.sort()
	if len(lst) % 2 == 0: # even
		return (lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1])/2
	else: 
		return lst[int(len(lst)/2)]
numbers = [4, 5, 5, 4]

print (median (numbers))
'''





### remove_duplicates
# remove_duplicates([1,1,2,2]) should return [1,2]
'''
def remove_duplicates(lst):
	new_lst = []
	for n in lst:
		if n not in new_lst:
			new_lst.append(n)
	return new_lst

words = [2,2,3,3,1,2,3,4,4,5,3,7,7,8,9,8,7,5,4,2]
print (remove_duplicates(words))
'''


###product
'''
def product(lst):
	total = 1
	for n in lst:
		total *= n
	return total
one = [4, 5, 5, 2]
print (product(one))
'''


### purify
# Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.
'''
def purify(lst):
	new_lst = []
	for n in lst:
		if n % 2 == 0:
			new_lst.append(n)
	return new_lst
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print (purify(a))
'''


### count
#Return the number of times the item occurs in the list. For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).
### my solution
'''
def count(sequence, item):
	total = 0
	for n in sequence:
		if n == item:
			total += 1
	print (total)
count (['a', 's', 5.2, 'a', 'b', 2, 'a'], 'a')
'''

### censor
# You can use string.split()  and  " ".join(list) to help you here.
#Remember: "*" * 4 equals "****"

#After splitting the string with string.split(), you can loop through the indices in the list and replace the words you are looking for with their asterisk equivalent. Join the list at the end to get your sentence!

### my solution
'''
def censor(text, word):
	lst = (text.split())
	for n in lst:
		if n == word:
			lst[(lst.index(n))] = "*" * len(n)
	return (" ".join(lst))
print (censor('hello my bad, badly fried', 'bad'))
'''
'''
### second solution
def censor (text, word):
	if word in text:
		text = text.replace(word, "*" * len(word))
	return text
print (censor('hello my bad, badly, fried', 'bad'))
'''
### third solution
'''
def censor (text, word):
	text = text.replace(word, "*" * len(word))
	return text
print (censor('hello my bad, badly, fried', 'bad'))
'''


### scrabble_score
'''
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
		"f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
		"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
		"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
		"x": 8, "z": 10}
		
def scrabble_score (word):
	word = word.lower()
	total = 0
	for char in word:
		if char in score:
			n = score[char]
			total += n
	return total
			
print(scrabble_score (input("Enter any word: ")))
'''









###anti_vowel "Hello my friend"
### my solution
'''
def anti_vowel(text):
	vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
	new_text = ''
	for char in text:
		for v in vowels:
			if v == char:
				a = True
				#return a
				break
			else:
				a = False
		if a == True:
			new_char = ''
			new_text += new_char
		else:
			new_text += char
	return new_text
print(anti_vowel(input("Type any phrase: " )))
'''
### simplest solution
'''
def anti_vowel(text): 
	total = ""
	for char in text:
		if char not in 'AEIOUaeiou':
			total = total + char
	return total
print(anti_vowel(input("Type any phrase: " )))
'''


	
	
	

### reverse my solution
'''
def reverse(text):
	total = ''
	m = len(text)
	for n in text:
		x = text[m-1]
		m -= 1
		total += x
	return total
		
print (reverse(input("Enter any word: ")))
'''
### reverse solution 1:
'''
def reverse(text):
	total = ''
	index = len(text) - 1
	while index >= 0:
		total += text[index]
		index -= 1
	return total
		
print (reverse(input("Enter any word: ")))
'''





'''
### even
def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False

def is_int(x):
	if x == int(x):
		return True
	else:
		return False

def digit_sum(n):
	total = 0
	for one in str(n):
		one = int(one)
		if one >= 1:
			total += int(one)
	return total

### factorial solution of mine
def factorial(x):
	a = 1
	n = 1
	for multi in range(x):
		a = a * n
		n += 1
	return(a)
		
factorial(3)

### factorial solution # 1
def factorial(x):
	total = 1
	for digit in range(1, x+1):
		total = total * digit
	return total
	
factorial(3)

### factorial solution # 2
def factorial(x):
	total=1
	while x>0:
		total *= x
		x-=1
	return total
factorial(7)
'''
### prime
'''
def is_prime(x):
	prime = True
	if x < 2:
		prime = False
	elif x == 2:
		prime = True
	else:
		for y in range(2, x):
			z = x % y
			if z == 0:
				prime = False
				break
			else:
				prime = True
	return prime
	
print (is_prime(int(input("Enter number: "))))
'''


	






# for/else
# Just like with while, for loops may have an else associated with them.
# In this case, the else statement is executed after the for, but only if the for ends normally—that is, not with a break. This code will break when it hits 'tomato', so the else block won't be executed.
'''
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
    if f == 'tomato':
        print ('A tomato is not a fruit!') # (It actually is.)
        break
    print ('A', f)
else:
    print ('A fine selection of fruits!')
'''




# Zip
'''
list_a = [1, 2, 3, 4, 5]
list_b = [100, 3, 4, 34, 43, 2, 4343, 34]

for a, b in zip(list_a, list_b):
    print (a,b)
'''

# Enumerate
'''
words = ['Hello', 'How', 'Where', 'Beautiful', 'Thanks', 'Take', 'Care', 'Doctor', 'Make', 'Sure', 'Do', 'Get', 'Go', 'Are', 'Table', 'Desk', 'Dictionary', 'Look']

for index, number in enumerate(words):
	print (index+1, number) # print from 1 instead 2
'''



# Looping over a dictionary
'''
dictionary =  { 'x' : 10, 'y' : 11, 'a' : 10, 'b' : 8, 'c' : 5, 'v' : 10 }

for n in dictionary:
	if dictionary[n] == 10:
		print ("getting key: ", n)
		print ("getting value by key: ", dictionary[n])
'''

#from random import randint
'''
import random
x = []
for n in range(10):
	n = random.randint(0,10)
	x.append(n)
print (x)

a = []
for n in x:
	n = n ** 2
	a.append(n)
print (a)
'''





# Replace char by 'for' loop
'''
phrase = "A bird in the hand..."
for char in phrase:
    if char == "A" or char == "a":
        char = "X"
        print (char, end=" ")
    else: 
        print (char, end=" ") 
'''



# Single Line Output for the 'for' loop in Python 3
'''
name = "Nice to meet you World!"
for x in name:
	print (x, end = " ") # 'end = " "' is the separator
'''







# Hobbies
'''
hobbies = []
nothing = ", "
h = 0
number = 1
# Add your code below!
while h < 3:
	b = input("What is your hobby №%s ? " % number)
	hobbies.append(b)
	h += 1
	number +=1
else:
	print ("Your hobbies is: ", nothing.join(hobbies))
'''	



	

# 8/19 
'''
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
guesses_left = 3
# Start your game!
while guesses_left > 0:
	guess = int(input("Guess number: "))
	if guess == random_number:
		print ("You are winner!")
		break
	guesses_left -= 1
else:
	print ("You lose!")
'''

# While/else
'''
import random
print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

count = 0
while count < 3:
    num = random.randint(1, 6)
    print (num)
    if num == 5:
        print ("Sorry, you lose!")
        break
    count += 1
else:
    print ("You win!") # else execute when 'while' ended, but 'else' don't execute if 'while' is 'break' 
'''



# Break
'''
count = 0
while True:
	print (count)
	count += 1
	if count >= 11:
		break
'''



# Simple Error
'''
userinput = input("Enter Y or X: ").upper()
while userinput != "Y" and userinput != "X":
	userinput = input("Try again! Only Y or X!: ").upper()
print ("You've entered: ", userinput)
'''



#While
'''
num = 1

while num <= 10:  
    print (num, "squared is ", num**2)
    num += 1
'''
   

'''
alphabet = "abcdefghijklmnopqrstuvwxyz" #change it into list
a = 0
b = len(alphabet)
c = " "

while a < b:
	d = (alphabet[a].upper() + alphabet[a]) + " "
	c += d
	print ("\n", c)
	a += 1
'''

	




#Battleship another version
'''
from random import randint

board = []
for s in range(10):
	s = ["O"]*10
	board.append(s)
	
def print_board(board):
	for row in board:
		print (" ".join(row))
		
print_board(board)

def random_row(board):
    return randint(0,len(board) - 1)
    
def random_col(board):
    return randint(0,len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print ("Ship Row: ", ship_row)
print ("Ship Col: ", ship_col)


for turn in range (4):
	print ("Round", turn + 1)
	guess_row = int(input("Guess Row: "))
	guess_col = int(input("Guess Col: "))
	if guess_row == ship_row and guess_col == ship_col:
		print ("Congratulations! You sunk my battleship!")
		break
	else:
		if guess_row not in range(0, 10) or guess_col not in range(0, 10):
			print ("Oops, that's not even in the ocean.")
		elif board[guess_col][guess_row] == "X":
			print ("You guessed that one already.")
		else:
			print ("You missed my battleship!")
			board[guess_col][guess_row] = "X"
			print_board(board)
		
	if turn == 3:
		print("Game Over")
'''

#BattleShip
'''
from random import randint

board = []
for s in range(5):
	s = ["O"]*5
	board.append(s)
	
def print_board(board):
	for row in board:
		print (" ".join(row))
		
print_board(board)

def random_row(board):
    return randint(0,len(board) - 1)
    
def random_col(board):
    return randint(0,len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

print ("Ship Row: ", ship_row)
print ("Ship Col: ", ship_col)


guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))


#############################

if guess_row == ship_row and guess_col == ship_col:
	print ("Congratulations! You sunk my battleship!")
	
else:
	if guess_row not in range(0, 5) or guess_col not in range(0, 5):
		print ("Oops, that's not even in the ocean.")
	elif(board[guess_row][guess_col] == "X"):
		print ("You guessed that one already.")
	else:
		print ("You missed my battleship!")
		board[ship_row][ship_col] = "X"
	for turn in range (4):
		print ("Turn", turn + 1)
		guess_row = int(input("Guess Row: "))
		guess_col = int(input("Guess Col: "))
	print_board(board)
	
	if turn == 3:
		print("Game Over")
'''

	



"""
guess_row = int(input("Guess Row: "))
guess_col = int (input("Guess Col: "))
"""





# list into list
'''
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(x):
	a = []
	for b in x:
		for c in b:
			a.append(c)
	return a
n = (flatten(n))

print (n)
'''






'''
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
	total = words[0] + words[1]
	return total

print(join_strings(n))
'''


'''
n = "asdfasdf"
a = "hello"
b = "Wow"
c = a + b + n
print (c)
'''



















# exercise 
'''
a = [2, 4, 5, 7, 9, 8, 10]

#method 1
for i in a:
	print (i)
	
#method 2
for i in range(0, len(a)):
	print (a[i])
	
# Method 1 is useful to loop through the list, but it's not possible to modify the list this way. Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed.

n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(0, len(numbers)):
        result = numbers[i] + result
    return result
    
print (total(n))
'''




#range 
'''
n = [3, 5, 7]
def double_list(x):
	for i in range(0, len(x)):
		x[i] = x[i] * 2
	return x

print (double_list(n))
'''

'''
n = [3, 5, 7]

def print_list(x):
	for i in range(1, len(x)):
		print (x[i])
    
print_list(n)
'''
#
'''
n = [3, 5, 7]

def print_list(x):
	for i in x:
		print (i)
    
print_list(n)
'''



# Student Becomes the Teacher
'''
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def average(numbers):
	total = sum(numbers)
	total = float(total)
	total = total / len(numbers)
	return total

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6
	
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
#print (get_letter_grade(get_average(alice)))
print (get_average(alice))

students = [lloyd, alice, tyler]
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
	


print (get_class_average(students))
print (get_letter_grade(get_class_average(students)))
'''








# remind how to create a dictionary
'''
animals = {
	"cat" : ['meow', 'purr'],
	"dog" : ['woof', 'bark']
}

print (animals['cat'])
'''








# Shopping
'''
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
print ("\n\nStock before sell:\n")
print (stock)

def compute_bill(food):
	total = 0 
	for n in food:
		if stock[n] > 0:
			total += prices[n]
			stock[n] = stock[n] - 1
	return total
print("\nTotal bill: ", compute_bill(shopping_list))

print ("\n\nStock after sell:\n")
print (stock)
'''

	





# Making a Purchase
'''
def Adding(numbers):
	total = 0
	for any in numbers:
		total += any # it's the same as total = total + any
	return total

x = [2, 4, 10, 6, 8]
print (Adding(x))
'''


# 8/13 Keeping Track of the Produce
'''
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print (key)
    print ("price: %s" % prices[key])
    print ("stock: %s" % stock[key])

total = 0
for key in prices:
	total += prices[key] * stock[key] # total = total + prices[key] * stock[key]
print ("\n", total)
'''

	





# My Functions
'''
def Funk(n, x):
	y = n + x
	return y


def Inputing():
	c = int(input("enter number: "))
	d = int(input("enter number: "))
	return Funk(c, d)
	

count = Inputing()

print (count)
'''









# String Looping
'''
print()
for asdf in "Codecademy":
	print (asdf)
	
word = "Hello, my friend! Have a nice day! I have to go!"

print()
print()

for n in word:
	if n == "H" or n == "h":
		print (n)

# Lists + Functions
#Functions can also take lists as inputs and perform various operations on those lists.
'''

# Write your function below!
'''
def fizz_count(x):
	count = 0 
	for n in x:
		if n == "fizz":
			count = count + 1
	return count
            
any = ['fizz', 'fizz', 'asdf', 'fizz', 'hi', 'fizz']
a = fizz_count(any)
print (a)
'''

'''
def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 5, 16, 4, 42, 7]
small = count_small(lost)
print(small)
'''




# Control Flow and Looping. n % 2 == 0 
'''
numbers = [1, 4, 4, 6, 7, 9, 11, 3, 12, 6, 9, 4]
for a in numbers:
	if a >= 9:
		print (a)

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for n in a:
    if n % 2 == 0:
        print (n)
'''

# for and key
'''
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
	print (webster[key])
'''


# Dictionaries
# A dictionary is similar to a list, but you access values by looking up a key instead of an index. A key can be any string or number. Dictionaries are enclosed in curly braces, like so:

# d = {'key1' : 1, 'key2' : 2, 'key3' : 3}

# Dictionaries are great for things like phone books (pairing a name with a phone number), login pages (pairing an e-mail address with a username), and more!
'''
dic = {'Nick' : 102, 'S' : 222, 'Jack' : 343 }

print (dic['Jack'], dic['S'])
print (dic['S'])
'''
#New Entries
'''
menu = {} # empty dictionary 
menu['Eggs'] = 20.50  # Adding new key-value pair
menu['Potatoes'] = 35
menu['Fish'] = 40
menu['Cheese'] = 37
#del menu['Cheese']
menu['Cheese'] = 11111

zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',

'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

print ('There\'is ' + str(len(menu)) + ' dishes in our menu.')
print (menu)
print (zoo_animals)
'''

# removing
'''
lists = ['one', 'two', 'three', 'four', 'five', 'six']

lists.remove('one')
print (lists)
'''

# list into a dictionary
'''
my_dic = {
	'number' : 124,
	'word' : 'any word',
	'lists' : [1, 2, 3, 4, 5, 7],
	'lists of words' : ['Hello', 'how', '!', 'b', ',', '4', 'hey', '.', 'OK', ';', 'Friend', ':', '-10', 'are', 'you', '?', 'About', 'about'],
	'float' : 3.5
}

my_dic['lists of words'].sort()

n = my_dic['float'] + my_dic['lists'][5]

print (len(my_dic))
print (my_dic['lists'][5], my_dic['float'])
print (n)
print (my_dic['lists of words'])
'''
#14/14
'''
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Adding a key 'pocket' and assigning a list to it
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Sorting the items into the list stored under 'backpack'
inventory['backpack'].sort() 

# Removing 'dagger' from the list of items stored under the 'backpack' key
inventory['backpack'].remove('dagger') 

# Adding 50 to the number stored under the 'gold' key
inventory['gold'] = inventory['gold'] + 50

n = 20 + inventory['gold']

print (inventory['gold'])
print (n)
'''

















#For One and All
# If you want to do something with every item in the list, you can use a FOR loop. 

# for variable in list_name:
    # Do stuff!
'''
my_list = [1, 3, 100, 23, 4, 9]

for n in my_list:
	print (n, " * 100 = ")
	print (100 * n)
'''
	
# More with 'for'
# If your list is a jumbled mess, you may need to .sort() it.
'''
animals = ["bat", "cat", "ant", "wolf", "bird", "bee"]
animals.sort()
print (animals)

for n in animals:
	print (n)
'''
###### 9/14 List, 'for', .append(), .sort()
'''
start_list = [25, 11, 12, 5, 1, 32, 3, 7, 9, 4, 100]
square_list = []
	

for n in start_list:
	n = n ** 2
	square_list.append(n)
	
square_list.sort()
print (square_list)
'''



	






# Maintaining Order (.index() , .insert() )
'''
animals = ["ant", "bat", "cat"]
#animals.insert(1, "dog")
n = animals.index("cat")
animals.insert(n, "panda")


print(animals.index("bat"))
print (animals)
'''

# Slicing Lists and Strings
'''
my_list = "Hello"

n = my_list[:2]
b = my_list[0:2]

print (n)
print (b)
'''


# List Slice 
'''
letter = ['a', 'b', 'c', 'd']
slice = letter[1:3]
print (slice)
print (letter)

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]            # Third and fourth items (index two and three)
last = suitcase[4:6] # or [4:]         

print (first)
print (middle)
print (last)
'''

# any program from cuberforum.ru. 
'''
print("Enter the number 1 and 2:")
a = int(input()) # use int to enter integer type 
b = int(input())
print("Your numbers were " + a + " and " + b + ".")

input() # to keep console open
'''



# Lists
'''
animals = ["bird", "bat", "bull", "bear"]

if len(animals) > 2:
	print ("First: " + animals[0])
	print ("Second: " + animals[3])
	print ("Third: " + animals[1])
	
numbers = [1, 3, 5]
 
print (numbers[2])

anylist = ['a', 'back', 'new']
anylist.append('ADDING')
print (len(anylist))
print (anylist)
'''


# The Cost Of The Trip
'''
def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        return cost - 50
    elif days >= 3:
        return cost - 20
    else:
        return cost
        
def trip_cost(city, days, spending_money):
    city = plane_ride_cost(city)
    days = rental_car_cost(days) + hotel_cost(days)
    return city + days + spending_money

a = str(input("Which city? "))
b = int(input("How many days? "))
c = int(input("How much money are you giving with you? "))
print ("Your trip will be cost", trip_cost(a, b, c) , "dollars")
input()
'''














'''
def double(n):
    return 2 * n
	
def triple(p):
    return 3 * p

def add(a, b):
    return double(a) + triple(b)

print (add (2, 2))
'''









# any code with or s
'''
def distance_from_zero(any):
    if type(any) == int or type(any) == float:
        return abs(any)
    else:
        return "Nope"
	
n = input("Enter any text")
print (distance_from_zero(n))
'''

# my exercise with function
'''
def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

n = input("Type your text")
s = n.lower()
print (shut_down(s))
'''






#the type() function returns the type of the data it receives as an argument.
'''
print (type (1234))
n = "hello"
b = 3.4
print (type(n))
print (type("hi"))
print (type(b))
'''

# On Beyond Strings 
'''
def biggest(*args):
	print (max(args))
	return max(args)
	
def smallest(*any):
	print (min(any))
	return min(any)
	
def distant_from_zero(number):
	print (abs(number))
	return abs(number)
	
biggest(-100, 8, 123, -2, 124, 5, 22)
smallest(-10, 3, 100, -3)
distant_from_zero(43)

n = max(1, 100, 3, 4)
m = min(-3, 0, 1234)
absolute = abs(1-10+3)
print (n, m, "and" , absolute)
'''






# Format method
'''
age = 22
name = "Anatoly"

print ("{0} is {1} years old" .format(name, age))
print ("Why is {0} playing with python?" .format(name))
'''





# The code in the editor will show you everything available in the math module.
'''
import math
everything = dir(math)
print (everything)
'''


# What is return.  return causes your function to exit and hand back a value to its caller.
'''
def square(n):
    return n * n
	

def add_one(n):
	return n + 1

print (square(12)) #square(12) - caller
print (add_one(square(12)))
print (add_one(144))
'''



#Function Junction
# def spam ():
	# """This is spam function"""
	# print ("Eggs")
# spam()

#Call and Response
# def square(n, b):
	# """returns the square of the number"""
	# x = n ** b
	# print("%d squared is %d." % (n, x))
	# #return x

# any = 10
# square(45, 2)




# Random with 100000 lines
'''
import random
a = 3
for turn in range(100000):
	if a < 4:
		c = random.randint(0, 1000000000000000000000000000000000000000000)
		print (c)
'''

# Random    Matrix
'''
import random
a = [1,2,3]
b = random.choice(a)

while b < 4: 
	c = random.randint(0,10000000000000000000000000000000000000000000000000)
	print (c)
'''
	

# Datetime
'''
from datetime import datetime

meal = 44.50
tax = 6.75/100
tip = 15.0/100

meal = meal + meal * tax

total = meal + meal*tip

print(total)
print("%.2f" % total)

brean = "Hello Brean!"

x = "There's a snake in my boot"
s = "cants"[0]

print ("The value a pi is around " + str(3.14))


now = datetime.now()

print (now.hour)
print (now.minute)
print (now.second)
'''


# STRING FORMATTING WITH %, PART 1
'''When you want to print a variable with a string, there is a better method than concatenating strings together.

name = "Mike"
print "Hello %s" % (name)

The % operator after a string is used to combine a string with variables. The % operator will replace a %s in the string with the string variable that comes after it.

'''
'''
x = input ("Enter you name ")
x = (x.upper())
y = len(x) 
print ("Your name is %s. Length of your name is %s symbols" % (x, y))

a = input ("Nice work! Try again: ")
a =(a.lower())
print ("%s" % (a))
'''




#Code from lesson
'''
def clinic():
	print ("You've just entered the clinic!")
	print ("Do you take the door on the left or the right?")
	answer = input("Type left or right and hit 'Enter'.").lower()
	if answer == "left" or answer == "l":
		print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
	elif answer == "right" or answer == "r":
		print ("Of course this is the Argument Room, I've told you that already!")
	else:
		print ("You didn't pick left or right! Try again.")
		clinic()

clinic()
'''
#Compare closely
'''
et's start with the simplest aspect of control flow: comparators. There are six:

Equal to (==)
Not equal to (!=)
Less than (<)
Less than or equal to (<=)
Greater than (>)
Greater than or equal to (>=)

'''

# This and That (or This, But Not That!)
'''
Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last.

For example, True or not False and False returns True. If this isn't clear, look at the Hint.

Parentheses () ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit.
'''







