from aima.logic import *
from aima.utils import *

KB = FolKB()

symptoms = [
    expr('Symptom("YellowOrangeBrownPustules")'),
    expr('Symptom("Defoliation")'),
    expr('Symptom("CircularIrregularlySpots")'),
    expr('Symptom("GrayBrownFuzz")'),
    expr('Symptom("StuntedFuzzyGrowth")'),
    expr('Symptom("YellowSpots")'),
    expr('Symptom("MustyOdor")'),
    expr('Symptom("DarkMushyDecayedRoots")'),
    expr('Symptom("CircularSpots")'),
    expr('Symptom("WaterSoakedSpots")'),
    expr('Symptom("DarkColoredSap")'),
    expr('Symptom("BrownBlackSpots")'),
    expr('Symptom("GreyPurpleFuzz")'),
    expr('Symptom("FuzzyWhiteMold")'),
    expr('Symptom("CurlyLeaves")'),
    expr('Symptom("OnlyOneSideIsAffected")'),
    expr('Symptom("AllThePlantIsAffected")'),
    expr('Symptom("BrownStricksOnViscularTissue")'),
    expr('Symptom("PinkishSporeMasses")')
]

diseases = [
    "Rust", "LeafSpotDiseases", "GrayMold", "RootRot", "VerticilliumWilt",
    "FusariumWilt", "Anthracnose", "LateBlight", "DownyMildew", "PowderyMildew"
]

for disease in diseases:
    KB.tell(expr(f'Disease("{disease}")'))

# Define rules
KB.tell(expr('Symptom("YellowOrangeBrownPustules") & Symptom("Defoliation") ==> Disease("Rust")'))
KB.tell(expr('Symptom("Defoliation") & Symptom("CircularIrregularlySpots") ==> Disease("LeafSpotDiseases")'))
KB.tell(expr('Symptom("GrayBrownFuzz") ==> Disease("GrayMold")'))
KB.tell(expr('Symptom("StuntedFuzzyGrowth") ==> Disease("RootRot")'))
KB.tell(expr('Symptom("YellowSpots") & Symptom("VerticilliumWilt") ==> Disease("VerticilliumWilt")'))
KB.tell(expr('Symptom("YellowSpots") & Symptom("FusariumWilt") ==> Disease("FusariumWilt")'))
KB.tell(expr('Symptom("YellowSpots") & Symptom("DownyMildew") ==> Disease("DownyMildew")'))
KB.tell(expr('Symptom("YellowSpots") & Symptom("PowderyMildew") ==> Disease("PowderyMildew")'))
KB.tell(expr('Symptom("MustyOdor") ==> Disease("GrayMold")'))
KB.tell(expr('Symptom("DarkMushyDecayedRoots") ==> Disease("RootRot")'))
KB.tell(expr('Symptom("CircularSpots") ==> Disease("LeafSpotDiseases")'))
KB.tell(expr('Symptom("WaterSoakedSpots") ==> Disease("GrayMold")'))
KB.tell(expr('Symptom("DarkColoredSap") ==> Disease("LateBlight")'))
KB.tell(expr('Symptom("BrownBlackSpots") ==> Disease("Anthracnose")'))
KB.tell(expr('Symptom("GreyPurpleFuzz") ==> Disease("GrayMold")'))
KB.tell(expr('Symptom("FuzzyWhiteMold") ==> Disease("PowderyMildew")'))
KB.tell(expr('Symptom("CurlyLeaves") ==> Disease("DownyMildew")'))
KB.tell(expr('Symptom("OnlyOneSideIsAffected") ==> Disease("VerticilliumWilt")'))
KB.tell(expr('Symptom("AllThePlantIsAffected") ==> Disease("VerticilliumWilt")'))
KB.tell(expr('Symptom("BrownStricksOnViscularTissue") & Symptom("RootRot") ==> Disease("RootRot")'))
KB.tell(expr('Symptom("BrownStricksOnViscularTissue") & Symptom("VerticilliumWilt") ==> Disease("VerticilliumWilt")'))
KB.tell(expr('Symptom("BrownStricksOnViscularTissue") & Symptom("FusariumWilt") ==> Disease("FusariumWilt")'))
KB.tell(expr('Symptom("BrownStricksOnViscularTissue") & Symptom("LateBlight") ==> Disease("LateBlight")'))
KB.tell(expr('Symptom("PinkishSporeMasses") ==> Disease("DownyMildew")'))


user_symptoms = input("Enter symptoms (comma-separated): ").split(',')

query = expr(f'Disease(x) & {" & ".join([f"Symptom({s.strip()})" for s in user_symptoms])}')

print(f"Querying KB with: {query}")

result = fol_bc_ask(KB, query)

# Extract diseases
common_diseases = [res.bindings['x'] for res in result]

if not common_diseases:
    print("No diseases found for the given symptoms.")
else:
    for disease in common_diseases:
        print(f"The disease might be: {disease}")