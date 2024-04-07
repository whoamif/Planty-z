import tkinter as tk
from tkinter import messagebox
from aima.utils import *
from aima.logic import *

kb = FolKB()

# Define diseases
diseases = ["Rust", "LeafSpotDiseases", "GrayMold", "RootRot", "VerticilliumWilt",
            "FusariumWilt", "DownyMildew", "PowderyMildew", "Anthracnose", "LateBlight"]

<<<<<<< Updated upstream
# Add the disease facts to the knowledge base
for disease in diseases:
    kb.tell(expr(f"Disease({disease})")) 
=======
    # Define diseases
    KB.tell(expr('Disease(Rust)'))
    KB.tell(expr('Disease(LeafSpotDiseases)'))
    KB.tell(expr('Disease(GrayMold)'))
    KB.tell(expr('Disease(RootRot)'))
    KB.tell(expr('Disease(VerticilliumWilt)'))
    KB.tell(expr('Disease(FusariumWilt)'))
    KB.tell(expr('Disease(DownyMildew)'))
    KB.tell(expr('Disease(PowderyMildew)'))
    KB.tell(expr('Disease(Anthracnose)'))
    KB.tell(expr('Disease(LateBlight)'))       
>>>>>>> Stashed changes

# Define user attributes in the knowledge base
kb.tell(expr('Person(Me)'))

# Define symptoms
symptoms = ["YellowOrangeBrownPustules", "Defoliation", "CircularIrregularlySpots",
            "GrayBrownFuzz", "StuntedFuzzyGrowth", "YellowSpots", "MustyOdor",
            "DarkMushyDecayedRoots", "CircularSpots", "WaterSoakedSpots",
            "DarkColoredSap", "BrownBlackSpots", "GreyPurpleFuzz", "FuzzyWhiteMold",
            "CurlyLeaves", "OnlyOneSideIsAffected", "AllThePlantIsAffected",
            "BrownStricksOnViscularTissue", "PinkishSporeMasses"]

<<<<<<< Updated upstream
# Add the symptom facts to the knowledge base
for symptom in symptoms:
    kb.tell(expr(f"Symptom(Me, {symptom})"))  # Modified here
=======
    for clause in KB.clauses:
        if '==>' in str(clause):
            lhs, rhs = str(clause).split('==>')
            lhs_symptoms = lhs.split('&')
            
            for lhs_symptom in lhs_symptoms:
                symptom_name = lhs_symptom.split('(')[1].split(')')[0]
                if symptom_name in user_symptoms:
                    matched_diseases.add(rhs.split('(')[1].split(')')[0])
                    break 
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
def suggest_disease(user_symptoms):
    for symptom in user_symptoms:
        kb.tell(expr(f'Symptom(Me, {symptom})'))
    
    likely_diseases = list(fol_fc_ask(kb, expr('RecommendDisease(x, Me)')))
    
    if not likely_diseases:
        messagebox.showinfo("Result", "No likely diseases found based on symptoms.")
        return
    
    
    
    suggested_disease = likely_diseases[0].bindings[0][expr('x')]
    messagebox.showinfo("Result", f"Suggested disease based on symptoms:\n{suggested_disease}")
=======
def check_symptoms(): 
    user_input = entry.get()
    user_symptoms = [symptom.strip() for symptom in user_input.split(',')]
    matched_diseases = get_matched_diseases(user_symptoms)
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
# Main application window
=======

# GUI Setup
>>>>>>> Stashed changes
root = tk.Tk()
root.title("Plant Disease Diagnosis")

button = tk.Button(root, text="Enter Symptoms", command=get_symptoms)
button.pack(pady=20)

root.mainloop()
