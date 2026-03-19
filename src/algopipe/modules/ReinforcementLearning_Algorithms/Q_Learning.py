from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="ReinforcementLearning_Algorithms")
class Q_Learning(BaseModule):
    name = "Q-Learning"
    description = "Q-Learning Algorithm for Reinforcement Learning"

    def get_imports(self):
        return [
            "import numpy as np",
            "import random"
        ]
    
    def get_code(self, variable_name="q_learning"):
        return (
            f"# Q-Learning Implementation\n"
            f"def q_learning(env, alpha, gamma, episodes):\n"
            f"    q_table = np.zeros((env.observation_space.n, env.action_space.n))\n"
            f"    for episode in range(episodes):\n"
            f"        state = env.reset()\n"
            f"        done = False\n"
            f"        while not done:\n"
            f"            action = np.argmax(q_table[state]) if random.uniform(0, 1) > 0.1 else env.action_space.sample()\n"
            f"            next_state, reward, done, _ = env.step(action)\n"
            f"            q_table[state][action] += alpha * (reward + gamma * np.max(q_table[next_state]) - q_table[state][action])\n"
            f"            state = next_state\n\n"
            f"# Example usage\n"
            f"{variable_name} = q_learning(env, alpha=0.1, gamma=0.9, episodes=1000)"
        )