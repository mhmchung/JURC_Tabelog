import React from "react";

const CategoryItem = ({ imageUri, title }) => (
  <div className="flex flex-col items-center">
    <div className="relative w-16 h-16 mb-1 overflow-hidden rounded-full">
      <img src={imageUri} alt={title} className="w-full h-full object-cover" />
      <div className="absolute inset-0 bg-black opacity-20"></div>
    </div>
    <p className="text-xs font-medium text-center text-gray-800">{title}</p>
  </div>
);

export default CategoryItem;
