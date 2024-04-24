import React from 'react';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';

function GallerySlider({ images }) {
  return (
    <Carousel >
      {images.map((image, index) => (
        <div key={index}>
          <img src={image.src} alt={image.alt} />
          <p className="legend">{image.caption}</p>
        </div>
      ))}
    </Carousel>
  );
}

export default GallerySlider;
