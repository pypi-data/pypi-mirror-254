Introduction
=============
MindTorch is MindSpore tool for adapting the PyTorch interface, which is designed to make PyTorch code perform efficiently on Ascend without changing the habits of the original PyTorch users.

|MindTorch-architecture|

Install
=======

MindTorch has some prerequisites that need to be installed first, including MindSpore, PIL, NumPy.

.. code:: bash

    # for last stable version
    pip install mindtorch

    # for latest release candidate
    pip install --upgrade --pre mindtorch

Alternatively, you can install the latest or development version by directly pulling from OpenI:

.. code:: bash

    pip3 install git+https://openi.pcl.ac.cn/OpenI/MSAdapter.git

User guide
===========
For data processing and model building, MindTorch can be used in the same way as PyTorch, while the model training part of the code needs to be customized, as shown in the following example.

1. Data processing (only modify the import package)

.. code:: python

    from mindtorch.torch.utils.data import DataLoader
    from mindtorch.torchvision import datasets, transforms

    transform = transforms.Compose([transforms.Resize((224, 224), interpolation=InterpolationMode.BICUBIC),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.4914, 0.4822, 0.4465], std=[0.247, 0.2435, 0.2616])
                                   ])
    train_images = datasets.CIFAR10('./', train=True, download=True, transform=transform)
    train_data = DataLoader(train_images, batch_size=128, shuffle=True, num_workers=2, drop_last=True)

2. Model construction (modify import package only)

.. code:: python

    from mindtorch.torch.nn import Module, Linear, Flatten

    class MLP(Module):
        def __init__(self):
            super(MLP, self).__init__()
            self.flatten = Flatten()
            self.line1 = Linear(in_features=1024, out_features=64)
            self.line2 = Linear(in_features=64, out_features=128, bias=False)
            self.line3 = Linear(in_features=128, out_features=10)

        def forward(self, inputs):
            x = self.flatten(inputs)
            x = self.line1(x)
            x = self.line2(x)
            x = self.line3(x)
            return x

3.Model training (custom training)

.. code:: python

    import mindtorch.torch as torch
    import mindtorch.torch.nn as nn
    import mindspore as ms

    net = MLP()
    net.train()
    epochs = 500
    criterion = nn.CrossEntropyLoss()
    optimizer = ms.nn.SGD(net.trainable_params(), learning_rate=0.01, momentum=0.9, weight_decay=0.0005)

    # Define the training process
    loss_net = ms.nn.WithLossCell(net, criterion)
    train_net = ms.nn.TrainOneStepCell(loss_net, optimizer)

    for i in range(epochs):
        for X, y in train_data:
            res = train_net(X, y)
            print("epoch:{}, loss:{:.6f}".format(i, res.asnumpy()))
    # Save model
    ms.save_checkpoint(net, "save_path.ckpt")


License
=======

MindTorch is released under the Apache 2.0 license.

.. |MindTorch-architecture| image:: https://openi.pcl.ac.cn/laich/pose_data/raw/branch/master/MSA_F.png