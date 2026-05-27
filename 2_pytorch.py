import torch 

b = torch.tensor(32)
w1 = torch.tensor(1.8)

X1 = torch.tensor([10.0, 30.0, 50.0, 100.0, 150.0])

y_pred = 1 * b + X1 * w1

print(X1.shape)
print(X1.size())

print(y_pred)

# access to individual value of tensor
print(X1[0])
print(X1[1])
print(X1[2])
print(X1[3])
print(X1[4])

# get the value of a tensor
print(X1[0].item())
print(X1[1].item())
print(X1[2].item())
print(X1[3].item())
print(X1[4].item())