class cal():
    def __init__(self,a ,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b

a= int(input('enter the no.'))
b= int(input('enter the no.'))
obj = cal(a, b)

print('result:', obj.add())
print('result:', obj.sub())
print('result:', obj.mul())
print('result:', obj.div())
