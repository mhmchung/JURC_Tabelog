import React from "react";

const RestaurantCard = ({ name, image, cuisine, price, rating }) => (
  <div className="flex bg-white shadow rounded-lg overflow-hidden max-w-3xl w-full mx-auto">
    <div className="w-1/4 max-w-[25%]">
      <img
        src={image}
        alt={name}
        className="w-full h-full object-cover"
        style={{ maxHeight: "200px" }}
      />
    </div>
    <div className="p-4 w-3/4 flex flex-col justify-center">
      <h3 className="text-2xl font-bold text-gray-900 mb-1">{name}</h3>
      <p className="text-lg text-gray-700">{cuisine} • {price} • {rating}</p>
    </div>
  </div>
);

export default RestaurantCard;
