import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()


def dataset_overview(df: pd.DataFrame):
    """Show dataset shape and column list."""

    table = Table(title="Dataset Overview")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Rows", str(df.shape[0]))
    table.add_row("Columns", str(df.shape[1]))

    console.print(table)

    console.print("\n[bold]Columns:[/bold]")
    for col in df.columns:
        console.print(f" • {col}")

    return df
