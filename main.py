
from vpython import * #for 3D animations and cube
import random #for randomizing the cube
def make_small_cube(colorsidefront, colorsideleft, colorsideright, colorsidedown, colorsideup, colorsideback):
    colorsidefront = colorsidefront
    colorsideleft = colorsideleft
    colorsideright = colorsideright
    colorsidedown = colorsidedown
    colorsideup = colorsideup
    colorsideback = colorsideback 
    #to color each side of a box i used 6 piramides with different colors
    container = box(pos=vector(0.5,0,0), size=vector(0.99,0.999,0.99), color= vector(0.5,0.5,0.5))
    blue = pyramid(pos=vector(0,0,0), size=vector(0.9,0.9,0.9),color=colorsideleft)
    side2 = pyramid(pos=vector(1,0,0), size=vector(0.9,0.9,0.9), axis=vector(-1,0,0),color=colorsideright)
    green = pyramid(pos=vector(0.5,-0.5,0), size=vector(0.9,0.9,0.9), axis=vector(0,1,0),color=colorsidedown)
    orange = pyramid(pos=vector(0.5,0.5,0), size=vector(0.9,0.9,0.9), axis=vector(0,-1,0),color=colorsideup)
    white = pyramid(pos=vector(0.5,0,-0.5), size=vector(0.9,0.9,0.9), axis=vector(0,0,1), color=colorsideback)
    yellow = pyramid(pos=vector(0.5,0,0.5), size=vector(0.9,0.9,0.9), axis=vector(0,0,-1), color=colorsidefront)
    return compound([container,blue,side2,green,orange,white,yellow])
#with function i made all posible small cubes in a rubiix
cube1 = make_small_cube(color.blue, color.red, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.white, vector(0.5,0.5,0.5))
cube2 = make_small_cube(color.blue, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.white, vector(0.5,0.5,0.5))
cube3 = make_small_cube(color.blue, vector(0.5,0.5,0.5), color.orange, vector(0.5,0.5,0.5), color.white, vector(0.5,0.5,0.5))
cube4 = make_small_cube(color.blue, color.red, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5))
cube5 = make_small_cube(color.blue, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5))
cube6 = make_small_cube(color.blue, vector(0.5,0.5,0.5), color.orange, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5))
cube7 = make_small_cube(color.blue, color.red, vector(0.5,0.5,0.5), color.yellow, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5))
cube8 = make_small_cube(color.blue, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.yellow, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5))
cube9 = make_small_cube(color.blue, vector(0.5,0.5,0.5), color.orange, color.yellow, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5))
cube10 = make_small_cube(vector(0.5,0.5,0.5), color.red, vector(0.5,0.5,0.5), color.yellow, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5))
cube11 = make_small_cube(vector(0.5,0.5,0.5), color.red, vector(0.5,0.5,0.5), color.yellow, vector(0.5,0.5,0.5), color.green)
cube12 = make_small_cube(vector(0.5,0.5,0.5), color.red, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5))
cube13 = make_small_cube(vector(0.5,0.5,0.5), color.red, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.green)
cube14 = make_small_cube(vector(0.5,0.5,0.5), color.red, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.white, vector(0.5,0.5,0.5))
cube15 = make_small_cube(vector(0.5,0.5,0.5), color.red, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.white, color.green)
cube16= make_small_cube(vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.orange, color.yellow, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5))
cube17 = make_small_cube(vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.orange, color.yellow, vector(0.5,0.5,0.5), color.green)
cube18= make_small_cube(vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.orange, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5))
cube19 = make_small_cube(vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.orange, vector(0.5,0.5,0.5),vector(0.5,0.5,0.5), color.green)
cube20= make_small_cube(vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.orange, vector(0.5,0.5,0.5), color.white, vector(0.5,0.5,0.5))
cube21 = make_small_cube(vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.orange, vector(0.5,0.5,0.5), color.white, color.green)
cube22= make_small_cube(vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.white, vector(0.5,0.5,0.5))
cube23 = make_small_cube(vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.white, color.green)
cube24= make_small_cube(vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.yellow, vector(0.5,0.5,0.5), vector(0.5,0.5,0.5))
cube25 = make_small_cube(vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.yellow, vector(0.5,0.5,0.5), color.green)
cube26 = make_small_cube(vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), vector(0.5,0.5,0.5), color.green)


