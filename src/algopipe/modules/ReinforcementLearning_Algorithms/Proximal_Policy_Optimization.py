from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="ReinforcementLearning_Algorithms")
class ProximalPolicyOptimization(BaseModule):
    name = "Proximal Policy Optimization"
    description = "Proximal Policy Optimization (PPO) Algorithm for Reinforcement Learning"

    def get_imports(self):
        return [
            "import numpy as np",
            "import tensorflow as tf"
        ]
    
    def get_code(self, variable_name="ppo"):
        return (
            f"# Proximal Policy Optimization Implementation\n"
            f"def ppo(env, policy, optimizer, episodes, clip_epsilon=0.2):\n"
            f"    for episode in range(episodes):\n"
            f"        state = env.reset()\n"
            f"        done = False\n"
            f"        while not done:\n"
            f"            action = policy(state)\n"
            f"            next_state, reward, done, _ = env.step(action)\n"
            f"            # Compute advantage and update policy using PPO objective\n"
            f"            advantage = compute_advantage(state, action, reward)\n"
            f"            optimizer.update(policy, state, action, advantage, clip_epsilon)\n"
            f"            state = next_state\n\n"
            f"# Example usage\n"
            f"{variable_name} = ppo(env, policy, optimizer, episodes=1000)"
        )