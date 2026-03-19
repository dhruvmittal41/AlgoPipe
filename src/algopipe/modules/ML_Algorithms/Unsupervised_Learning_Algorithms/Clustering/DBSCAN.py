from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Clustering_Algorithms")
class DBSCAN(BaseModule):
    name = "DBSCAN"
    description = "Density-Based Spatial Clustering of Applications with Noise (DBSCAN) using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.cluster import DBSCAN",
            "from sklearn.metrics import silhouette_score"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = DBSCAN(eps=0.5, min_samples=5)\n"
            f"{variable_name}.fit(X)\n\n"
            f"# Cluster Assignments\n"
            f"labels = {variable_name}.labels_\n"
            f"print(f'Silhouette Score: {{silhouette_score(X, labels)}}')"
        )
