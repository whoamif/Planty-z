import tkinter as tk
from tkinter import messagebox
from aima.utils import *
from aima.logic import *

kb = FolKB()

# Define diseases
diseases = ["Rust", "LeafSpotDiseases", "GrayMold", "RootRot", "VerticilliumWilt",
            "FusariumWilt", "DownyMildew", "PowderyMildew", "Anthracnose", "LateBlight"]

# Add the disease facts to the knowledge base
for disease in diseases:
    kb.tell(expr(f"Disease({disease})"))

# Define user attributes in the knowledge base
kb.tell(expr('Person(Me)'))

# Define symptoms
symptoms = ["YellowOrangeBrownPustules", "Defoliation", "CircularIrregularlySpots",
            "GrayBrownFuzz", "StuntedFuzzyGrowth", "YellowSpots", "MustyOdor",
            "DarkMushyDecayedRoots", "CircularSpots", "WaterSoakedSpots",
            "DarkColoredSap", "BrownBlackSpots", "GreyPurpleFuzz", "FuzzyWhiteMold",
            "CurlyLeaves", "OnlyOneSideIsAffected", "AllThePlantIsAffected",
            "BrownStricksOnViscularTissue", "PinkishSporeMasses"]

# Add the symptom facts to the knowledge base
for symptom in symptoms:
    kb.tell(expr(f"Symptom(Me, {symptom})"))  # Modified here

# Define rules based on symptoms and diseases
kb.tell(expr('Symptom(Me, x) & Symptom(Me, y) & Disease(z) ==> RecommendDisease(z, Me)'))
kb.tell(expr('Symptom(Me, x) & Symptom(Me, y) & Symptom(Me, z) & Disease(a) ==> RecommendDisease(a, Me)'))
kb.tell(expr('Symptom(Me, x) & Disease(y) ==> RecommendDisease(y, Me)'))
kb.tell(expr('Symptom(YellowOrangeBrownPustules) & Symptom(Defoliation) ==> Disease(Rust)'))
kb.tell(expr('Symptom(Defoliation) & Symptom(CircularIrregularlySpots) ==> Disease(LeafSpotDiseases)'))
kb.tell(expr('Symptom(GrayBrownFuzz) ==> Disease(GrayMold)'))
kb.tell(expr('Symptom(StuntedFuzzyGrowth) ==> Disease(RootRot)'))
kb.tell(expr('Symptom(YellowSpots) & Symptom(VerticilliumWilt) ==> Disease(VerticilliumWilt)'))
kb.tell(expr('Symptom(YellowSpots) & Symptom(FusariumWilt) ==> Disease(FusariumWilt)'))
kb.tell(expr('Symptom(YellowSpots) & Symptom(DownyMildew) ==> Disease(DownyMildew)'))
kb.tell(expr('Symptom(YellowSpots) & Symptom(PowderyMildew) ==> Disease(PowderyMildew)'))
kb.tell(expr('Symptom(MustyOdor) ==> Disease(GrayMold)'))
kb.tell(expr('Symptom(DarkMushyDecayedRoots) ==> Disease(RootRot)'))
kb.tell(expr('Symptom(CircularSpots) ==> Disease(LeafSpotDiseases)'))
kb.tell(expr('Symptom(WaterSoakedSpots) ==> Disease(GrayMold)'))
kb.tell(expr('Symptom(DarkColoredSap) ==> Disease(LateBlight)'))
kb.tell(expr('Symptom(BrownBlackSpots) ==> Disease(Anthracnose)'))
kb.tell(expr('Symptom(GreyPurpleFuzz) ==> Disease(GrayMold)'))
kb.tell(expr('Symptom(FuzzyWhiteMold) ==> Disease(PowderyMildew)'))
kb.tell(expr('Symptom(CurlyLeaves) ==> Disease(DownyMildew)'))
kb.tell(expr('Symptom(OnlyOneSideIsAffected) ==> Disease(VerticilliumWilt)'))
kb.tell(expr('Symptom(AllThePlantIsAffected) ==> Disease(VerticilliumWilt)'))
kb.tell(expr('Symptom(BrownStricksOnViscularTissue) & Symptom(RootRot) ==> Disease(RootRot)'))
kb.tell(expr('Symptom(BrownStricksOnViscularTissue) & Symptom(VerticilliumWilt) ==> Disease(VerticilliumWilt)'))
kb.tell(expr('Symptom(BrownStricksOnViscularTissue) & Symptom(FusariumWilt) ==> Disease(FusariumWilt)'))
kb.tell(expr('Symptom(BrownStricksOnViscularTissue) & Symptom(LateBlight) ==> Disease(LateBlight)'))
kb.tell(expr('Symptom(PinkishSporeMasses) ==> Disease(DownyMildew)'))

def suggest_disease(user_symptoms):
    for symptom in user_symptoms:
        kb.tell(expr(f'Symptom(Me, {symptom})'))
    
    likely_diseases = list(fol_fc_ask(kb, expr('RecommendDisease(x, Me)')))
    
    if not likely_diseases:
        messagebox.showinfo("Result", "No likely diseases found based on symptoms.")
        return
    
    diseases_count = {}
    for disease in likely_diseases:
        disease_name = disease[x]
        diseases_count[disease_name] = diseases_count.get(disease_name, 0) + 1
    
    suggested_disease = max(diseases_count, key=diseases_count.get)
    messagebox.showinfo("Result", f"Suggested disease based on symptoms:\n{suggested_disease}")

# Interface using tkinter
def get_symptoms():
    symptoms_window = tk.Toplevel()
    symptoms_window.title("Enter Symptoms")
    
    tk.Label(symptoms_window, text="Enter the symptoms separated by commas:").pack(pady=20)
    
    symptoms_entry = tk.Entry(symptoms_window, width=50)
    symptoms_entry.pack(pady=20)
    
    def on_submit():
        user_symptoms = [symptom.strip() for symptom in symptoms_entry.get().split(',')]
        suggest_disease(user_symptoms)
        symptoms_window.destroy()
    
    submit_button = tk.Button(symptoms_window, text="Submit", command=on_submit)
    submit_button.pack(pady=20)

# Main application window
root = tk.Tk()
root.title("Plant Disease Diagnosis")

button = tk.Button(root, text="Enter Symptoms", command=get_symptoms)
button.pack(pady=20)

root.mainloop()
