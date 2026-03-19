from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Ensemble_Learning_Algorithms")
class VotingClassifier(BaseModule):
    name = "Voting Classifier"
    description = "Voting Classifier using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.ensemble import VotingClassifier",
            "from sklearn.metrics import accuracy_score"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"estimators = [\n"
            f"    ('model1', SomeBaseClassifier1()),  # Replace with your base classifiers\n"
            f"    ('model2', SomeBaseClassifier2())\n"
            f"]\n"
            f"{variable_name} = VotingClassifier(estimators=estimators, voting='hard')\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'Accuracy: {{accuracy_score(y_test, preds)}}')"
        )
