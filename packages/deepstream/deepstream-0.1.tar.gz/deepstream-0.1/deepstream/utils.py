import torch
from torch import nn
import numpy as np

def load_deepstream(path):
    data = np.load(path)
    
    train_activations = data['train_activations']
    test_activations = data['test_activations']
    train_labels = data['train_labels']
    test_labels = data['test_labels']
    counters = data['counters']
    loss = data['loss']
    
    return (
        train_activations, test_activations,
        train_labels, test_labels,
        counters, loss
    )

class NN(nn.Module):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        
    def forward(self, x):
        return self.stack(x)

def get_device():
    return (
        "cuda"
        if torch.cuda.is_available()
        else "mps"
        if torch.backends.mps.is_available()
        else "cpu"
    )

def cifar_stack():
    return nn.Sequential(
        nn.Conv2d(3, 15, kernel_size=5),
        nn.MaxPool2d(2),
        nn.Flatten(),
        nn.ReLU(),
        nn.Linear(2940, 512),
        nn.ReLU(),
        nn.Linear(512, 512),
        nn.ReLU(),
        nn.Linear(512, 10)
        )
    
def mnist_stack():
    return nn.Sequential(
        nn.Conv2d(1, 15, kernel_size=5),
        nn.MaxPool2d(2),
        nn.Flatten(),
        nn.ReLU(),
        nn.Linear(2160, 512),
        nn.ReLU(),
        nn.Linear(512, 512),
        nn.ReLU(),
        nn.Linear(512, 10)
        )