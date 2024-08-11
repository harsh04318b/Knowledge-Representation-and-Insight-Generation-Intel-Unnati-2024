from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

app = Flask(__name__)
CORS(app)

# Load your pre-trained logistic regression model and scaler
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def index():
    return {'message': 'hello world'}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        input_data = np.array([
            data['male'], data['age'], data['currentSmoker'], data['cigsPerDay'],
            data['BPMeds'], data['prevalentStroke'], data['prevalentHyp'],
            data['diabetes'], data['totChol'], data['sysBP'], data['diaBP'],
            data['BMI'], data['heartRate'], data['glucose']
        ]).reshape(1, -1)
        
        # Apply the scaler to the input data
        scaled_input = scaler.transform(input_data)
        
        # Make prediction using the scaled input
        prediction = model.predict(scaled_input)
        
        output = 'In the risk of Heart Attack' if prediction[0] == 1 else 'no risk of heart attack'
        print(f"Prediction made: {output}")  # Server-side logging
        return jsonify(result=output)
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Server-side error logging
        return jsonify(error=str(e)), 400

def preprocess_data(df):
    df['cigsPerDay'] = df['cigsPerDay'].fillna(round(df['cigsPerDay'].mean(), 0))
    df['BPMeds'] = df['BPMeds'].fillna(1)
    df['totChol'] = df['totChol'].fillna(df['totChol'].mean())
    df['BMI'] = df['BMI'].fillna(df['BMI'].mean())
    df['heartRate'] = df['heartRate'].fillna(df['heartRate'].mean())
    df['glucose'] = df['glucose'].fillna(df['glucose'].mean())
    return df

