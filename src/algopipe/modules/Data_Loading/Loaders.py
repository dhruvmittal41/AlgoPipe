# modules/Data_Loading/Loaders.py
from algopipe.registry import Registry, BaseModule

@Registry.register("Data_Loading", subcategory="File_Loaders")
class CSVLoader(BaseModule):
    name = "CSV Loader"
    description = "Load dataset from a CSV file using pandas."

    def get_imports(self):
        return ["import pandas as pd"]
    
    def get_code(self):
        return (
            f"# Load Data\n"
            f"dataset_path = 'dataset.csv'  # TODO: Replace with your actual path\n"
            f"df = pd.read_csv(dataset_path)\n"
            f"print(f'Dataset loaded successfully! Shape: {{df.shape}}')\n"
        )

@Registry.register("Data_Loading", subcategory="File_Loaders")
class ExcelLoader(BaseModule):
    name = "Excel Loader"
    description = "Load dataset from an Excel file using pandas."

    def get_imports(self):
        return ["import pandas as pd"]
    
    def get_code(self):
        return (
            f"# Load Data\n"
            f"dataset_path = 'dataset.xlsx'  # TODO: Replace with your actual path\n"
            f"df = pd.read_excel(dataset_path)\n"
            f"print(f'Dataset loaded successfully! Shape: {{df.shape}}')\n"
        )

@Registry.register("Data_Loading", subcategory="Custom_Loaders")
class CustomDataLoader(BaseModule):
    name = "Custom Data Loader"
    description = "Placeholder template for custom data loading logic."

    def get_imports(self):
        return ["import pandas as pd"]
    
    def get_code(self):
        return (
            f"# Custom Data Loader Template\n"
            f"# TODO: Implement your custom data fetching logic here (e.g., API, SQL Database)\n"
            f"df = pd.DataFrame()  # Replace with your actual dataframe\n"
        )