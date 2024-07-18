from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import random
# Loading data
data_iris = load_iris()
# To get list of target names
label_target = data_iris.target_names
print()
print("Sample Data from Iris Dataset")
print("*"*30)
# to display the sample data from the iris dataset
for i in range(10):
 rn = random.randint(0,120)
 print(data_iris.data[rn],"===>",label_target[data_iris.target[rn]])
# Create feature and target arrays
X = data_iris.data
y = data_iris.target
# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size = 0.3, random_state=1)
print("The Training dataset length: ",len(X_train))
print("The Testing dataset length: ",len(X_test))
try:
 nn = int(input("Enter number of neighbors :"))
 knn = KNeighborsClassifier(nn)

 knn.fit(X_train, y_train)
 # to display the score
 print("The Score is :",knn.score(X_test, y_test))
 # To get test data from the user
 test_data = input("Enter Test Data :").split(",")
 for i in range(len(test_data)):
  test_data[i] = float(test_data[i])
 print()
 v = knn.predict([test_data])
 print("Predicted output is :",label_target[v])
except:
 print("Please supply valid input......")
