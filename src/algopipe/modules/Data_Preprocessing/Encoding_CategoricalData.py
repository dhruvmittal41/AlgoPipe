
from algopipe.registry import BaseModule, Registry



@Registry.register("Data_Preprocessing", subcategory="Categorical Encoding")
class OneHotEncodingModule(BaseModule):
    name = "One-Hot Encoding (Dummy Variables)"
    description = "Converts categorical variables into dummy/indicator variables."

    def get_imports(self):
        return ["import pandas as pd"]

    def get_code(self, variable_name="df"):
        return (
            f"# One-Hot Encoding\n"
            f"cat_cols = {variable_name}.select_dtypes(include=['object', 'category']).columns\n"
            f"{variable_name} = pd.get_dummies({variable_name}, columns=cat_cols, drop_first=True)\n"
            f"print(f'Applied One-Hot Encoding. New shape: {{{variable_name}.shape}}')"
        )
    

@Registry.register("Data_Preprocessing", subcategory="Categorical Encoding")
class OrdinalEncodingModule(BaseModule):
    name = "Ordinal Encoding"
    description = "Encodes categorical features as an integer array."

    def get_imports(self):
        return ["from sklearn.preprocessing import OrdinalEncoder"]

    def get_code(self, variable_name="df"):
        return (
            f"# Ordinal Encoding\n"
            f"encoder = OrdinalEncoder()\n"
            f"cat_cols = {variable_name}.select_dtypes(include=['object', 'category']).columns\n"
            f"if len(cat_cols) > 0:\n"
            f"    {variable_name}[cat_cols] = encoder.fit_transform({variable_name}[cat_cols].astype(str))\n"
            f"print('Applied Ordinal Encoding.')"
        )
    

@Registry.register("Data_Preprocessing", subcategory="Categorical Encoding")
class FrequencyEncodingModule(BaseModule):
    name = "Frequency Encoding"
    description = "Replaces categories with their frequency of occurrence."

    def get_imports(self):
        return []

    def get_code(self, variable_name="df"):
        return (
            f"# Frequency Encoding\n"
            f"cat_cols = {variable_name}.select_dtypes(include=['object', 'category']).columns\n"
            f"for col in cat_cols:\n"
            f"    freq_encoding = {variable_name}[col].value_counts(normalize=True)\n"
            f"    {variable_name}[col] = {variable_name}[col].map(freq_encoding)\n"
            f"print('Applied Frequency Encoding.')"
        )
    

@Registry.register("Data_Preprocessing", subcategory="Categorical Encoding")
class TargetEncodingModule(BaseModule):
    name = "Target Encoding"
    description = "Encodes categorical features using the mean of the target variable."

    def get_imports(self):
        return ["from sklearn.preprocessing import TargetEncoder"]

    def get_code(self, variable_name="df"):
        return (
            f"# Target Encoding\n"
            f"# WARNING: You must specify your target column name below.\n"
            f"target_col = 'TARGET_COLUMN_NAME' # <-- Update this!\n"
            f"if target_col in {variable_name}.columns:\n"
            f"    encoder = TargetEncoder(smooth='auto')\n"
            f"    cat_cols = {variable_name}.select_dtypes(include=['object', 'category']).columns\n"
            f"    cat_cols = cat_cols.drop(target_col, errors='ignore')\n"
            f"    if len(cat_cols) > 0:\n"
            f"        {variable_name}[cat_cols] = encoder.fit_transform({variable_name}[cat_cols], {variable_name}[target_col])\n"
            f"        print('Applied Target Encoding.')\n"
            f"else:\n"
            f"    print(f'Target column {{target_col}} not found. Skipping Target Encoding.')"
        )