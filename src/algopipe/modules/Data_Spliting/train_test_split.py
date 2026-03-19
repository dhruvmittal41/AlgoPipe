from algopipe.registry import Registry, BaseModule

@Registry.register("Data_Spliting")
class TrainTestSplit(BaseModule):
    name = "Train-Test Split (Sklearn)"
    description = "Splits data into training and testing sets."

    def get_imports(self):
        return ["from sklearn.model_selection import train_test_split"]

    def get_code(self, variable_name="data"):
        return (
            f"# Splitting data\n"
            f"X = df.drop(columns=['target']) # Assuming 'target' column exists\n"
            f"y = df['target']\n"
            f"X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"
        )