import React, { useState,useEffect } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import { Navigation } from "swiper/modules";
import "swiper/css/navigation";
import axios from "axios";
import symptom1 from "./assets/symptom1.png";
import symptom2 from "./assets/symptom2.png";
import symptom3 from "./assets/symptom3.png";
import symptom4 from "./assets/symptom4.png";
import symptom5 from "./assets/symptom5.png";
import symptom6 from "./assets/symptom6.png";
import symptom7 from "./assets/symptom7.png";
import symptom8 from "./assets/symptom8.png";
import symptom9 from "./assets/symptom9.png";
import symptom10 from "./assets/symptom10.png";

const Symptoms = () => {
  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [symptomsData, setSymptomsData] = useState([
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
    // Add more symptoms as needed
  ]);

  const toggleSymptom = (symptomName) => {
    if (selectedSymptoms.includes(symptomName)) {
      setSelectedSymptoms(selectedSymptoms.filter(item => item !== symptomName));
    } else {
      setSelectedSymptoms([...selectedSymptoms, symptomName]);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/suggest_disease', {
        symptoms: selectedSymptoms
      });
      const data = response.data;
      // Handle response data as needed
    } catch (error) {
      console.error('Error:', error);
    }
  };
  useEffect(() => {
    localStorage.setItem("selectedSymptoms", JSON.stringify(selectedSymptoms));
  }, [selectedSymptoms]);


  return (
    <div>
      <Swiper
        modules={[Navigation]}
        spaceBetween={10}
        slidesPerView={3}
        navigation
        className="w-5/6 flex m-auto"
      >
        {symptomsData.map((symptom, index) => (
          <SwiperSlide key={index}>
            <div
              className={`p-20 flex flex-col gap-4 cursor-pointer ${
                selectedSymptoms.includes(symptom.name) ? "bg-blue-100" : ""
              }`}
              onClick={() => toggleSymptom(symptom.name)}
            >
              <img
                className="hover:shadow-2xl w-96 h-56"
                src={symptom.image}
                alt={symptom.name}
              />
              <p className="text-black font-bold">{symptom.name}</p>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>

      <form onSubmit={handleSubmit}>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Symptoms;
