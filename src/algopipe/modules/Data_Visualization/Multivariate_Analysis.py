from algopipe.registry import Registry, BaseModule

@Registry.register("Data_Visualization", subcategory="Multivariate Analysis")
class MultivariateVizModule(BaseModule):
    name = "Multivariate Dashboard"
    description = "Generates advanced high-dimensional plots (3D Scatter, Parallel Coordinates, Andrews Curves, Radviz)."

    def get_imports(self):
        return [
            "import matplotlib.pyplot as plt",
            "from mpl_toolkits.mplot3d import Axes3D",
            "import pandas as pd",
            "from pandas.plotting import parallel_coordinates, andrews_curves, radviz"
        ]

    def get_code(self, variable_name="df"):
        return (
            f"# --- Multivariate Analysis ---\n"
            f"print('Generating Multivariate Dashboard...')\n"
            f"# Identify column types\n"
            f"numeric_cols = {variable_name}.select_dtypes(include=['number']).columns.tolist()\n"
            f"categorical_cols = {variable_name}.select_dtypes(include=['object', 'category']).columns.tolist()\n\n"

            f"# Check requirements: Need at least 3 numeric cols and 1 categorical col for most plots\n"
            f"if len(numeric_cols) < 3:\n"
            f"    print('Skipping Multivariate Analysis: Need at least 3 numeric columns.')\n"
            f"elif len(categorical_cols) == 0:\n"
            f"    print('Skipping Classification Plots: Need at least 1 categorical column for color coding.')\n"
            f"    # Fallback: Just show 3D Scatter if we have numbers but no categories\n"
            f"    fig = plt.figure(figsize=(10, 8))\n"
            f"    ax = fig.add_subplot(111, projection='3d')\n"
            f"    ax.scatter({variable_name}[numeric_cols[0]], {variable_name}[numeric_cols[1]], {variable_name}[numeric_cols[2]], c='skyblue', s=60)\n"
            f"    ax.set_xlabel(numeric_cols[0])\n"
            f"    ax.set_ylabel(numeric_cols[1])\n"
            f"    ax.set_zlabel(numeric_cols[2])\n"
            f"    plt.title('3D Scatter Plot (No Category)')\n"
            f"    plt.show()\n"
            f"else:\n"
            f"    # We have enough data for a full dashboard\n"
            f"    class_col = categorical_cols[0]\n"
            f"    subset_cols = numeric_cols[:5] + [class_col] # Limit to 5 numeric vars to avoid clutter\n"
            f"    subset_df = {variable_name}[subset_cols].dropna()\n\n"
            
            f"    # Create a 2x2 Layout\n"
            f"    fig = plt.figure(figsize=(16, 12))\n\n"

            f"    # 1. 3D Scatter Plot (Top-Left)\n"
            f"    ax1 = fig.add_subplot(2, 2, 1, projection='3d')\n"
            f"    # Simple coloring mapping for 3D plot\n"
            f"    colors = pd.factorize(subset_df[class_col])[0]\n"
            f"    ax1.scatter(subset_df[numeric_cols[0]], subset_df[numeric_cols[1]], subset_df[numeric_cols[2]], c=colors, cmap='viridis', s=40)\n"
            f"    ax1.set_xlabel(numeric_cols[0])\n"
            f"    ax1.set_ylabel(numeric_cols[1])\n"
            f"    ax1.set_zlabel(numeric_cols[2])\n"
            f"    ax1.set_title(f'3D Scatter by {{class_col}}')\n\n"

            f"    # 2. Parallel Coordinates (Top-Right)\n"
            f"    ax2 = fig.add_subplot(2, 2, 2)\n"
            f"    try:\n"
            f"        parallel_coordinates(subset_df, class_column=class_col, ax=ax2, color=('#556270', '#4ECDC4', '#C7F464'))\n"
            f"        ax2.set_title('Parallel Coordinates')\n"
            f"        # Rotate x labels if they overlap\n"
            f"        plt.setp(ax2.get_xticklabels(), rotation=45)\n"
            f"    except Exception as e: ax2.text(0.5, 0.5, 'Error plotting Parallel Coords', ha='center')\n\n"

            f"    # 3. Andrews Curves (Bottom-Left)\n"
            f"    ax3 = fig.add_subplot(2, 2, 3)\n"
            f"    try:\n"
            f"        andrews_curves(subset_df, class_column=class_col, ax=ax3, color=('#556270', '#4ECDC4', '#C7F464'))\n"
            f"        ax3.set_title('Andrews Curves')\n"
            f"    except Exception as e: ax3.text(0.5, 0.5, 'Error plotting Andrews Curves', ha='center')\n\n"

            f"    # 4. Radviz (Bottom-Right)\n"
            f"    ax4 = fig.add_subplot(2, 2, 4)\n"
            f"    try:\n"
            f"        radviz(subset_df, class_column=class_col, ax=ax4, color=('#556270', '#4ECDC4', '#C7F464'))\n"
            f"        ax4.set_title('Radviz')\n"
            f"    except Exception as e: ax4.text(0.5, 0.5, 'Error plotting Radviz', ha='center')\n\n"

            f"    plt.tight_layout()\n"
            f"    plt.show()"
        )