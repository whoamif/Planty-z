from aima3.logic import *
from aima3.utils import *

#symptomes facts 

KB = FolKB()
KB.tell(expr('Symptom(YellowOrangeBrownPustules)'))
KB.tell(expr('Symptom(Defoliation)'))
KB.tell(expr('Symptom(CircularIrregularlySpots)'))
KB.tell(expr('Symptom(GrayBrownFuzz)'))
KB.tell(expr('Symptom(WaterSoakedSpots )'))
KB.tell(expr('Symptom(MustyOdor)'))
KB.tell(expr('Symptom(StuntedFuzzyGrowth)'))
KB.tell(expr('Symptom(YellowBrownSpots)'))
KB.tell(expr('Symptom(Wiltning)'))
KB.tell(expr('Symptom(DarkMushyDecayedRoots)'))
KB.tell(expr('Symptom(YellowSpots)'))
KB.tell(expr('Symptom(BrownStricksOnViscularTissue)'))
KB.tell(expr('Symptom(OnlyOneSideIsAffected )'))
KB.tell(expr('Symptom(AllThePlantIsAffected )'))
KB.tell(expr('Symptom(CircularSpots )'))
KB.tell(expr('Symptom(DarkColoredSap )'))
KB.tell(expr('Symptom(PinkishSporeMasses )'))
KB.tell(expr('Symptom(BrownBlackSpots )'))
KB.tell(expr('Symptom(FuzzyWhiteMold )'))
KB.tell(expr('Symptom(YellowGreenSpots)'))
KB.tell(expr('Symptom(GreyPurpleFuzz)'))
KB.tell(expr('Symptom(CurlyLeaves)'))
KB.tell(expr('Symptom(PowderyFuzzyGrowth)'))
KB.tell(expr('Symptom(YellowBrownLeaves)'))



#diseases facts :
KB.tell(expr('Disease(Rust)'))
KB.tell(expr('Disease(LeafSpotDiseases)'))
KB.tell(expr('Disease(GrayMold)'))
KB.tell(expr('Disease(RootRot)'))
KB.tell(expr('Disease(VerticilliumWilt)'))
KB.tell(expr('Disease(FusariumWilt)'))
KB.tell(expr('Disease(Anthracnose)'))
KB.tell(expr('Disease(LateBlight)'))
KB.tell(expr('Disease(DownyMildew)'))
KB.tell(expr('Disease(PowderyMildew)'))

#rules : 
"""
KB.tell(expr('Symptom(x) ==> SymptomOf(x,y)'))

KB.tell(expr('Symptom(YellowOrangeBrownPustules) ==> SymptomOf(YellowOrangeBrownPustules,Rust)'))
KB.tell(expr('Symptom(Defoliation) ==> SymptomOf(Defoliation,Rust)')) 

KB.tell(expr('SymptomOf(x,y) ==> Disease(y)'))






KB.tell(expr('Symptom(Defoliation) ==> SymptomOf(Defoliation,LeafSpotDiseases)')) 
KB.tell(expr('Symptom(Defoliation) ==> SymptomOf(Defoliation,DownyMildew)')) 
KB.tell(expr('Symptom(Defoliation) ==> SymptomOf(Defoliation,PowderyMildew)')) 
KB.tell(expr('Symptom(CircularIrregularlySpots) ==> SymptomOf(CircularIrregularlySpots,LeafSpotDiseases)')) 
KB.tell(expr('Symptom(GrayBrownFuzz) ==> SymptomOf(GrayBrownFuzz,GrayMold'))
KB.tell(expr('Symptom(WaterSoakedSpots ) ==> SymptomOf(WaterSoakedSpots,GrayMold'))


###################################################"""
KB.tell(expr('Symptom(YellowOrangeBrownPustules) & Symptom(Defoliation) ==> Disease(Rust)'))
KB.tell(expr('Symptom(CircularIrregularlySpots) & Symptom(Defoliation) ==> Disease(LeafSpotDiseases)')) 
KB.tell(expr('Symptom(GrayBrownFuzz) & Symptom(WaterSoakedSpots) & Symptom(MustyOdor) ==> Disease(GrayMold)')) 
KB.tell(expr('Symptom(StuntedFuzzyGrowth) & Symptom(YellowBrownSpots) & Symptom(Wiltning) & Symptom(DarkMushyDecayedRoots)  ==> Disease(RootRot)')) 
KB.tell(expr('Symptom(YellowSpots) & Symptom(Wiltning) & Symptom(BrownStricksOnViscularTissue) & Symptom(OnlyOneSideIsAffected )  ==> Disease(VerticilliumWilt)')) 
KB.tell(expr('Symptom(YellowSpots) & Symptom(Wiltning) & Symptom(BrownStricksOnViscularTissue) & Symptom(AllThePlantIsAffected )  ==> Disease(FusariumWilt)')) 
KB.tell(expr('Symptom(CircularSpots ) & Symptom(DarkColoredSap ) & Symptom(PinkishSporeMasses ) ==> Disease(Anthracnose)')) 
KB.tell(expr('Symptom(WaterSoakedSpots ) & Symptom(BrownBlackSpots ) & Symptom(FuzzyWhiteMold ) ==> Disease(LateBlight)')) 
KB.tell(expr('Symptom(YellowGreenSpots) & Symptom(GreyPurpleFuzz) & Symptom(CurlyLeaves) & Symptom(Defoliation) ==> Disease(DownyMildew)')) 
KB.tell(expr('Symptom(PowderyFuzzyGrowth) & Symptom(YellowBrownLeaves) & Symptom(Defoliation) ==> Disease(PowderyMildew)')) 





# List of symptoms
#symptoms_list = ['Symptom(YellowOrangeBrownPustules)']

# Construct the query by combining all symptoms using logical AND
#query_expr = ' & '.join(symptoms_list)
#print("Query Expression:", query_expr)

# Print contents of the knowledge base
print("Knowledge Base:")
for sentence in KB.clauses:
    print(sentence)# Query the knowledge base

solution = KB.ask(expr('Disease(Rust)'))
print(solution)

if solution:
    print(f"The symptoms [{', '.join(symptoms_list)}] could be associated with the disease: {solution['?d']}")
else:
    print("No disease found for the given symptoms.") 

































