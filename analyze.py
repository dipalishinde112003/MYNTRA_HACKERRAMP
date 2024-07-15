from flask import Flask, jsonify, render_template
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Myntra Challenge Analytics!'

@app.route('/analyze')
def analyze():
    # Load the data
    data = pd.read_csv('responses.csv')
    
    # Example of basic analysis
    le = LabelEncoder()
    data['name_encoded'] = le.fit_transform(data['name'])
    
    # Create a simple plot
    plt.figure(figsize=(10, 6))
    plt.bar(data['name_encoded'], data['quizType'])
    plt.xlabel('User')
    plt.ylabel('Quiz Type')
    plt.title('User Quiz Participation')
    plt.savefig('static/plot.png')
    
    return render_template('analyze.html')

@app.route('/api/data')
def get_data():
    data = pd.read_csv('responses.csv')
    return jsonify(data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
