from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Probalistic&Bayesian_Methods")
class Gaussian_Processes(BaseModule):
    name = "Gaussian Processes"
    description = "Gaussian Processes for regression using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.gaussian_process import GaussianProcessRegressor",
            "from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C",
            "from sklearn.metrics import mean_squared_error"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Define the kernel and initialize the Gaussian Process Regressor\n"
            f"kernel = C(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-2, 1e2))\n"
            f"{variable_name} = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)\n\n"
            f"# Fit the model to the training data\n"
            f"{variable_name}.fit(X_train, y_train)\n\n"
            f"# Predictions\n"
            f"preds, sigma = {variable_name}.predict(X_test, return_std=True)\n"
            f"print(f'Mean Squared Error: {{mean_squared_error(y_test, preds)}}')\n"
            f"print(f'Predicted values: {{preds}}')\n"
            f"print(f'Prediction standard deviation: {{sigma}}')"
        )