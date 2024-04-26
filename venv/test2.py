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

treatments = [

'RemoveInfectedParts',
'ApplyFungicides',
'ImproveAirCirculation',
'RemoveDebris',
'ApplyCopperFungicides',
'AvoidOverheadWatering',
'ApplyChlorothalonilFungicides',
'RotateCrops',
'PruneAffectedParts',
'PlantResistantVarieties',
'AvoidOverWatering',
'ApplyThiophanate-methylFungicides',
'SolarizeSoil',
'ImproveDrainage',
'RemoveInfectedLeaves',
]

for treatment in treatments:
    KB.tell(expr(f'Treatment({treatment})'))

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
KB.tell(expr('PlantSymptom(x,CircularSpots) & PlantSymptom(x,DarkColoredSap) & PlantSymptom(x,PinkishSporeMasses) ==> PlantDisease(x,Anthracnose)'))


KB.tell(expr('PlantSymptom(x, z) & PlantSymptom(x, y) & PlantDisease(x, disease) & Symptom(z) & Symptom(y) ==> Resultat(disease)'))

KB.tell(expr('PlantDisease(x,Rust) ==> PlantTreatment(x,RemoveInfectedParts)'))
KB.tell(expr('PlantDisease(x,Rust) ==> PlantTreatment(x,ApplyCopperFungicides)'))
KB.tell(expr('PlantDisease(x,Rust) ==> PlantTreatment(x,RotateCrops)'))

KB.tell(expr('PlantDisease(x,LeafSpotDiseases) ==> PlantTreatment(x,RemoveInfectedParts)'))
KB.tell(expr('PlantDisease(x,LeafSpotDiseases) ==> PlantTreatment(x,ApplyChlorothalonilFungicides)'))
KB.tell(expr('PlantDisease(x,LeafSpotDiseases) ==> PlantTreatment(x,AvoidOverheadWatering)')) 

KB.tell(expr('PlantDisease(x,GrayMold) ==> PlantTreatment(x,RemoveInfectedParts)'))
KB.tell(expr('PlantDisease(x,GrayMold) ==> PlantTreatment(x,ImproveAirCirculation)'))
KB.tell(expr('PlantDisease(x,GrayMold) ==> PlantTreatment(x,ApplyFungicides)')) 

KB.tell(expr('PlantDisease(x,RootRot) ==> PlantTreatment(x,ImproveDrainage)'))
KB.tell(expr('PlantDisease(x,RootRot) ==> PlantTreatment(x,AvoidOverWatering)'))
KB.tell(expr('PlantDisease(x,RootRot) ==> PlantTreatment(x,ApplyFungicides)')) 

KB.tell(expr('PlantDisease(x,VerticilliumWilt) ==> PlantTreatment(x,RemoveInfectedParts)'))
KB.tell(expr('PlantDisease(x,VerticilliumWilt) ==> PlantTreatment(x,ApplyThiophanate-methylFungicides)'))
KB.tell(expr('PlantDisease(x,VerticilliumWilt) ==> PlantTreatment(x,SolarizeSoil)')) 

KB.tell(expr('PlantDisease(x,FusariumWilt) ==> PlantTreatment(x,PlantResistantVarieties)'))
KB.tell(expr('PlantDisease(x,FusariumWilt) ==> PlantTreatment(x,RotateCrops)'))
KB.tell(expr('PlantDisease(x,FusariumWilt) ==> PlantTreatment(x,AvoidOverWatering)')) 

KB.tell(expr('PlantDisease(x,LateBlight) ==> PlantTreatment(x,RemoveInfectedParts)'))
KB.tell(expr('PlantDisease(x,LateBlight) ==> PlantTreatment(x,ApplyChlorothalonilFungicides)'))
KB.tell(expr('PlantDisease(x,LateBlight) ==> PlantTreatment(x,RotateCrops)')) 

KB.tell(expr('PlantDisease(x,DownyMildew) ==> PlantTreatment(x,RemoveDebris)'))
KB.tell(expr('PlantDisease(x,DownyMildew) ==> PlantTreatment(x,ApplyCopperFungicides)'))
KB.tell(expr('PlantDisease(x,DownyMildew) ==> PlantTreatment(x,AvoidOverheadWatering)')) 

KB.tell(expr('PlantDisease(x,PowderyMildew) ==> PlantTreatment(x,RemoveInfectedParts)'))
KB.tell(expr('PlantDisease(x,PowderyMildew) ==> PlantTreatment(x,ApplyFungicides)'))
KB.tell(expr('PlantDisease(x,PowderyMildew) ==> PlantTreatment(x,ImproveAirCirculation)')) 

KB.tell(expr('PlantDisease(x,Anthracnose) ==> PlantTreatment(x,PruneAffectedParts)'))
KB.tell(expr('PlantDisease(x,Anthracnose) ==> PlantTreatment(x,ApplyCopperFungicides)'))
KB.tell(expr('PlantDisease(x,Anthracnose) ==> PlantTreatment(x,RemoveDebris)')) 





"""
# so based on the entered symptomes one disease will be matched and printed 
for disease in diseases:
    query = expr(f'PlantDisease(x,{disease})')
    #backward chaining  
    solution = KB.ask(query)
    print(solution) 

    if solution:
        
        print(f"The associated disease is : {disease}")
        break

for treatment in treatments: 
    tr=KB.ask(expr(f'PlantTreatment(x,{treatment})')) 
    if tr:
        print(treatment)"""


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
    show_treatments_button.pack()

def query_kb():
    for disease in diseases:
        query = expr(f'PlantDisease(x,{disease})')
        solution = KB.ask(query)
        if solution:
            return f"The associated disease is: {disease}"
    return "No matching disease found." 

def show_treatments():
    treats=[]
    disease = label_result.cget("text").split(": ")[-1]
    for treatment in treatments: 
        tr=KB.ask(expr(f'PlantTreatment(x,{treatment})')) 
        if tr:
            treats.append(treatment)
    
    treatments_text = "\n".join(treats) 
    label_treatments.config(text=f"Treatments for {disease}:\n{treatments_text}")


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

show_treatments_button = tk.Button(root, text="Show Treatments", command=show_treatments)

# Label to display treatments
label_treatments = tk.Label(root, text="")
label_treatments.pack()

# Start the Tkinter event loop
root.mainloop()






























































































































































"""
#forward chaining
solution_generator = fol_fc_ask(KB, expr('Resultat(disease)'))
print(solution_generator) 
for solution in solution_generator:
    disease = solution('disease')
    print(f"The symptoms could be associated with the disease: {disease}") """












"""
if solution:
    disease = solution('X')
    print(f"The symptoms {query} could be associated with the disease: {disease}")
else:
    print("No disease found for the given symptoms.")"""  

    


