from algopipe.registry import Registry, BaseModule

@Registry.register("DL_Algorithms",subcategory="Convolutional_NN")
class MobileNet(BaseModule):
    name = "MobileNet"
    description = "MobileNet: A lightweight convolutional neural network architecture for mobile and embedded vision applications"

    def get_imports(self):
        return [
            "import torch",
            "import torch.nn as nn",
            "import torch.nn.functional as F"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# MobileNet Architecture\n"
            f"class MobileNet(nn.Module):\n"
            f"    def __init__(self, num_classes=10):\n"
            f"        super(MobileNet, self).__init__()\n"
            f"        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=2, padding=1)\n"
            f"        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)\n"
            f"        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1)\n"
            f"        self.conv4 = nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1)\n"
            f"        self.pool = nn.AdaptiveAvgPool2d((1, 1))\n"
            f"        self.fc = nn.Linear(256, num_classes)\n\n"
            f"    def forward(self, x):\n"
            f"        x = F.relu(self.conv1(x))\n"
            f"        x = F.relu(self.conv2(x))\n"
            f"        x = F.relu(self.conv3(x))\n"
            f"        x = F.relu(self.conv4(x))\n"
            f"        x = self.pool(x)\n"
            f"        x = x.view(-1, 256)\n"
            f"        x = self.fc(x)\n"
            f"        return x\n\n"
            f"# Initialize model\n"
            f"{variable_name} = MobileNet(num_classes=10)"
        )