import React, { useState, useEffect } from 'react'

function ImageSlider() {

    const [index, setIndex] = useState(0);
    const images = [
        'https://www.clearygottlieb.com/-/media/organize-archive/cgsh/images/pages/location/locations_0014_newyork.jpg?h=492&w=900&sc_lang=en&hash=F69D547AFC1FD330C3A71A9DAA8CE4E8',
        'https://this.deakin.edu.au/wp-content/uploads/2017/02/New-York.jpg',
        'https://wallpaperaccess.com/full/450430.jpg'
    ];

    useEffect(() => {
        const intervalId = setInterval(() => {
            setIndex(prevIndex => (prevIndex + 1) % images.length);
        }, 5000);

        return () => clearInterval(intervalId);
    }, []);

    return (
        <img className="slider-image" src={images[index]} alt='Slider' />
    );
}

export default ImageSlider;









