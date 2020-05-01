numberOfInput = 5;inputs = []
for i in range(numberOfInput):
    try:
        i = int(input("Enter number{0} ".format(i+1)))
        inputs.append(i)
    except ValueError:
        print("That's not an int!")
print(sum(inputs))
print(inputs)