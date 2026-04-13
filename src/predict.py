import pandas as pd
import numpy as np
from tensorflow import keras
import pickle

class CareerPredictor:

    def __init__(self, 
                 model_path='models/career_fit_model.h5', 
                 encoder_path='models/label_encoder.pkl', 
                 scaler_path='models/scaler.pkl', 
                 careers_path='data/onet_careers.csv'):
        self.model = keras.models.load_model(model_path)
        self.le = pickle.load(open(encoder_path, 'rb'))
        self.scaler = pickle.load(open(scaler_path, 'rb'))
        self.careers_df = pd.read_csv(careers_path)
    
    def predict(self, features):
        """
        features: numpy array of shape (1, 15)
        returns: dict with prediction results
        """
        features_scaled = self.scaler.transform(features)
        probs = self.model.predict(features_scaled, verbose=0)[0]
        
        archetype_idx = np.argmax(probs)
        archetype = self.le.classes_[archetype_idx]
        confidence = probs[archetype_idx]
        
        # Get careers for this archetype
        career_row = self.careers_df[self.careers_df['archetype'] == archetype].iloc[0]
        careers = [career_row['career_1'], career_row['career_2'], 
                   career_row['career_3'], career_row['career_4'], 
                   career_row['career_5']]
        
        return {
            'archetype': archetype,
            'confidence': float(confidence),
            'probs': dict(zip(self.le.classes_, probs)),
            'careers': careers,
            'all_archetypes': list(zip(self.le.classes_, probs))
        }

        