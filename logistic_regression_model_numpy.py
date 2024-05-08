import numpy as np

class LogisticRegression:
    def __init__(self, lr=0.01, num_iterations=1000):
        self.lr = lr
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def sigmoid(self,z):
        return 1 / (1+np.exp(-z))

    def cost_function(self, h, y):
        return (-y * np.log(h) - (1-y)*np.log(1-h)).mean()

    def fit(self, X, y):
        m,n = X.shape
        self.weights = np.zeros(n)
        self.bias = 0

        for i in range(self.num_iterations):
            z = np.dot(X, self.weights) + self.bias
            h = self.sigmoid(z)
            gw = np.dot(X.T, (h-y)) / m
            gb = np.sum(h-y) / m

            self.weights -= self.lr * gw
            self.bias -= self.lr * gb


    def predict(self,X):
        z = np.dot(X, self.weights) + self.bias
        return np.round(self.sigmoid(z))


if __name__ == "__main__":
    X_train = np.array([[1,2],
                        [2,3],
                        [3,4],
                        [4,5]
                        ])
    y_train = np.array([0,0,1,1])

    model = LogisticRegression()
    model.fit(X_train, y_train)

    X_test = np.array([[5,6],
                       [6,7]])

    prediction = model.predict(X_test)
    print(prediction)


