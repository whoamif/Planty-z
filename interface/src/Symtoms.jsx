import React from 'react';
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import 'swiper/css/navigation';
import plant1 from './assets/img1.png';
import plant2 from './assets/img2.png';
import plant3 from './assets/img3.png';

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
    { name: "YellowingOfLowerLeaves", image: symptom26 }
    // Ajoutez les autres symptômes avec leurs images correspondantes ici...
];
function Symtoms() {
    return (
        <Swiper 
            modules={[Navigation]}
            spaceBetween={50}
            slidesPerView={3}
            navigation
            className='w-5/6 flex m-auto'
        >
            {symptoms.map((symptom, index) => (
                <SwiperSlide key={index}>
                    <div className='p-20 flex flex-col gap-4 cursor-pointer'>
                        <img className='hover:shadow-2xl' src={symptom.image} alt={symptom.name} />
                        <p className='text-black font-bold'>{symptom.name}</p>
                    </div>
                </SwiperSlide>
            ))}
        </Swiper>
    );
}

export default Symtoms;
