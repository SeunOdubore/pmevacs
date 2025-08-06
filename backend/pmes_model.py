# backend/pmes_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Generate sample data (replace with real data)
data = {
    'age': [18,20,22,25,30,19,24,27,21,23],
    'gender': ['M','F','M','F','M','F','M','F','M','F'],
    'location': ['Lagos','Kano','Abuja','Lagos','Enugu','Ibadan','PortHar','Lagos','Abuja','Kaduna'],
    'education': ['Secondary','University','University','Poly','Degree','SSCE','Diploma','Uni','Uni','Poly'],
    'employment': ['No','Yes','Yes','No','Yes','No','Yes','No','Yes','Yes'],
    'voter_registered': [1,1,1,0,1,0,1,1,0,1],
    'social_media_use': ['High','Medium','High','Low','High','Medium','Medium','High','Low','High'],
    'political_interest': ['Low','Medium','High','Low','Medium','Low','Medium','High','Low','Medium'],
    'previous_voted': [0,1,1,0,1,0,1,1,0,1]
}
df = pd.DataFrame(data)

# Preprocess
df = pd.get_dummies(df, columns=['gender','location','education','employment','social_media_use','political_interest'], drop_first=True)
X = df.drop('previous_voted', axis=1)
y = df['previous_voted']

# Train
model = RandomForestClassifier()
model.fit(X, y)

# Save
joblib.dump(model, 'backend/pmes_voter_turnout_model.pkl')
joblib.dump(X.columns.tolist(), 'backend/model_features.pkl')
print("Model trained and saved.")