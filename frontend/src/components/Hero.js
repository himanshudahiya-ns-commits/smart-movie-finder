import React from 'react';
import './Hero.css';

function Hero() {
  return (
    <div className="hero-section">
      <div className="hero-content">
        <div className="hero-text">
          <h1 className="hero-title">Smart Movie Finder</h1>
          <p className="hero-subtitle">Your personalized movie discovery companion</p>
          <p className="hero-description">Search movies from multiple sources and get detailed information instantly</p>
        </div>
        <div className="hero-image">
          <img src="/images/movie-banner.png" alt="Movie Banner" className="banner-image" />
        </div>
      </div>
    </div>
  );
}

export default Hero;
