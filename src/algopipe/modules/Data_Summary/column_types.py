import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()


def column_type_summary(df: pd.DataFrame):
    """Show numeric vs categorical columns."""

    numeric = df.select_dtypes(include="number").columns.tolist()
    categorical = df.select_dtypes(exclude="number").columns.tolist()

    table = Table(title="Column Types")
    table.add_column("Type")
    table.add_column("Count")
    table.add_column("Columns")

    table.add_row("Numeric", str(len(numeric)), ", ".join(numeric))
    table.add_row("Categorical", str(len(categorical)), ", ".join(categorical))

    console.print(table)

    return df
