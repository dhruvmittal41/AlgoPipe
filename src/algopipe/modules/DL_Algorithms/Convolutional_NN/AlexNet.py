from algopipe.registry import Registry, BaseModule

@Registry.register("DL_Algorithms",subcategory="Convolutional_NN")
class AlexNet(BaseModule):
    name = "AlexNet"
    description = "AlexNet architecture for image classification"

    def get_imports(self):
        return [
            "import torch",
            "import torch.nn as nn",
            "import torch.optim as optim",
            "from torchvision import datasets, transforms"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Define AlexNet Architecture\n"
            f"class AlexNet(nn.Module):\n"
            f"    def __init__(self, num_classes=1000):\n"
            f"        super(AlexNet, self).__init__()\n"
            f"        self.features = nn.Sequential(\n"
            f"            nn.Conv2d(3, 96, kernel_size=11, stride=4),\n"
            f"            nn.ReLU(inplace=True),\n"
            f"            nn.MaxPool2d(kernel_size=3, stride=2),\n"
            f"            nn.Conv2d(96, 256, kernel_size=5, padding=2),\n"
            f"            nn.ReLU(inplace=True),\n"
            f"            nn.MaxPool2d(kernel_size=3, stride=2),\n"
            f"            nn.Conv2d(256, 384, kernel_size=3, padding=1),\n"
            f"            nn.ReLU(inplace=True),\n"
            f"            nn.Conv2d(384, 384, kernel_size=3, padding=1),\n"
            f"            nn.ReLU(inplace=True),\n"
            f"            nn.Conv2d(384, 256, kernel_size=3, padding=1),\n"
            f"            nn.ReLU(inplace=True),\n"
            f"            nn.MaxPool2d(kernel_size=3, stride=2)\n"
            f"        )\n\n"
            f"        self.classifier = nn.Sequential(\n"
            f"            nn.Dropout(),\n"
            f"            nn.Linear(256 * 6 * 6, 4096),\n"
            f"            nn.ReLU(inplace=True),\n"
            f"            nn.Dropout(),\n"
            f"            nn.Linear(4096, 4096),\n"
            f"            nn.ReLU(inplace=True),\n"
            f"            nn.Linear(4096, num_classes)\n"
            f"        )\n\n"
            f"    def forward(self, x):\n"
            f"        x = self.features(x)\n"
            f"        x = x.view(x.size(0), 256 * 6 * 6)\n"
            f"        x = self.classifier(x)\n"
            f"        return x\n\n"
            f"# Initialize Model\n"
            f"{variable_name} = AlexNet(num_classes=1000)\n\n"
            f"# Example Training Loop\n"
            f"criterion = nn.CrossEntropyLoss()\n"
            f"optimizer = optim.SGD({variable_name}.parameters(), lr=0.01, momentum=0.9)\n\n"
            f"for epoch in range(10):\n"
            f"    for inputs, labels in train_loader:\n"
            f"        optimizer.zero_grad()\n"
            f"        outputs = {variable_name}(inputs)\n"
            f"        loss = criterion(outputs, labels)\n"
            f"        loss.backward()\n"
            f"        optimizer.step()\n"
        )