from algopipe.registry import Registry, BaseModule

@Registry.register("DL_Algorithms",subcategory="Convolutional_NN")
class ResNet(BaseModule):
    name = "ResNet"
    description = "ResNet: A deep convolutional neural network architecture with residual connections"

    def get_imports(self):
        return [
            "import torch",
            "import torch.nn as nn",
            "import torch.nn.functional as F"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# ResNet Architecture\n"
            f"class BasicBlock(nn.Module):\n"
            f"    def __init__(self, in_channels, out_channels, stride=1):\n"
            f"        super(BasicBlock, self).__init__()\n"
            f"        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1)\n"
            f"        self.bn1 = nn.BatchNorm2d(out_channels)\n"
            f"        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1)\n"
            f"        self.bn2 = nn.BatchNorm2d(out_channels)\n"
            f"        self.shortcut = nn.Sequential()\n"
            f"        if stride != 1 or in_channels != out_channels:\n"
            f"            self.shortcut = nn.Sequential(\n"
            f"                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride),\n"
            f"                nn.BatchNorm2d(out_channels)\n"
            f"            )\n\n"
            f"    def forward(self, x):\n"
            f"        out = F.relu(self.bn1(self.conv1(x)))\n"
            f"        out = self.bn2(self.conv2(out))\n"
            f"        out += self.shortcut(x)\n"
            f"        out = F.relu(out)\n"
            f"        return out\n\n"
            f"class ResNet(nn.Module):\n"
            f"    def __init__(self, block, num_blocks, num_classes=10):\n"
            f"        super(ResNet, self).__init__()\n"
            f"        self.in_channels = 64\n"
            f"        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)\n"
            f"        self.bn1 = nn.BatchNorm2d(64)\n"
            f"        self.layer1 = self._make_layer(block, 64, num_blocks[0], stride=1)\n"
            f"        self.layer2 = self._make_layer(block, 128, num_blocks[1], stride=2)\n"
            f"        self.layer3 = self._make_layer(block, 256, num_blocks[2], stride=2)\n"
            f"        self.layer4 = self._make_layer(block, 512, num_blocks[3], stride=2)\n"
            f"        self.linear = nn.Linear(512, num_classes)\n\n"
            f"    def _make_layer(self, block, out_channels, num_blocks, stride):\n"
            f"        strides = [stride] + [1] * (num_blocks - 1)\n"
            f"        layers = []\n"
            f"        for stride in strides:\n"
            f"            layers.append(block(self.in_channels, out_channels, stride))\n"
            f"            self.in_channels = out_channels\n"
            f"        return nn.Sequential(*layers)\n\n"
            f"    def forward(self, x):\n"
            f"        out = F.relu(self.bn1(self.conv1(x)))\n"
            f"        out = self.layer1(out)\n"
            f"        out = self.layer2(out)\n"
            f"        out = self.layer3(out)\n"
            f"        out = self.layer4(out)\n"
            f"        out = F.avg_pool2d(out, 4)\n"
            f"        out = out.view(out.size(0), -1)\n"
            f"        out = self.linear(out)\n"
            f"        return out\n\n"
            f"# Initialize model\n"
            f"{variable_name} = ResNet(BasicBlock, [2, 2, 2, 2], num_classes=10)"
        )