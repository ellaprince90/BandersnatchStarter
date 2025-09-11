from pandas import DataFrame
from joblib import dump, load
from datetime import datetime
from sklearn.linear_model import LogisticRegression


class Machine:

    def __init__(self, df: DataFrame):
        '''Initializes the machine learning model'''
        self.name = "Logistic Regression"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        target = df["Rarity"]
        features = df.drop(columns=["Rarity"])
        self.model = LogisticRegression()
        self.model.fit(features, target)

    def __call__(self, feature_basis: DataFrame):
        '''This makes predictions based on the trained model'''
        prediction = self.model.predict(feature_basis)[0]
        proba = self.model.predict_proba(feature_basis)[0]
        class_index = self.model.classes_.tolist().index(prediction)
        confidence = proba[class_index]
        return prediction, confidence

    def save(self, filepath):
        '''Saves the model to the disk'''
        dump(self.model, filepath)

    @classmethod
    def open(cls, filepath):
        '''This opens the specified filepath without creating a new
        instance of the __init__'''
        model = load(filepath)
        instance = cls.__new__(cls)
        instance.model = model
        instance.name = "Logistic Regression"
        instance.timestamp = datetime.now()
        return instance

    def info(self):
        return f'''Model: {self.name},
        Initialized: {self.timestamp.strftime('%B %#d, %Y %H%M')}'''
