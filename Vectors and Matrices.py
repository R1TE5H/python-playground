# Array: Vector and Matrix
# NumPy Package
    # Allows the creation of Arrays and algebraic operations
import numpy as np
    
# Creating Arrays

# Converting a List or Tuple
array1 = np.array([0,1,2,3,4])

# Creating a Vector -- (p1 = start, p2 = end, p3 = step)
vect1 = np.arange(0,4,0.5)

# Creating an Empty Vector (single component is number of components)
vect2 = np.zeros(4)

# Set a Vector's Components
vect2[0] = 3.4
vect2[2] = 4

# Create a Unity Array (Unit Matrix)
vect3 = np.eye(3)

#Creating a 2D Array

# 2D Array Using a List of Lists
vect4 = np.array([[3,4,5,], [2,3,4]])

# 2D Array/Matrix Using the Zeros Method 
    # p1 is the number of rows and p2 is the number of columns
vect5 = np.zeros((5,4))

# Creating a Matrix With Random Values
A = np.random.randint(50,121,(3,5))
B = np.random.randint(10,61,(5,6))

# Creating a Matrix with Specified Values
u = np.array([[1,3,2,4], [7,9,2,1], [3,9,1,6]])

# Find the shape of a matrix using the shape function
    # Returns a tuple: (Num Columns, Num Rows)
vect5.shape()

# Accessing Individual Elements of a Matrix
vect5[0,1] = 99 # First Row, Second Element
vect5[4,3] = 10 # Fifth Row, Fourth Element (Last element in 5 X 4 Matrix)

#--------------------------------------------------------------------------

# Operating on a Matrix or Vector with a Number
    # Use Math Operations and each element will be operated on
vect1 *=2 # Will multiply every element by 2

# Operating on a Vector or Matrix with another Vector or Matrix
    # Use the Dot Function
    # Matrices must follow Matrix Mutliplication Laws
x = np.array([[1,2,3],[2,3,4]])
y = np.array([[9,8],[6,5], [10,11]])
z = np.dot(x,y)

#--------------------------------------------------------------------------
# Solving Linear Equations
    # Using Numpy's Linear Algebra Package
import numpy.linalg as LA

# Equations:
    # 2x + y - 2z = 3
    # x - y - z = 0
    # x + y + 3z = 12
D = np.array([[2,1,-2],[1,-1,-1],[1,1,3]])
F = np.array([3,0,12])
E = LA.solve(D,F)
print(E) # x = 3.5, y = 1, z = 2.5
    
#--------------------------------------------------------------------------
# Practice

x = np.arange(5,20,2 )
y = np.zeros(20)
y[3] = 6
y[9] = 9
y[13]= 12
y[15] = 24
z = np.sin(x)   # Trig Functions use Radians
print(x,z)
r = y +10
print(r)

u = np.array([[1,3,2,4], [7,9,2,1], [3,9,1,6]])
print(u)