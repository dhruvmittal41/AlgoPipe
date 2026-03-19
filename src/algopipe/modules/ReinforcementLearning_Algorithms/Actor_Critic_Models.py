from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="ReinforcementLearning_Algorithms")
class ActorCriticModel(BaseModule):
    name = "Actor-Critic Model"
    description = "Actor-Critic Model for Reinforcement Learning using PyTorch"

    def get_imports(self):
        return [
            "import torch",
            "import torch.nn as nn",
            "import torch.optim as optim"
        ]
    
    def get_code(self, variable_name="model"):
        return (
            f"# Define Actor-Critic Network\n"
            f"class ActorCritic(nn.Module):\n"
            f"    def __init__(self, state_dim, action_dim):\n"
            f"        super(ActorCritic, self).__init__()\n"
            f"        self.actor = nn.Sequential(\n"
            f"            nn.Linear(state_dim, 128),\n"
            f"            nn.ReLU(),\n"
            f"            nn.Linear(128, action_dim),\n"
            f"            nn.Softmax(dim=-1)\n"
            f"        )\n"
            f"        self.critic = nn.Sequential(\n"
            f"            nn.Linear(state_dim, 128),\n"
            f"            nn.ReLU(),\n"
            f"            nn.Linear(128, 1)\n"
            f"        )\n\n"
            f"    def forward(self, state):\n"
            f"        action_probs = self.actor(state)\n"
            f"        state_value = self.critic(state)\n"
            f"        return action_probs, state_value\n\n"
            f"# Initialize Actor-Critic Model\n"
            f"{variable_name} = ActorCritic(state_dim, action_dim)\n"
            f"optimizer = optim.Adam({variable_name}.parameters(), lr=0.001)\n\n"
            f"# Training Loop (simplified)\n"
            f"for episode in range(num_episodes):\n"
            f"    state = env.reset()\n"
            f"    done = False\n"
            f"    while not done:\n"
            f"        state_tensor = torch.FloatTensor(state).unsqueeze(0)\n"
            f"        action_probs, state_value = {variable_name}(state_tensor)\n"
            f"        action = torch.multinomial(action_probs, 1).item()\n"
            f"        next_state, reward, done, _ = env.step(action)\n"
            f"        # Compute loss and update model (not shown)\n"
            f"        state = next_state"
        )