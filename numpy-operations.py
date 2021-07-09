# Used For Mathmetical Operations ,Multidimentioal Array

import numpy as np 

# Create Nummpy Array

a = np.array([1,2,3,6])

 # "ndim() "Calculate Dimension of Numpy Array

# 2d Array =>>Matrix

b = np.array([[1,2,3],[4,5,6]]) #SHAPE OF 2D Array ,Count Num. of Rows and cols

C = np.array([[[1,2],[3,4]],[[6,8],[9,6]]]) # Create 3d Array 

# Funnctions
numPyArrange=np.arange(1,60,2) # 1 = start , 60= end Point But include, 2 = gap between from 1 to 60 

# Linear Space
npLinespace = np.linspace(0,1,3) # 0 = start , 1 = end Point , 3= from 0 to 1 divide in 3 Equal parts 

npOnes = np.ones((2,6)) # Creating Matrix With 5 rows and 6 colums with Once
npZeros = np.zeros((5,6)) # Creating Matrix With 5 rows and 6 colums with Zeros

np.Eye= np.eye(2,3) # For Diagonal Element Will be 1 Rest are 0

diagonalMatrix = np.diag([5,6,9,8]) # Diag() , 5,6,9,8 will be diagonal elemet rest are zero 

getOnlyDiagonalElemets = np.diag(diagonalMatrix) # Get Only Diagonal Elemets 

# Create Random Numbers/Array/Matrixs
RandomNumberGenerator = np.random.rand(4) # Return array of random number size 4

RandomNumber = np.random.randint(1,40,6) # Total Number = 6 , From 1 , To 40

a = np.arange(6) # [1,2,3,4,5,6] means Integer Type 

a.dtype    #  Result int64 cause it , But I Want Float 

floatValues = np.arange(6,dtype='float64') # [0.,1.,2.,3.,4.,5.,6.] Becuse We Define Dtype as FLOAT

floatValues.dtype # Retrun me Float Data type Value

BooleanArray = np.array([True,False,False,True])

typeOfBolleanArray =BooleanArray.dtype  # Outpu is Boolean 

# Some Index Calculations
Demo = np.array([2,6,9,3]) 

p = Demo[2]  # Output = 9 , coz Array starts with index 0

# Create a Diagonal Matrix
diagonalMatrixD = np.diag([2,6,9,3])  # Create Dummy Diagonal Matrix

# Question : How To Access "6" from Above Matrix
# Ans 

diagonalMatrixD[2,2]  # We will Access 2,d Rwo and 2nd Colum

# We Can Assign Value To Specifi Matrix Location 
# Exp : 
diagonalMatrixD[2,2] = 15 # now above diagonal element at postion 2nd row and 2nd colum will changae from 9 to 15

# Sharing memory (IMPORTANT POINT OF MEMORY SPACE)
a = np.arange(10) # OUTPUT = [0,1,2,3,4,5,6,7,8,9]
b =a[::2] #output => [0,2,4,6,8]

# share_memory Function Means, the array a,b share same memory Location and diffrenciate There Values  
p =np.shares_memory(a, b)  # True =>Share Memory False Not share memory 

a = np.arange(5) # Output = Generate [0,1,2,3,4] npArray

aPlusOne = a+1  # Output = [1,2,3,4,5] it Will Add 1 into all Elements This Operations are ELEMET WISE OPERATIONS

squerOfA = a**2 # Copute squere Coz This Operations are ELEMET WISE OPERATIONS 

b = np.ones(5)+1

c = a-b # Oprtaion Perform Element Wise if Element are not same in both show Error 

DiagonalDummy = np.diag([1,2,3,4])
# let Us Dot Product of Matrix 
dotProductResult = DiagonalDummy.dot(DiagonalDummy)

# How To Compair Two Numpy Arrays
a = np.array([1,2,3,4,5]);
b = np.array([1,2,6,5,9])
c = a==b # OUTPUT [True  True False False False], Compair Element Wise, retrun BooleanArray 
d=a>b # Mean We Can use Other Operatos like (<,>,<=,>=,+,-,*,/ )

# Logical Operator Example
a = np.array([1,1,0,0],dtype=bool)
b=np.array([1,0,1,0],dtype=bool)
np.logical_or(a,b)  #[ True  True  True False]
np.logical_and(a,b) # [ True False False False]
np.logical_and(a,b) #[ True False False False]
np.logical_not(a,b)  #[False False  True  True]


# Transcendental (Trigonmatric) Functions
a = np.arange(5) #output = [0,1,2,3,4]
np.sin(a) # Output Give me sin Vlaue Of 0 to 4
#  np.log(a)  => # Give Me Log Value from 0 to 4
# np.exp(a)  => # For Exponentional

# Basic Reductions 
x= np.array([1,2,3,4])
sum(x) # Output  = 10  sum of above NP array

x = np.array([[1,2],[2,2]])

columWiseSum = x.sum(axis=0)  # [3,4] cuse axis = 0 measn colum Wise Sum(Operations)
RowWiseSum = x.sum(axis=1) # [3,4] Row Wise Sum 

y = np.arange(9)

z = y.min()  # Output = 0 (Value), Get minimum Value 
v = y.max() # Output = 8 (Value) , Get Maximum Vlaue 
argMin = y.argmin()  # Output = 0 (Index) At Index 0 has You have Smallest Vlaue , Return Smallest Index
argMax = y.argmax()  # Output = 8 (Index) , At Index 8 You Have largest Value , Return Largest  Index


# Logical Operations 
np.all([True,True,False]) #output => FALSE becsuse All Element Are Not TRUE or  FALSE
np.all([True,True,True]) #output => True becsuse All Element Are Not TRUE 
np.all([False,False,False]) #output => True becsuse All Element Are Not False 

np.any([True,True, False]) # return True , If anyone is Tre retun True


a = np.arange(50,50)
np.any(a!=0)  # If Any of one Is not Equal To 0 (NO ) Result Is False 

a = np.array([1,2,3,2])
b = np.array([2,2,3,2])
c = np.array([6,4,4,5])
((a<=b) & (b<=c)).all()


# STASTICS
x= np.array([1,2,3,1])  
y = np.array([[1,2,3],[5,6,1]])
x.mean() # output  (1+2+3+1)/4 = 1.75
y.mean() # OUtput ((1+2+3)/3,(5+6+1)/3) ==>> (2,4) ==>> (2+4)/2 = 3.0
np.median(x)





# BRODCASTING

# Documentations : https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html

a = np.tile(np.arange(0,40,10),(3,1))
a =a.T
b = np.array([0,1,2])
c = a+b
aa = np.arange(0,40,10)
print(aa)

aa = aa[:,np.newaxis]
# If We Not Create from 1d to 2d array using np.newaxis it will show error or mismatch row and colum from aa, b 
