from algopipe.registry import Registry,BaseModule

@Registry.register("ML_Algorithms",subcategory="Classification_Algorithms")
class LinearDiscriminantAnalysis(BaseModule):
    name = "Linear Discriminant Analysis"
    description = "Linear Discriminant Analysis Classifier using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.discriminant_analysis import LinearDiscriminantAnalysis",
            "from sklearn.metrics import accuracy_score"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = LinearDiscriminantAnalysis()\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'Accuracy: {{accuracy_score(y_test, preds)}}')"
        )