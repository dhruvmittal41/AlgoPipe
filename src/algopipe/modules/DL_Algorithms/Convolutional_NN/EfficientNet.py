from algopipe.registry import Registry, BaseModule

@Registry.register("DL_Algorithms",subcategory="Convolutional_NN")
class EfficientNet(BaseModule):
    name = "EfficientNet"
    description = "EfficientNet: A family of convolutional neural networks that achieve high accuracy with fewer parameters"

    def get_imports(self):
        return [
            "import torch",
            "import torch.nn as nn",
            "import torch.nn.functional as F"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# EfficientNet Architecture\n"
            f"class EfficientNet(nn.Module):\n"
            f"    def __init__(self, num_classes=10):\n"
            f"        super(EfficientNet, self).__init__()\n"
            f"        # Define layers here (this is a simplified version)\n"
            f"        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)\n"
            f"        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)\n"
            f"        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)\n"
            f"        self.pool = nn.MaxPool2d(2, 2)\n"
            f"        self.fc1 = nn.Linear(128 * 4 * 4, 512)\n"
            f"        self.fc2 = nn.Linear(512, num_classes)\n\n"
            f"    def forward(self, x):\n"
            f"        x = F.relu(self.conv1(x))\n"
            f"        x = self.pool(x)\n"
            f"        x = F.relu(self.conv2(x))\n"
            f"        x = self.pool(x)\n"
            f"        x = F.relu(self.conv3(x))\n"
            f"        x = self.pool(x)\n"
            f"        x = x.view(-1, 128 * 4 * 4)\n"
            f"        x = F.relu(self.fc1(x))\n"
            f"        x = self.fc2(x)\n"
            f"        return x\n\n"
            f"# Initialize model\n"
            f"{variable_name} = EfficientNet(num_classes=10)"
        )