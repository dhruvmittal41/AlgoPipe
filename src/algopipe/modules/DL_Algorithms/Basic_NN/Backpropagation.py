from algopipe.registry import Registry, BaseModule

@Registry.register("DL_Algorithms",subcategory="Basic_NN")
class Backpropagation(BaseModule):
    name = "Backpropagation"
    description = "Backpropagation Algorithm for training neural networks"

    def get_imports(self):
        return [
            "import numpy as np"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Backpropagation Algorithm\n"
            f"def backpropagation(X, y, weights, learning_rate=0.01):\n"
            f"    # Forward pass\n"
            f"    outputs = np.dot(X, weights)\n"
            f"    predictions = 1 / (1 + np.exp(-outputs))  # Sigmoid activation\n\n"
            f"    # Compute error\n"
            f"    error = predictions - y\n\n"
            f"    # Backward pass (compute gradients)\n"
            f"    gradients = np.dot(X.T, error) / len(X)\n\n"
            f"    # Update weights\n"
            f"    weights -= learning_rate * gradients\n\n"
            f"    return weights"
            f"# Example usage\n"
            f"{variable_name} = backpropagation(X, y, weights)"
        )
