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
        try:  # check if y array is not one-hot, in that case make it one-hot
            if y.shape[0] * y.shape[1] == len(y):
                y = one_hot(y)
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
                self.b_2 = self.b_2 - self.alpha * np.sum(-out_error, axis=0)
                self.w_2 = self.w_2 - self.alpha * np.dot(a_1.T, -out_error * self.output_derivatives) + l2 * self.w_2
                h_delta = np.dot(out_error, self.w_2.T)  # batch x o . o x h = batch x h
                self.b_1 = self.b_1 - self.alpha * np.sum(-h_delta, axis=0)
                self.w_1 = self.w_1 - self.alpha * np.dot(x_batch.T, -h_delta * self.hidden_derivatives) + l2 * self.w_1
                h_previous_delta = np.dot(h_delta, self.w_1.T)  # batch x h_1 . h_1 x input = batch x input (times other derivative)
            print(f'Epoch: {e} | loss: {mse:.3f}')
        return self


class CustomNeuralNetworkRegressor:
    """
    Custom (1 hidden layer) neural network regressor
    using mse as error with gradient descent
    """
    def __init__(self, input_size: int, hidden_size: int, batch_size=32, alpha=1/1_000):
        self.input_size = input_size
        self.b_1 = np.zeros(hidden_size) + 1e-4
        self.w_1 = np.zeros([input_size, hidden_size]) + 1e-4
        self.b_2 = np.zeros(1) + 1e-4
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
                self.b_2 = self.b_2 - self.alpha * np.sum(-out_error, axis=0)
                self.w_2 = self.w_2 - self.alpha * np.dot(a_1.T, -out_error * 1) + l2 * self.w_2
                h_delta = np.dot(out_error, self.w_2.T)
                self.b_1 = self.b_1 - self.alpha * np.sum(-h_delta, axis=0)
                self.w_1 = self.w_1 - self.alpha * np.dot(x_batch.T, -h_delta * self.hidden_layer_derivatives) + l2 * self.w_1
            print(f'Epoch: {e} | loss: {mse:.3f}')
        return self


class CustomNeuralNetworkRegressorFull:
    """
    Custom neural network regressor
    using mse as error with gradient descent
    """
    def __init__(self, input_size: int, hidden_s, batch_size=32, alpha=1/1_000):
        self.input_size = input_size
        self.hidden_s = hidden_s  # shape of the hidden layers
        self.batch_size = batch_size
        self.alpha = alpha
        self.bs, self.ws = [], []  # weights of the hidden layers excluding outputs
        self.out_b, self.out_w = None, None  # outputs weights
        self.derivatives = []
        self._build_layers()

    def _build_layers(self):
        previous_size = self.input_size
        for h in self.hidden_s:
            self.bs.append(np.zeros(h) + 1e-2)
            self.ws.append(np.zeros([previous_size, h]) + 1e-2)
            previous_size = h
        self.out_b = np.zeros(1) + 1e-2
        self.out_w = np.zeros([self.hidden_s[-1], 1]) + 1e-2

    def _activation(self, x):
        return x.clip(min=0)

    def _calculate(self, x):
        self.derivatives.clear()
        a = x
        z_s, a_s = [], []
        for i in range(len(self.hidden_s)):
            z = self.bs[i] + np.dot(a, self.ws[i])
            a = self._activation(z)
            self.derivatives.append(np.where(a > 0, 1, 0))
            z_s.append(z)
            a_s.append(a)
        z_out = self.out_b + np.dot(a, self.out_w)  # no need for output derivatives since it's linear output
        return z_s, a_s, z_out

    def predict(self, x):
        a = x
        for i in range(len(self.hidden_s)):
            z = self.bs[i] + np.dot(a, self.ws[i])
            a = self._activation(z)
        z_out = self.out_b + np.dot(a, self.out_w)
        return z_out

    def _learn(self, out_error, a_s, batch):
        # output layer bias and weights of the output (last) layer
        self.out_b = self.out_b - self.alpha * np.sum(-out_error, axis=0)
        self.out_w = self.out_w - self.alpha * np.dot(a_s[-1].T, -out_error * 1)
        delta = np.dot(out_error, self.out_w.T)
        for i in range(len(a_s) - 1):  # need to skip the first layer to multiply it with feature data
            self.bs[-(i+1)] = self.bs[-(i+1)] - self.alpha * np.sum(-delta, axis=0)
            # weights are moved by alpha * dot(previous activation output transposed, - delta * activation derivatives)
            self.ws[-(i+1)] = self.ws[-(i+1)] - self.alpha * np.dot(a_s[-(i+2)].T, -delta * self.derivatives[-(i+1)])
            delta = np.dot(delta, self.ws[-(i+1)].T)
        # first layer weights depends on batch feature data
        self.bs[0] = self.bs[0] - self.alpha * np.sum(-delta, axis=0)
        self.ws[0] = self.ws[0] - self.alpha * np.dot(batch.T, -delta * self.derivatives[0])

    def fit(self, x, y, epochs=500):
        """
        :param x: np.array 2d matrix with feature data
        :param y: np.array 1d representation of target data
        """
        for e in range(1, epochs+1):
            mse = 0
            for idx in range(0, x.shape[0], self.batch_size):
                if idx+self.batch_size <= x.shape[0]:
                    x_batch, y_batch = x[idx: idx+self.batch_size], y[idx: idx+self.batch_size]
                else:
                    x_batch, y_batch = x[idx:], y[idx:]
                _, a_s, z_out = self._calculate(x_batch)
                out_error = y_batch - z_out
                mse += 1/x_batch.shape[0] * np.sum(out_error ** 2)
                self._learn(out_error, a_s, x_batch)
            print(f'Epoch: {e} | loss: {mse:.3f}')
        return self


