from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Probalistic&Bayesian_Methods")
class Kalman_Filters(BaseModule):
    name = "Kalman Filters"
    description = "kalman filter implementation using filterpy library"

    def get_imports(self):
        return [
            "from filterpy.kalman import KalmanFilter",
            "import numpy as np"
        ]

    def get_code(self, variable_name="model"):
        return (
            f"# Initialize Kalman Filter\n"
            f"{variable_name} = KalmanFilter(dim_x=4, dim_z=2)\n"
            f"{variable_name}.F = np.array([[1, 0, 1, 0],\n"
            f"                             [0, 1, 0, 1],\n"
            f"                             [0, 0, 1, 0],\n"
            f"                             [0, 0, 0, 1]])  # State transition matrix\n"
            f"{variable_name}.H = np.array([[1, 0, 0, 0],\n"
            f"                             [0, 1, 0, 0]])  # Measurement function\n"
            f"{variable_name}.R = np.eye(2) * 0.1  # Measurement noise\n"
            f"{variable_name}.P = np.eye(4) * 1000  # Initial state covariance\n"
            f"{variable_name}.x = np.array([[0], [0], [1], [1]])  # Initial state\n\n"
            f"# Simulate some measurements (replace with actual measurements)\n"
            f"measurements = np.array([[1.2, 1.1], [2.3, 2.2], [3.4, 3.3]])\n\n"
            f"# Kalman Filter update loop\n"
            f"for z in measurements:\n"
            f"    {variable_name}.predict()\n"
            f"    {variable_name}.update(z)\n"
            f"    print(f'Updated state: {{ {variable_name}.x.flatten() }}')"
        )