import React from "react";
import header from "./assets/home.png";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Symptoms from "./Symptoms";
import { useState } from "react";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faFacebookF,
  faInstagram,
  faTwitter,
} from "@fortawesome/free-brands-svg-icons";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";
import GallerySlider from "./GallerySlider";

// Add all the imported icons to the library
library.add(faFacebookF, faInstagram, faTwitter);

function App() {
  const [showModal, setShowModal] = useState(false);

  const handleResultClick = () => {
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
  };
  const images = [
    {
      src: header,
      alt: "img1",
      caption: "Caption 1",
      className: "w-32 h-32",
    },
    {
      src: header,
      alt: "img2",
      caption: "Caption 2",
      className: "w-32 h-32",
    },
    {
      src: header,
      alt: "img3",
      caption: "Caption 3",
      className: "w-32 h-32",
    },
  ];
  return (
    <div className="flex flex-col w-screen min-h-screen m-auto  ">
      <div className="flex gap-16 font-bold text-lg	h-20 fixed quicksand p-10 shadow-md items-center relative ">
        <a className=" text-black" href="logo">
          Planty'z
        </a>
        <a className=" text-black" href="home">
          home
        </a>
        <a className=" text-black" href="contact">
          contact
        </a>
        <a className=" text-black" href="about">
          about
        </a>
      </div>
      <div className="flex w-screen m-auto mb-24">
        <img
          className="w-500  ml-20 mt-20 justify-center"
          src={header}
          alt="home"
        />{" "}
        {/* Use curly braces and correct variable name */}
      </div>

      <div className="w-screen flex m-auto gap-40 justify-center  ">
        <div className="ml-20 mt-20  whitespace-nowrap items-baseline">
          {" "}
          <h1>PLants in algeria</h1>
        </div>
        <div className="w-90 h-90 p-10 m-auto">
          <GallerySlider images={images} />
        </div>
      </div>
        <div className="flex justify-center mt-12 font-bold text-3xl w-screen ">
            TRY IT NOW
            
        </div>
      <br />
      <br />
       <div className="flex m  gap-20 bg-[#C1DCDC]	 min-w-screen min-h-max ">
        <div className="w-screen flex justify-center h-2/3">
        <Symptoms></Symptoms>
        </div>
       
      </div>
      <div className="w-screen flex mt-12 justify-center">
      <button className=" bg-blue-100 w-52 h-16 hover:text-red-500 border-0  hover:bg-red-50 " onClick={handleResultClick}>See Result</button>
      </div>
      
      {showModal && (
        <div className="fixed top-0 left-0 w-full h-full bg-gray-500 bg-opacity-50 flex justify-center items-center z-50">
          <div className="w-96 h-72 bg-blue-300 flex flex-col justify-center items-center relative">
            <button className="absolute top-2 right-2 text-xs	border-0" onClick={closeModal}>
              X
            </button>
            <div>
              Disease: Some Disease
            </div>
            <div>
              Treatment: Some Treatment
            </div>
          </div>
        </div>
      )}




      <div className=" p-20 justify-center m-auto flex flex-col">
       <p className="font-bold "> <h1> Who we are ? </h1> </p> 
        <br />
       <h2>
       a Group of developers that inspired by ai and technologie ,
        created this plateforme to help the plants lover to diagonize there
        plants for free using ai
       </h2>
        
      </div>
      <div className="flex flex-col gap-20 bg-[#C1DCDC]	 w-screen min-h-full pt-20 pl-20 pr-20 pb-5 m-0">
        <div className="flex justify-between ">
          <div className="flex flex-col gap-2">
            <h1>Planty'z</h1>
            <p>We help you diagnose your plants</p>
          </div>
          <div className="flex text-white text-2xl gap-12 mt-4 ml-96 ">
            <FontAwesomeIcon
              className="cursor-pointer hover:text-blue-500"
              icon={faFacebookF}
            />
            <FontAwesomeIcon
              className="cursor-pointer hover:text-blue-500"
              icon={faInstagram}
            />
            <FontAwesomeIcon
              className="cursor-pointer hover:text-blue-500"
              icon={faTwitter}
            />
          </div>
        </div>

        <div className="flex justify-center">
          2024 all Right Reserved Term of use Planty’z
        </div>
      </div>
      
    </div>
  );
}

export default App;
