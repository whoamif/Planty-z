from flask import Flask, request, jsonify
from rules import suggest_disease

app = Flask(__name__)

@app.route('/api/suggest_disease', methods=['POST'])
def suggest_disease_endpoint():
    data = request.get_json()
    user_symptoms = data.get('symptoms', [])
    if not user_symptoms:
        return jsonify({'error': 'Symptoms not provided'}), 400

    result = suggest_disease(user_symptoms)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
