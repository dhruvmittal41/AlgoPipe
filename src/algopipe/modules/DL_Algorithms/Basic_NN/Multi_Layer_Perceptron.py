from algopipe.registry import Registry, BaseModule

@Registry.register("DL_Algorithms",subcategory="Basic_NN")
class MultiLayerPerceptron(BaseModule):
    name = "Multi-Layer Perceptron"
    description = "Multi-Layer Perceptron (MLP) implementation using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.neural_network import MLPClassifier",
            "from sklearn.metrics import accuracy_score"
        ],
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, random_state=42)\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'Accuracy: {{accuracy_score(y_test, preds)}}')"
        )