#Here I defined classes for different types of small cubes. corners, edges and middels ech one has coordinates and functions that changes coordinates acording to movments
class corner_cube:
    def __init__(self, position, correct_position, name):
        self.position = position
        self.correct_position = correct_position
        self.name = name

    def front_turn_clock(self):
        if self.position == vector(0,2,0):
            self.position = vector(2,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,2,0):
            self.position = vector(2,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,0,0):
            self.position = vector(0,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(0,0,0):
            self.position = vector(0,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position


    def front_turn_counter(self):
        if self.position == vector(0,2,0):
            self.position = vector(0,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,2,0):
            self.position = vector(0,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,0,0):
            self.position = vector(2,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(0,0,0):
            self.position = vector(2,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position


    def right_turn_clock(self):
        if self.position == vector(2,0,0):
            self.position = vector(2,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,2,0):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,2,-2):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,0,-2):
            self.position = vector(2,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position


    def right_turn_counter(self):
        if self.position == vector(2,0,0):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
  
        elif self.position == vector(2,2,0):
            self.position = vector(2,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,2,-2):
            self.position = vector(2,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,0,-2):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position


    def left_turn_counter(self):
        if self.position == vector(0,0,0):
            self.position = vector(0,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(0,2,0):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(0,2,-2):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(0,0,-2):
            self.position = vector(0,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position


    def left_turn_clock(self):
        if self.position == vector(0,0,0):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif  self.position == vector(0,2,0):
            self.position = vector(0,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(0,2,-2):
            self.position = vector(0,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(0,0,-2):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position


    def top_turn_clock(self):
        if  self.position == vector(2,2,0):
            self.position = vector(0,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif  self.position == vector(0,2,0):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif  self.position == vector(0,2,-2):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif  self.position == vector(2,2,-2):
            self.position = vector(2,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

    
    def top_turn_counter(self):
        if  self.position == vector(2,2,0):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif  self.position == vector(0,2,0):
            self.position = vector(2,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif  self.position == vector(0,2,-2):
            self.position = vector(0,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif  self.position == vector(2,2,-2):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

    
    def down_turn_counter(self):
        if  self.position == vector(0,0,0):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(0,0,-2):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,0,-2):
            self.position = vector(2,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,0,0):
            self.position = vector(0,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position


    def down_turn_clock(self):
        if  self.position == vector(0,0,0):
            self.position = vector(2,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(0,0,-2):
            self.position = vector(0,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,0,-2):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,0,0):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position


    def back_turn_counter(self):
        if self.position == vector(0,0,-2):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(0,2,-2):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,2,-2):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,0,-2):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position


    def back_turn_clock(self):
        if self.position == vector(0,0,-2):
            self.position = vector(2,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(0,2,-2):
            self.position = vector(0,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
   
        elif self.position == vector(2,2,-2):
            self.position = vector(0,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

        elif self.position == vector(2,0,-2):
            self.position = vector(2,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position

class edge_cube:
    def __init__(self,position, correct_position, name, orientation1, correct_orientation1, orientation2, correct_orientation2):
        self.position = position
        self.correct_position = correct_position
        self.name = name
        self.orientation1 = orientation1
        self.correct_orientation1 = correct_orientation1
        self.orientation2 = orientation2
        self.correct_orientation2 = correct_orientation2
        #orientblue = vector(0,0,1)
        #orientgreen = vector(0,0,-1)
    def front_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,1,0)
        if self.position == vector(1,0,0):
            self.position = vector(0,1,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,0):
            self.position = vector(1,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,2,0):
            self.position = vector(2,1,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,0):
            self.position = vector(1,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def front_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,-1,0)

        if self.position == vector(1,0,0):
            self.position = vector(2,1,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,0):
            self.position = vector(1,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,2,0):
            self.position = vector(0,1,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,0):
            self.position = vector(1,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def right_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,-1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,-1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,1,0)
        if self.position == vector(2,1,0):
            self.position = vector(2,2,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,2,-1):
            self.position = vector(2,1,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,-2):
            self.position = vector(2,0,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,0,-1):
            self.position = vector(2,1,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def right_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,-1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,-1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,-1,0)
        if self.position == vector(2,1,0):
            self.position = vector(2,0,-1)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,2,-1):
            self.position = vector(2,1,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,-2):
            self.position = vector(2,2,-1)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,0,-1):
            self.position = vector(2,1,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    
    def left_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,-1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,-1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,1,0)
        if self.position == vector(0,1,0):
            self.position = vector(0,2,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,2,-1):
            self.position = vector(0,1,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,-2):
            self.position = vector(0,0,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,0,-1):
            self.position = vector(0,1,0)
            self.name.rotate(angle=-1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        

    def left_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(0,0,1)    
            elif self.orientation1 == vector(0,0,-1):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(0,0,-1)
            elif self.orientation1 == vector(0,0,1): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(0,0,1)    
            elif self.orientation2 == vector(0,0,-1):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(0,0,-1)
            elif self.orientation2 == vector(0,0,1): 
                self.orientation2 = vector(0,-1,0)
        if self.position == vector(0,1,0):
            self.position = vector(0,0,-1)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,2,-1):
            self.position = vector(0,1,0)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,-2):
            self.position = vector(0,2,-1)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,0,-1):
            self.position = vector(0,1,-2)
            self.name.rotate(angle=1.57079633, axis=vector(1,0,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
       
    def top_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,-1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,-1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,1)
        if  self.position == vector(1,2,0):
            self.position = vector(0,2,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(0,2,-1):
            self.position = vector(1,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(1,2,-2):
            self.position = vector(2,2,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(2,2,-1):
            self.position = vector(1,2,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    
    def top_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,-1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,-1)
        
        if  self.position == vector(1,2,0):
            self.position = vector(2,2,-1)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(0,2,-1):
            self.position = vector(1,2,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(1,2,-2):
            self.position = vector(0,2,-1)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif  self.position == vector(2,2,-1):
            self.position = vector(1,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def down_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,-1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,-1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,1)
        if  self.position == vector(1,0,0):
            self.position = vector(0,0,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,0,-1):
            self.position = vector(1,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,0,-2):
            self.position = vector(2,0,-1)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,0,-1):
            self.position = vector(1,0,0)
            self.name.rotate(angle=-1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def down_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,0,1):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(-1,0,0):    
                self.orientation1 = vector(0,0,1) 
            elif self.orientation1 == vector(0,0,-1): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(1,0,0): 
                self.orientation1 = vector(0,0,-1)

            if self.orientation2 == vector(0,0,1):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(-1,0,0):    
                self.orientation2 = vector(0,0,1) 
            elif self.orientation2 == vector(0,0,-1): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(1,0,0): 
                self.orientation2 = vector(0,0,-1)
        if  self.position == vector(1,0,0):
            self.position = vector(2,0,-1)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,0,-1):
            self.position = vector(1,0,0)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,0,-2):
            self.position = vector(0,0,-1)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,0,-1):
            self.position = vector(1,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,1,0), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def back_turn_counter(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,-1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(-1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,-1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(-1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,1,0)
        if self.position == vector(1,0,-2):
            self.position = vector(0,1,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,-2):
            self.position = vector(1,2,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,2,-2):
            self.position = vector(2,1,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,-2):
            self.position = vector(1,0,-2)
            self.name.rotate(angle=-1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        
    def back_turn_clock(self):
        def orientation_changer(self):
            if self.orientation1 == vector(0,1,0):
                self.orientation1 =  vector(-1,0,0)    
            elif self.orientation1 == vector(1,0,0):    
                self.orientation1 = vector(0,1,0) 
            elif self.orientation1 == vector(0,-1,0): 
                self.orientation1 = vector(1,0,0)
            elif self.orientation1 == vector(-1,0,0): 
                self.orientation1 = vector(0,-1,0)

            if self.orientation2 == vector(0,1,0):
                self.orientation2 =  vector(-1,0,0)    
            elif self.orientation2 == vector(1,0,0):    
                self.orientation2 = vector(0,1,0) 
            elif self.orientation2 == vector(0,-1,0): 
                self.orientation2 = vector(1,0,0)
            elif self.orientation2 == vector(-1,0,0): 
                self.orientation2 = vector(0,-1,0)
        if self.position == vector(1,0,-2):
            self.position = vector(2,1,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(0,1,-2):
            self.position = vector(1,0,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(1,2,-2):
            self.position = vector(0,1,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
        elif self.position == vector(2,1,-2):
            self.position = vector(1,2,-2)
            self.name.rotate(angle=1.57079633, axis=vector(0,0,1), origin=vector(0,0,0))
            self.name.pos = self.position
            orientation_changer(self)
v1 = vector(0,2,0) 
v2 = vector(1,2,0)
v3 = vector(2,2,0)
v4 = vector(0,1,0)
v5 = vector(1,1,0)
v6 = vector(2,1,0)
v7 = vector(0,0,0)
v8 = vector(1,0,0)
v9 = vector(2,0,0)
v10 = vector(0,0,-1)
v11 = vector(0,0,-2)
v12 = vector(0,1,-1)
v13 = vector(0,1,-2)
v14 = vector(0,2,-1)
v15 = vector(0,2,-2)
v16 = vector(2,0,-1)
v17 = vector(2,0,-2)
v18 = vector(2,1,-1)
v19 = vector(2,1,-2)
v20 = vector(2,2,-1)
v21 = vector(2,2,-2)
v22 = vector(1,2,-1)
v23 = vector(1,2,-2)
v24 = vector(1,0,-1)
v25 = vector(1,0,-2)
v26 = vector(1,1,-2) 

orientwhite = vector(0,1,0)
orientblue = vector(0,0,1)
orientyellow = vector(0,-1,0)
orientred = vector(-1,0,0)
orientorange = vector(1,0,0)
orientgreen = vector(0,0,-1)

#different types of smal cubes
cube1.pos=v1 #middle
cube2.pos=v2 
cube3.pos=v3 #middle
cube4.pos=v4
cube5.pos=v5
cube6.pos=v6
cube7.pos=v7 #middle
cube8.pos=v8
cube9.pos=v9 #middle
cube10.pos=v10
cube11.pos=v11 #middle
cube12.pos=v12
cube13.pos=v13
cube14.pos=v14
cube15.pos=v15 #middle
cube16.pos=v16
cube17.pos=v17 #middle
cube18.pos=v18
cube19.pos=v19
cube20.pos=v20
cube21.pos=v21 #middle
cube22.pos=v22
cube23.pos=v23
cube24.pos=v24
cube25.pos=v25
cube26.pos=v26
#here I defined small cubes to object according to where they are located. Look at line 45
c1 = corner_cube(v1,v1,cube1)
c3 = corner_cube(v3,v3,cube3)
c7 = corner_cube(v7,v7,cube7)
c9 = corner_cube(v9,v9,cube9)
c11 = corner_cube(v11,v11,cube11)
c15 = corner_cube(v15,v15,cube15)
c17 = corner_cube(v17,v17,cube17)
c21 = corner_cube(v21,v21,cube21)


c2 = edge_cube(v2,v2,cube2,orientwhite, orientwhite, orientblue, orientblue)
c4 = edge_cube(v4,v4,cube4,orientblue,orientblue, orientred, orientred)
c6 = edge_cube(v6,v6,cube6,orientblue,orientblue, orientorange, orientorange)
c8 = edge_cube(v8,v8,cube8,orientblue,orientblue,orientyellow,orientyellow)
c10 = edge_cube(v10,v10,cube10, orientred, orientred, orientyellow,orientyellow)
c13 = edge_cube(v13,v13,cube13, orientyellow,orientyellow, orientgreen, orientgreen)
c14 = edge_cube(v14,v14,cube14, orientwhite, orientwhite, orientred, orientred)
c16 = edge_cube(v16,v16,cube16, orientyellow,orientyellow, orientorange, orientorange)
c19 = edge_cube(v19,v19,cube19, orientorange, orientorange,orientgreen, orientgreen)
c20 = edge_cube(v20,v20,cube20, orientwhite, orientwhite, orientorange, orientorange)
c23 = edge_cube(v23,v23,cube23, orientwhite, orientwhite, orientgreen, orientgreen)
c25 = edge_cube(v25,v25,cube25, orientred, orientred, orientgreen, orientgreen)

#All functions forr rotations
def front_rotation_clock():
    c1.front_turn_clock()
    c3.front_turn_clock()
    c7.front_turn_clock()
    c9.front_turn_clock()
    c11.front_turn_clock()
    c15.front_turn_clock()
    c17.front_turn_clock()
    c21.front_turn_clock()

    c2.front_turn_clock()
    c4.front_turn_clock()
    c6.front_turn_clock()
    c8.front_turn_clock()
    c10.front_turn_clock()
    c13.front_turn_clock()
    c14.front_turn_clock()
    c16.front_turn_clock()
    c19.front_turn_clock()
    c20.front_turn_clock()
    c23.front_turn_clock()
    c25.front_turn_clock()

def front_rotation_counter():
    c1.front_turn_counter()
    c3.front_turn_counter()
    c7.front_turn_counter()
    c9.front_turn_counter()
    c11.front_turn_counter()
    c15.front_turn_counter()
    c17.front_turn_counter()
    c21.front_turn_counter()

    c2.front_turn_counter()
    c4.front_turn_counter()
    c6.front_turn_counter()
    c8.front_turn_counter()
    c10.front_turn_counter()
    c13.front_turn_counter()
    c14.front_turn_counter()
    c16.front_turn_counter()
    c19.front_turn_counter()
    c20.front_turn_counter()
    c23.front_turn_counter()
    c25.front_turn_counter()

def back_rotation_clock():
    c1.back_turn_clock()
    c3.back_turn_clock()
    c7.back_turn_clock()
    c9.back_turn_clock()
    c11.back_turn_clock()
    c15.back_turn_clock()
    c17.back_turn_clock()
    c21.back_turn_clock()

    c2.back_turn_clock()
    c4.back_turn_clock()
    c6.back_turn_clock()
    c8.back_turn_clock()
    c10.back_turn_clock()
    c13.back_turn_clock()
    c14.back_turn_clock()
    c16.back_turn_clock()
    c19.back_turn_clock()
    c20.back_turn_clock()
    c23.back_turn_clock()
    c25.back_turn_clock()

def back_rotation_counter():
    c1.back_turn_counter()
    c3.back_turn_counter()
    c7.back_turn_counter()
    c9.back_turn_counter()
    c11.back_turn_counter()
    c15.back_turn_counter()
    c17.back_turn_counter()
    c21.back_turn_counter()

    c2.back_turn_counter()
    c4.back_turn_counter()
    c6.back_turn_counter()
    c8.back_turn_counter()
    c10.back_turn_counter()
    c13.back_turn_counter()
    c14.back_turn_counter()
    c16.back_turn_counter()
    c19.back_turn_counter()
    c20.back_turn_counter()
    c23.back_turn_counter()
    c25.back_turn_counter()
   
def top_rotation_counter():
    c1.top_turn_counter()
    c3.top_turn_counter()
    c7.top_turn_counter()
    c9.top_turn_counter()
    c11.top_turn_counter()
    c15.top_turn_counter()
    c17.top_turn_counter()
    c21.top_turn_counter()

    c2.top_turn_counter()
    c4.top_turn_counter()
    c6.top_turn_counter()
    c8.top_turn_counter()
    c10.top_turn_counter()
    c13.top_turn_counter()
    c14.top_turn_counter()
    c16.top_turn_counter()
    c19.top_turn_counter()
    c20.top_turn_counter()
    c23.top_turn_counter()
    c25.top_turn_counter()
    
def top_rotation_clock():
    c1.top_turn_clock()
    c3.top_turn_clock()
    c7.top_turn_clock()
    c9.top_turn_clock()
    c11.top_turn_clock()
    c15.top_turn_clock()
    c17.top_turn_clock()
    c21.top_turn_clock()

    c2.top_turn_clock()
    c4.top_turn_clock()
    c6.top_turn_clock()
    c8.top_turn_clock()
    c10.top_turn_clock()
    c13.top_turn_clock()
    c14.top_turn_clock()
    c16.top_turn_clock()
    c19.top_turn_clock()
    c20.top_turn_clock()
    c23.top_turn_clock()
    c25.top_turn_clock()
    
def down_rotation_clock():
    c1.down_turn_clock()
    c3.down_turn_clock()
    c7.down_turn_clock()
    c9.down_turn_clock()
    c11.down_turn_clock()
    c15.down_turn_clock()
    c17.down_turn_clock()
    c21.down_turn_clock()

    c2.down_turn_clock()
    c4.down_turn_clock()
    c6.down_turn_clock()
    c8.down_turn_clock()
    c10.down_turn_clock()
    c13.down_turn_clock()
    c14.down_turn_clock()
    c16.down_turn_clock()
    c19.down_turn_clock()
    c20.down_turn_clock()
    c23.down_turn_clock()
    c25.down_turn_clock()
    
def down_rotation_counter():
    c1.down_turn_counter()
    c3.down_turn_counter()
    c7.down_turn_counter()
    c9.down_turn_counter()
    c11.down_turn_counter()
    c15.down_turn_counter()
    c17.down_turn_counter()
    c21.down_turn_counter()

    c2.down_turn_counter()
    c4.down_turn_counter()
    c6.down_turn_counter()
    c8.down_turn_counter()
    c10.down_turn_counter()
    c13.down_turn_counter()
    c14.down_turn_counter()
    c16.down_turn_counter()
    c19.down_turn_counter()
    c20.down_turn_counter()
    c23.down_turn_counter()
    c25.down_turn_counter()
    
def right_rotation_clock():
    c1.right_turn_clock()
    c3.right_turn_clock()
    c7.right_turn_clock()
    c9.right_turn_clock()
    c11.right_turn_clock()
    c15.right_turn_clock()
    c17.right_turn_clock()
    c21.right_turn_clock()

    c2.right_turn_clock()
    c4.right_turn_clock()
    c6.right_turn_clock()
    c8.right_turn_clock()
    c10.right_turn_clock()
    c13.right_turn_clock()
    c14.right_turn_clock()
    c16.right_turn_clock()
    c19.right_turn_clock()
    c20.right_turn_clock()
    c23.right_turn_clock()
    c25.right_turn_clock()
    

def right_rotation_counter():
    c1.right_turn_counter()
    c3.right_turn_counter()
    c7.right_turn_counter()
    c9.right_turn_counter()
    c11.right_turn_counter()
    c15.right_turn_counter()
    c17.right_turn_counter()
    c21.right_turn_counter()

    c2.right_turn_counter()
    c4.right_turn_counter()
    c6.right_turn_counter()
    c8.right_turn_counter()
    c10.right_turn_counter()
    c13.right_turn_counter()
    c14.right_turn_counter()
    c16.right_turn_counter()
    c19.right_turn_counter()
    c20.right_turn_counter()
    c23.right_turn_counter()
    c25.right_turn_counter()
    

def left_rotation_clock():
    c1.left_turn_clock()
    c3.left_turn_clock()
    c7.left_turn_clock()
    c9.left_turn_clock()
    c11.left_turn_clock()
    c15.left_turn_clock()
    c17.left_turn_clock()
    c21.left_turn_clock()

    c2.left_turn_clock()
    c4.left_turn_clock()
    c6.left_turn_clock()
    c8.left_turn_clock()
    c10.left_turn_clock()
    c13.left_turn_clock()
    c14.left_turn_clock()
    c16.left_turn_clock()
    c19.left_turn_clock()
    c20.left_turn_clock()
    c23.left_turn_clock()
    c25.left_turn_clock()
    
def left_rotation_counter():
    c1.left_turn_counter()
    c3.left_turn_counter()
    c7.left_turn_counter()
    c9.left_turn_counter()
    c11.left_turn_counter()
    c15.left_turn_counter()
    c17.left_turn_counter()
    c21.left_turn_counter()

    c2.left_turn_counter()
    c4.left_turn_counter()
    c6.left_turn_counter()
    c8.left_turn_counter()
    c10.left_turn_counter()
    c13.left_turn_counter()
    c14.left_turn_counter()
    c16.left_turn_counter()
    c19.left_turn_counter()
    c20.left_turn_counter()
    c23.left_turn_counter()
    c25.left_turn_counter()

#randomizer
def randomizer():
    random_num1 = random.randint(200,500)
    while random_num1 >0:
        random_num2 = random.randint(0,3)
        random_num3 = random.randint(0,3)
        random_num4 = random.randint(0,3)
        random_num5 = random.randint(0,3)
        random_num6 = random.randint(0,3)
        random_num7 = random.randint(0,3)
        while random_num2 > 0:
            front_rotation_clock()
            random_num2 -= 1
        while random_num3 > 0:
            top_rotation_clock()
            random_num3 -= 1
        while random_num4 > 0:
            right_rotation_clock()
            random_num4 -= 1
        while random_num5 > 0:
            left_rotation_clock()
            random_num5 -= 1
        while random_num6 > 0:
            down_rotation_clock()
            random_num6 -= 1
        while random_num7 > 0:
            back_rotation_clock()
            random_num7 -= 1
        random_num1 -= 1
    

#A.I. algorithems to solve a cube

#The cross
def solver():
    def cross_filler(pos):
        if pos == vector(2,0,-1):
            right_rotation_clock()
            left_rotation_counter()
            front_rotation_counter()
            right_rotation_counter()
            left_rotation_clock()
        elif pos == vector(1,0,0):
            back_rotation_counter()
            front_rotation_clock()
            left_rotation_counter()
            back_rotation_clock()
            front_rotation_counter()
        elif pos == vector(0,0,-1):
            right_rotation_counter()
            left_rotation_clock()
            back_rotation_counter()
            right_rotation_clock()
            left_rotation_counter()
        elif pos == vector(1,0,-2):
            back_rotation_clock()
            front_rotation_counter()
            right_rotation_counter()
            back_rotation_counter()
            front_rotation_clock()

    def unlocking_for_white_cross(pos):
        if pos == vector(0,1,-2):
            back_rotation_clock()
            down_rotation_counter()
            back_rotation_counter()
        if pos == vector(2,1,-2):
            back_rotation_counter()
            down_rotation_counter()
            back_rotation_clock()
        if pos == vector(0,1,0):
            front_rotation_counter()
            down_rotation_clock()
            front_rotation_clock()
        if pos == vector(2,1,0):
            front_rotation_clock()
            down_rotation_clock()
            front_rotation_counter()

    def bringing_piece_from_the_top(pos):
        if pos == vector(1,2,0):
            right_rotation_clock()
            left_rotation_counter()
            front_rotation_counter()
            right_rotation_counter()
            left_rotation_clock()
        if pos == vector(1,2,-2):
            right_rotation_counter()
            left_rotation_clock()
            back_rotation_clock()
            right_rotation_clock()
            left_rotation_counter()
        if pos == vector(0,2,-1):
            front_rotation_clock()
            back_rotation_counter()
            left_rotation_clock() 
            front_rotation_counter()
            back_rotation_clock()
        if pos == vector(2,2,-1):  
            front_rotation_counter()
            back_rotation_clock()
            right_rotation_clock()
            front_rotation_clock()
            back_rotation_counter()

    def orienting_cross_pieces(pos,name):
        if pos == vector(1,2,0):
            right_rotation_clock()
            left_rotation_counter()
            front_rotation_clock()
            front_rotation_clock()
            right_rotation_clock()
            left_rotation_counter()
            down_rotation_clock()
            cross_filler(name.position)
        if pos == vector(0,2,-1):
            front_rotation_clock()
            back_rotation_counter()
            left_rotation_clock()
            left_rotation_clock()
            front_rotation_counter()
            back_rotation_clock()
            down_rotation_clock()
            cross_filler(name.position)
        if pos == vector(2,2,-1):
            front_rotation_counter()
            back_rotation_clock()
            right_rotation_clock()
            right_rotation_clock()
            front_rotation_clock()
            back_rotation_counter()
            down_rotation_clock()
            cross_filler(name.position)
        if pos == vector(1,2,-2):
            right_rotation_clock()
            left_rotation_counter()
            back_rotation_clock()
            back_rotation_clock()
            down_rotation_clock()
            cross_filler(name.position)

    while c2.position != c2.correct_position:
        if c2.position == vector(1,0,0):
            front_rotation_clock()
            front_rotation_clock()
        elif c2.position == vector(0,1,0):
            front_rotation_clock()
        elif c2.position == vector(2,1,0):
            front_rotation_counter()
        elif c2.position == vector(2,0,-1):
            cross_filler(c2.position)
        elif c2.position == vector(1,0,-2):
            down_rotation_counter()
            cross_filler(c2.position)
        elif c2.position == vector(0,0,-1):
            down_rotation_clock()
            cross_filler(c2.position)
        elif c2.position == vector(0,2,-1):
            top_rotation_counter()
        elif c2.position == vector(2,2,-1):
            top_rotation_clock()
        elif c2.position == vector(1,2,-2):
            top_rotation_clock()
            top_rotation_clock()
        elif c2.position == vector(0,1,-2) or c2.position == vector(2,1,-2):
            unlocking_for_white_cross(c2.position)
            cross_filler(c2.position)
    if c2.orientation1 != c2.correct_orientation1:
        orienting_cross_pieces(c2.position,c2)
    while c14.position != c14.correct_position:
        if c14.position == vector(0,1,0):
            left_rotation_counter()
        elif c14.position == vector(0,0,-1):
            left_rotation_counter()
            left_rotation_counter()
        elif c14.position == vector(0,1,-2):
            left_rotation_clock()
        elif c14.position == vector(1,0,0):
            cross_filler(c14.position)
        elif c14.position == vector(2,0,-1):
            down_rotation_counter()
            cross_filler(c14.position)
        elif c14.position == vector(1,0,-2):
            down_rotation_counter()
            down_rotation_counter()
            cross_filler(c14.position)
        elif c14.position == vector(2,1,-2) or c14.position == vector(2,1,0):
            unlocking_for_white_cross(c14.position)
        else:
            bringing_piece_from_the_top(c14.position)
    if c14.orientation1 != c14.correct_orientation1:
        orienting_cross_pieces(c14.position,c14)

    while c20.position != c20.correct_position:
        if c20.position == vector(2,1,0):
            right_rotation_clock()
        elif c20.position == vector(2,0,-1):
            right_rotation_clock()
            right_rotation_clock()
        elif c20.position == vector(2,1,-2):
            right_rotation_counter()
        elif c20.position == vector(1,0,-2):
            cross_filler(c20.position)
        elif c20.position == vector(0,0,-1):
            down_rotation_counter()
            cross_filler(c20.position)
        elif c20.position == vector(1,0,0):
            down_rotation_counter()
            down_rotation_counter()
            cross_filler(c20.position)
        elif c20.position == vector(0,1,0) or c20.position == vector(0,1,-2):
            unlocking_for_white_cross(c20.position)
        else:
            bringing_piece_from_the_top(c20.position)
    if c20.orientation1 != c20.correct_orientation1:
        orienting_cross_pieces(c20.position,c20)
    while c23.position != c23.correct_position:
        if c23.position == vector(0,1,-2):
            back_rotation_counter()
        elif c23.position == vector(1,0,-2):
            back_rotation_counter()
            back_rotation_counter()
        elif c23.position == vector(2,1,-2):
            back_rotation_clock()
        elif c23.position == vector(0,0,-1):
            cross_filler(c23.position)
        elif c23.position == vector(1,0,0):
            down_rotation_counter()
            cross_filler(c23.position)
        elif c23.position == vector(2,0,-1):
            down_rotation_counter()
            down_rotation_counter()
            cross_filler(c23.position)
        elif c23.position == vector(0,1,0) or c23.position == vector(2,1,0):
            unlocking_for_white_cross(c23.position)
    if c23.orientation1 != c23.correct_orientation1:
        orienting_cross_pieces(c23.position,c23)
    
#control buttons
button(bind=randomizer, text="Randomize")
button(bind=solver, text="Solver")
scene.append_to_caption('\n\n')
button(bind=front_rotation_clock, text="Front Clock")
button(bind=back_rotation_clock, text="Back Clock")
button(bind=right_rotation_clock, text="right Clock")
button(bind=left_rotation_clock, text="left Clock")
button(bind=top_rotation_clock, text="top Clock")
button(bind=down_rotation_clock, text="down Clock")
