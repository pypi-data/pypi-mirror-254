import torch
import numpy as np
from .utils import get_device, NN
from torch.utils.data import DataLoader
from tqdm import tqdm

class DeepStream():
    def __init__(self, 
                 train_data,
                 test_data,
                 stack,
                 loss_fn = torch.nn.CrossEntropyLoss(),
                 optim_cc = {'optimc': torch.optim.SGD, 'kwargs': {'lr': 1e-3}},
                 batch_size = 250,
                 n_epochs = 50,
                 device = get_device(),
                 dtype = np.float16,
                 drop_unequal = True
                ):
        
        # Assign data
        self.train_data = train_data
        self.test_data = test_data
        self.dtype = dtype
        self.drop_unequal = drop_unequal
                
        # Identify classes in training data
        if hasattr(train_data, 'targets'):
            self.classes = np.unique(train_data.targets)
        elif hasattr(train_data, 'labels'):
            self.classes = np.unique(train_data.labels)
        self.n_classes = self.classes.shape[0]
        
        # Initialize model
        self.device = device
        self.stack = stack
        self.model = NN(self.stack).to(self.device)
        
        # Prepare training environment
        self.batch_size = batch_size
        self.n_epochs = n_epochs

        self.loss_fn = loss_fn
        self.optimizer = optim_cc['optimc'](self.model.parameters(),
                                            **optim_cc['kwargs'])
        
    def process(self):
        # Initializing counters
        train_epoch = 0
        train_batch = 0
        
        test_epoch = 0
        test_batch = 0
        overal_batch = 0

        # Preparing dataloaders
        train_dataloader = DataLoader(self.train_data, 
                                      batch_size=self.batch_size)
        test_dataloader = DataLoader(self.test_data, 
                                     batch_size=self.batch_size)
        n_steps = self.n_epochs * len(train_dataloader)

        # Preparing the storage space
        _train_activations = []
        _test_activations = []
        _train_labels = []
        _test_labels = []
        _counters = []
        _loss = []
                
        # Initializing iterators and starting the processing loop
        it_train = iter(train_dataloader)
        it_test = iter(test_dataloader)
        
        pbar = tqdm(total=n_steps)
        while train_epoch < self.n_epochs:
            # Iterate training set
            try:
                X_train, y_train = next(it_train)
                if self.drop_unequal and X_train.shape[0] != self.batch_size:
                    raise StopIteration
            except StopIteration:
                train_epoch += 1
                if train_epoch == self.n_epochs:
                    break
                train_batch = 0
                it_train = iter(train_dataloader)
                X_train, y_train = next(it_train)
                
            # Iterate test set
            try:
                X_test, y_test = next(it_test)
                if self.drop_unequal and X_test.shape[0] != self.batch_size:
                    raise StopIteration
            except StopIteration:
                test_epoch += 1
                test_batch = 0
                it_test = iter(test_dataloader)
                X_test, y_test = next(it_test)

            # Update progress bar
            pbar.update(1)
            pbar.set_description('%s | %s' % (
                ('Epochs (tr%04i:te%04i)' % (train_epoch, test_epoch)),
                ('Batches (tr%04i:te%04i)' % (train_batch, test_batch))
            ))

            """
            Main processing
            """
            # Process training data
            self.model.train()
            train_activation = self.model(X_train.to(self.device))
            loss = self.loss_fn(train_activation, y_train.to(self.device))
            
            # Backpropagation
            loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()
            
            # Process test data
            self.model.eval()
            test_activation = self.model(X_test.to(self.device))
            
            # Store
            _train_activations.append(train_activation.cpu().detach().numpy().astype(self.dtype))
            _test_activations.append(test_activation.cpu().detach().numpy().astype(self.dtype))

            _train_labels.append(y_train.cpu().detach().numpy().astype(self.dtype))
            _test_labels.append(y_test.cpu().detach().numpy().astype(self.dtype))
            
            _counters.append([overal_batch, train_batch, test_batch, train_epoch, test_epoch])
            _loss.append(loss.item())

            # Ending increments
            train_batch += 1
            test_batch += 1
            overal_batch += 1
            
        # Postprocessing
        self.train_activations = np.array(_train_activations)
        self.test_activations = np.array(_test_activations)

        self.train_labels = np.array(_train_labels)
        self.test_labels = np.array(_test_labels)
        
        self.counters = np.array(_counters)
        self.loss = np.array(_loss)

    def save_artifacts(self, path):
        np.savez(path, 
                 train_activations = self.train_activations,
                 test_activations = self.test_activations,
                 train_labels = self.train_labels,
                 test_labels = self.test_labels,
                 counters = self.counters,
                 loss = self.loss)