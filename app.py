from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load data from the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

@app.route('/', methods=['GET'])
def index():
    
    patient_id = request.args.get('patientId')

    if patient_id:
        filtered_data = [entry for entry in data if entry["PatientID"] == patient_id]
    else:
        filtered_data = data

    return render_template('index.html', data=filtered_data)

@app.route('/patient/<patient_id>')
def patient_detail(patient_id):

    patient = next((p for p in data if p["PatientID"] == patient_id), None)

    if patient:
        return render_template('detail.html', patient=patient)
    else:
        return "Patient not found", 404

if __name__ == '__main__':
    app.run(debug=True)
