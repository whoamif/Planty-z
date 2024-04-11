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
    kb.tell(expr(f"Symptom(Me, {symptom})"))

# Define rules based on symptoms and diseases
kb.tell(expr('Symptom(Me, YellowOrangeBrownPustules) & Symptom(Me, Defoliation) ==> RecommendDisease(Rust, Me)'))
kb.tell(expr('Symptom(Me, Defoliation) & Symptom(Me, CircularIrregularlySpots) ==> RecommendDisease(LeafSpotDiseases, Me)'))
kb.tell(expr('Symptom(Me, GrayBrownFuzz) ==> RecommendDisease(GrayMold, Me)'))
kb.tell(expr('Symptom(Me, StuntedFuzzyGrowth) ==> RecommendDisease(RootRot, Me)'))
kb.tell(expr('Symptom(Me, YellowSpots) & Symptom(Me, VerticilliumWilt) ==> RecommendDisease(VerticilliumWilt, Me)'))
kb.tell(expr('Symptom(Me, YellowSpots) & Symptom(Me, FusariumWilt) ==> RecommendDisease(FusariumWilt, Me)'))
kb.tell(expr('Symptom(Me, YellowSpots) & Symptom(Me, DownyMildew) ==> RecommendDisease(DownyMildew, Me)'))
kb.tell(expr('Symptom(Me, YellowSpots) & Symptom(Me, PowderyMildew) ==> RecommendDisease(PowderyMildew, Me)'))
kb.tell(expr('Symptom(Me, MustyOdor) ==> RecommendDisease(GrayMold, Me)'))
kb.tell(expr('Symptom(Me, DarkMushyDecayedRoots) ==> RecommendDisease(RootRot, Me)'))
kb.tell(expr('Symptom(Me, CircularSpots) ==> RecommendDisease(LeafSpotDiseases, Me)'))
kb.tell(expr('Symptom(Me, WaterSoakedSpots) ==> RecommendDisease(GrayMold, Me)'))
kb.tell(expr('Symptom(Me, DarkColoredSap) ==> RecommendDisease(LateBlight, Me)'))
kb.tell(expr('Symptom(Me, BrownBlackSpots) ==> RecommendDisease(Anthracnose, Me)'))
kb.tell(expr('Symptom(Me, GreyPurpleFuzz) ==> RecommendDisease(GrayMold, Me)'))
kb.tell(expr('Symptom(Me, FuzzyWhiteMold) ==> RecommendDisease(PowderyMildew, Me)'))
kb.tell(expr('Symptom(Me, CurlyLeaves) ==> RecommendDisease(DownyMildew, Me)'))
kb.tell(expr('Symptom(Me, OnlyOneSideIsAffected) ==> RecommendDisease(VerticilliumWilt, Me)'))
kb.tell(expr('Symptom(Me, AllThePlantIsAffected) ==> RecommendDisease(VerticilliumWilt, Me)'))
kb.tell(expr('Symptom(Me, BrownStricksOnViscularTissue) & Symptom(Me, RootRot) ==> RecommendDisease(RootRot, Me)'))
kb.tell(expr('Symptom(Me, BrownStricksOnViscularTissue) & Symptom(Me, VerticilliumWilt) ==> RecommendDisease(VerticilliumWilt, Me)'))
kb.tell(expr('Symptom(Me, BrownStricksOnViscularTissue) & Symptom(Me, FusariumWilt) ==> RecommendDisease(FusariumWilt, Me)'))
kb.tell(expr('Symptom(Me, BrownStricksOnViscularTissue) & Symptom(Me, LateBlight) ==> RecommendDisease(LateBlight, Me)'))
kb.tell(expr('Symptom(Me, PinkishSporeMasses) ==> RecommendDisease(DownyMildew, Me)'))

def suggest_disease(user_symptoms):
    for symptom in user_symptoms:
        kb.tell(expr(f'Symptom(Me, {symptom})'))
    
    likely_diseases = fol_bc_ask(kb, expr('RecommendDisease(x, Me)'))
    
    suggested_diseases = [str(disease[x]) for disease in likely_diseases]
    
    if not suggested_diseases:
        messagebox.showinfo("Result", "No likely diseases found based on symptoms.")
        return
    
    messagebox.showinfo("Result", f"Suggested disease(s) based on symptoms:\n{', '.join(set(suggested_diseases))}")

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
