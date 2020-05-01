#Question 1
class A:
    def __init__(self):
        print(1)
class B(A):
    def init(self):
        super().__init__()
        print(2)

obj = B()
#Question 2
class C:
    def __init__(self):
        print(1)
class D(C):
    def __init__(self):
        super().__init__()
        print(2)

obj = D()
#Question 3
class E:
    def __init__(self):
        print(1)
class F(E):
    def init(self):
        super().__init__()
        print(2)

obj = F()
print(obj.init())