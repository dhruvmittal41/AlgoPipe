from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="ReinforcementLearning_Algorithms")
class DeepQNetworks(BaseModule):
    name = "Deep Q-Networks"
    description = "Deep Q-Networks (DQN) implementation for reinforcement learning"

    def get_imports(self):
        return [
            "import numpy as np",
            "import tensorflow as tf",
            "from collections import deque",
            "import random"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# DQN Hyperparameters\n"
            f"state_size = 4  # Example state size\n"
            f"action_size = 2  # Example action size\n"
            f"learning_rate = 0.001\n"
            f"gamma = 0.95\n"
            f"epsilon = 1.0\n"
            f"epsilon_decay = 0.995\n"
            f"epsilon_min = 0.01\n"
            f"batch_size = 64\n"
            f"memory = deque(maxlen=2000)\n\n"
            
            f"# Build DQN Model\n"
            f"{variable_name} = tf.keras.Sequential([\n"
            f"    tf.keras.layers.Dense(24, input_dim=state_size, activation='relu'),\n"
            f"    tf.keras.layers.Dense(24, activation='relu'),\n"
            f"    tf.keras.layers.Dense(action_size, activation='linear')\n"
            f"])\n"
            f"{variable_name}.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=learning_rate))\n\n"
            
            f"# Example of storing experience in memory and training the model would go here."
        )