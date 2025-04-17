import React from "react";

const ReviewCard = ({ userImage, userName, restaurant, reviewText }) => (
  <div className="bg-white p-3 rounded-lg shadow">
    <div className="flex items-center mb-3">
      <img src={userImage} alt={userName} className="w-10 h-10 rounded-full mr-3" />
      <div>
        <div className="font-bold text-gray-800">{userName}</div>
        <div className="text-xs text-gray-600">Reviewed {restaurant}</div>
      </div>
    </div>
    <p className="text-sm text-gray-700">{reviewText}</p>
  </div>
);

export default ReviewCard;
