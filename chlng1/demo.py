# Modified version of Gender Classifier

# import dependencies
from sklearn import tree

# import training data

#[height, weight, shoe size]
X = [[181,80,44], [177,70,43], [160,60,38], [154,54,37], [166,65,40], [190,90,47], 
	[175,64,39], [177,70,40], [159,55,37], [171,75,42], [181,85,43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']

# initialize vars used in loop
count = 0
iterations = 1000

# main loop
for i in range(0,iterations):
	print ("Iteration", i)
	# create a decision tree...
	clf = tree.DecisionTreeClassifier()
	# ... and train it on data from X and Y
	clf = clf.fit(X,Y)
	# make a prediction about a person with the following parameters
	prediction = clf.predict([[163,80,45]])
	# if the person is male, increment count
	if prediction == 'male':
		count += 1

print (float(count / iterations) * 100, "% male")
print (100 - float(count / iterations) * 100, "% female")
