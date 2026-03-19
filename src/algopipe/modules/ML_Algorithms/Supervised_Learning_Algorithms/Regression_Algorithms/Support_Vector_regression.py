from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Regression_Algorithms")
class SupportVectorRegression(BaseModule):
    name = "Support Vector Regression"
    description = "Support Vector Regression model"

    def get_imports(self):
        return [
            "from sklearn.svm import SVR",
            "from sklearn.metrics import mean_squared_error"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'MSE: {{mean_squared_error(y_test, preds)}}')"
        )