from flask import Flask, request, jsonify
from aima3.logic import *
from aima3.utils import *

app = Flask(__name__)

# Knowledge Base (KB)
kb = FolKB()

# Define diseases
diseases = ["Rust", "LeafSpotDiseases", "GrayMold", "RootRot", "VerticilliumWilt",
            "FusariumWilt", "DownyMildew", "PowderyMildew", "Anthracnose", "LateBlight"]

# Add disease facts to the knowledge base
for disease in diseases:
    kb.tell(expr(f"Disease({disease})"))

# Define treatments
treatments = {
    "Rust": "Apply fungicides such as chlorothalonil or copper-based fungicides.",
    "LeafSpotDiseases": "Remove and destroy infected leaves. Apply fungicides as needed.",
    "GrayMold": "Improve air circulation and reduce humidity. Apply fungicides as needed.",
    "RootRot": "Improve soil drainage. Remove and destroy infected plants. Apply fungicides as needed.",
    "VerticilliumWilt": "There are no effective chemical treatments. Remove and destroy infected plants.",
    "FusariumWilt": "There are no effective chemical treatments. Remove and destroy infected plants.",
    "DownyMildew": "Apply fungicides such as copper-based fungicides. Improve air circulation.",
    "PowderyMildew": "Apply sulfur-based fungicides. Improve air circulation.",
    "Anthracnose": "Remove and destroy infected plant parts. Apply fungicides as needed.",
    "LateBlight": "Apply copper-based fungicides. Remove and destroy infected plants."
}

# Add treatment facts to the knowledge base
for disease, treatment in treatments.items():
    kb.tell(expr(f"Treatment({disease}, '{treatment}')"))

# Define user attributes in the knowledge base
kb.tell(expr('Person(Me)'))

# Define symptoms
symptoms = ["YellowOrangeBrownPustules", "Defoliation", "CircularIrregularlySpots",
            "GrayBrownFuzz", "StuntedFuzzyGrowth", "YellowSpots", "YellowBrownSpots", "MustyOdor",
            "DarkMushyDecayedRoots", "CircularSpots", "WaterSoakedSpots",
            "RottedLeaves", "YellowedPlants", "Wilting", "MottledLeaves",
            "NecroticTissue", "WhitePowderyGrowth", "LeafCurling"]

for symptom in symptoms:
    kb.tell(expr(f"Symptom({symptom})"))

def suggest_disease(user_symptoms):
    for symptom in user_symptoms:
        kb.tell(expr(f'Symptom(Me, {symptom})'))

    likely_diseases = list(fol_bc_ask(kb, expr('RecommendDisease(x, Me)')))

    if not likely_diseases:
        return {'Result': "No likely diseases found based on symptoms."}

    disease_count = {}
    max_count = 0

    for disease_dict in likely_diseases:
        for key, value in disease_dict.items():
            if key == expr('x'):
                disease_name = value.op
                disease_count[disease_name] = disease_count.get(disease_name, 0) + 1
                max_count = max(max_count, disease_count[disease_name])

    if not disease_count:
        return {'Result': "No likely diseases found based on symptoms."}

    likely_disease = [disease for disease, count in disease_count.items() if count == max_count]

    if likely_disease:
        disease = likely_disease[0]
        return {
            'Disease': disease,
            'Treatment': treatments.get(disease, "No specific treatment available.")
        }

    return {'Result': "No likely diseases found based on symptoms."}

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
