import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

    def linear(self):
        self.fc0 = nn.Linear(28*28, 27)
        self.ntw = 'linear'

    def conv2d(self):
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)
        # self.fc0 = nn.Conv2d(16, 33, 3, stride=1, padding=0 )
        self.ntw = 'conv2d'

    def forward(self, x):
        if (self.ntw == 'linear'):
            x = self.fc0(x.view(x.size(0), -1))
            return F.log_softmax(x)
        elif (self.ntw == 'conv2d'):
            x = F.relu(self.conv1(x))
            return F.relu(self.conv2(x))
            # x = self.fc0(x.view(x.size(0), -1))
            # return F.relu(x)
