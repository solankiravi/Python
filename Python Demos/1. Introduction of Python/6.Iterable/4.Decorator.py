#Example 0
def sample():
    print("Sample")
    def pass_within_sample():
        print("Inside Sample")


sampleDecorator = sample()
print(sampleDecorator)

#Example 0.1
def sample1(pass_within_sample1):
    print("Sample 1")
    return pass_within_sample1()

def pass_within_sample1():
    print("Inside Sample 1")

call_func = sample1(pass_within_sample1)
print(call_func)

#Example 1
def HelloWorld(Test):
    Test()
    print("Hello")

@HelloWorld
def Test():
    print("Test")

# Example 2
islogintrue=False
def loginDecorator(run_this):
    if(islogintrue):
        run_this()
    else:
        print("Please login first")

@loginDecorator
def run_this():
    print("Login successful")


"""
Above code is similar to
def run_this():
    print("Login successful")

login_dec = run_this(loginDecorator)


"""

