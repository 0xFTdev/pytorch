import torch

x = torch.rand(4, 4)
print(x)
y = x.view(-1, 8)
print(y.size())

