class student():
    def __init__(self,__name,rollno):
        self.__name = __name
        self.rollno = rollno

    def display(self):
       return f'student detail : \nname: {self.__name} \nrollno: {self.rollno}'

    def set__name(self,username):
        if username == 'manan':
            return self.__name 
        else:
            print('enter value is not valid')

    def get__name(self):
        return self.__name
    
    def set_rollno(self):
        return self.rollno

    def get_rollno(self):
        return self.rollno
    
__name__ = input('enter the name')
rollno = int(input('enter the no'))


student = student( __name__, rollno)
data = student.display()
student.set__name(__name__)
print(data)

