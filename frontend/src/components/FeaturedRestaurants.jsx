import React from "react";
import RestaurantCard from "./RestaurantCard";

const restaurants = [
  {
    id: "1",
    name: "Sushi Master",
    image: "https://images.pexels.com/photos/16266744/pexels-photo-16266744.jpeg",
    cuisine: "Japanese",
    price: "$$$",
    rating: "4.8 ⭐",
  },
  {
    id: "2",
    name: "La Cucina",
    image: "https://images.pexels.com/photos/12406772/pexels-photo-12406772.jpeg",
    cuisine: "Italian",
    price: "$$",
    rating: "4.6 ⭐",
  },
  {
    id: "3",
    name: "Prime Steakhouse",
    image: "https://images.pexels.com/photos/8477294/pexels-photo-8477294.jpeg",
    cuisine: "Steakhouse",
    price: "$$$$",
    rating: "4.9 ⭐",
  },
];

const FeaturedRestaurants = () => (
  <div className="mb-16">
    <h2 className="text-3xl font-bold text-gray-900 mb-6">Featured Restaurants</h2>
    <div className="flex flex-col gap-8">
      {restaurants.map((r) => (
        <RestaurantCard key={r.id} {...r} />
      ))}
    </div>
  </div>
);

export default FeaturedRestaurants;
