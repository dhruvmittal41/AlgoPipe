

PROBLEM_TYPES = ["Classification", "Regression", "Clustering","Dimensionality Reduction"]

DATASET_TYPES = ["CSV", "Excel", "Custom Loader"]
DATA_SPLITTING_OPTIONS = [
    "Train-Test Split"
]

PREPROCESSING_STEPS = {
    "Handle Missing Values": [
        "Mean Imputation",
        "Drop Missing Values",
        "Median Imputation",
        "Mode Imputation (Frequent)",
        "KNN Imputation",
        "Constant Value Imputation",
        "Forward Fill",
        "Iterative Imputer (Random Forest)",
        ],
    "Feature Scaling": [
        "Standard Scaler",
        "Min-Max Scaler",
        "Robust Scaler",
        "Log Transformation",
        "Power Transformer (Yeo-Johnson)",
        "Normalization (L2)"  
        ],
    "Encode Categorical Variables": [
        "One-Hot Encoding (Dummy Variables)",
        "Ordinal Encoding",
        "Frequency Encoding",
        "Target Encoding"
    ],
}

MODELS = {
    "Classification": [
        "Random Forest",
        "Logistic Regression",
        "SVM",
        "KNN",
        "Decision Tree Classifier",
        "Gradient Boosting Machines",
        "AdaBoost",
        "catboost",
        "LightGBM",
        "LDA",
        "Naive Bayes",
        "QDA",
        "XGBoost"
    ],
    "Regression": [
        "Random Forest Regressor",
        "Linear Regression",
        "SVR",
        "Ridge Regression",
        "Lasso Regression"
    ],
    "Clustering": [
        "K-Means",
        "DBSCAN",
        "Hierarchical Clustering",
        "Affinity Propagation",
        "Gaussian Mixture Models",
        "Mean Shift",
        "Spectral Clustering",

    ],
    "Dimensionality Reduction": [
        "PCA",
        "t-SNE",
        "UMAP",
        "LDA",
        "Autoencoder",
        "Factor Analysis",
        "Independent Component Analysis (ICA)"
    ]
}


METRICS = {
    "Classification": ["Accuracy", "F1 Score", "Precision", "Recall"],
    "Regression": ["MSE", "RMSE", "R2 Score"],
}

EXTRAS = [
    "Cross Validation",
    "Hyperparameter Tuning",
    "Save Model"
]



UI_TO_REGISTRY_MAP = {
    # --- Classification Models ---
    "Random Forest": "Random Forest Classifier",
    "Logistic Regression": "Logistic Regression",
    "SVM": "Support Vector Machine",
    "KNN": "K-Nearest Neighbors",
    "Decision Tree Classifier": "Decision Tree Classifier",
    "Gradient Boosting Machines": "Gradient Boosting Machines",
    "AdaBoost": "AdaBoost",
    "catboost": "CatBoost Classifier",
    "LightGBM": "LightGBM Classifier",
    "LDA": "Linear Discriminant Analysis",
    "Naive Bayes": "Naive Bayes",
    "QDA": "Quadratic Discriminant Analysis",
    "XGBoost": "XGBoost",

    
    # --- Regression Models ---
    "Random Forest Regressor": "Random Forest Regression",
    "Linear Regression": "Linear Regression",
    "SVR": "Support Vector Regression",
    "Ridge Regression": "Ridge Regression",
    "Lasso Regression": "Lasso Regression",
    "Bayesian Regression": "Bayesian Regression",
    "Decision Tree Regressor": "Decision Tree Regression",
    "Gradient Boosting Regressor": "Gradient Boosting Regression",
    "Elastic Net": "Elastic Net Regression",
    "polynomial regression": "Polynomial Regression",
    "Support Vector Regression": "Support Vector Regression",
    
    # --- Clustering Models ---
    "K-Means": "K-Means Clustering",
    "DBSCAN": "DBSCAN",
    "Hierarchical Clustering": "Hierarchical Clustering",
    "Affinity Propagation": "Affinity Propagation",
    "Gaussian Mixture Models": "Gaussian Mixture Models",
    "hierarchical clustering": "Hierarchical Clustering",
    "Mean Shift": "Mean Shift Clustering",
    "Spectral Clustering": "Spectral Clustering",


    # --- Dimensionality Reduction Models ---
    "Autoencoder": "Autoencoders",
    "Factor Analysis": "Factor Analysis",
    "Independent Component Analysis (ICA)": "Independent Component Analysis",
    "LDA": "Linear Discriminant Analysis (LDA)",
    "PCA": "Principal Component Analysis (PCA)",
    "t-SNE": "t-Distributed Stochastic Neighbor Embedding (t-SNE)",
    "UMAP": "Uniform Manifold Approximation and Projection (UMAP)",



    # --- Handling Missing Values ---
    "Mean Imputation": "Mean Imputation",
    "Drop Missing Values": "Drop Missing Values",
    "Median Imputation": "Median Imputation",
    "Mode Imputation (Frequent)": "Mode Imputation (Frequent)",
    "KNN Imputation": "KNN Imputation",
    "Constant Value Imputation": "Constant Value Imputation",
    "Forward Fill": "Forward Fill",
    "Iterative Imputer (Random Forest)": "Iterative Imputer (Random Forest)",

    #--- Feature Scaling ---
    "Standard Scaler": "Standard Scaler",
    "Min-Max Scaler": "Min-Max Scaler",
    "Robust Scaler": "Robust Scaler",
    "Log Transformation": "Log Transformation",
    "Power Transformer (Yeo-Johnson)": "Power Transformer (Yeo-Johnson)",
    "Normalization (L2)": "Normalization (L2)",

   # --- encoding categorical variables ---
    "One-Hot Encoding (Dummy Variables)": "One-Hot Encoding (Dummy Variables)",
    "Ordinal Encoding": "Ordinal Encoding",
    "Frequency Encoding": "Frequency Encoding",
    "Target Encoding": "Target Encoding",

    # --- Preprocessing ---
    "Feature Selection": "Principal Component Analysis (PCA)", 
    "Encode Categorical Variables": "Label Encoder",

    #--Data Splitting---
    "Train-Test Split": "Train-Test Split (Sklearn)",
    
    # --- Loaders & Metrics ---
    "CSV": "CSV Loader",
    "Excel": "Excel Loader",
    "Custom Loader": "Custom Data Loader",
    "Accuracy": "Accuracy Metric",
    "F1 Score": "F1 Score Metric",
    "MSE": "Mean Squared Error Metric",
    "RMSE": "RMSE Metric",
    "R2 Score": "R2 Score Metric",
    "Precision": "Precision Metric",
    "Recall": "Recall Metric"
}