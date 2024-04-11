import tkinter as tk
from aima3.logic import *
from aima3.utils import * 


# Define knowledge base
KB = FolKB()

# Symptom facts
symptoms = [
    'YellowOrangeBrownPustules',
    'Defoliation',
    'CircularIrregularlySpots',
    'GrayBrownFuzz',
    'WaterSoakedSpots',
    'MustyOdor',
    'StuntedFuzzyGrowth',
    'YellowBrownSpots',
    'Wiltning',
    'DarkMushyDecayedRoots',
    'YellowSpots',
    'BrownStricksOnViscularTissue',
    'OnlyOneSideIsAffected',
    'AllThePlantIsAffected',
    'CircularSpots',
    'DarkColoredSap',
    'PinkishSporeMasses',
    'BrownBlackSpots',
    'FuzzyWhiteMold',
    'YellowGreenSpots',
    'GreyPurpleFuzz',
    'CurlyLeaves',
    'PowderyFuzzyGrowth',
    'YellowBrownLeaves'
]

for symptom in symptoms:
    KB.tell(expr(f'Symptom({symptom})'))

# Disease facts
diseases = [
    'Rust',
    'LeafSpotDiseases',
    'GrayMold',
    'RootRot',
    'VerticilliumWilt',
    'FusariumWilt',
    'Anthracnose',
    'LateBlight',
    'DownyMildew',
    'PowderyMildew'
]

for disease in diseases:
    KB.tell(expr(f'Disease({disease})'))


# plant symptoms facts are added by the user :


KB.tell(expr('Plant(x)'))



# Rules for inferring diseases from symptoms 


KB.tell(expr('PlantSymptom(x,YellowOrangeBrownPustules) & PlantSymptom(x,Defoliation) ==> PlantDisease(x,Rust)')) 
KB.tell(expr('PlantSymptom(x,CircularIrregularlySpots) & PlantSymptom(x,Defoliation) ==> PlantDisease(x,LeafSpotDiseases)')) 
KB.tell(expr('PlantSymptom(x,GrayBrownFuzz) & PlantSymptom(x,WaterSoakedSpots) & PlantSymptom(x,MustyOdor) ==> PlantDisease(x,GrayMold)'))
KB.tell(expr('PlantSymptom(x,StuntedFuzzyGrowth) & PlantSymptom(x,YellowBrownSpots) & PlantSymptom(x,Wiltning) & PlantSymptom(x,DarkMushyDecayedRoots) ==> PlantDisease(x,RootRot)')) 
KB.tell(expr('PlantSymptom(x,YellowSpots) & PlantSymptom(x,Wiltning) & PlantSymptom(x,BrownStricksOnViscularTissue) & PlantSymptom(x,OnlyOneSideIsAffected) ==> PlantDisease(x,VerticilliumWilt)'))
KB.tell(expr('PlantSymptom(x,YellowSpots) & PlantSymptom(x,Wiltning) & PlantSymptom(x,BrownStricksOnViscularTissue) & PlantSymptom(x,AllThePlantIsAffected) ==> PlantDisease(x,FusariumWilt)'))
KB.tell(expr('PlantSymptom(x,WaterSoakedSpots) & PlantSymptom(x,BrownBlackSpots) & PlantSymptom(x,FuzzyWhiteMold) ==> PlantDisease(x,LateBlight)'))
KB.tell(expr('PlantSymptom(x,YellowGreenSpots) & PlantSymptom(x,GreyPurpleFuzz) & PlantSymptom(x,CurlyLeaves) & PlantSymptom(x,Defoliation) ==> PlantDisease(x,DownyMildew)'))
KB.tell(expr('PlantSymptom(x,PowderyFuzzyGrowth) & PlantSymptom(x,YellowBrownLeaves) & PlantSymptom(x,Defoliation) ==> PlantDisease(x,PowderyMildew)'))


