class soni:
    def __init__(self ):
        self.name = 'sonu'
        self.age = 5
    def update(self):
        self.name="mohan"
    def compare(self,other):
        if self.age == (other.age):
            return True
        else:
            return False




com1 =  soni()
com2 =  soni()

com1.update()
com2.age = 12
com1.age=12
com1.name="sonu1"
print(com1.name)
print(com2.age)
if com1.compare(com2):
  print("pass")
else:
    print("not same")

class son:
    college = 'arya college of engineering and it'
    def __init__(self):
        print("sonu9588")
        self.name = "sonu"
    def maa(self,n):
        print("hello sir my name is sonu vishwkarma "+n,self.name)
    def update(self):
        num2.name='vishwkamra'
        son.college='sonu'
num1 = son()
num2= son()
num2.update()

num1.maa('sonu')
num2.maa('sonu')
print(num1.college)
print(num2.college)

class A:
    def __init__(self):
        print("A")
    def feat1(self):
        print("feat1 for one")

class B:
    def __init__(self):

        print("B")

    def feat2(self):
        print("feat2 for two")
class C(B,A):
    def __init__(self):
        super().__init__()

        print("8hello")
    def feat3(self):
        print("feat3 for three")
a1= C()
a1.feat3()



