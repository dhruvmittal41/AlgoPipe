from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Clustering_Algorithms")
class HierarchicalClustering(BaseModule):
    name = "Hierarchical Clustering"
    description = "Hierarchical Clustering Algorithm using scikit-learn"

    def get_imports(self):
        return [
            "from sklearn.cluster import AgglomerativeClustering",
            "from sklearn.metrics import silhouette_score"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = AgglomerativeClustering(n_clusters=3)\n"
            f"{variable_name}.fit(X)\n\n"
            f"# Cluster Assignments\n"
            f"labels = {variable_name}.labels_\n"
            f"print(f'Silhouette Score: {{silhouette_score(X, labels)}}')"
        )