
def f():
    #To tell Python, that we want to use the global variable, we have to use the keyword "global"
    global s
    print(s) #print Python is great!
    s = "That's clear."
    print(s) #print That's clear.


s = "Python is great!" 
f()
print (s)