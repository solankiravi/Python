from sklearn import tree

#Height,weight,waist
x=[
    [140,80,32],[169,80,36],[176,80,22],[156,80,36],[160,80,34],[169,80,22],
    [189,80,38],[120,80,30],[159,80,35],[159,80,22],[150,85,2],[160,90,9]
]

y= [
    'Male','Female','Male','Female','Male','Female',
    'Male','Female','Male','Female','Male','Male'
]

clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)

prediction=clf.predict([[160,90,2]])
print(prediction)