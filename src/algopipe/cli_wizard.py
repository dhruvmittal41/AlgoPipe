# cli_wizard.py
import questionary
from rich.console import Console
from rich.table import Table
import algopipe.cli_config

console = Console()

def ask_problem_type():
    console.print("\n[bold cyan]Step 1/7: Problem Definition[/bold cyan]")
    return questionary.select(
        "What type of problem are you solving?",
        choices=algopipe.cli_config.PROBLEM_TYPES
    ).ask()

def ask_dataset_type():
    console.print("\n[bold cyan]Step 2/7: Dataset Loader[/bold cyan]")
    return questionary.select(
        "What type of dataset are you using?",
        choices=algopipe.cli_config.DATASET_TYPES
    ).ask()

def ask_target():
    console.print("\n[bold cyan]Step 3/7: Target Variable[/bold cyan]")
    return questionary.text(
        "Enter target column name:",
        default="target"
    ).ask()

def ask_preprocessing():
    console.print("\n[bold cyan]Step 4/7: Preprocessing[/bold cyan]")
    categories = questionary.checkbox(
        "Which preprocessing categories would you like to configure?",
        choices=algopipe.cli_config.PREPROCESSING_STEPS.keys()
    ).ask()

    final_selections = []
    for category in categories:
        options = algopipe.cli_config.PREPROCESSING_STEPS.get(category, [])
        
        if options:
            selected_sub_options = questionary.checkbox(
                [f"Select methods for {category}:"],
                choices=options
            ).ask()
            final_selections.extend(selected_sub_options)

    return final_selections

def ask_data_splitting():
    console.print("\n[bold cyan]Step 5/7: Data Splitting[/bold cyan]")
    return questionary.select(
        "How would you like to split your data?",
        choices=algopipe.cli_config.DATA_SPLITTING_OPTIONS
    ).ask()

def ask_model(problem_type):
    console.print("\n[bold cyan]Step 6/7: Model Selection[/bold cyan]")
    choices = algopipe.cli_config.MODELS.get(problem_type, [])
    
    if not choices:
        return None

    selected = questionary.select(
        "Choose model:",
        choices=choices
    ).ask()
    
    if not selected:
        return None
        
    # Strip the recommended star to match mapping keys
    return selected.split(" ⭐")[0].strip()

def ask_metrics(problem_type):
    console.print("\n[bold cyan]Step 7/7: Evaluation Metrics[/bold cyan]")
    choices = algopipe.cli_config.METRICS.get(problem_type, [])
    
    if not choices:
        return []
    
    return questionary.checkbox(
        "Select evaluation metrics:",
        choices=choices
    ).ask()

def ask_extras():
    console.print("\n[bold cyan]Optional Features[/bold cyan]")
    return questionary.checkbox(
        "Add advanced features:",
        choices=algopipe.cli_config.EXTRAS
    ).ask()

def show_summary(config):
    table = Table(title="📦 Pipeline Summary")
    table.add_column("Component", style="cyan")
    table.add_column("Selection", style="green")
    
    for key, value in config.items():
        if value is None or (isinstance(value, list) and not value):
            display_val = "None"
        elif isinstance(value, list):
            display_val = ", ".join(value)
        else:
            display_val = str(value)
            
        table.add_row(key, display_val)
        
    console.print(table)
    return questionary.confirm("Proceed with code generation?").ask()

def ask_output_format():
    console.print("\n[bold cyan]Output Format[/bold cyan]")
    return questionary.select(
        "How would you like to export your pipeline?",
        choices=["Python Script (.py)", "Jupyter Notebook (.ipynb)"]
    ).ask()