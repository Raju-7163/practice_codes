'''class Computer:

    cpu="i7"
    def __init__(self,name,age):
        self.name=name  #instance variable
        self.age=age
    def storage(self,ram):
        print("storage is: ",ram)
c1=Computer("raju",18)
# c2=Computer()
c1.storage(8)
print(c1.name,c1.age,c1.cpu)'''


# singke level inheritence
'''class A:
    def feauture1(self):
        print("feauture 1 is working")
    def feauture2(self):
        print("feauture 2 is working")

class B(A):
    def feauture3(self):
        print("feauture 3 is working")
    def feauture4(self):
        print("feauture 4 is working")

a1=A()
b1=B()
b1.feauture1()
b1.feauture2()
b1.feauture3()'''

'''class A:
    def feauture1(self):
        print("feauture 1 is working")
    def feauture2(self):
        print("feauture 2 is working")

class B(A):
    def feauture3(self):
        print("feauture 3 is working")
    def feauture4(self):
        print("feauture 4 is working")

class C(B):
    def feauture5(self):
        print("feauture 3 is working")
    def feauture6(self):
        print("feauture 4 is working")



a1=A()
b1=B()
c1=C()
c1.feauture3()
b1.feauture1()
b1.feauture2()
b1.feauture3()'''

'''class python:
    def code(self):
        print("coding...")
class student:
    def execute(self):
        print("running")
        print("compililng..")
class Code:
    def laptop(self,ide):
        ide.execute()
ide=student()
c1=Code()
c1.laptop(ide)'''

'''class Demo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        return self.a+self.b
    
d1=Demo(3,4)
print(d1.display())'''

def Tuple(*arr):
    numbers=[]
    diecimals=[]
    strings=[]
    for i in arr:
        if isinstance(i,int):
            numbers.append(i)
        elif isinstance(i,float):
            diecimals.append(i)
        else:
            strings.append(i)
    return numbers,diecimals,strings
x,y,z=Tuple(1,2,3.4,5.4,"kk")
print(x)
print(y)
print(z)

         