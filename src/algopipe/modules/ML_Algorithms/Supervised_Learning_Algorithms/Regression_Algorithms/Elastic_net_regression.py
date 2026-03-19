from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Regression_Algorithms")
class ElasticNetRegression(BaseModule):
    name = "Elastic Net Regression"
    description = "Elastic Net Regression model"

    def get_imports(self):
        return [
            "from sklearn.linear_model import ElasticNet",
            "from sklearn.metrics import mean_squared_error"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = ElasticNet(alpha=0.1, l1_ratio=0.5)\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_test)\n"
            f"print(f'MSE: {{mean_squared_error(y_test, preds)}}')"
        )