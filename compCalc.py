import math
from os import name, system
from time import sleep


# Arithmetic
def add(x,y):
  return float(x+y)
  
def subtract(x,y):
  return float(x-y)
  
def multiply(x,y):
  return float(x*y)
  
def divide(x,y):
  return float(x/y)
  
def square(x):
  return float(x**2)
  
def squareRoot(x):
  return float(x**1/2)
  
def power(x,y):
  return float(x**y)

  
# Trigonometry
pi = math.pi

def pythagoreanAB(x,y):
  return float(squareRoot(square(x) + square(y)))

def pythagoreanBC(x,y):
  return float(squareRoot(square(x) - square(y)))



# Geometry
def areaOfCircle(x):
  return float(pi*square(x))

def circumferenceOfCircle(x):
  return float(pi*x*2)

def areaOfRect(x,y):
  return float(x*y)

def perimeterOfRect(x,y):
  return float(2*x + 2*y)

def areaOfRightTri(x,y):
  return float(1/2*areaOfRect(x,y))

def volumeOfSphere(x):
  return float(4/3*pi*power(x,3))

def volumeOfCube(x):
  return float(power(x,3))

def volumeOfRect(x,y,z):
  return float(x*y*z)

def volumeOfCylindar(x,h):
  return float(areaOfCircle(x)*h)

def volumeOfWedge(x,y,h):
  return float(areaOfRightTri(x,y)*h)



#Algebra
def average(nums):
  i = 0
  sum = 0
  while(i < nums.length):
    current = nums[i]
    sum = sum + current
    i += 1

  return float(sum/nums.length)

def stndDev(nums):
  mean = average(nums)
  i = 0
  sum = 0
  while(i < nums.length):
    sum = sum + square(nums(i) - mean)

  return float(squareRoot(sum/(nums.length-1)))




# Calculus
e = math.e

#Derivatives
def derivePower(x,y):
  return y*x^(y-1)

def deriveSine(x):
  return math.cos(x)

def deriveCosine(x):
  return -math.sin(x)

def deriveTangent(x):
  return 1/(math.cos(x)^2)

def deriveSecant(x):
  return math.tan(x)/math.cos(x)

def deriveCosecant(x):
  return -1/(math.sin(x)*math.tan(x))

def deriveCotangent(x):
  return -1/(math.sin(x)^2)

def deriveEToTheX(x):
  return e^x

def deriveNaturalLog(x):
  return 1/x

#Come back to work on this, need to figure out how to maintain the value of the derivative as a string
def multiplyDerivatives():
  dfx = float(input("Please enter the desired derivative of the first expression: "))
  gx = float(input("Please enter the second expression: "))
  dgx = float(input("Please enter the desired derivative of the second expression: "))
  fx = float(input("Please enter the first expression: "))
  
  return str(dfx*gx + dgx*fx)

def divideDerivatives():
  dfx = float(input("Please enter the desired derivative of the first expression: "))
  gx = float(input("Please enter the second expression: "))
  dgx = float(input("Please enter the desired derivative of the second expression: "))
  fx = float(input("Please enter the first expression: "))
  
  return str((dfx*gx + dgx*fx)/gx^2)


#Integrals

def constantIntegral(a):
  return a + "x + C"

def powerIntegral(a):
  b = a+1
  return "(x^" + b + ")/" + a + " + C"

def eIntegral():
  return "e^x + C"

def sineIntegral(x):
  return -math.cos(x)

def cosineIntegral(x):
  return math.sin(x)

def tangentSecantSqrd(x):
  return math.tan(x)



# Misc
def save(numList):
  with open('savedValue.txt', 'w') as savefile:
    for num in numList:
      savefile.write(num + '\n')
      
def load():
  with open('savedValue.txt', 'r') as loaded:
    reload = loaded.readlines()
    return reload







