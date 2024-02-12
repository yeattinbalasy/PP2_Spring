# i decided to make all task in 1 file beacuse varibles are visible by their classes and there no same class names
# all the commented initalisations are made to check how code works
#i separeted all task by '------'
# 1 task 
class stringer:
    def __init__(self, string):
       self.string = string
    def getString(self):
        self.string = str(input())
    def printString(self):
        print(self.string.upper())

# s = stringer

# s.getString(s)
# s.printString(s)
#----------


#2 task 
class Square:
    def __init__(self, length ):
        self.length  = length

    def area (self):
        print(self.length * self.length == 0)  

class Shape(Square):
    def __init__(self, length = 0 ):
        self.length  = length
    
    def area (self) :
        print(self.length * self.length)        
#----------

class Rectangle(Shape):

    def __init__(self,  width):
        self.width = width

    def area (self, w):
        print( self.length  * w)  
        

# sq = Square
# sh =Shape
# r = Rectangle
# len = 8
# w = 5
# t = sq(len)
# sh.area(t)

# r.area(t,w)

# -------
import math

class point:
    def __init__(self, x = 5  , y = 9 ):
        self.x  = x
        self.y  = y

    def show(self):
        print(f'{self.x}'+ ' '+ f'{self.y}')

    def move(self, x , y):
        self.x = x
        self.y = y
        print('New coor:',self.x,self.y)

    def dist(self,x,y):
        d = math.sqrt(pow((self.x - x),2) + pow((self.y - y),2))
        print(d)

# p = point()
# p.show()

# p.move(7 , 8)

# k = point(1 , 1)

# k.show()
# p.show()

# p.dist(5,9)

#-----
class bank:
    def __init__(self, name  , balance = 0 ):
        self.name  = name
        self.balance  = balance
    def plus(self,add):
        self.balance = self.balance+add
        print('balance of',self.name,':',self.balance)
    def denote(self,min):
        if min > self.balance:
            print("nehvatka")
        else:
            self.balance = self.balance - min
            print('balance of',self.name,':',self.balance)



# f = bank('Arman',200)
# f.plus(50)
# f.denote(251)


# s = bank('Aza-stavochnik', 50)
# s.plus(1000)
# s.denote(500)
# s.plus(50000)
# s.denote(50550)

#---------
def isPrime(x):
    d = 2
    while x % d != 0 and pow(d,2) < x:
        d+=1
    if x % d == 0:
        return False
    else: 
        return True

def filt(li):
    print(list(map(lambda x : isPrime(x), li)))
    # Не очень понял какой именно аутпут мы должны получить
    print(list(filter(isPrime, [1, 3, 2,5 , 20, 21])))

# filt([1, 3, 2,5 , 20, 21])