def train():
    # Save training code and hyperparameters
    experiment = keepsake.init(path=".", params={...})
    model = Model()

    for epoch in range(num_epochs):
        # ...

        torch.save(model, "model.pth")
