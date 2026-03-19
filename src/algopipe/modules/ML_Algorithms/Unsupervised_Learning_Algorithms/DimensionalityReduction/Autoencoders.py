from algopipe.registry import Registry, BaseModule

@Registry.register("ML_Algorithms",subcategory="Dimensionality_Reduction_Algorithms")
class Autoencoders(BaseModule):
    name = "Autoencoders"
    description = "Dimensionality Reduction using Autoencoders with Keras"

    def get_imports(self):
        return [
            "from keras.layers import Input, Dense",
            "from keras.models import Model",
            "from sklearn.metrics import mean_squared_error"
        ]
    
    def get_code(self, variable_name="autoencoder"):
        return (
            f"# Define Autoencoder Architecture\n"
            f"input_dim = X.shape[1]\n"
            f"encoding_dim = 2  # Dimension to reduce to\n\n"
            f"input_layer = Input(shape=(input_dim,))\n"
            f"encoded = Dense(encoding_dim, activation='relu')(input_layer)\n"
            f"decoded = Dense(input_dim, activation='sigmoid')(encoded)\n\n"
            f"{variable_name} = Model(input_layer, decoded)\n"
            f"{variable_name}.compile(optimizer='adam', loss='mse')\n\n"
            f"# Train Autoencoder\n"
            f"{variable_name}.fit(X, X, epochs=50, batch_size=256, shuffle=True)\n\n"
            f"# Get Encoded Representations\n"
            f"encoder = Model(input_layer, encoded)\n"
            f"encoded_X = encoder.predict(X)\n\n"
            f"# Evaluate Reconstruction Error\n"
            f"reconstructed_X = {variable_name}.predict(X)\n"
            f"print(f'Mean Squared Reconstruction Error: {{mean_squared_error(X, reconstructed_X)}}')"
        )