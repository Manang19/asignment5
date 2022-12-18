class list():
    def  __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

       
    
    def sum_of_squares_formula(self):
        print(f'x:{self.x*x+self.y*y+self.z*z}')

     
x=int(input('enter the no'))
y=int(input('enter the no'))
z=int(input('enter the no'))

obj = list(x,y,z)
obj.sum_of_squares_formula()

