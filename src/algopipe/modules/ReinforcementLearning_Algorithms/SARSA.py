from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="ReinforcementLearning_Algorithms")
class SARSA(BaseModule):
    name = "SARSA"
    description = "SARSA Algorithm for Reinforcement Learning"

    def get_imports(self):
        return [
            "import numpy as np"
        ]
    
    def get_code(self, variable_name="sarsa"):
        return (
            f"# SARSA Implementation\n"
            f"def sarsa(env, alpha, gamma, epsilon, episodes):\n"
            f"    Q = np.zeros((env.observation_space.n, env.action_space.n))\n"
            f"    for episode in range(episodes):\n"
            f"        state = env.reset()\n"
            f"        action = np.random.choice(env.action_space.n) if np.random.rand() < epsilon else np.argmax(Q[state])\n"
            f"        done = False\n"
            f"        while not done:\n"
            f"            next_state, reward, done, _ = env.step(action)\n"
            f"            next_action = np.random.choice(env.action_space.n) if np.random.rand() < epsilon else np.argmax(Q[next_state])\n"
            f"            Q[state][action] += alpha * (reward + gamma * Q[next_state][next_action] - Q[state][action])\n"
            f"            state, action = next_state, next_action\n\n"
            f"# Example usage\n"
            f"{variable_name} = sarsa(env, alpha=0.1, gamma=0.99, epsilon=0.1, episodes=1000)"
        )