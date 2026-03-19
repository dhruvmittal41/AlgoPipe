# modules/Evaluation_Metrics/Classification_Metrics.py
from algopipe.registry import Registry, BaseModule

@Registry.register("Evaluation_Metrics", subcategory="Classification")
class AccuracyMetric(BaseModule):
    name = "Accuracy Metric"
    
    def get_imports(self):
        return ["from sklearn.metrics import accuracy_score"]
    
    def get_code(self):
        return "print(f'Accuracy: {accuracy_score(y_test, preds):.4f}')"

@Registry.register("Evaluation_Metrics", subcategory="Classification")
class F1ScoreMetric(BaseModule):
    name = "F1 Score Metric"
    
    def get_imports(self):
        return ["from sklearn.metrics import f1_score"]
    
    def get_code(self):
        return "print(f'F1 Score (Weighted): {f1_score(y_test, preds, average=\"weighted\"):.4f}')"

@Registry.register("Evaluation_Metrics", subcategory="Classification")
class PrecisionMetric(BaseModule):
    name = "Precision Metric"
    
    def get_imports(self):
        return ["from sklearn.metrics import precision_score"]
    
    def get_code(self):
        return "print(f'Precision (Weighted): {precision_score(y_test, preds, average=\"weighted\"):.4f}')"

@Registry.register("Evaluation_Metrics", subcategory="Classification")
class RecallMetric(BaseModule):
    name = "Recall Metric"
    
    def get_imports(self):
        return ["from sklearn.metrics import recall_score"]
    
    def get_code(self):
        return "print(f'Recall (Weighted): {recall_score(y_test, preds, average=\"weighted\"):.4f}')"