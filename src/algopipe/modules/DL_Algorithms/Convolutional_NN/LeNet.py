from algopipe.registry import Registry, BaseModule

@Registry.register("DL_Algorithms",subcategory="Convolutional_NN")
class LeNet(BaseModule):
    name = "LeNet"
    description = "LeNet-5: A pioneering convolutional neural network architecture for digit recognition"

    def get_imports(self):
        return [
            "import torch",
            "import torch.nn as nn",
            "import torch.nn.functional as F"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# LeNet-5 Architecture\n"
            f"class LeNet(nn.Module):\n"
            f"    def __init__(self, num_classes=10):\n"
            f"        super(LeNet, self).__init__()\n"
            f"        self.conv1 = nn.Conv2d(1, 6, kernel_size=5)\n"
            f"        self.conv2 = nn.Conv2d(6, 16, kernel_size=5)\n"
            f"        self.pool = nn.AvgPool2d(2, 2)\n"
            f"        self.fc1 = nn.Linear(16 * 4 * 4, 120)\n"
            f"        self.fc2 = nn.Linear(120, 84)\n"
            f"        self.fc3 = nn.Linear(84, num_classes)\n\n"
            f"    def forward(self, x):\n"
            f"        x = F.relu(self.conv1(x))\n"
            f"        x = self.pool(x)\n"
            f"        x = F.relu(self.conv2(x))\n"
            f"        x = self.pool(x)\n"
            f"        x = x.view(-1, 16 * 4 * 4)\n"
            f"        x = F.relu(self.fc1(x))\n"
            f"        x = F.relu(self.fc2(x))\n"
            f"        x = self.fc3(x)\n"
            f"        return x\n\n"
            f"# Initialize model\n"
            f"{variable_name} = LeNet(num_classes=10)"
        )