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
  const symptomsData = [
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
  ];

  const toggleSymptom = (symptomName) => {
    console.log("Toggling symptom:", symptomName); // Debug statement
    setSelectedSymptoms((prevSelected) => 
      prevSelected.includes(symptomName)
        ? prevSelected.filter(item => item !== symptomName)
        : [...prevSelected, symptomName]
    );
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log("Submitting symptoms:", selectedSymptoms); // Debug statement
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/suggest_disease', {
        symptoms: selectedSymptoms
      });
      const data = response.data;
      console.log("Response data:", data); // Debug statement
      // Handle response data as needed
    } catch (error) {
      console.error('Error:', error);
    }
  };

  useEffect(() => {
    console.log("Selected symptoms updated:", selectedSymptoms); // Debug statement
    localStorage.setItem("selectedSymptoms", JSON.stringify(selectedSymptoms));
  }, [selectedSymptoms]);

  return (
    <>
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
    </>
  );
};

export default Symptoms;
