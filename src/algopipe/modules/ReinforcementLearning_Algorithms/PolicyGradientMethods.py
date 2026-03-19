from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="ReinforcementLearning_Algorithms")
class PolicyGradientMethods(BaseModule):
    name = "Policy Gradient Methods"
    description = "Policy Gradient Methods for Reinforcement Learning"

    def get_imports(self):
        return [
            "import numpy as np",
            "import tensorflow as tf"
        ]
    
    def get_code(self, variable_name="policy_gradient"):
        return (
            f"# Policy Gradient Methods Implementation\n"
            f"def policy_gradient(env, policy, optimizer, episodes):\n"
            f"    for episode in range(episodes):\n"
            f"        state = env.reset()\n"
            f"        done = False\n"
            f"        while not done:\n"
            f"            action = policy(state)\n"
            f"            next_state, reward, done, _ = env.step(action)\n"
            f"            # Update policy using reward\n"
            f"            optimizer.update(policy, state, action, reward)\n"
            f"            state = next_state\n\n"
            f"# Example usage\n"
            f"{variable_name} = policy_gradient(env, policy, optimizer, episodes=1000)"
        )