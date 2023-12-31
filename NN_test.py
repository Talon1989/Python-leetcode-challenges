import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


# data = pd.read_csv('data/Student_Marks.csv')
# x_ = data.iloc[:, 0:-1].to_numpy()
# y_ = data.iloc[:, -1].to_numpy().reshape([-1, 1])
data = pd.read_csv('data/iris.csv')
x_ = data.iloc[:, 0:-2].to_numpy()
y_ = data.iloc[:, -2].to_numpy()
x_train, x_test, y_train, y_test = train_test_split(x_, y_, train_size=8/10)
dataset = TensorDataset(torch.tensor(x_train, dtype=torch.float32), torch.tensor(y_train, dtype=torch.float32))
dataloader = DataLoader(dataset, shuffle=True, batch_size=32)


class Regressor(nn.Module):
    def __init__(self, x_shape):
        super().__init__()
        self.layer_1 = nn.Linear(x_shape, 8)
        self.layer_2 = nn.Linear(8, 16)
        self.layer_3 = nn.Linear(16, 32)
        self.out = nn.Linear(32, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.layer_1(x))
        x = self.relu(self.layer_2(x))
        x = self.relu(self.layer_3(x))
        out = self.out(x)
        return out

    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            # module.weight.data.normal_(mean=0., std=1.)
            module.weight.data.fill_(0. + 1e-2)


regressor = Regressor(x_.shape[1])
# regressor.apply(regressor._init_weights)
optimizer = torch.optim.Adam(params=regressor.parameters(), lr=1/1_000)
criterion = nn.MSELoss()


def fit(dataloader, model=regressor, opt=optimizer, criterion=criterion):
    for epoch in range(1, 501):
        total_loss = 0
        for x, y in dataloader:
            optimizer.zero_grad()
            model.train()
            preds = model(x)
            loss = criterion(preds, y)
            loss.backward()
            optimizer.step()
            total_loss += loss.detach().numpy()
        print(f'Epoch {epoch} | loss: {total_loss:.3f}')


fit(dataloader)
predictions = regressor(torch.tensor(x_test, dtype=torch.float32))
print(f'R2: {r2_score(y_test, predictions.detach().numpy())}')

