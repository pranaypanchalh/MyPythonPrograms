class A:
    def classAFunc(self):
        print("This is class A Function")
class B(A):
    def classBFunc(self):
        print("This is class B Function")
class C(B):
    def classCFunc(self):
        print("This is class C Function")

c = C()
c.classAFunc()
c.classBFunc()
c.classCFunc()