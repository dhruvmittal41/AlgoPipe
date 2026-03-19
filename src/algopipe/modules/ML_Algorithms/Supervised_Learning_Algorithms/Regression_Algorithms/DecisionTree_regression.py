from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Regression_Algorithms")
class DecisionTreeRegression(BaseModule):
    name = "Decision Tree Regression"
    description = "Decision Tree Regression model"

    def get_imports(self):
        return [
            "from sklearn.tree import DecisionTreeRegressor",
            "from sklearn.metrics import mean_squared_error"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = DecisionTreeRegressor(random_state=42)\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'MSE: {{mean_squared_error(y_test, preds)}}')"
        )