def generate_graphs(df):
    graphs = []

    # Discrete Features Count Plot
    plt.figure(figsize=(20, 9))
    discreteFeat = ['male', 'currentSmoker', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes']
    for n, f in enumerate(discreteFeat, 1):
        plt.subplot(2, 3, n)
        sns.countplot(x=f, data=df, alpha=0.85)
    plt.tight_layout()
    graphs.append(('Discrete Features Count Plot', plt_to_base64()))

    # Continuous Features Histogram
    plt.figure(figsize=(20, 9))
    contFeat = ['age', 'cigsPerDay', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose']
    for n, f in enumerate(contFeat, 1):
        plt.subplot(2, 4, n)
        sns.histplot(df[f], bins=40, color='red', kde=True)
        plt.title(f'Histogram of {f}')
    plt.tight_layout()
    graphs.append(('Continuous Features Histogram', plt_to_base64()))

    # Age vs Heart Rate and BMI Scatter Plots
    plt.figure(figsize=(20, 9))
    plt.subplot(1, 2, 1)
    sns.scatterplot(data=df, x='age', y='heartRate', hue='TenYearCHD', palette={0: 'blue', 1: 'red'})
    plt.title('Age vs Heart Rate and relation for heart attack')
    plt.subplot(1, 2, 2)
    sns.scatterplot(data=df, x='age', y='BMI', hue='TenYearCHD', palette={0: 'blue', 1: 'red'})
    plt.title('Age vs Body Mass Index')
    plt.tight_layout()
    graphs.append(('Age vs Heart Rate and BMI', plt_to_base64()))

    # Blood Pressure Scatter Plot
    plt.figure(figsize=(20, 9))
    sns.scatterplot(data=df, x='sysBP', y='diaBP', hue='TenYearCHD', palette={0: 'blue', 1: 'red'})
    plt.xlabel('Systolic Blood Pressure')
    plt.ylabel('Diastolic Blood Pressure')
    plt.title('Systolic vs Diastolic Blood Pressure')
    graphs.append(('Blood Pressure Scatter Plot', plt_to_base64()))

    # Heart Attack Incidence by Age and Gender
    grouped = df.groupby(['male', 'age'])['TenYearCHD'].mean().reset_index()
    plt.figure(figsize=(14, 8))
    sns.barplot(data=grouped, x='age', y='TenYearCHD', hue='male', palette=['blue', 'red'])
    plt.title('Heart Attack Incidence by Age and Gender')
    plt.xlabel('Age')
    plt.ylabel('Incidence of Heart Attack (Proportion)')
    plt.legend(title='Gender', labels=['Female', 'Male'])
    graphs.append(('Heart Attack Incidence by Age and Gender', plt_to_base64()))

    # Cigarettes Per Day by Age and Gender
    grouped = df.groupby(['male', 'age'])['cigsPerDay'].mean().reset_index()
    plt.figure(figsize=(14, 8))
    sns.barplot(data=grouped, x='age', y='cigsPerDay', hue='male', palette=['blue', 'red'])
    plt.title('Cigarettes Per Day by Age and Gender')
    plt.xlabel('Age')
    plt.ylabel('Cigarettes Per Day (Average)')
    plt.legend(title='Gender', labels=['Female', 'Male'])
    graphs.append(('Cigarettes Per Day by Age and Gender', plt_to_base64()))

    # Smokers by Age Group
    graph = df.groupby("age", as_index=False).currentSmoker.sum()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=graph["age"], y=graph["currentSmoker"])
    plt.title("Smokers by Age Group")
    plt.xlabel("Age")
    plt.ylabel("Number of Smokers")
    graphs.append(('Smokers by Age Group', plt_to_base64()))

    # Ten-Year CHD Risk by Prevalent Hypertension
    grouped = df.groupby('prevalentHyp')['TenYearCHD'].mean().reset_index()
    plt.figure(figsize=(8, 6))
    sns.barplot(x='prevalentHyp', y='TenYearCHD', data=grouped, palette='Set2')
    plt.title('Ten-Year CHD Risk by Prevalent Hypertension')
    plt.xlabel('Prevalent Hypertension (0: No, 1: Yes)')
    plt.ylabel('Ten-Year CHD Risk (Proportion)')
    plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
    graphs.append(('Ten-Year CHD Risk by Prevalent Hypertension', plt_to_base64()))

    # Ten-Year CHD Risk by Diabetes
    grouped = df.groupby('diabetes')['TenYearCHD'].mean().reset_index()
    plt.figure(figsize=(8, 6))
    sns.barplot(x='diabetes', y='TenYearCHD', data=grouped, palette='Set2')
    plt.title('Ten-Year CHD Risk by Diabetes')
    plt.xlabel('Diabetes (0: No, 1: Yes)')
    plt.ylabel('Ten-Year CHD Risk (Proportion)')
    plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
    graphs.append(('Ten-Year CHD Risk by Diabetes', plt_to_base64()))

    # Heart Attack Incidence by Total Cholesterol and BMI
    plt.figure(figsize=(12, 8))
    plt.hexbin(df['totChol'], df['BMI'], C=df['TenYearCHD'], gridsize=20, cmap='coolwarm')
    plt.colorbar(label='10-Year CHD Risk')
    plt.title('Total Cholesterol vs BMI with 10-Year CHD Risk')
    plt.xlabel('Total Cholesterol')
    plt.ylabel('BMI')
    graphs.append(('Heart Attack Incidence by Total Cholesterol and BMI', plt_to_base64()))

    # Distribution of Cigarettes Per Day by Ten-Year CHD Risk
    filtered_df = df[df['cigsPerDay'] > 0]
    plt.figure(figsize=(10, 6))
    sns.violinplot(x='TenYearCHD', y='cigsPerDay', data=filtered_df, palette='Set2')
    plt.title('Distribution of Cigarettes Per Day (Non-Zero) by Ten-Year CHD Risk')
    plt.xlabel('Ten-Year CHD Risk (0: No, 1: Yes)')
    plt.ylabel('Cigarettes Per Day')
    graphs.append(('Distribution of Cigarettes Per Day by Ten-Year CHD Risk', plt_to_base64()))

    return graphs

def plt_to_base64():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    plt.close()
    return graph

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and file.filename.endswith('.csv'):
        try:
            df = pd.read_csv(file)
            df = preprocess_data(df)
            graphs = generate_graphs(df)
            return jsonify({
                'graphs': [{'title': title, 'image': image} for title, image in graphs]
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file format. Please upload a CSV file.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
