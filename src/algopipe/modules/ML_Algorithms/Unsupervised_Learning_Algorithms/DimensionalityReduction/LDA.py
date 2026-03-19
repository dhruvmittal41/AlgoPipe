from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Dimensionality_Reduction_Algorithms")
class LDA(BaseModule):
    name = "Linear Discriminant Analysis (LDA)"
    description = "LDA for Dimensionality Reduction using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.discriminant_analysis import LinearDiscriminantAnalysis",
            "from sklearn.metrics import mean_squared_error"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Fit Model\n"
            f"{variable_name} = LinearDiscriminantAnalysis(n_components=2)\n"
            f"X_reduced = {variable_name}.fit_transform(X, y)\n\n"
            f"# Reconstruct Data and Evaluate\n"
            f"X_approx = {variable_name}.inverse_transform(X_reduced)\n"
            f"print(f'Mean Squared Reconstruction Error: {{mean_squared_error(X, X_approx)}}')"
        )