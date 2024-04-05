import tkinter as tk
from tkinter import messagebox
from aima.logic import *
from aima.utils import *


def get_matched_diseases(user_symptoms):
    KB = FolKB()
    # Define symptoms
    KB.tell(expr('Symptom(YellowOrangeBrownPustules)'))
    KB.tell(expr('Symptom(Defoliation)'))
    KB.tell(expr('Symptom(CircularIrregularlySpots)'))
    KB.tell(expr('Symptom(GrayBrownFuzz)'))
    KB.tell(expr('Symptom(StuntedFuzzyGrowth)'))
    KB.tell(expr('Symptom(YellowSpots)'))
    KB.tell(expr('Symptom(MustyOdor)'))
    KB.tell(expr('Symptom(DarkMushyDecayedRoots)'))
    KB.tell(expr('Symptom(CircularSpots)'))
    KB.tell(expr('Symptom(WaterSoakedSpots)'))
    KB.tell(expr('Symptom(DarkColoredSap)'))
    KB.tell(expr('Symptom(BrownBlackSpots)'))
    KB.tell(expr('Symptom(GreyPurpleFuzz)'))
    KB.tell(expr('Symptom(FuzzyWhiteMold)'))
    KB.tell(expr('Symptom(CurlyLeaves)'))
    KB.tell(expr('Symptom(OnlyOneSideIsAffected)'))
    KB.tell(expr('Symptom(AllThePlantIsAffected)'))
    KB.tell(expr('Symptom(BrownStricksOnViscularTissue)'))
    KB.tell(expr('Symptom(PinkishSporeMasses)'))

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

    # Define rules
    KB.tell(expr('Symptom(YellowOrangeBrownPustules) & Symptom(Defoliation) ==> Disease(Rust)'))
    KB.tell(expr('Symptom(Defoliation) & Symptom(CircularIrregularlySpots) ==> Disease(LeafSpotDiseases)'))
    KB.tell(expr('Symptom(GrayBrownFuzz) ==> Disease(GrayMold)'))
    KB.tell(expr('Symptom(StuntedFuzzyGrowth) ==> Disease(RootRot)'))
    KB.tell(expr('Symptom(YellowSpots) & Symptom(VerticilliumWilt) ==> Disease(VerticilliumWilt)'))
    KB.tell(expr('Symptom(YellowSpots) & Symptom(FusariumWilt) ==> Disease(FusariumWilt)'))
    KB.tell(expr('Symptom(YellowSpots) & Symptom(DownyMildew) ==> Disease(DownyMildew)'))
    KB.tell(expr('Symptom(YellowSpots) & Symptom(PowderyMildew) ==> Disease(PowderyMildew)'))
    KB.tell(expr('Symptom(MustyOdor) ==> Disease(GrayMold)'))
    KB.tell(expr('Symptom(DarkMushyDecayedRoots) ==> Disease(RootRot)'))
    KB.tell(expr('Symptom(CircularSpots) ==> Disease(LeafSpotDiseases)'))
    KB.tell(expr('Symptom(WaterSoakedSpots) ==> Disease(GrayMold)'))
    KB.tell(expr('Symptom(DarkColoredSap) ==> Disease(LateBlight)'))
    KB.tell(expr('Symptom(BrownBlackSpots) ==> Disease(Anthracnose)'))
    KB.tell(expr('Symptom(GreyPurpleFuzz) ==> Disease(GrayMold)'))
    KB.tell(expr('Symptom(FuzzyWhiteMold) ==> Disease(PowderyMildew)'))
    KB.tell(expr('Symptom(CurlyLeaves) ==> Disease(DownyMildew)'))
    KB.tell(expr('Symptom(OnlyOneSideIsAffected) ==> Disease(VerticilliumWilt)'))
    KB.tell(expr('Symptom(AllThePlantIsAffected) ==> Disease(VerticilliumWilt)'))
    KB.tell(expr('Symptom(BrownStricksOnViscularTissue) & Symptom(RootRot) ==> Disease(RootRot)'))
    KB.tell(expr('Symptom(BrownStricksOnViscularTissue) & Symptom(VerticilliumWilt) ==> Disease(VerticilliumWilt)'))
    KB.tell(expr('Symptom(BrownStricksOnViscularTissue) & Symptom(FusariumWilt) ==> Disease(FusariumWilt)'))
    KB.tell(expr('Symptom(BrownStricksOnViscularTissue) & Symptom(LateBlight) ==> Disease(LateBlight)'))
    KB.tell(expr('Symptom(PinkishSporeMasses) ==> Disease(DownyMildew)'))

    matched_diseases = set()

    for clause in KB.clauses:
        if '==>' in str(clause):
            lhs, rhs = str(clause).split('==>')
            lhs_symptoms = lhs.split('&')
            
            for lhs_symptom in lhs_symptoms:
                symptom_name = lhs_symptom.split('(')[1].split(')')[0]
                if symptom_name in user_symptoms:
                    matched_diseases.add(rhs.split('(')[1].split(')')[0])
                    break

    return matched_diseases

def check_symptoms():
    user_input = entry.get()
    user_symptoms = [symptom.strip() for symptom in user_input.split(',')]
    matched_diseases = get_matched_diseases(user_symptoms)

    if not matched_diseases:
        messagebox.showinfo("Result", "No diseases found for the given symptoms.")
    else:
        messagebox.showinfo("Result", f"The possible diseases might be: {', '.join(matched_diseases)}")

# GUI Setup
root = tk.Tk()
root.title("Disease Identifier")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Enter symptoms (comma-separated):")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

button = tk.Button(frame, text="Check Symptoms", command=check_symptoms)
button.grid(row=1, columnspan=2)

root.mainloop()