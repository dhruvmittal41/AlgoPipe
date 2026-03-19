from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Dimensionality_Reduction_Algorithms")
class UMAP(BaseModule):
    name = "Uniform Manifold Approximation and Projection (UMAP)"
    description = "UMAP for Dimensionality Reduction using umap-learn library"

    def get_imports(self):
        return [
            "import umap",
            "from sklearn.metrics import mean_squared_error"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Fit Model\n"
            f"{variable_name} = umap.UMAP(n_components=2, random_state=42)\n"
            f"X_reduced = {variable_name}.fit_transform(X)\n\n"
            f"# Note: UMAP does not have an inverse_transform method, so we cannot reconstruct the original data.\n"
            f"print('UMAP does not support data reconstruction, so mean squared error cannot be calculated.')"
        )