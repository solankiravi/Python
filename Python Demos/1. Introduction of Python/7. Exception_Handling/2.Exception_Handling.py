import os
val=None
try:
    with open('filedoesnotexist.txt') as f:
        val = f.read()
except Exception as identifier:
    val=0
    with open('filedoesnotexist.txt','w') as f:
        f.write(str(val))
else:
    os.remove('filedoesnotexist.txt')
    print("Exception didi not occured. Good Job")
finally:
    print(val)
    