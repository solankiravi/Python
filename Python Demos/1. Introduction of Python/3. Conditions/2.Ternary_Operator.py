isITPositive = -1


# if (isITPositive > 0):
# 	if(isITPositive == 5):
# 		print("Yesssssa")
# 	else:
# 		print("It is Positive but It is not 5. :(")
# elif(isITPositive == 0):
# 	print("It is Zero")
# else :
# 	print(":( It is Negative")

print(":( It is Negative") if isITPositive < 0  else ( print("It is Zero") if isITPositive == 0 else (print("It is Positive but it is not 5. :(") if isITPositive != 5 else print("Yessssa")))