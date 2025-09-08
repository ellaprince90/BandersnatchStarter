from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load
from datetime import datetime



class Machine:

    def __init__(self, df: DataFrame):
        '''Initializes the machine learning model'''
        self.name = "Random Forest Classifier"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, feature_basis: DataFrame):
        '''This makes predictions based on the trained model'''
        prediction = self.model.predict(feature_basis)[0]
        proba = self.model.predict_proba(feature_basis)[0]
        class_index = self.model.classes_.tolist().index(prediction)
        confidence = proba[class_index]
        return prediction, confidence

    def save(self, filepath):
        dump(self.model, filepath)

    @classmethod
    def open(cls, filepath):
        model = load(filepath)
        instance = cls.__new__(cls)
        instance.model = model
        instance.name = "Random Forest Classifier"
        instance.timestamp = datetime.now()
        return instance

    def info(self):
        return f"Model: {self.name}, Initialized: {self.timestamp.strftime('%B %#d, %Y %H%M')}"
