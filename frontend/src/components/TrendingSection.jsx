import React from "react";
import RestaurantCard from "./RestaurantCard";

const trendingRestaurants = [
  {
    id: "1",
    name: "The Modern Kitchen",
    image: "https://images.pexels.com/photos/3201921/pexels-photo-3201921.jpeg",
    cuisine: "Contemporary",
    price: "$$$$",
    rating: "New Opening",
  },
  {
    id: "2",
    name: "Bistro Romantique",
    image: "https://images.pexels.com/photos/31505466/pexels-photo-31505466.jpeg",
    cuisine: "French",
    price: "$$$",
    rating: "Most Romantic",
  },
];

const TrendingSection = () => (
  <div className="mb-16">
    <h2 className="text-3xl font-bold text-gray-900 mb-6">Trending This Week</h2>
    <div className="flex flex-col gap-8">
      {trendingRestaurants.map((r) => (
        <RestaurantCard key={r.id} {...r} />
      ))}
    </div>
  </div>
);

export default TrendingSection;
