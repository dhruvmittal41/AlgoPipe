from algopipe.registry import Registry, BaseModule

@Registry.register("Data_Visualization", subcategory="Bivariate Analysis")
class BivariateAnalysisModule(BaseModule):
    name = "Comprehensive Bivariate Analysis"
    description = "Generates Scatter, Box, Violin, KDE, and Heatmaps for all feature pairs."

    def get_imports(self):
        return [
            "import seaborn as sns",
            "import matplotlib.pyplot as plt",
            "import pandas as pd"
        ]

    def get_code(self, variable_name="df"):
    
    
        return (
            f"# --- Bivariate Analysis ---\n"
            f"# Identify column types dynamically\n"
            f"numeric_cols = {variable_name}.select_dtypes(include=['number']).columns.tolist()\n"
            f"categorical_cols = {variable_name}.select_dtypes(include=['object', 'category']).columns.tolist()\n\n"
            
            f"print(f'Analyzing {{len(numeric_cols)}} numeric and {{len(categorical_cols)}} categorical columns...')\n\n"

            f"# 1. Correlation Heatmap\n"
            f"if len(numeric_cols) >= 2:\n"
            f"    plt.figure(figsize=(10, 8))\n"
            f"    sns.heatmap({variable_name}[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')\n"
            f"    plt.title('Correlation Heatmap')\n"
            f"    plt.show()\n\n"

            f"# 2. Scatter Plots (Numeric vs Numeric)\n"
            f"# Using Pairplot for efficiency instead of manual loops\n"
            f"if len(numeric_cols) >= 2:\n"
            f"    print('Generating Pairplot (Scatter matrix)...')\n"
            f"    sns.pairplot({variable_name}[numeric_cols], diag_kind='kde')\n"
            f"    plt.show()\n\n"

            f"# 3. Box & Violin Plots (Categorical vs Numeric)\n"
            f"for cat in categorical_cols:\n"
            f"    for num in numeric_cols:\n"
            f"        fig, axes = plt.subplots(1, 2, figsize=(14, 6))\n"
            f"        \n"
            f"        # Box Plot\n"
            f"        sns.boxplot(x={variable_name}[cat], y={variable_name}[num], ax=axes[0])\n"
            f"        axes[0].set_title(f'Box Plot: {{num}} by {{cat}}')\n"
            f"        \n"
            f"        # Violin Plot\n"
            f"        sns.violinplot(x={variable_name}[cat], y={variable_name}[num], ax=axes[1])\n"
            f"        axes[1].set_title(f'Violin Plot: {{num}} by {{cat}}')\n"
            f"        \n"
            f"        plt.tight_layout()\n"
            f"        plt.show()\n\n"

            f"# 4. 2D KDE Plots (First 2 numeric cols only to avoid clutter)\n"
            f"if len(numeric_cols) >= 2:\n"
            f"    x_col, y_col = numeric_cols[0], numeric_cols[1]\n"
            f"    plt.figure(figsize=(8, 6))\n"
            f"    sns.kdeplot(x={variable_name}[x_col], y={variable_name}[y_col], fill=True, cmap='mako')\n"
            f"    plt.title(f'2D KDE: {{x_col}} vs {{y_col}}')\n"
            f"    plt.show()"
        )