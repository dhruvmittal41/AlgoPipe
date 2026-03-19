import sys
import os
import questionary
from rich.console import Console
from rich.panel import Panel
import algopipe.modules 
from algopipe.registry import Registry
from algopipe.generator import PipelineGenerator

console = Console()

def main():
    console.print(Panel.fit("AI Tool - Interactive Pipeline Builder", style="bold blue"))
    
    generator = PipelineGenerator()
    
    while True:
        
        categories = Registry.get_categories()
        category = questionary.select(
            "What would you like to add next?",
            choices=categories + ["Done (Generate Code)", "Exit"]
        ).ask()

        if category == "Exit":
            sys.exit()
        if category == "Done (Generate Code)":
            break

        
        subcategories = Registry.get_subcategories(category)
        
        
        if len(subcategories) == 1:
            subcategory = subcategories[0]
        else:
            subcategory = questionary.select(
                f"Select a type of {category}:",
                choices=subcategories
            ).ask()

        
        modules = Registry.get_modules(category, subcategory)
        if not modules:
            console.print(f"[yellow]No modules found.[/yellow]")
            continue

        module_name = questionary.select(
            f"Choose algorithm:",
            choices=modules
        ).ask()

        
        module_instance = Registry.get_module(category, subcategory, module_name)
        generator.add_step(module_instance)
        console.print(f"[green]Added {module_name} to pipeline.[/green]")

    
    output_filename = questionary.text("Output filename:", default="pipeline.py").ask()
    
    code = generator.generate_code()
    
    
    try:
        import black
        code = black.format_str(code, mode=black.Mode())
    except ImportError:
        pass

    with open(output_filename, "w") as f:
        f.write(code)

    console.print(Panel(f"Successfully generated pipeline at [bold]{os.path.abspath(output_filename)}[/bold]", style="green"))

if __name__ == "__main__":
    main()