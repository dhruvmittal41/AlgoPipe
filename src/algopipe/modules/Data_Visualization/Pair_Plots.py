from algopipe.registry import Registry, BaseModule

@Registry.register("Data_Visualization", subcategory="Pairwise Analysis")
class PairPlotsModule(BaseModule):
    name = "Pair Plots & Joint Plots"
    description = "Visualizes pairwise relationships (PairGrid) and joint distributions between numeric variables."

    def get_imports(self):
        return [
            "import seaborn as sns",
            "import matplotlib.pyplot as plt",
            "import pandas as pd"
        ]

    def get_code(self, variable_name="df"):
        return (
            f"# --- Pairwise Analysis ---\n"
            f"print('Generating Pairwise Plots...')\n"
            f"# Identify columns\n"
            f"numeric_cols = {variable_name}.select_dtypes(include=['number']).columns.tolist()\n"
            f"categorical_cols = {variable_name}.select_dtypes(include=['object', 'category']).columns.tolist()\n\n"

            f"if len(numeric_cols) < 2:\n"
            f"    print('Skipping Pair Plots: Need at least 2 numeric columns.')\n"
            f"else:\n"
            f"    # 1. Pairplot (Scatter Matrix)\n"
            f"    # Use a categorical column for 'hue' (color) if available\n"
            f"    hue_col = categorical_cols[0] if categorical_cols else None\n"
            f"    print(f'Creating Pairplot (Color by: {{hue_col if hue_col else \"None\"}})...')\n"
            f"    \n"
            f"    try:\n"
            f"        sns.pairplot({variable_name}, vars=numeric_cols, hue=hue_col, corner=True, diag_kind='kde')\n"
            f"        plt.suptitle('Pairwise Relationships', y=1.02) # Adjust title position\n"
            f"        plt.show()\n"
            f"    except Exception as e:\n"
            f"        print(f'Error generating pairplot: {{e}}')\n\n"

            f"    # 2. Jointplot (Detailed view of first two numeric cols)\n"
            f"    x_col, y_col = numeric_cols[0], numeric_cols[1]\n"
            f"    print(f'Creating Jointplot for {{x_col}} vs {{y_col}}...')\n"
            f"    \n"
            f"    try:\n"
            f"        sns.jointplot(data={variable_name}, x=x_col, y=y_col, kind='reg', color='m')\n"
            f"        plt.show()\n"
            f"    except Exception as e:\n"
            f"        print(f'Error generating jointplot: {{e}}')"
        )