# Diamond Problem
##################A#################################
################/   \###############################
###############/     \##############################
#############B1       B2############################
###############\     /##############################
################\   /###############################
##################D#################################
class A:
    def CallMethod(self):
        print("CallMethod of A called")
class B1(A):
    def CallMethod(self):
        print("CallMethod of B1 called")   
class B2(A):
    def CallMethod(self):
        print("CallMethod of B2 called")
class B3(A):
    def CallMethod(self):
        print("CallMethod of B3 called")        

class D(B2,B1,B3):
    pass
x = D()
print(x.CallMethod())