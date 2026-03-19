from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Ensemble_Learning_Algorithms")
class Blending(BaseModule):
    name = "Blending"
    description = "Blending Classifier using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.ensemble import StackingClassifier",
            "from sklearn.metrics import accuracy_score"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"estimators = [\n"
            f"    ('model1', SomeBaseClassifier1()),  # Replace with your base classifiers\n"
            f"    ('model2', SomeBaseClassifier2())\n"
            f"]\n"
            f"{variable_name} = StackingClassifier(estimators=estimators, final_estimator=SomeFinalEstimator())\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'Accuracy: {{accuracy_score(y_test, preds)}}')"
        )