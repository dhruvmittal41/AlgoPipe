from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Semi_Supervised_Learning_Algorithms")
class PseudoLabeling(BaseModule):
    name = "Pseudo Labeling"
    description = "Pseudo Labeling Algorithm for Semi-Supervised Learning using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.semi_supervised import SelfTrainingClassifier",
            "from sklearn.metrics import accuracy_score"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"base_model = SomeBaseClassifier()  # Replace with your base classifier\n"
            f"{variable_name} = SelfTrainingClassifier(base_model)\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'Accuracy: {{accuracy_score(y_test, preds)}}')"
        )