KB.tell(expr('PlantSymptom(x, z) & PlantSymptom(x, y) & PlantDisease(x, disease) & Symptom(z) & Symptom(y) ==> Resultat(disease)'))


"""
KB.tell(expr('Symptom(x) ==> Disease(y)'))      
KB.tell(expr('Symptom(YellowOrangeBrownPustules) & Symptom(Defoliation) ==> Disease(Rust)')) 
KB.tell(expr('Symptom(CircularIrregularlySpots) & Symptom(Defoliation) ==> Disease(LeafSpotDiseases)'))
KB.tell(expr('Symptom(GrayBrownFuzz) & Symptom(WaterSoakedSpots) & Symptom(MustyOdor) ==> Disease(GrayMold)'))
KB.tell(expr('Symptom(StuntedFuzzyGrowth) & Symptom(YellowBrownSpots) & Symptom(Wiltning) & Symptom(DarkMushyDecayedRoots) ==> Disease(RootRot)'))
KB.tell(expr('Symptom(YellowSpots) & Symptom(Wiltning) & Symptom(BrownStricksOnViscularTissue) & Symptom(OnlyOneSideIsAffected) ==> Disease(VerticilliumWilt)'))
KB.tell(expr('Symptom(YellowSpots) & Symptom(Wiltning) & Symptom(BrownStricksOnViscularTissue) & Symptom(AllThePlantIsAffected) ==> Disease(FusariumWilt)'))
KB.tell(expr('Symptom(CircularSpots) & Symptom(DarkColoredSap) & Symptom(PinkishSporeMasses) ==> Disease(Anthracnose)'))
KB.tell(expr('Symptom(WaterSoakedSpots) & Symptom(BrownBlackSpots) & Symptom(FuzzyWhiteMold) ==> Disease(LateBlight)'))
KB.tell(expr('Symptom(YellowGreenSpots) & Symptom(GreyPurpleFuzz) & Symptom(CurlyLeaves) & Symptom(Defoliation) ==> Disease(DownyMildew)'))
KB.tell(expr('Symptom(PowderyFuzzyGrowth) & Symptom(YellowBrownLeaves) & Symptom(Defoliation) ==> Disease(PowderyMildew)'))

# so based on the entered symptomes one disease will be matched and printed 
for disease in diseases:
    query = expr(f'PlantDisease(x,{disease})')
    #backward chaining  
    solution = KB.ask(query)
    print(solution) 

    if solution:
        
        print(f"The associated disease is : {disease}")
        break
"""

# Initialize Tkinter
root = tk.Tk()
root.title("Plant Disease Diagnosis")

def add_symptom(symptom):
    # Add the symptom to the knowledge base
    KB.tell(expr(f'PlantSymptom(x,{symptom})'))
    # Update the label to display the selected symptoms
    label_selected_symptoms.config(text=label_selected_symptoms.cget("text") + f" {symptom},")


def diagnose():
    # Query the knowledge base
    query_result = query_kb()
    # Display the result
    label_result.config(text=query_result)

def query_kb():
    for disease in diseases:
        query = expr(f'PlantDisease(user,{disease})')
        solution = KB.ask(query)
        if solution:
            return f"The associated disease is: {disease}"
    return "No matching disease found." 


# Interface layout
label_instruction = tk.Label(root, text="Select all plant symptoms:")
label_instruction.pack()

# Create buttons for each symptom
symptom_buttons = []
for symptom in symptoms:
    button = tk.Button(root, text=symptom, command=lambda s=symptom: add_symptom(s))
    button.pack()
    symptom_buttons.append(button)

# Label to display selected symptoms
label_selected_symptoms = tk.Label(root, text="")
label_selected_symptoms.pack()

# Button to diagnose
button_diagnose = tk.Button(root, text="Diagnose", command=diagnose)
button_diagnose.pack()

# Label to display diagnosis result
label_result = tk.Label(root, text="")
label_result.pack()

# Start the Tkinter event loop
root.mainloop()



    


