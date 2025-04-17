import React from "react";
import ReviewCard from "./ReviewCard";

const reviews = [
  {
    id: "1",
    userImage: "https://images.pexels.com/photos/31533939/pexels-photo-31533939.jpeg",
    userName: "Sarah J.",
    restaurant: "Sushi Master",
    reviewText: "Amazing fresh sushi, great atmosphere!",
  },
  {
    id: "2",
    userImage: "https://images.pexels.com/photos/31517042/pexels-photo-31517042.jpeg",
    userName: "Mike R.",
    restaurant: "Prime Steakhouse",
    reviewText: "Best steak I've ever had. Worth every penny!",
  },
];


const LatestReviews = () => (
  <div className="mb-8">
    <h2 className="text-xl font-bold text-gray-800 mb-4">Latest Reviews</h2>
    <div className="flex flex-wrap justify-between gap-4">
      {reviews.map((review) => (
        <div key={review.id} className="w-[48%]">
          <ReviewCard {...review} />
        </div>
      ))}
    </div>
  </div>
);

export default LatestReviews;
