import React, { useState } from "react";

const HeroSection = () => {
  const [searchQuery, setSearchQuery] = useState("");

  return (
    <div className="relative mb-8 overflow-hidden rounded-xl">
      <img
        src="https://images.pexels.com/photos/31491019/pexels-photo-31491019.jpeg"
        alt="Restaurant hero"
        className="w-full h-48 object-cover"
      />
      <div className="absolute inset-0 bg-black opacity-40"></div>
      <div className="absolute inset-0 flex flex-col justify-center items-center p-4">
        <h2 className="text-xl font-bold text-white text-center mb-2">
          Discover & Book Amazing Restaurants
        </h2>
        <input
          className="bg-white p-3 rounded-lg text-gray-800 w-full max-w-md"
          placeholder="Search restaurants by name, cuisine, or location"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
      </div>
    </div>
  );
};

export default HeroSection;
