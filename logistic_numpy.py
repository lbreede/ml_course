import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets

class LogisticRegression:
    def __init__(self, lr=0.001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        return 1 / (1+np.exp(-z))

    def cost_function(self, h ,y):
        epsilon = 1e-10
        return (-y * np.log(h+epsilon) + (1-y) * np.log(1-h+epsilon)).mean()

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            linear_pred = np.dot(X, self.weights) + self.bias
            predictions = self.sigmoid(linear_pred)

            gw = np.dot(X.T, (predictions-y)) / n_samples
            gb = np.sum(predictions-y)/ n_samples

            self.weights -= self.lr * gw
            self.bias -= self.lr * gb

        final_z = np.dot(X, self.weights) + self.bias
        final_h = self.sigmoid(final_z)
        final_cost = self.cost_function(final_h, y)
        return final_cost

    def predict(self, X, threshold=0.5):
        linear_pred = np.dot(X, self.weights) + self.bias
        predictions = self.sigmoid(linear_pred)
        class_pred = [0 if y <=threshold else 1 for y in predictions]
        return class_pred

if __name__ == "__main__":
    bc = datasets.load_breast_cancer()
    X, y = bc.data, bc.target

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=101)
    classification_model = LogisticRegression(lr=0.001)
    classification_model.fit(X_train, y_train)
    y_pred = classification_model.predict(X_test)

    def accuracy(y_pred, y_test):
        return np.sum(y_pred==y_test)/len(y_test)

    acc = accuracy(y_pred, y_test)

    print(acc)


