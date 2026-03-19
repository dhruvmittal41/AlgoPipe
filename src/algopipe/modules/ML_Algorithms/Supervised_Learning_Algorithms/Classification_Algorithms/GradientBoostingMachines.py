from algopipe.registry import Registry,BaseModule

@Registry.register("ML_Algorithms",subcategory="Classification_Algorithms")
class GradientBoostingMachines(BaseModule):
    name = "Gradient Boosting Machines"
    description = "Gradient Boosting Classifier using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.ensemble import GradientBoostingClassifier",
            "from sklearn.metrics import accuracy_score"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'Accuracy: {{accuracy_score(y_test, preds)}}')"
        )