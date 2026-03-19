from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Probalistic&Bayesian_Methods")
class Bayesian_Networks(BaseModule):
    name = "Bayesian Networks"
    description = "Bayesian Networks using pgmpy library"

    def get_imports(self):
        return [
            "from pgmpy.models import BayesianModel",
            "from pgmpy.inference import VariableElimination",
            "from sklearn.metrics import accuracy_score"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Define the structure of the Bayesian Network\n"
            f"{variable_name} = BayesianModel([('A', 'B'), ('B', 'C')])  # Example structure\n\n"
            f"# Fit the model to the data (assuming data is in a pandas DataFrame called 'data')\n"
            f"{variable_name}.fit(data)\n\n"
            f"# Perform inference\n"
            f"inference = VariableElimination({variable_name})\n"
            f"query_result = inference.query(variables=['C'], evidence={{'A': 1}})  # Example query\n"
            f"print(query_result)"
        )