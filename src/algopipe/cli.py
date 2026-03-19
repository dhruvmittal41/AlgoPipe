# cli.py
import sys
import os
import questionary
from rich.console import Console
from rich.panel import Panel

# Ensure modules are imported so the Registry populates
import algopipe.modules 
from algopipe.registry import Registry
from algopipe.generator import PipelineGenerator

# Import our separated configs and UI
from algopipe.cli_config import UI_TO_REGISTRY_MAP
import algopipe.cli_wizard

console = Console()

# -----------------------------
# PIPELINE BUILDER HELPER
# -----------------------------
def find_and_add_module(generator, ui_selection):
    registry_name = UI_TO_REGISTRY_MAP.get(ui_selection, ui_selection)
    
    for category in Registry.get_categories():
        for sub in Registry.get_subcategories(category):
            modules = Registry.get_modules(category, sub)
            
            if modules and registry_name in modules:
                module_instance = Registry.get_module(category, sub, registry_name)
                generator.add_step(module_instance)
                console.print(f"[green]✔ Added {registry_name} to pipeline.[/green]")
                return True
                
    console.print(f"[yellow]⚠ Warning: Module '{registry_name}' not found in Registry. Did you create the file and import it in modules/__init__.py?[/yellow]")
    return False

# -----------------------------
# MAIN FLOW
# -----------------------------
def main():
    console.print(Panel.fit("🚀 AlgoPipe - ML Pipeline Builder", style="bold blue"))
    generator = PipelineGenerator()
    
    # 1. Run Wizard
    config = {}
    config["Problem Type"] = algopipe.cli_wizard.ask_problem_type()
    if not config["Problem Type"]:
        sys.exit()

    config["Dataset"] = algopipe.cli_wizard.ask_dataset_type()
    # config["Target"] = algopipe.cli_wizard.ask_target()
    config["Preprocessing"] = algopipe.cli_wizard.ask_preprocessing()
    config["Data Splitting"] = algopipe.cli_wizard.ask_data_splitting()
    config["Model"] = algopipe.cli_wizard.ask_model(config["Problem Type"])
    config["Metrics"] = algopipe.cli_wizard.ask_metrics(config["Problem Type"])
    # config["Extras"] = algopipe.cli_wizard.ask_extras()

    # 2. Show Summary
    if not algopipe.cli_wizard.show_summary(config):
        console.print("[red]Pipeline generation cancelled.[/red]")
        sys.exit()

    console.print("\n[bold cyan]Building Pipeline...[/bold cyan]")

    # 3. Assemble Pipeline
    try:
        if config["Dataset"]:
            find_and_add_module(generator, config["Dataset"])
            
        if config["Preprocessing"]:
            for step in config["Preprocessing"]:
                find_and_add_module(generator, step)

        if config["Data Splitting"]:
            find_and_add_module(generator, config["Data Splitting"])
                
        if config["Model"]:
            find_and_add_module(generator, config["Model"])
            
        if config["Metrics"]:
            for metric in config["Metrics"]:
                find_and_add_module(generator, metric)
                
    except Exception as e:
        console.print(f"[bold red]Error building pipeline:[/bold red] {e}")
        sys.exit(1)

   # 4. Generate Output
    output_format = algopipe.cli_wizard.ask_output_format()
    if not output_format:
        sys.exit()

    is_script = "Script" in output_format
    default_name = "pipeline.py" if is_script else "pipeline.ipynb"
    
    output_filename = questionary.text("Output filename:", default=default_name).ask()
    if not output_filename:
        output_filename = default_name

    try:
        if is_script:
            # Generate and format Python script
            code = generator.generate_code()
            try:
                import black
                code = black.format_str(code, mode=black.Mode())
            except ImportError:
                pass
            
            if not output_filename.endswith('.py'):
                output_filename = output_filename.rsplit('.', 1)[0] + '.py'
                
            with open(output_filename, "w") as f:
                f.write(code)
                
            console.print(Panel(f"✅ Python Script generated at:\n[bold]{os.path.abspath(output_filename)}[/bold]", style="green"))
            
        else:
            # Generate and save Jupyter Notebook
            notebook_data = generator.generate_notebook()
            
            if not output_filename.endswith('.ipynb'):
                output_filename = output_filename.rsplit('.', 1)[0] + '.ipynb'
                
            with open(output_filename, "w", encoding="utf-8") as f:
                import json
                json.dump(notebook_data, f, indent=1)
                
            console.print(Panel(f"✅ Jupyter Notebook generated at:\n[bold]{os.path.abspath(output_filename)}[/bold]", style="green"))
            
    except IOError as e:
        console.print(f"[bold red]Failed to write file:[/bold red] {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Exiting AlgoPipe Builder...[/red]")
        sys.exit(0)