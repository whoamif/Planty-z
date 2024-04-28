import React from 'react';
import "./App.css";
import { Navigation} from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import 'swiper/css/navigation';
import plant1 from './assets/img1.png';
import plant2 from './assets/img2.png';
import plant3 from './assets/img3.png';


function Symtoms() {
  return (
    <Swiper
      spaceBetween={50}
      slidesPerView={3}
      navigation
      className=' w-5/6 flex m-auto '
    >
      <SwiperSlide>
        <div className=' p-20 flex flex-col gap-4  cursor-pointer hover:shadow-2xl'>
          <img className='' src={plant1} alt="Plant 1" />
          <p className='text-black font-bold'>Plant Name 1</p>
          <p className='text-black font-thin'>Description of plant 1...</p>
         
        </div>
      </SwiperSlide>
      <SwiperSlide>
        <div className='p-20 flex flex-col gap-4  cursor-pointer hover:shadow-2xl'>
          <img className='' src={plant2} alt="Plant 2" />
          <p className='text-black font-bold'>Plant Name 2</p>
          <p className='text-black font-thin'>Description of plant 2...</p>
          
        </div>
      </SwiperSlide>
      <SwiperSlide>
        <div className='p-20 flex flex-col gap-4  cursor-pointer hover:shadow-2xl'>
          <img className='' src={plant3} alt="Plant 3" />
          <p className='text-black font-bold'>Plant Name 3</p>
          <p className='text-black font-thin'>Description of plant 3...</p>
         
        </div>
      </SwiperSlide>
      <SwiperSlide>
        <div className='p-20 flex flex-col gap-4  cursor-pointer hover:shadow-2xl'>
          <img className='' src={plant3} alt="Plant 3" />
          <p className='text-black font-bold'>Plant Name 3</p>
          <p className='text-black font-thin'>Description of plant 3...</p>
         
        </div>
      </SwiperSlide>
    </Swiper>
  );
}

export default Symtoms;
