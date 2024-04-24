import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';

// Import your symptom images
import yellowOrangeBrownPustulesImage from './assets/yellowOrangeBrownPustules.png';
import defoliationImage from './assets/defoliation.png';
// Import other symptom images...

export default () => {
  // Define an array of symptom data containing image URLs and corresponding text
  const symptoms = [
    { image: yellowOrangeBrownPustulesImage, text: 'Yellow Orange Brown Pustules' },
    { image: defoliationImage, text: 'Defoliation' },
    // Add other symptom data...
  ];

  return (
    <Swiper
      spaceBetween={10}
      slidesPerView={3}
      onSlideChange={() => console.log('slide change')}
      onSwiper={(swiper) => console.log(swiper)}
      className='m-auto'
    >
      {symptoms.map((symptom, index) => (
        <SwiperSlide key={index}>
          <div className='felx flex-col '>
            <img src={symptom.image} alt={symptom.text} />
            <p>{symptom.text}</p>
          </div>
        </SwiperSlide>
      ))}
    </Swiper>
  );
};
