# Coding challenge #1.

# import dependencies
from sklearn import svm, neighbors
from sklearn.linear_model import SGDClassifier

# import training data
X = [[181,80,44], [177,70,43], [160,60,38], [154,54,37], [166,65,40], [190,90,47], 
	[175,64,39], [177,70,40], [159,55,37], [171,75,42], [181,85,43]]

Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']

# 1. Support vector machine (yields the best results for this dataset!)
clfSVM = svm.SVC(gamma='scale')
clfSVM = clfSVM.fit(X,Y)
predictionSVM = clfSVM.predict([[160, 55, 38]])
print(predictionSVM)

# 2. Stochastic gradient descent
clfSGD = SGDClassifier(loss="hinge", penalty="l2", max_iter=100, tol=1e-3)
clfSGD = clfSGD.fit(X,Y)
predictionSGD = clfSGD.predict([[160, 55, 38]])
print(predictionSGD)

# 3. Nearest Neighbors Classification
clfKNC = neighbors.KNeighborsClassifier(11, weights='uniform')
clfKNC = clfKNC.fit(X,Y)
predictionKNC = clfKNC.predict([[160, 55, 38]])
print(predictionKNC)
