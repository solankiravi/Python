for x in range(1,10):
	if(x == 5):
		continue	# returns the control to the beginning of the loop
	elif(x == 8):
		break		# brings control out of the loop
	else:
		pass		# It is used to write empty loops
	print(x)
	