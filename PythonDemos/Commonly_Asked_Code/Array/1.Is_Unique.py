word='abcd'



def is_unique_1(word: str):
    if len(word) == 1:
        return True
    temp_arr=[]    
    for char in word:
        if char not in temp_arr:
            temp_arr.append(char)
        else:
            return False
    return True

def is_unique_2(word:str):
    return len(set(word)) == len(word)

print(is_unique_1(word))
print(is_unique_2(word))