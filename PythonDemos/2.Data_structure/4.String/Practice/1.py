'''
Get two digit number from string
'''
word='509255'

word_list=list(word)
word_list.sort()
print(word_list[-1]+word_list[-2])
