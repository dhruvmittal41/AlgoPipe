from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Dimensionality_Reduction_Algorithms")
class FactorAnalysis(BaseModule):
    name = "Factor Analysis"
    description = "Factor Analysis for Dimensionality Reduction using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.decomposition import FactorAnalysis",
            "from sklearn.metrics import mean_squared_error"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Fit Model\n"
            f"{variable_name} = FactorAnalysis(n_components=2, random_state=42)\n"
            f"X_reduced = {variable_name}.fit_transform(X)\n\n"
            f"# Reconstruct Data and Evaluate\n"
            f"X_approx = {variable_name}.inverse_transform(X_reduced)\n"
            f"print(f'Mean Squared Reconstruction Error: {{mean_squared_error(X, X_approx)}}')"
        )