from algopipe.registry import Registry, BaseModule

@Registry.register("DL_Algorithms",subcategory="Basic_NN")
class Perceptron(BaseModule):
    name = "Perceptron"
    description = "Perceptron Algorithm for binary classification"

    def get_imports(self):
        return [
            "import numpy as np"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Perceptron Algorithm\n"
            f"def perceptron(X, y, weights, learning_rate=0.01, epochs=1000):\n"
            f"    for epoch in range(epochs):\n"
            f"        for i in range(len(X)):\n"
            f"            linear_output = np.dot(X[i], weights)\n"
            f"            predicted = 1 if linear_output >= 0 else 0\n\n"
            f"            # Update weights\n"
            f"            update = learning_rate * (y[i] - predicted)\n"
            f"            weights += update * X[i]\n\n"
            f"    return weights\n\n"
            f"# Example usage\n"
            f"{variable_name} = perceptron(X, y, weights)"
        )