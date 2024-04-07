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


# plant symptoms facts :


KB.tell(expr('PlantSymptom(x,YellowOrangeBrownPustules)'))
KB.tell(expr('PlantSymptom(x,Defoliation)'))


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
KB.tell(expr('PlantSymptom(x,z) & PlantSymptom(x,y) & PlantDisease(x,d) ==> Resultat(x,d)'))         



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






# Query the knowledge base

#forward chaining 
solution_generator = fol_fc_ask(KB, expr('Resultat(x,d)'))
print(solution_generator)
for solution in solution_generator:
    print(solution)


"""#backward chaining
solution = KB.ask(expr('PlantDisease(x,Rust)'))
print(solution) """



"""
if solution:
    disease = solution('X')
    print(f"The symptoms {query} could be associated with the disease: {disease}")
else:
    print("No disease found for the given symptoms.")"""

    


