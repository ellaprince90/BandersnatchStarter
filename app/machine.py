from pandas import DataFrame
from xgboost import XGBRegressor
from joblib import dump, load
from datetime import datetime



class Machine:

    def __init__(self, df: DataFrame):
        '''Initializes the machine learning model'''
        self.name = "XGB Regressor"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = XGBRegressor(
            n_estimators=100,
            max_depth=5,
            learning_rate=0.1,
            random_state=42
        )
        self.model.fit(features, target)

    def __call__(self, feature_basis: DataFrame):
        '''This makes predictions based on the trained model'''
        prediction = self.model.predict(feature_basis)[0]
        # proba = self.model.predict_proba(feature_basis)[0]
        # class_index = self.model.classes_.tolist().index(prediction)
        confidence = None
        return prediction, confidence

    def save(self, filepath):
        dump(self.model, filepath)

    @classmethod
    def open(cls, filepath):
        model = load(filepath)
        instance = cls.__new__(cls)
        instance.model = model
        instance.name = "XGBoost Regressor"
        instance.timestamp = datetime.now()
        return instance

    def info(self):
        return f"Model: {self.name}, Initialized: {self.timestamp.strftime('%B %#d, %Y %H%M')}"