# Client
def mainMenu():
  system('clear')
  sleep(1)
  print("*---------------------------------------*")
  print("Welcome to the Comprehensive Calculator!")
  print("Options:")
  print("Arithmetic : 1")
  print("Trigonometry : 2")
  print("Geometry : 3")
  print("Algebra : 4")
  print("Calculus : 5")
  print("Misc : 6")
  print("Quit : 0")

def arithmetic():
  system('clear')
  sleep(1)
  print("*--------------Arithmetic---------------*")
  print("Options:")
  print("Add : 1")
  print("Subtract : 2")
  print("Multiply : 3")
  print("Divide : 4")
  print("Square : 5")
  print("Square Root : 6")
  print("Power : 7")
  print("Quit : 0")

def trig():
  system('clear')
  sleep(1)
  print("*--------------Trigonometry---------------*")
  print("Options:")
  print("PythagoreanAB : 1")
  print("PythagoreanBC : 2")
  print("Quit : 0")

def geometry():
  system('clear')
  sleep(1)
  print("*--------------Geometry---------------*")
  print("Options:")
  print("Area of a Circle : 1")
  print("Area of a Rectangle : 2")
  print("Area of a Right Triangle : 3")
  print("Circumference of a Circle : 4")
  print("Perimeter of a Rectangle : 5")
  print("Volume of a Sphere : 6")
  print("Volume of a Cube : 7")
  print("Volume of a Rectangle : 8")
  print("Volume of a Cylindar : 9")
  print("Volume of a Wedge : 10")
  print("Quit : 0")

def waitTime():
  moveOnChoice = "111"
  while (moveOnChoice != "0"):
    print("Options:")
    print("Save answer: 1")
    print("Delete answer and go back to main menu: 0")
    moveOnChoice = input("Please enter choice here: ")

def main():
  turnoff = False
  while (turnoff is not True):
    mainMenu()
    clientIn = int(input("Please enter desired functionality: "))
    
    match clientIn:

      case 0:
        turnoff = True
        break
      
      case 1:
        
        arithmetic()

        
        arithChoice = int(input("Please enter desired functionality: "))
        match arithChoice:
        
          case 0:
            turnoff = True
            break
            
          case 1:
            x = float(input("Please enter first number to add: "))
            y = float(input("Please enter second number to add: "))
            print(add(x,y))
            waitTime()
            
          case 2:
            x = float(input("Please enter first number to subtract: "))
            y = float(input("Please enter second number to subtract: "))
            print(subtract(x,y))
            waitTime()

          case 3:
            x = float(input("Please enter first number to multiply: "))
            y = float(input("Please enter second number to multiply: "))
            print(multiply(x,y))
            waitTime()

          case 4:
            x = float(input("Please enter first number to divide: "))
            y = float(input("Please enter second number to divide: "))
            print(divide(x,y))
            waitTime()

          case 5:
            x = float(input("Please enter the number you would like to square: "))
            print(square(x))
            waitTime()

          case 6:
            x = float(input("Please enter the number you would like to square root: "))
            print(squareRoot(x))
            waitTime()

          case 7:
            x = float(input("Please enter the number you want to have as the base: "))
            y = float(input("Please enter the number you want to have as the exp: "))
            print(power(x,y))
            waitTime()

      case 2:
        
        trig()

        trigChoice = int(input("Please enter desired functionality: "))
        match trigChoice:
          case 0:
            turnoff = True
            break

          case 1:
            x = float(input("Please enter the base of the triangle: "))
            y = float(input("Please enter height of the triangle: "))
            print(pythagoreanAB(x,y))
            waitTime()

          case 2:
            x = float(input("Please enter the base of the triangle: "))
            y = float(input("Please enter hypotenuse of the triangle: "))
            print(pythagoreanBC(x,y))
            waitTime()
        
      case 3:

        geometry()

        geoChoice = int(input("Please enter desired functionality: "))
        match geoChoice:
          case 0:
            turnoff = True
            break

          




main()