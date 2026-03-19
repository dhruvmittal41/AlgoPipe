from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Probalistic&Bayesian_Methods")
class HiddenMarkovModels(BaseModule):
    name = "Hidden Markov Models"
    description = "Hidden Markov Models using hmmlearn library"

    def get_imports(self):
        return [
            "from hmmlearn import hmm",
            "import numpy as np"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Initialize and Train Model\n"
            f"{variable_name} = hmm.GaussianHMM(n_components=3, covariance_type='diag', n_iter=100)\n"
            f"{variable_name}.fit(X_train)\n\n"
            f"# Predict hidden states\n"
            f"hidden_states = {variable_name}.predict(X_test)\n"
            f"print(f'Predicted hidden states: {{hidden_states}}')"
        )