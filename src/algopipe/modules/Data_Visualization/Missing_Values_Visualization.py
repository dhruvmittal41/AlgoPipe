from algopipe.registry import Registry, BaseModule

@Registry.register("Data_Visualization", subcategory="Missing Values")
class MissingValuesVizModule(BaseModule):
    name = "Missing Values Dashboard"
    description = "Generates a 4-panel dashboard (Matrix, Bar, Heatmap, Dendrogram) using missingno."

    def get_imports(self):
        return [
            "import missingno as msno",
            "import matplotlib.pyplot as plt",
            "import pandas as pd"
        ]

    def get_code(self, variable_name="df"):
        return (
            f"# --- Missing Values Visualization ---\n"
            f"print('Generating Missing Values Dashboard...')\n"
            f"# Check if there are missing values to visualize\n"
            f"if {variable_name}.isnull().sum().sum() == 0:\n"
            f"    print('Great news! No missing values found in the dataset.')\n"
            f"else:\n"
            f"    # Create a 2x2 grid for the dashboard\n"
            f"    fig, axes = plt.subplots(2, 2, figsize=(16, 12))\n"
            f"    \n"
            f"    # 1. Matrix Plot (Top-Left)\n"
            f"    msno.matrix({variable_name}, ax=axes[0, 0], fontsize=10)\n"
            f"    axes[0, 0].set_title('Missing Values Matrix', fontsize=12)\n"
            f"    \n"
            f"    # 2. Bar Plot (Top-Right)\n"
            f"    msno.bar({variable_name}, ax=axes[0, 1], fontsize=10)\n"
            f"    axes[0, 1].set_title('Missing Values Bar Chart', fontsize=12)\n"
            f"    \n"
            f"    # 3. Heatmap (Bottom-Left) - Only works if there are correlations\n"
            f"    try:\n"
            f"        msno.heatmap({variable_name}, ax=axes[1, 0], fontsize=10)\n"
            f"        axes[1, 0].set_title('Nullity Correlation Heatmap', fontsize=12)\n"
            f"    except ValueError:\n"
            f"        # Heatmap fails if less than 2 columns have missing values\n"
            f"        axes[1, 0].text(0.5, 0.5, 'Not enough missing data for Heatmap', \n"
            f"                        ha='center', va='center')\n"
            f"    \n"
            f"    # 4. Dendrogram (Bottom-Right)\n"
            f"    try:\n"
            f"        msno.dendrogram({variable_name}, ax=axes[1, 1], fontsize=10)\n"
            f"        axes[1, 1].set_title('Nullity Dendrogram', fontsize=12)\n"
            f"    except ValueError:\n"
            f"        axes[1, 1].text(0.5, 0.5, 'Not enough missing data for Dendrogram', \n"
            f"                        ha='center', va='center')\n"
            f"    \n"
            f"    plt.tight_layout()\n"
            f"    plt.show()"
        )