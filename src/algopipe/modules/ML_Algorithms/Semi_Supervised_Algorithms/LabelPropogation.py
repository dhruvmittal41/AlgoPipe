from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Semi_Supervised_Learning_Algorithms")
class LabelPropagation(BaseModule):
    name = "Label Propagation"
    description = "Label Propagation Algorithm for Semi-Supervised Learning using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.semi_supervised import LabelPropagation",
            "from sklearn.metrics import accuracy_score"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = LabelPropagation()\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'Accuracy: {{accuracy_score(y_test, preds)}}')"
        )