from algopipe.registry import Registry, BaseModule

@Registry.register("DL_Algorithms",subcategory="Generative_Models")
class Autoencoders(BaseModule):
    name = "Autoencoders"
    description = "Autoencoders: A type of neural network used for unsupervised learning of efficient codings"

    def get_imports(self):
        return [
            "import torch",
            "import torch.nn as nn",
            "import torch.optim as optim"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Autoencoder Architecture\n"
            f"class Autoencoder(nn.Module):\n"
            f"    def __init__(self):\n"
            f"        super(Autoencoder, self).__init__()\n"
            f"        # Define encoder and decoder layers here\n"
            f"        pass\n\n"
            f"    def forward(self, x):\n"
            f"        # Define the forward pass here\n"
            f"        pass\n\n"
            f"# Initialize model\n"
            f"{variable_name} = Autoencoder()"
        )