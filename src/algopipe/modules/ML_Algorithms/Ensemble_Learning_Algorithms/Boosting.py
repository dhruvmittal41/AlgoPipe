from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Ensemble_Learning_Algorithms")
class Boosting(BaseModule):
    name = "Boosting"
    description = "Boosting Classifier using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.ensemble import AdaBoostClassifier",
            "from sklearn.metrics import accuracy_score"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = AdaBoostClassifier(n_estimators=100, random_state=42)\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'Accuracy: {{accuracy_score(y_test, preds)}}')"
        )