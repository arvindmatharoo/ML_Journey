class A:
    def method(self):
        print("methods")
class B:
    def method2(self):
        print("method2")
class C(A,B):
    pass        
c1 = C()
c1.method()
c1.method2()