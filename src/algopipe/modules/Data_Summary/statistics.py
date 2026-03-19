import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()


def numeric_statistics(df: pd.DataFrame):
    """Show basic statistics for numeric columns."""

    desc = df.describe().T

    table = Table(title="Numeric Statistics")

    table.add_column("Column")
    for stat in desc.columns:
        table.add_column(stat)

    for col, row in desc.iterrows():
        table.add_row(col, *[f"{v:.2f}" for v in row])

    console.print(table)

    return df
