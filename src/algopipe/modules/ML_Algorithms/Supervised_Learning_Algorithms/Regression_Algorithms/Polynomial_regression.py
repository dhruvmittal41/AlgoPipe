from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Regression_Algorithms")
class PolynomialRegression(BaseModule):
    name = "Polynomial Regression"
    description = "Polynomial Regression model"

    def get_imports(self):
        return [
            "from sklearn.preprocessing import PolynomialFeatures",
            "from sklearn.linear_model import LinearRegression",
            "from sklearn.metrics import mean_squared_error"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Transform features to polynomial features\n"
            f"poly = PolynomialFeatures(degree=2)\n"
            f"X_poly_train = poly.fit_transform(X_train)\n"
            f"X_poly_test = poly.transform(X_test)\n\n"
            f"# Initialize and Train Model\n"
            f"{variable_name} = LinearRegression()\n"
            f"{variable_name}.fit(X_poly_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds = {variable_name}.predict(X_poly_test)\n"
            f"print(f'MSE: {{mean_squared_error(y_test, preds)}}')"
        )