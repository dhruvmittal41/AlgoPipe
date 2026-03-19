from algopipe.registry import Registry, BaseModule

@Registry.register("Data_Visualization", subcategory="Univariate Analysis")
class UnivariateVizModule(BaseModule):
    name = "Univariate Analysis (All Columns)"
    description = "Generates detailed distribution plots (Hist, Box, Violin, Pie) for every column."

    def get_imports(self):
        return [
            "import seaborn as sns",
            "import matplotlib.pyplot as plt",
            "import pandas as pd"
        ]

    def get_code(self, variable_name="df"):
        return (
            f"# --- Univariate Analysis ---\n"
            f"print('Generating Univariate Plots...')\n"
            f"# Identify column types\n"
            f"numeric_cols = {variable_name}.select_dtypes(include=['number']).columns.tolist()\n"
            f"categorical_cols = {variable_name}.select_dtypes(include=['object', 'category']).columns.tolist()\n\n"
            
            f"# 1. Analyze Numeric Columns (Histogram, Box, Violin, KDE)\n"
            f"for col in numeric_cols:\n"
            f"    print(f'Plotting numeric: {{col}}')\n"
            f"    fig, axes = plt.subplots(2, 2, figsize=(14, 10))\n"
            f"    fig.suptitle(f'Univariate Analysis: {{col}}', fontsize=16, fontweight='bold')\n\n"
            
            f"    # Histogram\n"
            f"    sns.histplot(data={variable_name}, x=col, kde=True, ax=axes[0, 0], color='skyblue')\n"
            f"    axes[0, 0].set_title('Histogram & KDE')\n\n"
            
            f"    # Box Plot\n"
            f"    sns.boxplot(data={variable_name}, x=col, ax=axes[0, 1], color='lightcoral')\n"
            f"    axes[0, 1].set_title('Box Plot')\n\n"
            
            f"    # Violin Plot\n"
            f"    sns.violinplot(data={variable_name}, x=col, ax=axes[1, 0], color='lightgreen')\n"
            f"    axes[1, 0].set_title('Violin Plot')\n\n"
            
            f"    # KDE Plot (Pure density)\n"
            f"    sns.kdeplot(data={variable_name}, x=col, fill=True, ax=axes[1, 1], color='orange')\n"
            f"    axes[1, 1].set_title('Density Distribution')\n\n"
            
            f"    plt.tight_layout(rect=[0, 0.03, 1, 0.95])\n"
            f"    plt.show()\n\n"

            f"# 2. Analyze Categorical Columns (Bar, Count, Pie)\n"
            f"for col in categorical_cols:\n"
            f"    print(f'Plotting categorical: {{col}}')\n"
            f"    fig, axes = plt.subplots(1, 3, figsize=(18, 5))\n"
            f"    fig.suptitle(f'Univariate Analysis: {{col}}', fontsize=16, fontweight='bold')\n\n"
            
            f"    # Bar Plot\n"
            f"    sns.barplot(x={variable_name}[col].value_counts().values, \n"
            f"                y={variable_name}[col].value_counts().index, \n"
            f"                palette='mako', ax=axes[0])\n"
            f"    axes[0].set_title('Frequency Bar Chart')\n\n"
            
            f"    # Count Plot\n"
            f"    sns.countplot(y={variable_name}[col], order={variable_name}[col].value_counts().index, \n"
            f"                  palette='viridis', ax=axes[1])\n"
            f"    axes[1].set_title('Count Plot')\n\n"
            
            f"    # Pie Chart\n"
            f"    try:\n"
            f"        counts = {variable_name}[col].value_counts()\n"
            f"        axes[2].pie(counts.values, labels=counts.index, autopct='%1.1f%%', \n"
            f"                    startangle=140, colors=sns.color_palette('pastel'))\n"
            f"        axes[2].set_title('Distribution Pie Chart')\n"
            f"    except Exception as e:\n"
            f"        # If too many categories, Pie Chart looks bad or fails\n"
            f"        axes[2].text(0.5, 0.5, 'Too many categories for Pie Chart', ha='center')\n\n"
            
            f"    plt.tight_layout(rect=[0, 0.03, 1, 0.95])\n"
            f"    plt.show()"
        )