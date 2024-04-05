from aima.logic import *
from aima.utils import *

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

# Path: main.py
#This prompts the user to input a comma-separated list of symptoms
user_symptoms = [symptom.strip() for symptom in input("Enter symptoms (comma-separated): ").split(',')]
# Check if the symptoms match any disease
# If a symptom matches a disease, add the disease to the matched_diseases set
matched_diseases = set()

#loop through all the clauses in the knowledge base
for clause in KB.clauses:
    #check if the clause contains the implication symbol '==>' that is, if it is a rule
    if '==>' in str(clause):
        #split the clause into the left-hand side (lhs) and right-hand side (rhs) of the implication
        lhs, rhs = str(clause).split('==>')
        #split the lhs into individual symptoms
        lhs_symptoms = lhs.split('&')
        #loop through all the symptoms in the lhs
        for lhs_symptom in lhs_symptoms:
            
            symptom_name = lhs_symptom.split('(')[1].split(')')[0]
            
            if symptom_name in user_symptoms:
                #if the symptom is in the user's input, add the disease to the matched_diseases set
                matched_diseases.add(rhs.split('(')[1].split(')')[0])
                break

if not matched_diseases:
    print("No diseases found for the given symptoms.")
else:
    print(f"The possible diseases might be: {', '.join(matched_diseases)}")
