import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar
from aima3.logic import *
from aima3.utils import * 

kb = FolKB()

# Define diseases
diseases = ["Rust", "LeafSpotDiseases", "GrayMold", "RootRot", "VerticilliumWilt",
            "FusariumWilt", "DownyMildew", "PowderyMildew", "Anthracnose", "LateBlight"]

# Add the disease facts to the knowledge base
for disease in diseases:
    kb.tell(expr(f"Disease({disease})"))

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

# Add the treatment facts to the knowledge base
for disease, treatment in treatments.items():
    #print(f"Adding treatment for {disease}: {treatment}")
    kb.tell(expr(f"Treatment({disease}, '{treatment}')"))    

# Define user attributes in the knowledge base
kb.tell(expr('Person(Me)'))

# Define symptoms
symptoms = ["YellowOrangeBrownPustules", "Defoliation", "CircularIrregularlySpots",
            "GrayBrownFuzz", "StuntedFuzzyGrowth", "YellowSpots","YellowBrownSpots" "MustyOdor",
            "DarkMushyDecayedRoots", "CircularSpots", "WaterSoakedSpots",
            "DarkColoredSap", "BrownBlackSpots", "GreyPurpleFuzz", "FuzzyWhiteMold",
            "CurlyLeaves", "OnlyOneSideIsAffected", "AllThePlantIsAffected",
            "BrownStricksOnViscularTissue", "PinkishSporeMasses",
            "Wilting", "YellowingOfLeaves", "StuntedGrowth", "RottingOfRoots",
            "WhitePowderySubstanceOnLeaves", "YellowingOfLowerLeaves",]

# Add the symptom facts to the knowledge base
for symptom in symptoms:
    kb.tell(expr(f"Symptom(Me, {symptom})"))

# Define rules based on symptoms and diseases
kb.tell(expr('Symptom(Me, YellowOrangeBrownPustules) & Symptom(Me, Defoliation) ==> RecommendDisease(Rust, Me)'))
kb.tell(expr('Symptom(Me, Defoliation) & Symptom(Me, CircularIrregularlySpots) ==> RecommendDisease(LeafSpotDiseases, Me)'))
kb.tell(expr('Symptom(Me, GrayBrownFuzz) & (Symptom(Me, WaterSoakedSpots) & Symptom(Me, MustyOdor)) ==> RecommendDisease(GrayMold, Me)'))
kb.tell(expr('Symptom(Me, StuntedFuzzyGrowth) & Symptom(Me, YellowBrownSpots) & (Symptom(Me, Wilting) & (Symptom(Me, DarkMushyDecayedRoots))) ==> RecommendDisease(RootRot, Me)'))

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

# Function to suggest disease based on symptoms
#ncreayi 2 end points desease and treatment fi flask rest api 
def suggest_disease(user_symptoms):
    for symptom in user_symptoms:
        kb.tell(expr(f'Symptom(Me, {symptom})'))
    
    #print("Symptoms added to KB:", user_symptoms)
    
    likely_diseases = list(fol_bc_ask(kb, expr('RecommendDisease(x, Me)')))
    
    #print("Likely diseases:", likely_diseases)
    
    if not likely_diseases:
        print("Result", "No likely diseases found based on symptoms.")
        return
    
    disease_count = {}
    max_count = 0
    
    for disease_dict in likely_diseases:
        for key, value in disease_dict.items():
            if key == expr('x'):
                disease_name = value.op
                disease_count[disease_name] = disease_count.get(disease_name, 0) + 1
                max_count = max(max_count, disease_count[disease_name])

    if not disease_count:
        print("Result", "No likely diseases found based on symptoms.")
        return
    
    print("Likely diseases and their counts:")
    for disease, count in disease_count.items():
        if count == max_count:
            print(f"{disease}")
            if disease in treatments:
                print("Treatment:", treatments[disease])
            else:
                print("No specific treatment available.")
    
    #suggested_diseases = [disease for disease, count in disease_count.items() if count == max_count]
    #messagebox.showinfo("Result", f"Suggested disease(s) based on symptoms:\n{suggested_diseases}\n\nTreatment(s):\n{[treatments[disease] if disease in treatments else 'No specific treatment available' for disease in suggested_diseases]}")

suggest_disease(["YellowOrangeBrownPustules","Defoliation"])



"""
# Interface using tkinter
def get_symptoms():
    symptoms_window = tk.Toplevel()
    symptoms_window.title("Enter Symptoms")
    
    tk.Label(symptoms_window, text="Select the symptoms:").pack(pady=10)
    
    scrollbar = Scrollbar(symptoms_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    listbox = Listbox(symptoms_window, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set)
    for symptom in symptoms:
        listbox.insert(tk.END, symptom)
    listbox.pack(pady=10)
    
    scrollbar.config(command=listbox.yview)
    
    def on_submit():
        selected_indices = listbox.curselection()
        user_symptoms = [listbox.get(idx) for idx in selected_indices]
        suggest_disease(user_symptoms)
        symptoms_window.destroy()
    
    submit_button = tk.Button(symptoms_window, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

# Main application window
root = tk.Tk()
root.title("Plant Disease Diagnosis")

button = tk.Button(root, text="Select Symptoms", command=get_symptoms)
button.pack(pady=20)

root.mainloop()
"""