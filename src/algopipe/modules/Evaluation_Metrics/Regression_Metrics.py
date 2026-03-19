# modules/Evaluation_Metrics/Regression_Metrics.py
from algopipe.registry import Registry, BaseModule

@Registry.register("Evaluation_Metrics", subcategory="Regression")
class MSEMetric(BaseModule):
    name = "Mean Squared Error Metric"
    
    def get_imports(self):
        return ["from sklearn.metrics import mean_squared_error"]
    
    def get_code(self):
        return "print(f'Mean Squared Error (MSE): {mean_squared_error(y_test, preds):.4f}')"

@Registry.register("Evaluation_Metrics", subcategory="Regression")
class RMSEMetric(BaseModule):
    name = "RMSE Metric"
    
    def get_imports(self):
        return [
            "from sklearn.metrics import mean_squared_error",
            "import numpy as np"
        ]
    
    def get_code(self):
        return "print(f'Root Mean Squared Error (RMSE): {np.sqrt(mean_squared_error(y_test, preds)):.4f}')"

@Registry.register("Evaluation_Metrics", subcategory="Regression")
class R2ScoreMetric(BaseModule):
    name = "R2 Score Metric"
    
    def get_imports(self):
        return ["from sklearn.metrics import r2_score"]
    
    def get_code(self):
        return "print(f'R2 Score: {r2_score(y_test, preds):.4f}')"