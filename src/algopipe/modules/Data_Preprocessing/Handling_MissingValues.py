from algopipe.registry import Registry, BaseModule

# --- DROP MISSING ---
@Registry.register("Data_Preprocessing", subcategory="Handling Missing Values")
class DropMissingModule(BaseModule):
    name = "Drop Missing Values"
    description = "Drops rows containing missing values."

    def get_imports(self):
        return ["import numpy as np"]

    def get_code(self, variable_name="df"):
        return (
            f"# Drop Missing Values\n"
            f"# Standardize missing values first\n"
            f"{variable_name} = {variable_name}.replace(['NaN', 'nan', 'N/A', 'n/a', ''], np.nan)\n"
            f"{variable_name} = {variable_name}.dropna()\n"
            f"print('Dropped rows with missing values.')"
        )

# --- MEAN IMPUTATION ---
@Registry.register("Data_Preprocessing", subcategory="Handling Missing Values")
class MeanImputationModule(BaseModule):
    name = "Mean Imputation"
    description = "Fills missing values with the column mean."

    def get_imports(self):
        return ["from sklearn.impute import SimpleImputer"]

    def get_code(self, variable_name="df"):
        return (
            f"# Mean Imputation\n"
            f"imputer = SimpleImputer(strategy='mean')\n"
            f"# Select only numeric columns for mean imputation\n"
            f"numeric_cols = {variable_name}.select_dtypes(include=['number']).columns\n"
            f"{variable_name}[numeric_cols] = imputer.fit_transform({variable_name}[numeric_cols])"
        )

# --- MEDIAN IMPUTATION ---
@Registry.register("Data_Preprocessing")
class MedianImputationModule(BaseModule):
    name = "Median Imputation"
    description = "Fills missing values with the column median."

    def get_imports(self):
        return ["from sklearn.impute import SimpleImputer"]

    def get_code(self, variable_name="df"):
        return (
            f"# Median Imputation\n"
            f"imputer = SimpleImputer(strategy='median')\n"
            f"numeric_cols = {variable_name}.select_dtypes(include=['number']).columns\n"
            f"{variable_name}[numeric_cols] = imputer.fit_transform({variable_name}[numeric_cols])"
        )

# --- MODE IMPUTATION ---
@Registry.register("Data_Preprocessing", subcategory="Handling Missing Values")
class ModeImputationModule(BaseModule):
    name = "Mode Imputation (Frequent)"
    description = "Fills missing values with the most frequent value (good for categorical)."

    def get_imports(self):
        return ["from sklearn.impute import SimpleImputer"]

    def get_code(self, variable_name="df"):
        return (
            f"# Mode Imputation\n"
            f"imputer = SimpleImputer(strategy='most_frequent')\n"
            f"{variable_name}[:] = imputer.fit_transform({variable_name})"
        )

# --- KNN IMPUTATION ---
@Registry.register("Data_Preprocessing", subcategory="Handling Missing Values")
class KNNImputationModule(BaseModule):
    name = "KNN Imputation"
    description = "Fills missing values using K-Nearest Neighbors."

    def get_imports(self):
        return ["from sklearn.impute import KNNImputer"]

    def get_code(self, variable_name="df"):
        return (
            f"# KNN Imputation\n"
            f"imputer = KNNImputer(n_neighbors=3)\n"
            f"# Note: KNN only works on numeric data\n"
            f"numeric_cols = {variable_name}.select_dtypes(include=['number']).columns\n"
            f"{variable_name}[numeric_cols] = imputer.fit_transform({variable_name}[numeric_cols])"
        )

# --- CONSTANT IMPUTATION (Numeric) ---
@Registry.register("Data_Preprocessing")
class ConstantNumericImputeModule(BaseModule):
    name = "Constant Value Impute (0)"
    description = "Fills missing numerical values with 0."

    def get_imports(self):
        return []

    def get_code(self, variable_name="df"):
        return (
            f"# Constant Imputation (Numeric)\n"
            f"numeric_cols = {variable_name}.select_dtypes(include=['number']).columns\n"
            f"{variable_name}[numeric_cols] = {variable_name}[numeric_cols].fillna(0)"
        )

# --- FORWARD FILL ---
@Registry.register("Data_Preprocessing", subcategory="Handling Missing Values")
class ForwardFillModule(BaseModule):
    name = "Forward Fill"
    description = "Propagates last valid observation forward (Time Series)."

    def get_imports(self):
        return []

    def get_code(self, variable_name="df"):
        return (
            f"# Forward Fill\n"
            f"{variable_name} = {variable_name}.ffill()"
        )

# --- ITERATIVE IMPUTATION ---
@Registry.register("Data_Preprocessing", subcategory="Handling Missing Values")
class IterativeImputationModule(BaseModule):
    name = "Iterative Imputer (Random Forest)"
    description = "Multivariate imputation by chaining Random Forests."

    def get_imports(self):
        return [
            "from sklearn.experimental import enable_iterative_imputer",
            "from sklearn.impute import IterativeImputer",
            "from sklearn.ensemble import RandomForestRegressor"
        ]

    def get_code(self, variable_name="df"):
        return (
            f"# Iterative Imputation\n"
            f"imputer = IterativeImputer(estimator=RandomForestRegressor(), max_iter=10, random_state=0)\n"
            f"numeric_cols = {variable_name}.select_dtypes(include=['number']).columns\n"
            f"{variable_name}[numeric_cols] = imputer.fit_transform({variable_name}[numeric_cols])"
        )