from algopipe.registry import Registry, BaseModule

@Registry.register("DL_Algorithms",subcategory="Convolutional_NN")
class DenseNet(BaseModule):
    name = "DenseNet"
    description = "DenseNet: Densely Connected Convolutional Networks"

    def get_imports(self):
        return [
            "import torch",
            "import torch.nn as nn",
            "import torch.nn.functional as F"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# DenseNet Architecture\n"
            f"class DenseBlock(nn.Module):\n"
            f"    def __init__(self, num_layers, in_channels, growth_rate):\n"
            f"        super(DenseBlock, self).__init__()\n"
            f"        self.layers = nn.ModuleList()\n"
            f"        for i in range(num_layers):\n"
            f"            self.layers.append(nn.Sequential(\n"
            f"                nn.BatchNorm2d(in_channels + i * growth_rate),\n"
            f"                nn.ReLU(inplace=True),\n"
            f"                nn.Conv2d(in_channels + i * growth_rate, growth_rate, kernel_size=3, padding=1)\n"
            f"            ))\n\n"
            f"    def forward(self, x):\n"
            f"        features = [x]\n"
            f"        for layer in self.layers:\n"
            f"            new_feature = layer(torch.cat(features, 1))\n"
            f"            features.append(new_feature)\n"
            f"        return torch.cat(features, 1)\n\n"
            f"class DenseNet(nn.Module):\n"
            f"    def __init__(self, growth_rate=32, num_blocks=4, num_layers_per_block=6, num_classes=10):\n"
            f"        super(DenseNet, self).__init__()\n"
            f"        self.conv1 = nn.Conv2d(3, growth_rate * 2, kernel_size=7, stride=2, padding=3)\n"
            f"        self.pool = nn.MaxPool2d(3, stride=2, padding=1)\n"
            f"        self.blocks = nn.ModuleList()\n"
            f"        num_channels = growth_rate * 2\n"
            f"        for _ in range(num_blocks):\n"
            f"            block = DenseBlock(num_layers_per_block, num_channels, growth_rate)\n"
            f"            self.blocks.append(block)\n"
            f"            num_channels += num_layers_per_block * growth_rate\n"
            f"        self.classifier = nn.Linear(num_channels, num_classes)\n\n"
            f"    def forward(self, x):\n"
            f"        x = self.conv1(x)\n"
            f"        x = self.pool(x)\n"
            f"        for block in self.blocks:\n"
            f"            x = block(x)\n"
            f"        x = F.adaptive_avg_pool2d(x, (1, 1))\n"
            f"        x = x.view(x.size(0), -1)\n"
            f"        x = self.classifier(x)\n"
            f"        return x\n\n"
            f"# Initialize model\n"
            f"{variable_name} = DenseNet(growth_rate=32, num_blocks=4, num_layers_per_block=6, num_classes=10)"
        )