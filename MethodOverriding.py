class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c=None):
        s = a +b + c
        return s
s1 = Student(76,75)
print(s1.sum(2,4,5))