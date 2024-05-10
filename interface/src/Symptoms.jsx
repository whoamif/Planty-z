import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import { useState } from 'react';
import 'swiper/css';
import { Navigation} from 'swiper/modules';
import 'swiper/css/navigation';
import axios from 'axios';
import symptom1 from './assets/symptom1.png';
import symptom2 from './assets/symptom2.png';
import symptom3 from './assets/symptom3.png';
import symptom4 from './assets/symptom4.png';
import symptom5 from './assets/symptom5.png';
import symptom6 from './assets/symptom6.png';
import symptom7 from './assets/symptom7.png';
import symptom8 from './assets/symptom8.png';
import symptom9 from './assets/symptom9.png';
import symptom10 from './assets/symptom10.png';
{/*import symptom11 from './assets/symptom11.png';
import symptom12 from './assets/symptom12.png';
import symptom13 from './assets/symptom13.png';
import symptom14 from './assets/symptom14.png';
import symptom15 from './assets/symptom15.png';
import symptom16 from './assets/symptom16.png';
import symptom17 from './assets/symptom17.png';
import symptom18 from './assets/symptom18.png';
import symptom19 from './assets/symptom19.png';
import symptom20 from './assets/symptom20.png';
import symptom21 from './assets/symptom21.png';
import symptom22 from './assets/symptom22.png';
import symptom23 from './assets/symptom23.png';
import symptom24 from './assets/symptom24.png';
import symptom25 from './assets/symptom25.png';
import symptom26 from './assets/symptom26.png';/*}*/}
const Symptoms = () => {
    
const [selectedSymptoms, setSelectedSymptoms] = useState([]);
const symptoms = [
    { name: "YellowOrangeBrownPustules", image: symptom1 },
    { name: "Defoliation", image: symptom2 },
    { name: "CircularIrregularlySpots", image: symptom3 },
    { name: "GrayBrownFuzz", image: symptom4 },
    { name: "StuntedFuzzyGrowth", image: symptom5 },
    { name: "YellowSpots", image: symptom6 },
    { name: "YellowBrownSpots", image: symptom7 },
    { name: "MustyOdor", image: symptom8 },
    { name: "DarkMushyDecayedRoots", image: symptom9 },
    { name: "CircularSpots", image: symptom10 },
    {/*
    { name: "WaterSoakedSpots", image: symptom11 },
    { name: "DarkColoredSap", image: symptom12 },
    { name: "BrownBlackSpots", image: symptom13 },
    { name: "GreyPurpleFuzz", image: symptom14 },
    { name: "FuzzyWhiteMold", image: symptom15 },
    { name: "CurlyLeaves", image: symptom16 },
    { name: "OnlyOneSideIsAffected", image: symptom17 },
    { name: "AllThePlantIsAffected", image: symptom18 },
    { name: "BrownStricksOnViscularTissue", image: symptom19 },
    { name: "PinkishSporeMasses", image: symptom20 },
    { name: "Wilting", image: symptom21 },
    { name: "YellowingOfLeaves", image: symptom22 },
    { name: "StuntedGrowth", image: symptom23 },
    { name: "RottingOfRoots", image: symptom24 },
    { name: "WhitePowderySubstanceOnLeaves", image: symptom25 },
{ name: "YellowingOfLowerLeaves", image: symptom26 }*/} 
    // Ajoutez les autres symptômes avec leurs images correspondantes ici...
];
const toggleSymptom = (symptom) => {
    if (selectedSymptoms.includes(symptom)) {
        setSelectedSymptoms(selectedSymptoms.filter(item => item !== symptom));
    } else {
        setSelectedSymptoms([...selectedSymptoms, symptom]);
    }
};


    return (
        <>
        <Swiper 
            modules={[Navigation]}
            spaceBetween={10}
            slidesPerView={3}
            navigation
            className='w-5/6 flex m-auto'
        >
            {symptoms.map((symptom, index) => (
                <SwiperSlide key={index}>
                    <div className={`p-20 flex flex-col gap-4 cursor-pointer ${selectedSymptoms.includes(symptom.name) ? 'bg-blue-100' : ''}`} onClick={() => toggleSymptom(symptom.name)}>
                        <img className='hover:shadow-2xl w-96 h-56' src={symptom.image} alt={symptom.name} />
                        <p className='text-black font-bold'>{symptom.name}</p>
                    </div>
                </SwiperSlide>
            ))}
            
        </Swiper>
        
    </>
    );
}

export default Symptoms;
