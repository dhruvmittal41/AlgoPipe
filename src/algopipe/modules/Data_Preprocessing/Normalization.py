from algopipe.registry import BaseModule, Registry

@Registry.register("Data_Preprocessing", subcategory="Feature Scaling")
class StandardScalerModule(BaseModule):
    name = "Standard Scaler"
    description = "Standardize features by removing the mean and scaling to unit variance."

    def get_imports(self):
        return ["from sklearn.preprocessing import StandardScaler"]

    def get_code(self, variable_name="df"):
        return (
            f"# Standard Scaling (Z-score)\n"
            f"scaler = StandardScaler()\n"
            f"num_cols = {variable_name}.select_dtypes(include=['number']).columns\n"
            f"{variable_name}[num_cols] = scaler.fit_transform({variable_name}[num_cols])"
        )
    
@Registry.register("Data_Preprocessing", subcategory="Feature Scaling")
class MinMaxScalerModule(BaseModule):
    name = "Min-Max Scaler"
    description = "Transforms features by scaling each feature to a given range (0 to 1)."

    def get_imports(self):
        return ["from sklearn.preprocessing import MinMaxScaler"]

    def get_code(self, variable_name="df"):
        return (
            f"# Min-Max Scaling\n"
            f"scaler = MinMaxScaler()\n"
            f"num_cols = {variable_name}.select_dtypes(include=['number']).columns\n"
            f"{variable_name}[num_cols] = scaler.fit_transform({variable_name}[num_cols])"
        )
    
@Registry.register("Data_Preprocessing", subcategory="Feature Scaling")
class RobustScalerModule(BaseModule):
    name = "Robust Scaler"
    description = "Scales features using statistics that are robust to outliers."

    def get_imports(self):
        return ["from sklearn.preprocessing import RobustScaler"]

    def get_code(self, variable_name="df"):
        return (
            f"# Robust Scaling (Outlier Resistant)\n"
            f"scaler = RobustScaler()\n"
            f"num_cols = {variable_name}.select_dtypes(include=['number']).columns\n"
            f"{variable_name}[num_cols] = scaler.fit_transform({variable_name}[num_cols])"
        )
    
@Registry.register("Data_Preprocessing", subcategory="Feature Transformation")
class LogTransformModule(BaseModule):
    name = "Log Transformation"
    description = "Applies log(1+x) transformation to handle right-skewed data."

    def get_imports(self):
        return ["import numpy as np"]

    def get_code(self, variable_name="df"):
        return (
            f"# Log Transformation\n"
            f"num_cols = {variable_name}.select_dtypes(include=['number']).columns\n"
            f"# Applying log1p to handle zeros safely\n"
            f"{variable_name}[num_cols] = {variable_name}[num_cols].apply(np.log1p)"
        )
    
@Registry.register("Data_Preprocessing", subcategory="Feature Transformation")
class PowerTransformModule(BaseModule):
    name = "Power Transformer (Yeo-Johnson)"
    description = "Optimal for making data more Gaussian-like."

    def get_imports(self):
        return ["from sklearn.preprocessing import PowerTransformer"]

    def get_code(self, variable_name="df"):
        return (
            f"# Yeo-Johnson Transformation\n"
            f"pt = PowerTransformer(method='yeo-johnson')\n"
            f"num_cols = {variable_name}.select_dtypes(include=['number']).columns\n"
            f"{variable_name}[num_cols] = pt.fit_transform({variable_name}[num_cols])"
        )
    

@Registry.register("Data_Preprocessing", subcategory="Normalization")
class NormalizerModule(BaseModule):
    name = "Normalizer (L2)"
    description = "Scales individual samples to have unit norm (row-wise)."

    def get_imports(self):
        return ["from sklearn.preprocessing import Normalizer"]

    def get_code(self, variable_name="df"):
        return (
            f"# L2 Normalization (Row-wise)\n"
            f"normalizer = Normalizer(norm='l2')\n"
            f"num_cols = {variable_name}.select_dtypes(include=['number']).columns\n"
            f"{variable_name}[num_cols] = normalizer.fit_transform({variable_name}[num_cols])"
        )