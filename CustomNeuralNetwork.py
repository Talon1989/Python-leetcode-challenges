import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score


def one_hot(x: np.array):
    """
    :param x: np.array in shape [n]
    :return: one-hot x transformation in shape [n, n_unique]
    """
    n_unique = np.unique(x).shape[0]
    x_out = np.zeros([x.shape[0], n_unique])
    for idx, value in enumerate(x):
        x_out[idx, int(value)] = 1
    return x_out


class CustomNeuralNetworkClassifier:
    """
    Custom (1 hidden layer) neural network classifier
    using sigmoid function as activation and mse as error with gradient descent
    """
    def __init__(self, input_size: int, hidden_size: int, output_size: int, batch_size=32, alpha=1/1_000):
        self.input_size = input_size
        self.b_1 = np.zeros(hidden_size)
        self.w_1 = np.random.normal(0, 1, [input_size, hidden_size])
        self.b_2 = np.zeros(output_size)
        self.w_2 = np.random.normal(0, 1, [hidden_size, output_size])
        self.batch_size = batch_size
        self.alpha = alpha
        self.hidden_derivatives = None  # hidden layers derivatives at point x
        self.output_derivatives = None

    def _activation_sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def _activation_relu(self, x):
        return x.clip(min=0)

    def _calculate(self, x):
        z_1 = self.b_1 + np.dot(x, self.w_1)
        a_1 = self._activation_relu(z_1)
        self.hidden_derivatives = np.where(a_1 > 0, 1, 0)
        z_2 = self.b_2 + np.dot(a_1, self.w_2)
        a_2 = self._activation_sigmoid(z_2)
        self.output_derivatives = a_2 * (1 - a_2)
        return a_1, a_2

    def predict(self, x):
        z_1 = self.b_1 + np.dot(x, self.w_1)
        a_1 = self._activation_relu(z_1)
        z_2 = self.b_2 + np.dot(a_1, self.w_2)
        return z_2

    def fit(self, x, y, epochs=500, l2=0):
        """
        :param x: np.array matrix with feature data
        :param y: np.array representation of target data
        """
        try:  # in case target data is not in one-hot form it will be transformed into one-hot
            y.shape[1]
        except IndexError:
            y = one_hot(y)
        for e in range(1, epochs+1):
            mse = None
            for idx in range(0, x.shape[0], self.batch_size):
                if idx+self.batch_size <= x.shape[0]:
                    x_batch, y_batch = x[idx: idx+self.batch_size], y[idx: idx+self.batch_size]
                else:
                    x_batch, y_batch = x[idx:], y[idx:]
                a_1, preds = self._calculate(x_batch)
                out_error = y_batch - preds
                mse = 1/x_batch.shape[0] * np.sum(out_error ** 2)
                out_delta = np.dot(a_1.T, -out_error * self.output_derivatives)   # h x batch . batch x o = h x o
                self.b_2 = self.b_2 - self.alpha * np.sum(-out_error, axis=0)
                self.w_2 = self.w_2 - self.alpha * out_delta + l2 * self.w_2
                h_delta = np.dot(out_error, self.w_2.T)  # batch x o . o x h = batch x h
                self.b_1 = self.b_1 - self.alpha * np.sum(-h_delta, axis=0)
                self.w_1 = self.w_1 - self.alpha * np.dot(x_batch.T, -h_delta * self.hidden_derivatives) + l2 * self.w_1
                h_previous_delta = np.dot(h_delta, self.w_1.T)  # batch x h_1 . h_1 x input = batch x input (times other derivative)
            print(f'Epoch: {e} | loss: {mse:.3f}')
        return self


class CustomNeuralNetworkRegressor:
    """
    Custom (1 hidden layer) neural network regressor
    using sigmoid function as activation and mse as error with gradient descent
    """
    def __init__(self, input_size: int, hidden_size: int, batch_size=32, alpha=1/1_000):
        self.input_size = input_size
        self.b_1 = np.zeros(hidden_size)
        # self.w_1 = np.random.normal(0, 1, [input_size, hidden_size])
        self.w_1 = np.zeros([input_size, hidden_size]) + 1e-4
        self.b_2 = np.zeros(1)
        # self.w_2 = np.random.normal(0, 1, [hidden_size, 1])
        self.w_2 = np.zeros([hidden_size, 1]) + 1e-4
        self.batch_size = batch_size
        self.alpha = alpha
        self.hidden_layer_derivatives = None

    def _activation(self, x):
        return x.clip(min=0)

    def _calculate(self, x):
        z_1 = self.b_1 + np.dot(x, self.w_1)
        a_1 = self._activation(z_1)
        a = a_1.copy()
        # self.hidden_layer_derivatives = a[a > 0] = 1
        self.hidden_layer_derivatives = np.where(a > 0, 1, 0)
        z_2 = self.b_2 + np.dot(a_1, self.w_2)
        a_2 = self._activation(z_2)
        return z_1, a_1, z_2, a_2

    def predict(self, x):
        z_1 = self.b_1 + np.dot(x, self.w_1)
        a_1 = self._activation(z_1)
        z_2 = self.b_2 + np.dot(a_1, self.w_2)
        return z_2

    def fit(self, x, y, epochs=500, l2=0):
        """
        :param x: np.array matrix with feature data
        :param y: np.array representation of target data
        """
        for e in range(1, epochs+1):
            mse = None
            for idx in range(0, x.shape[0], self.batch_size):
                if idx+self.batch_size <= x.shape[0]:
                    x_batch, y_batch = x[idx: idx+self.batch_size], y[idx: idx+self.batch_size]
                else:
                    x_batch, y_batch = x[idx:], y[idx:]
                z_1, a_1, z_2, a_2 = self._calculate(x_batch)
                out_error = y_batch - z_2
                mse = 1/x_batch.shape[0] * np.sum(out_error ** 2)
                out_delta = np.dot(a_1.T, -out_error)
                self.b_2 = self.b_2 - self.alpha * np.sum(-out_error, axis=0)
                self.w_2 = self.w_2 - self.alpha * out_delta + l2 * self.w_2
                h_delta = np.dot(out_error, self.w_2.T)
                self.b_1 = self.b_1 - self.alpha * np.sum(-h_delta, axis=0)
                self.w_1 = self.w_1 - self.alpha * np.dot(x_batch.T, -h_delta * self.hidden_layer_derivatives) + l2 * self.w_1
            print(f'Epoch: {e} | loss: {mse:.3f}')
        return self


iris = pd.read_csv('data/iris.csv')


# x = iris.iloc[:, 0:-1].to_numpy()
# y = LabelEncoder().fit_transform(iris.iloc[:, -1].to_numpy())
# yy = one_hot(y)
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=7/10, stratify=yy)
# nn = CustomNeuralNetworkClassifier(x.shape[1], 8, 3)
# nn.fit(x_train, y_train)
# predictions = nn.predict(x_test)
# predictions = np.argmax(predictions, axis=1)
# print('Accuracy:')
# print(np.sum(predictions == y_test) / len(predictions))


x = iris.iloc[:, 0:-2].to_numpy()
y = iris.iloc[:, -2].to_numpy().reshape([-1, 1])
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=8/10)
nn = CustomNeuralNetworkRegressor(x.shape[1], 8)
nn.fit(x_train, y_train)
prediction = nn.predict(x_test)
print(r2_score(y_test, prediction))
