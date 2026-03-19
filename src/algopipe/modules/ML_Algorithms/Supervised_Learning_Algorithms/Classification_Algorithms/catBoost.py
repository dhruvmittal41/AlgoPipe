from algopipe.registry import Registry,BaseModule

@Registry.register("ML_Algorithms",subcategory="Classification_Algorithms")
class CatBoost(BaseModule):
    name = "catBoost"
    description = "CatBoost Classifier"

    def get_imports(self):
        return [
            "from catboost import CatBoostClassifier",
            "from sklearn.metrics import accuracy_score"
        ]
    
    def get_code(self, variable_name = "model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = CatBoostClassifier(iterations=1000, learning_rate=0.1, depth=6, verbose=0)\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'Accuracy: {{accuracy_score(y_test, preds)}}')"
        )