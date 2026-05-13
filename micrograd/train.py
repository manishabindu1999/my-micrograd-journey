from nn import MLP


# dataset
xs = [
    [2.0, 3.0, -1.0],
    [3.0, -1.0, 0.5],
    [0.5, 1.0, 1.0],
    [1.0, 1.0, -1.0],
]

ys = [1.0, -1.0, -1.0, 1.0]


# model
model = MLP(3, [4, 4, 1])


# training loop
for k in range(50):

    # forward pass
    ypred = [model(x) for x in xs]

    # loss
    loss = sum((yout - ygt)**2 for ygt, yout in zip(ys, ypred))

    # zero gradients
    model.zero_grad()

    # backward pass
    loss.backward()

    # update parameters
    for p in model.parameters():
        p.data += -0.05 * p.grad

    print(k, loss.data)


# predictions
print("\nFinal Predictions:")

for x in xs:
    print(model(x).data)