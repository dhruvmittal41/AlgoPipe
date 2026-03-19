from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Dimensionality_Reduction_Algorithms")
class t_SNE(BaseModule):
    name = "t-Distributed Stochastic Neighbor Embedding (t-SNE)"
    description = "t-SNE for Dimensionality Reduction using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.manifold import TSNE",
            "from sklearn.metrics import mean_squared_error"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Fit Model\n"
            f"{variable_name} = TSNE(n_components=2, random_state=42)\n"
            f"X_reduced = {variable_name}.fit_transform(X)\n\n"
            f"# Note: t-SNE does not have an inverse transform method, so we cannot reconstruct the original data.\n"
            f"print('t-SNE does not support inverse transformation, so reconstruction error cannot be calculated.')"
        )