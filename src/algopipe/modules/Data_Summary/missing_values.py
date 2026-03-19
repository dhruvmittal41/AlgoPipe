import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()


def missing_value_summary(df: pd.DataFrame):
    """Show missing values per column."""

    missing = df.isna().sum()
    total = len(df)

    table = Table(title="Missing Values Summary")
    table.add_column("Column")
    table.add_column("Missing Count")
    table.add_column("Missing %")

    for col, count in missing.items():
        if count > 0:
            pct = f"{(count / total) * 100:.2f}%"
            table.add_row(col, str(count), pct)

    if not any(missing):
        console.print("[green]No missing values found 🎉[/green]")
    else:
        console.print(table)

    return df