class CustomNeuralNetworkClassifierFull:
    """
    Custom neural network classifier
    activation functions are relu for non-output layers and sigmoid for output layer
    using mse as error with gradient descent
    y data needs to be numerical
    """
    def __init__(self, input_size: int, hidden_s, output_size: int, batch_size=32, alpha=1/1_000):
        """
        :param input_size: number of features
        :param hidden_s: hidden shape
        :param output_size: output size (one-hot)
        :param batch_size: batch size
        :param alpha: learning rate
        """
        self.input_size = input_size
        self.hidden_s = hidden_s  # shape of the hidden layers
        self.output_size = output_size
        self.batch_size = batch_size
        self.alpha = alpha
        self.bs, self.ws = [], []  # weights of the hidden layers excluding outputs
        self.out_b, self.out_w = None, None  # outputs weights
        self.derivatives = []
        self._build_layers()

    def _build_layers(self):
        previous_size = self.input_size
        for h in self.hidden_s:
            self.bs.append(np.zeros(h) + 1e-2)
            self.ws.append(np.zeros([previous_size, h]) + 1e-2)
            # self.bs.append(np.random.binomial(1, 1/3, h) * 1e-4)
            # self.ws.append(np.random.binomial(1, 1/3, [previous_size, h]) * 1e-4)
            previous_size = h
        self.out_b = np.zeros(self.output_size) + 1e-2
        # self.out_w = np.random.normal(0, 1, [self.hidden_s[-1], self.output_size])
        self.out_w = np.zeros([self.hidden_s[-1], self.output_size]) + 1e-2

    def _activation_sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _activation_relu(self, x):
        return x.clip(min=0)

    def _calculate(self, x):
        self.derivatives.clear()
        a = x
        z_s, a_s = [], []
        for i in range(len(self.hidden_s)):
            z = self.bs[i] + np.dot(a, self.ws[i])
            a = self._activation_relu(z)
            self.derivatives.append(np.where(a > 0, 1, 0))
            z_s.append(z)
            a_s.append(a)
        z_out = self.out_b + np.dot(a, self.out_w)
        a_out = self._activation_sigmoid(z_out)
        self.derivatives.append(a_out * (1 - a_out))
        return z_s, a_s, z_out, a_out

    def predict(self, x):
        a = x
        for i in range(len(self.hidden_s)):
            z = self.bs[i] + np.dot(a, self.ws[i])
            a = self._activation_relu(z)
        z_out = self.out_b + np.dot(a, self.out_w)
        return z_out

    def _learn(self, out_error, a_s, batch):
        # output layer bias and weights of the output (last) layer
        self.out_b = self.out_b - self.alpha * np.sum(-out_error, axis=0)
        self.out_w = self.out_w - self.alpha * np.dot(a_s[-1].T, -out_error * self.derivatives[-1])
        delta = np.dot(out_error, self.out_w.T)
        for i in range(len(a_s) - 1):  # need to skip the first layer to multiply it with feature data
            self.bs[-(i+1)] = self.bs[-(i+1)] - self.alpha * np.sum(-delta, axis=0)
            # weights are moved by alpha * dot(previous activation output transposed, - delta * activation derivatives)
            self.ws[-(i+1)] = self.ws[-(i+1)] - self.alpha * np.dot(a_s[-(i+2)].T, -delta * self.derivatives[-(i+2)])
            delta = np.dot(delta, self.ws[-(i+1)].T)
        # first layer weights depends on batch feature data
        self.bs[0] = self.bs[0] - self.alpha * np.sum(-delta, axis=0)
        self.ws[0] = self.ws[0] - self.alpha * np.dot(batch.T, -delta * self.derivatives[0])

    def _learn_2(self, out_error, z_s, batch):
        # output layer bias and weights of the output (last) layer
        self.out_b = self.out_b - self.alpha * np.sum(-out_error, axis=0)
        self.out_w = self.out_w - self.alpha * np.dot(z_s[-1].T, -out_error * self.derivatives[-1])
        delta = np.dot(out_error, self.out_w.T)
        for i in range(len(z_s) - 1):  # need to skip the first layer to multiply it with feature data
            self.bs[-(i+1)] = self.bs[-(i+1)] - self.alpha * np.sum(-delta, axis=0)
            # weights are moved by alpha * dot(previous activation output transposed, - delta * activation derivatives)
            self.ws[-(i+1)] = self.ws[-(i+1)] - self.alpha * np.dot(z_s[-(i+2)].T, -delta)
            delta = np.dot(delta, self.ws[-(i+1)].T)
        # first layer weights depends on batch feature data
        self.bs[0] = self.bs[0] - self.alpha * np.sum(-delta, axis=0)
        self.ws[0] = self.ws[0] - self.alpha * np.dot(batch.T, -delta)

    def fit(self, x, y, epochs=500):
        """
        :param x: np.array 2d matrix with feature data
        :param y: np.array 1d representation of target data
        """
        try:  # check if y array is not one-hot, in that case make it one-hot
            if y.shape[0] * y.shape[1] == len(y):
                y = one_hot(y)
        except IndexError:
            y = one_hot(y)
        for e in range(1, epochs+1):
            mse = 0
            for idx in range(0, x.shape[0], self.batch_size):
                if idx+self.batch_size <= x.shape[0]:
                    x_batch, y_batch = x[idx: idx+self.batch_size], y[idx: idx+self.batch_size]
                else:
                    x_batch, y_batch = x[idx:], y[idx:]
                z_s, a_s, z_out, a_out = self._calculate(x_batch)
                out_error = y_batch - a_out
                mse += 1/x_batch.shape[0] * np.sum(out_error ** 2)
                # self._learn_2(out_error, z_s, x_batch)
                self._learn(out_error, a_s, x_batch)
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
# print(f'\nAccuracy: {np.sum(predictions == y_test) / len(predictions): .3f}')


# x = iris.iloc[:, 0:-2].to_numpy()
# y = iris.iloc[:, -2].to_numpy().reshape([-1, 1])
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=8/10)
# nn = CustomNeuralNetworkRegressor(x.shape[1], 8)
# nn.fit(x_train, y_train)
# prediction = nn.predict(x_test)
# print(r2_score(y_test, prediction))


# x = iris.iloc[:, 0:-2].to_numpy()
# y = iris.iloc[:, -2].to_numpy().reshape([-1, 1])
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=8/10)
# nn = CustomNeuralNetworkRegressorFull(x.shape[1], [8, 16, 32, 32])
# nn.fit(x_train, y_train, epochs=500)
# prediction = nn.predict(x_test)
# print(r2_score(y_test, prediction))


x = iris.iloc[:, 0:-1].to_numpy()
y = iris.iloc[:, -1].to_numpy()
y = LabelEncoder().fit_transform(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=8/10)
nn = CustomNeuralNetworkClassifierFull(x.shape[1], [8, 16, 32], 3)
nn.fit(x_train, y_train, epochs=500)
predictions = nn.predict(x_test)
predictions = np.argmax(predictions, axis=1)
print(f'\nAccuracy: {np.sum(predictions == y_test) / len(predictions): .3f}')
