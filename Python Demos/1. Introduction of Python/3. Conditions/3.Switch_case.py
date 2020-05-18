#To use switch case, we need to use Dictionary 
def call_method_1():
    return "Hello method 1"

def call_method_2():
    return "HelloMethod 2"
#switcher is a dictionary, based on key, functions values are being assigned.
switcher= {
    '1': call_method_1(),
    '2': call_method_2()
}

#call your case by getting the key value of dictionary
print(switcher.get('1'))